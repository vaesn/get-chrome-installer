# Google Chrome Offline Installers (Auto Update)

> Windows x64 / Windows ARM64 / macOS x64 — Stable 离线安装包，定时同步 Google Update 服务并发布到本仓库 Release。

[打开最新 Release](https://github.com/vaesn/get-chrome-installer/releases/latest)

## Latest Stable

| Platform | Version | Size | Google Direct | GitHub Release Mirror | SHA-256 |
| -------- | ------- | ---- | ------------- | --------------------- | ------- |
| **Windows x64** | `156.0.8078.74` | 501.13 MB | [dl.google.com](https://dl.google.com/release2/chrome/adnbzwqfdty3qpprdhwig7aufvyq_156.0.8078.74/156.0.8078.74_chrome_installer_uncompressed.exe) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/x64_156.0.8078.74_chrome_installer_uncompressed.exe) | <details><summary><code>8783e3a9a3bb263a…</code></summary><code>8783e3a9a3bb263a6b39da9e9ea6bdb7f31bb9dc9806f9b438ae7c1dde0480b0</code></details> |
| **Windows ARM64** | `156.0.8078.74` | 426.83 MB | [dl.google.com](https://dl.google.com/release2/chrome/bepev3654e27wbgt7ik5uai53y_156.0.8078.74/156.0.8078.74_chrome_installer_uncompressed.exe) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/arm64_156.0.8078.74_chrome_installer_uncompressed.exe) | <details><summary><code>e20a565fa070c445…</code></summary><code>e20a565fa070c4453947eef0e5b460756d39682205882efe3879923bcd3e7949</code></details> |
| **macOS x64** | `156.0.8078.74` | 265.99 MB | [dl.google.com](https://dl.google.com/release2/chrome/acg2teiapq4qsajscuhoyboaquhq_156.0.8078.74/GoogleChrome-156.0.8078.74.dmg) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/x64_GoogleChrome-156.0.8078.74.dmg) | <details><summary><code>55d7c75223f4f27a…</code></summary><code>55d7c75223f4f27a748b8c7ec985d7a752ef357ead43f5bf1a5477aedb797551</code></details> |

## 校验方法

点击表格 SHA-256 列展开完整哈希，下载后与本地计算结果比对。

<details>
<summary><strong>命令行校验（点击展开）</strong></summary>

### Windows x64

文件名：`x64_156.0.8078.74_chrome_installer_uncompressed.exe`

```text
8783e3a9a3bb263a6b39da9e9ea6bdb7f31bb9dc9806f9b438ae7c1dde0480b0
```

PowerShell（在文件所在目录执行）：

```powershell
Get-FileHash .\x64_156.0.8078.74_chrome_installer_uncompressed.exe -Algorithm SHA256
```

CMD（可选）：

```bat
certutil -hashfile x64_156.0.8078.74_chrome_installer_uncompressed.exe SHA256
```

### Windows ARM64

文件名：`arm64_156.0.8078.74_chrome_installer_uncompressed.exe`

```text
e20a565fa070c4453947eef0e5b460756d39682205882efe3879923bcd3e7949
```

PowerShell（在文件所在目录执行）：

```powershell
Get-FileHash .\arm64_156.0.8078.74_chrome_installer_uncompressed.exe -Algorithm SHA256
```

CMD（可选）：

```bat
certutil -hashfile arm64_156.0.8078.74_chrome_installer_uncompressed.exe SHA256
```

### macOS x64

文件名：`x64_GoogleChrome-156.0.8078.74.dmg`

```text
55d7c75223f4f27a748b8c7ec985d7a752ef357ead43f5bf1a5477aedb797551
```

macOS / Linux：

```bash
shasum -a 256 x64_GoogleChrome-156.0.8078.74.dmg
```

</details>

## Notes

- 使用 7-Zip 解压并配合[chrome_plus](https://github.com/Bush2021/chrome_plus)以实现便携化使用。
- Tag 固定为 `latest`，每次版本更新时旧 Release 会被自动替换，仓库始终只保留一个 Release。
- `data.json` 保存了全部 13 个渠道/架构的原始响应（Stable / Beta / Dev / Canary × win x86/x64/arm64 / mac x64）
