# Google Chrome Offline Installers (Auto Update)

> Windows x64 / Windows ARM64 / macOS x64 — Stable 离线安装包，定时同步 Google Update 服务并发布到本仓库 Release。

[打开最新 Release](https://github.com/vaesn/get-chrome-installer/releases/latest)

## Latest Stable

| Platform | Version | Size | SHA-256 (前 16 位) |
| -------- | ------- | ---- | ------------------- |
| **Windows x64** | `155.0.8059.40` | 498.41 MB | `c43d400e13d421f4…` |
| **Windows ARM64** | `155.0.8059.40` | 422.8 MB | `f586ddb44ced63c6…` |
| **macOS x64** | `155.0.8059.40` | 263.24 MB | `004c039b5c0c7be3…` |

## Downloads

| Platform | Google Direct | GitHub Release Mirror |
| -------- | ------------- | ---------------------- |
| **Windows x64** | [dl.google.com](https://dl.google.com/release2/chrome/adeicfs34nqhzmry2l2sdlpo7l2q_155.0.8059.40/155.0.8059.40_chrome_installer_uncompressed.exe) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/x64_155.0.8059.40_chrome_installer_uncompressed.exe) |
| **Windows ARM64** | [dl.google.com](https://dl.google.com/release2/chrome/acebtw7pmgyxqsd5b653vx6idjoa_155.0.8059.40/155.0.8059.40_chrome_installer_uncompressed.exe) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/arm64_155.0.8059.40_chrome_installer_uncompressed.exe) |
| **macOS x64** | [dl.google.com](https://dl.google.com/release2/chrome/lr7fpw3uxyyx5tnf7oone26c6m_155.0.8059.40/GoogleChrome-155.0.8059.40.dmg) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/x64_GoogleChrome-155.0.8059.40.dmg) |

## SHA-256 校验

```
c43d400e13d421f43ea3bba7e502004f2fe428e5679b32975e3a343bc1d97f06  x64_155.0.8059.40_chrome_installer_uncompressed.exe
f586ddb44ced63c62759a9bfd44fa040c9bd9fa952cad56d688d6b25b2b75f24  arm64_155.0.8059.40_chrome_installer_uncompressed.exe
004c039b5c0c7be3d61fa5254e2b095c3725378ae199c653f324b70f4aed894c  x64_GoogleChrome-155.0.8059.40.dmg
```

## Notes

- 使用 7-Zip 解压并配合chrome_plus以实现便携化使用。
- Tag 固定为 `latest`，每次版本更新时旧 Release 会被自动替换，仓库始终只保留一个 Release。
- `data.json` 保存了全部 13 个渠道/架构的原始响应（Stable / Beta / Dev / Canary × win x86/x64/arm64 / mac x64）
