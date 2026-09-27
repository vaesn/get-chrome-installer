# Google Chrome Offline Installers (Auto Update)

> Windows x64 / Windows ARM64 / macOS x64 — Stable 离线安装包，定时同步 Google Update 服务并发布到本仓库 Release。

[打开最新 Release](https://github.com/vaesn/get-chrome-installer/releases/latest)

## Latest Stable

| Platform | Version | Size | SHA-256 (前 16 位) |
| -------- | ------- | ---- | ------------------- |
| **Windows x64** | `154.0.8037.58` | 496.05 MB | `addd2ef92bcf7b03…` |
| **Windows ARM64** | `154.0.8037.58` | 417.99 MB | `f6aabc920ea97614…` |
| **macOS x64** | `154.0.8037.58` | 261.77 MB | `2df467b9bbf5fa93…` |

## Downloads

| Platform | Google Direct | GitHub Release Mirror |
| -------- | ------------- | ---------------------- |
| **Windows x64** | [dl.google.com](https://dl.google.com/release2/chrome/acalovr2zbqjgtc257lbvuvb5pka_154.0.8037.58/154.0.8037.58_chrome_installer_uncompressed.exe) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/x64_154.0.8037.58_chrome_installer_uncompressed.exe) |
| **Windows ARM64** | [dl.google.com](https://dl.google.com/release2/chrome/diykj2uwzb5vf5pzqzkcrg6qee_154.0.8037.58/154.0.8037.58_chrome_installer_uncompressed.exe) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/arm64_154.0.8037.58_chrome_installer_uncompressed.exe) |
| **macOS x64** | [dl.google.com](https://dl.google.com/release2/chrome/esexjcwror2yyct27xsikjz3bq_154.0.8037.58/GoogleChrome-154.0.8037.58.dmg) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/x64_GoogleChrome-154.0.8037.58.dmg) |

## SHA-256 校验

```
addd2ef92bcf7b036860f7a6d85fb8187aa62d4a323fc8bdb5ea8ecb6eb5caa2  x64_154.0.8037.58_chrome_installer_uncompressed.exe
f6aabc920ea976149b840fbf81afae90d995529088039553aec996cff759076b  arm64_154.0.8037.58_chrome_installer_uncompressed.exe
2df467b9bbf5fa93e2a3b59b79906a8ebd9e3677d1b61857f6c9d99e62eacb43  x64_GoogleChrome-154.0.8037.58.dmg
```

## Notes

- 使用 7-Zip 解压并配合chrome_plus以实现便携化使用。
- Tag 固定为 `latest`，每次版本更新时旧 Release 会被自动替换，仓库始终只保留一个 Release。
- `data.json` 保存了全部 13 个渠道/架构的原始响应（Stable / Beta / Dev / Canary × win x86/x64/arm64 / mac x64）
