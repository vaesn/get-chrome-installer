# Google Chrome Offline Installers (Auto Update)

> Windows x64 / Windows ARM64 / macOS x64 — Stable 离线安装包，定时同步 Google Update 服务并发布到本仓库 Release。

[打开最新 Release](https://github.com/vaesn/get-chrome-installer/releases/latest)

## Latest Stable

| Platform | Version | Size | SHA-256 (前 16 位) |
| -------- | ------- | ---- | ------------------- |
| **Windows x64** | `155.0.8059.85` | 496.35 MB | `2a9b18526096b614…` |
| **Windows ARM64** | `155.0.8059.85` | 422.74 MB | `c09c2d05dd835f70…` |
| **macOS x64** | `155.0.8059.85` | 263.19 MB | `2adfb136bea19ea9…` |

## Downloads

| Platform | Google Direct | GitHub Release Mirror |
| -------- | ------------- | ---------------------- |
| **Windows x64** | [dl.google.com](https://dl.google.com/release2/chrome/ps7jv2y4q3yo32dl6v6liqauri_155.0.8059.85/155.0.8059.85_chrome_installer_uncompressed.exe) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/x64_155.0.8059.85_chrome_installer_uncompressed.exe) |
| **Windows ARM64** | [dl.google.com](https://dl.google.com/release2/chrome/adbjr4cmfx5bv3456rjqcnhm3zta_155.0.8059.85/155.0.8059.85_chrome_installer_uncompressed.exe) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/arm64_155.0.8059.85_chrome_installer_uncompressed.exe) |
| **macOS x64** | [dl.google.com](https://dl.google.com/release2/chrome/o2mzgo6gshgwjzckj3bvrpe4nm_155.0.8059.85/GoogleChrome-155.0.8059.85.dmg) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/x64_GoogleChrome-155.0.8059.85.dmg) |

## SHA-256 校验

```
2a9b18526096b614fbfda4324280fc69316e42dcb0668301f2cd8a4524054664  x64_155.0.8059.85_chrome_installer_uncompressed.exe
c09c2d05dd835f7005e67159f82ce20ca011705fb4db65c28d547ac13b2c0dd6  arm64_155.0.8059.85_chrome_installer_uncompressed.exe
2adfb136bea19ea9f6386a3b408aae4b81b5a3c0955fc3a3093b6ae184c527e7  x64_GoogleChrome-155.0.8059.85.dmg
```

## Notes

- 使用 7-Zip 解压并配合chrome_plus以实现便携化使用。
- Tag 固定为 `latest`，每次版本更新时旧 Release 会被自动替换，仓库始终只保留一个 Release。
- `data.json` 保存了全部 13 个渠道/架构的原始响应（Stable / Beta / Dev / Canary × win x86/x64/arm64 / mac x64）
