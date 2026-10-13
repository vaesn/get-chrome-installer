# Google Chrome Offline Installers (Auto Update)

> Windows x64 / Windows ARM64 / macOS x64 — Stable 离线安装包，定时同步 Google Update 服务并发布到本仓库 Release。

[打开最新 Release](https://github.com/vaesn/get-chrome-installer/releases/latest)

## Latest Stable

| Platform | Version | Size | SHA-256 (前 16 位) |
| -------- | ------- | ---- | ------------------- |
| **Windows x64** | `155.0.8059.80` | 498.98 MB | `90f385e76ae2d728…` |
| **Windows ARM64** | `155.0.8059.80` | 422.69 MB | `0926ac8f3182e3c2…` |
| **macOS x64** | `155.0.8059.80` | 263.22 MB | `5ce0d9e0ca8627c5…` |

## Downloads

| Platform | Google Direct | GitHub Release Mirror |
| -------- | ------------- | ---------------------- |
| **Windows x64** | [dl.google.com](https://dl.google.com/release2/chrome/advybryxffwkweengdiwcshvtpwa_155.0.8059.80/155.0.8059.80_chrome_installer_uncompressed.exe) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/x64_155.0.8059.80_chrome_installer_uncompressed.exe) |
| **Windows ARM64** | [dl.google.com](https://dl.google.com/release2/chrome/adlprnv7saqjcdzfp7kop6nofxea_155.0.8059.80/155.0.8059.80_chrome_installer_uncompressed.exe) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/arm64_155.0.8059.80_chrome_installer_uncompressed.exe) |
| **macOS x64** | [dl.google.com](https://dl.google.com/release2/chrome/lmb4243t4ixokmugtdcax7yo7m_155.0.8059.80/GoogleChrome-155.0.8059.80.dmg) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/x64_GoogleChrome-155.0.8059.80.dmg) |

## SHA-256 校验

```
90f385e76ae2d728551f72e457a07f8ccb60d85494346e79c2f1bd401bd72aa0  x64_155.0.8059.80_chrome_installer_uncompressed.exe
0926ac8f3182e3c244a715176662b192eade7a5eae36610ddf9d186f00cf483f  arm64_155.0.8059.80_chrome_installer_uncompressed.exe
5ce0d9e0ca8627c5f5fb5f7be34c4a4ae402880db2488b9b074969272bf5a83c  x64_GoogleChrome-155.0.8059.80.dmg
```

## Notes

- 使用 7-Zip 解压并配合chrome_plus以实现便携化使用。
- Tag 固定为 `latest`，每次版本更新时旧 Release 会被自动替换，仓库始终只保留一个 Release。
- `data.json` 保存了全部 13 个渠道/架构的原始响应（Stable / Beta / Dev / Canary × win x86/x64/arm64 / mac x64）
