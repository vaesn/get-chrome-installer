import argparse
import hashlib
import json
import os
import shutil
import sys

import requests

CHUNK = 1024 * 1024


def asset_name(key, version):
    if key.startswith("mac_"):
        return f"mac_{version}.dmg"
    arch_id = key.split("_")[-1]
    return f"{arch_id}_{version}_chrome_installer_uncompressed.exe"


def pick_url(urls):
    for u in urls:
        if u.startswith("https://dl.google.com/"):
            return u
    for u in urls:
        if u.startswith("https://"):
            return u
    return urls[0] if urls else ""


def download(arch_key, entry):
    version = entry.get("version") or ""
    urls = entry.get("urls") or []
    expected = (entry.get("sha256") or "").lower()
    if not version or not urls or not expected:
        raise SystemExit(f"[download] {arch_key}: invalid data.json entry")
    filename = asset_name(arch_key, version)
    if os.path.exists(filename):
        print(f"[download] {arch_key}: {filename} already exists, skip")
        return
    url = pick_url(urls)
    print(f"[download] {arch_key}: v{version}")
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
            f"[download] {arch_key}: sha256 mismatch, expected={expected} actual={actual}"
        )
    print(f"[download] {arch_key}: {filename} verified")


def main():
    parser = argparse.ArgumentParser(description="Download Chrome installers by arch key")
    parser.add_argument(
        "--arch",
        nargs="+",
        default=["win_stable_x64", "win_stable_arm64", "mac_stable_x64"],
        choices=["win_stable_x64", "win_stable_arm64", "mac_stable_x64"],
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