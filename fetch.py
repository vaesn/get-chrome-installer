
import json
import os
import sys
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor

import requests

UPDATE_URL = "https://tools.google.com/service/update2"
SESSION_ID = "{3597644B-2952-4F92-AE55-D315F45F80A5}"
REQUEST_ID = "{CD7523AD-A40D-49F4-AEEF-8C114B804658}"

TARGETS = {
    "win_stable_x64": {
        "os": "win", "os_version": "10.0", "arch": "x64",
        "appid": "{8A69D345-D564-463C-AFF1-A69D9E530F96}",
        "ap": "x64-stable-multi-chrome",
    },
    "win_stable_arm64": {
        "os": "win", "os_version": "10.0", "arch": "arm64",
        "appid": "{8A69D345-D564-463C-AFF1-A69D9E530F96}",
        "ap": "arm64-stable",
    },
    "mac_stable_x64": {
        "os": "mac", "os_version": "46.0.2490.86", "arch": "x64",
        "appid": "com.google.Chrome",
        "ap": "",
    },
}

TARGET_ORDER = ["win_stable_x64", "win_stable_arm64", "mac_stable_x64"]
DISPLAY_NAME = {
    "win_stable_x64": "Windows x64",
    "win_stable_arm64": "Windows ARM64",
    "mac_stable_x64": "macOS x64",
}


def build_xml(t):
    os_attr = f"platform='{t['os']}' version='{t['os_version']}' arch='{t['arch']}'"
    app_attr = f"appid='{t['appid']}' ap='{t['ap']}'"
    return (
        "<?xml version='1.0' encoding='UTF-8'?>\n"
        "<request protocol='3.0' version='1.3.23.9' shell_version='1.3.21.103' ismachine='0'\n"
        f"    sessionid='{SESSION_ID}' installsource='ondemandcheckforupdate'\n"
        f"    requestid='{REQUEST_ID}' dedup='cr'>\n"
        "<hw sse='1' sse2='1' sse3='1' ssse3='1' sse41='1' sse42='1' avx='1' physmemory='12582912' />\n"
        f"<os {os_attr}/>\n"
        f"<app {app_attr} version='' nextversion='' lang='' brand='GGLS' client=''><updatecheck/></app>\n"
        "</request>"
    )


def fetch_one(key, t):
    try:
        resp = requests.post(UPDATE_URL, data=build_xml(t), timeout=30)
        resp.raise_for_status()
        root = ET.fromstring(resp.text)
        manifest = root.find(".//manifest")
        pkg = root.find(".//package")
        if manifest is None or pkg is None:
            raise ValueError("invalid response: missing <manifest> or <package>")
        pkg_name = pkg.get("name") or ""
        urls = [n.get("codebase", "") + pkg_name for n in root.findall(".//url")]
        urls = [u for u in urls if u.startswith("https://") or u.startswith("http://")]
        if not urls:
            raise ValueError("no download urls in response")
        return {
            "version": manifest.get("version") or "",
            "size": int(pkg.get("size") or 0),
            "sha256": (pkg.get("hash_sha256") or "").lower(),
            "urls": urls,
            "error": "",
        }
    except Exception as exc:
        return {"version": "", "size": 0, "sha256": "", "urls": [], "error": str(exc)}


def fetch_all():
    results = {}
    with ThreadPoolExecutor(max_workers=len(TARGETS)) as pool:
        futures = {pool.submit(fetch_one, k, v): k for k, v in TARGETS.items()}
        for fut in futures:
            results[futures[fut]] = fut.result()
    return results


def humansize(nbytes):
    for unit in ("B", "KB", "MB", "GB"):
        if nbytes < 1024:
            return f"{nbytes:.2f}".rstrip("0").rstrip(".") + " " + unit
        nbytes /= 1024.0
    return f"{nbytes:.2f} TB"


def load_json(path="data.json"):
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f) or {}
    except (json.JSONDecodeError, ValueError):
        return {}


def needs_update(new_results, old_data):
    if not old_data:
        return True
    for key in TARGET_ORDER:
        old = old_data.get(key) or {}
        new = new_results.get(key) or {}
        if old.get("version") != new.get("version"):
            return True
    return False


def set_github_env(key, value):
    github_env = os.environ.get("GITHUB_ENV")
    if github_env and os.path.exists(github_env):
        with open(github_env, "a", encoding="utf-8") as f:
            f.write(f"{key}={value}\n")


def repo_slug():
    return os.environ.get("GITHUB_REPOSITORY", "OWNER/REPO")


def asset_name(key, version):
    if key.startswith("mac_"):
        return f"mac_{version}.dmg"
    arch_id = key.split("_")[-1]
    return f"{arch_id}_{version}_chrome_installer_uncompressed.exe"


def build_readme(results, path="README.md"):
    slug = repo_slug()
    lines = []
    lines.append("# Google Chrome Offline Installers (Auto Update)")
    lines.append("")
    lines.append("> Windows x64 / Windows ARM64 / macOS x64 — Stable 离线安装包，定时同步 Google Update 服务并发布到本仓库 Release。")
    lines.append("")
    lines.append(f"[下载最新版](https://github.com/{slug}/releases/latest)")
    lines.append("")
    lines.append("## Latest Version")
    lines.append("")
    lines.append("| Platform | Version | Size | SHA-256 |")
    lines.append("| -------- | ------- | ---- | ------- |")
    for key in TARGET_ORDER:
        info = results.get(key) or {}
        if info.get("version"):
            short_sha = (info.get("sha256") or "")[:16] + "…"
            lines.append(
                f"| **{DISPLAY_NAME[key]}** | `{info['version']}` | {humansize(info['size'])} | `{short_sha}` |"
            )
    lines.append("")
    lines.append("## Downloads")
    lines.append("")
    lines.append("| File | Link |")
    lines.append("| ---- | ---- |")
    for key in TARGET_ORDER:
        info = results.get(key) or {}
        if info.get("version"):
            asset = asset_name(key, info["version"])
            url = f"https://github.com/{slug}/releases/latest/download/{asset}"
            lines.append(f"| {asset} | [Download]({url}) |")
    lines.append("")
    lines.append("## SHA-256")
    lines.append("")
    lines.append("```")
    for key in TARGET_ORDER:
        info = results.get(key) or {}
        if info.get("version"):
            asset = asset_name(key, info["version"])
            lines.append(f"{info['sha256']}  {asset}")
    lines.append("```")
    lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append("- 安装包未加壳，可直接使用 7-Zip 解压或双击安装。")
    lines.append("- 下载后请用上方 SHA-256 校验文件完整性（`sha256sum -c`）。")
    lines.append("- Tag 固定为 `latest`，每次有版本更新时旧 Release 会被自动替换。")
    lines.append("")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main():
    new_results = fetch_all()
    for key in TARGET_ORDER:
        info = new_results.get(key) or {}
        if info.get("version"):
            print(f"[fetch] {key}: v{info['version']}")
        else:
            print(f"[fetch] {key}: ERROR - {info.get('error', 'unknown')}")
    failed = [k for k in TARGET_ORDER if (new_results.get(k) or {}).get("error")]
    if failed:
        sys.exit(f"[fetch] failed targets: {', '.join(failed)}")

    old_data = load_json()
    if needs_update(new_results, old_data):
        build_readme(new_results)
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(new_results, f, indent=2, ensure_ascii=False)
        set_github_env("updated", "true")
        print("[fetch] version changed, data.json & README.md updated")
    else:
        set_github_env("updated", "false")
        print("[fetch] no version change, skip rewriting")


if __name__ == "__main__":
    main()