# Google Chrome Offline Installers (Auto Update)

> Windows x64 / Windows ARM64 / macOS x64 — Stable 离线安装包，定时同步 Google Update 服务并发布到本仓库 Release。

[打开最新 Release](https://github.com/vaesn/get-chrome-installer/releases/latest)

## Latest Stable

| Platform | Version | Size | SHA-256 (前 16 位) |
| -------- | ------- | ---- | ------------------- |
| **Windows x64** | `154.0.8037.93` | 495.82 MB | `dc19d591b8c6d084…` |
| **Windows ARM64** | `154.0.8037.93` | 418.02 MB | `8afed0a458de53ae…` |
| **macOS x64** | `154.0.8037.93` | 261.56 MB | `a9367b6a78a0e7a4…` |

## Downloads

| Platform | Google Direct | GitHub Release Mirror |
| -------- | ------------- | ---------------------- |
| **Windows x64** | [dl.google.com](https://dl.google.com/release2/chrome/jn2gux5cxlyyg3xmconseuamzu_154.0.8037.93/154.0.8037.93_chrome_installer_uncompressed.exe) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/x64_154.0.8037.93_chrome_installer_uncompressed.exe) |
| **Windows ARM64** | [dl.google.com](https://dl.google.com/release2/chrome/ad2o76wk76c3nmahm2zvf5u3nzya_154.0.8037.93/154.0.8037.93_chrome_installer_uncompressed.exe) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/arm64_154.0.8037.93_chrome_installer_uncompressed.exe) |
| **macOS x64** | [dl.google.com](https://dl.google.com/release2/chrome/adufpe5jsoouz6tduwoz7auvmjhq_154.0.8037.93/GoogleChrome-154.0.8037.93.dmg) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/x64_GoogleChrome-154.0.8037.93.dmg) |

## SHA-256 校验

```
dc19d591b8c6d08476d96c81497538c3e0d4fb35a5c16a1e02845f1644964c38  x64_154.0.8037.93_chrome_installer_uncompressed.exe
8afed0a458de53ae20fac377fbb351d26e30bb9f701b9895b9c20bee2f01e767  arm64_154.0.8037.93_chrome_installer_uncompressed.exe
a9367b6a78a0e7a42df032f2411274dbdacab1b415a25fe868bbc331aec99bbc  x64_GoogleChrome-154.0.8037.93.dmg
```

## Notes

- 使用 7-Zip 解压并配合chrome_plus以实现便携化使用。
- Tag 固定为 `latest`，每次版本更新时旧 Release 会被自动替换，仓库始终只保留一个 Release。
- `data.json` 保存了全部 13 个渠道/架构的原始响应（Stable / Beta / Dev / Canary × win x86/x64/arm64 / mac x64）
