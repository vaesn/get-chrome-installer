# Google Chrome Offline Installers (Auto Update)

> Windows x64 / Windows ARM64 / macOS x64 — Stable 离线安装包，定时同步 Google Update 服务并发布到本仓库 Release。

[打开最新 Release](https://github.com/vaesn/get-chrome-installer/releases/latest)

## Latest Stable

| Platform | Version | Size | SHA-256 (前 16 位) |
| -------- | ------- | ---- | ------------------- |
| **Windows x64** | `154.0.8037.98` | 495.33 MB | `2d5f2073185cdf8e…` |
| **Windows ARM64** | `154.0.8037.98` | 418.02 MB | `dd9945e3271a08f6…` |
| **macOS x64** | `154.0.8037.98` | 261.05 MB | `7f85cdec42632b48…` |

## Downloads

| Platform | Google Direct | GitHub Release Mirror |
| -------- | ------------- | ---------------------- |
| **Windows x64** | [dl.google.com](https://dl.google.com/release2/chrome/ac3stf7x6z62hvwmphhro6dpbhpq_154.0.8037.98/154.0.8037.98_chrome_installer_uncompressed.exe) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/x64_154.0.8037.98_chrome_installer_uncompressed.exe) |
| **Windows ARM64** | [dl.google.com](https://dl.google.com/release2/chrome/adlncrhrlmip6efjsmh5j3rnq6vq_154.0.8037.98/154.0.8037.98_chrome_installer_uncompressed.exe) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/arm64_154.0.8037.98_chrome_installer_uncompressed.exe) |
| **macOS x64** | [dl.google.com](https://dl.google.com/release2/chrome/oesfoc5zcpr4zxi27ozbzxre4i_154.0.8037.98/GoogleChrome-154.0.8037.98.dmg) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/x64_GoogleChrome-154.0.8037.98.dmg) |

## SHA-256 校验

```
2d5f2073185cdf8e72bd70b19970bcb2e1ade19a85d68b6be2a3fe672816941d  x64_154.0.8037.98_chrome_installer_uncompressed.exe
dd9945e3271a08f6cef1b67169fcf906ac3dee37ee027f669d177e8b508a5781  arm64_154.0.8037.98_chrome_installer_uncompressed.exe
7f85cdec42632b482b2afc5fe8ee04bcf730082cec1328c0041d788632f57542  x64_GoogleChrome-154.0.8037.98.dmg
```

## Notes

- 使用 7-Zip 解压并配合chrome_plus以实现便携化使用。
- Tag 固定为 `latest`，每次版本更新时旧 Release 会被自动替换，仓库始终只保留一个 Release。
- `data.json` 保存了全部 13 个渠道/架构的原始响应（Stable / Beta / Dev / Canary × win x86/x64/arm64 / mac x64）
