import argparse
import hashlib
import json
import os
import shutil

import requests

CHUNK = 1024 * 1024


def pick_url(urls):
    for u in urls:
        if u.startswith("https://dl.google.com/"):
            return u
    for u in urls:
        if u.startswith("https://"):
            return u
    return urls[0] if urls else ""


def asset_name(key, entry):
    """与 fetch.py 中的 asset_name() 保持完全一致"""
    url = pick_url(entry.get("urls") or [])
    if not url:
        return ""
    original = url.split("/")[-1]
    arch_id = key.split("_")[-1]
    return f"{arch_id}_{original}"


def download(key, entry):
    if entry.get("error"):
        raise SystemExit(f"[download] {key}: upstream error: {entry['error']}")
    version = entry.get("version") or ""
    urls = entry.get("urls") or []
    expected = (entry.get("sha256") or "").lower()
    if not version or not urls or not expected:
        raise SystemExit(f"[download] {key}: invalid data.json entry")

    filename = asset_name(key, entry)
    if os.path.exists(filename):
        print(f"[download] {key}: {filename} already exists, skip")
        return

    url = pick_url(urls)
    print(f"[download] {key}: v{version}")
    with requests.get(url, stream=True, timeout=60) as resp:
        resp.raise_for_status()
        digest = hashlib.sha256()
        with open(filename, "wb") as fh:
            for chunk in resp.iter_content(chunk_size=CHUNK):
                if chunk:
                    fh.write(chunk)
                    digest.update(chunk)
    actual = digest.hexdigest()
    if actual != expected:
        try:
            os.remove(filename)
        except OSError:
            pass
        raise SystemExit(
            f"[download] {key}: sha256 mismatch expected={expected} actual={actual}"
        )
    print(f"[download] {key}: {filename} verified")


def main():
    parser = argparse.ArgumentParser(description="Download Chrome installers by arch key")
    parser.add_argument(
        "--arch",
        nargs="+",
        default=["win_stable_x64", "win_stable_arm64", "mac_stable_x64"],
    )
    args = parser.parse_args()
    try:
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        raise SystemExit(f"[download] failed to load data.json: {exc}")

    for arch in args.arch:
        if arch not in data:
            raise SystemExit(f"[download] {arch} missing from data.json")
        download(arch, data[arch])

    if os.path.isdir("__pycache__"):
        shutil.rmtree("__pycache__")


if __name__ == "__main__":
    main()