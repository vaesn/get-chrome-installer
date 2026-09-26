
import json
import os
import sys
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor

import requests

UPDATE_URL = "https://tools.google.com/service/update2"
SESSION_ID = "{3597644B-2952-4F92-AE55-D315F45F80A5}"
REQUEST_ID = "{CD7523AD-A40D-49F4-AEEF-8C114B804658}"

WIN_APPID = "{8A69D345-D564-463C-AFF1-A69D9E530F96}"
CANARY_APPID = "{4EA16AC7-FD5A-47C3-875B-DBF4A2008C20}"
MAC_STABLE_APPID = "com.google.Chrome"
MAC_BETA_APPID = "com.google.Chrome.Beta"
MAC_DEV_APPID = "com.google.Chrome.Dev"
MAC_CANARY_APPID = "com.google.Chrome.Canary"

MAC_OS_VERSION = "46.0.2490.86"

# 13 条查询目标：全部写入 data.json（原始响应结构）
TARGETS = {
    # === Stable ===
    "win_stable_x64":   {"os": "win", "os_version": "10.0", "arch": "x64",
                          "appid": WIN_APPID, "ap": "x64-stable-multi-chrome"},
    "win_stable_x86":   {"os": "win", "os_version": "10.0", "arch": "x86",
                          "appid": WIN_APPID, "ap": "-multi-chrome"},
    "win_stable_arm64": {"os": "win", "os_version": "10.0", "arch": "arm64",
                          "appid": WIN_APPID, "ap": "arm64-stable"},
    "mac_stable_x64":   {"os": "mac", "os_version": MAC_OS_VERSION, "arch": "x64",
                          "appid": MAC_STABLE_APPID, "ap": ""},
    # === Beta ===
    "win_beta_x64":     {"os": "win", "os_version": "10.0", "arch": "x64",
                          "appid": WIN_APPID, "ap": "x64-beta-multi-chrome"},
    "win_beta_x86":     {"os": "win", "os_version": "10.0", "arch": "x86",
                          "appid": WIN_APPID, "ap": "1.1-beta"},
    "mac_beta_x64":     {"os": "mac", "os_version": MAC_OS_VERSION, "arch": "x64",
                          "appid": MAC_BETA_APPID, "ap": "betachannel"},
    # === Dev ===
    "win_dev_x64":      {"os": "win", "os_version": "10.0", "arch": "x64",
                          "appid": WIN_APPID, "ap": "x64-dev-multi-chrome"},
    "win_dev_x86":      {"os": "win", "os_version": "10.0", "arch": "x86",
                          "appid": WIN_APPID, "ap": "2.0-dev"},
    "mac_dev_x64":      {"os": "mac", "os_version": MAC_OS_VERSION, "arch": "x64",
                          "appid": MAC_DEV_APPID, "ap": "devchannel"},
    # === Canary ===
    "win_canary_x64":   {"os": "win", "os_version": "10.0", "arch": "x64",
                          "appid": CANARY_APPID, "ap": "x64-canary"},
    "win_canary_x86":   {"os": "win", "os_version": "10.0", "arch": "x86",
                          "appid": CANARY_APPID, "ap": ""},
    "mac_canary_x64":   {"os": "mac", "os_version": MAC_OS_VERSION, "arch": "x64",
                          "appid": MAC_CANARY_APPID, "ap": ""},
}

# 只下载/发布的 3 个目标
DOWNLOAD_TARGETS = ["win_stable_x64", "win_stable_arm64", "mac_stable_x64"]
DISPLAY_NAME = {
    "win_stable_x64":   "Windows x64",
    "win_stable_arm64": "Windows ARM64",
    "mac_stable_x64":   "macOS x64",
}


def build_xml(t):
    return (
        "<?xml version='1.0' encoding='UTF-8'?>\n"
        "<request protocol='3.0' version='1.3.23.9' shell_version='1.3.21.103' ismachine='0'\n"
        f"    sessionid='{SESSION_ID}' installsource='ondemandcheckforupdate'\n"
        f"    requestid='{REQUEST_ID}' dedup='cr'>\n"
        "<hw sse='1' sse2='1' sse3='1' ssse3='1' sse41='1' sse42='1' avx='1' physmemory='12582912' />\n"
        f"<os platform='{t['os']}' version='{t['os_version']}' arch='{t['arch']}'/>\n"
        f"<app appid='{t['appid']}' ap='{t['ap']}' version='' nextversion='' lang='' brand='GGLS' client=''>"
        "<updatecheck/></app>\n"
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
        urls = [u for u in urls if u]
        if not urls:
            raise ValueError("no download urls in response")
        return {
            "error": "",
            "version": manifest.get("version") or "",
            "size": pkg.get("size") or "0",
            "sha256": (pkg.get("hash_sha256") or "").lower(),
            "urls": urls,
        }
    except Exception as exc:
        return {"error": str(exc), "version": "", "size": "0", "sha256": "", "urls": []}


def fetch_all():
    results = {}
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(fetch_one, k, v): k for k, v in TARGETS.items()}
        for fut in futures:
            results[futures[fut]] = fut.result()
    return results


def pick_google_direct(urls):
    """优先返回 https://dl.google.com 开头的直链，其次任意 https google.com，最后第一个"""
    for u in urls:
        if u.startswith("https://dl.google.com/"):
            return u
    for u in urls:
        if u.startswith("https://") and "google.com" in u:
            return u
    return urls[0] if urls else ""


def asset_name(key, entry):
    """生成 Release 资产名：{arch_id}_{原始文件名}
    必须与 download.py 中的 asset_name() 保持完全一致"""
    url = pick_google_direct(entry.get("urls") or [])
    if not url:
        return ""
    original = url.split("/")[-1]
    arch_id = key.split("_")[-1]
    return f"{arch_id}_{original}"


def humansize(n):
    try:
        n = float(n)
    except (ValueError, TypeError):
        return "N/A"
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024:
            return f"{n:.2f}".rstrip("0").rstrip(".") + " " + unit
        n /= 1024.0
    return f"{n:.2f} PB"


def load_json(path="data.json"):
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f) or {}
    except (json.JSONDecodeError, ValueError):
        return {}


def needs_update(new_results, old_data):
    """只关注 3 个下载目标的版本变化"""
    if not old_data:
        return True
    for key in DOWNLOAD_TARGETS:
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


def build_readme(results, path="README.md"):
    slug = repo_slug()
    lines = []
    lines.append("# Google Chrome Offline Installers (Auto Update)")
    lines.append("")
    lines.append("> Windows x64 / Windows ARM64 / macOS x64 — Stable 离线安装包，定时同步 Google Update 服务并发布到本仓库 Release。")
    lines.append("")
    lines.append(f"[打开最新 Release](https://github.com/{slug}/releases/latest)")
    lines.append("")
    lines.append("## Latest Stable")
    lines.append("")
    lines.append("| Platform | Version | Size | SHA-256 (前 16 位) |")
    lines.append("| -------- | ------- | ---- | ------------------- |")
    for key in DOWNLOAD_TARGETS:
        info = results.get(key) or {}
        if info.get("version"):
            short_sha = (info.get("sha256") or "")[:16] + "…"
            lines.append(
                f"| **{DISPLAY_NAME[key]}** | `{info['version']}` | {humansize(info['size'])} | `{short_sha}` |"
            )
    lines.append("")
    lines.append("## Downloads")
    lines.append("")
    lines.append("| Platform | Google Direct | GitHub Release Mirror |")
    lines.append("| -------- | ------------- | ---------------------- |")
    for key in DOWNLOAD_TARGETS:
        info = results.get(key) or {}
        if info.get("version"):
            google_url = pick_google_direct(info["urls"])
            mirror_url = f"https://github.com/{slug}/releases/latest/download/{asset_name(key, info)}"
            lines.append(
                f"| **{DISPLAY_NAME[key]}** | [dl.google.com]({google_url}) | [GitHub Release]({mirror_url}) |"
            )
    lines.append("")
    lines.append("## SHA-256 校验")
    lines.append("")
    lines.append("```")
    for key in DOWNLOAD_TARGETS:
        info = results.get(key) or {}
        if info.get("version"):
            lines.append(f"{info['sha256']}  {asset_name(key, info)}")
    lines.append("```")
    lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append("- 直接使用 7-Zip 解压,配合chrome++使用。")
    lines.append("- Tag 固定为 `latest`，每次版本更新时旧 Release 会被自动替换，仓库始终只保留一个 Release。")
    lines.append("- `data.json` 保存了全部 13 个渠道/架构的原始响应（Stable / Beta / Dev / Canary × win x86/x64/arm64 / mac x64）")
    lines.append("")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main():
    new_results = fetch_all()
    for key in DOWNLOAD_TARGETS:
        info = new_results.get(key) or {}
        if info.get("version"):
            print(f"[fetch] {key}: v{info['version']}")
        else:
            print(f"[fetch] {key}: ERROR - {info.get('error', 'unknown')}")
    failed = [k for k in DOWNLOAD_TARGETS if (new_results.get(k) or {}).get("error")]
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