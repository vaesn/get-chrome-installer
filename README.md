# Google Chrome Offline Installers (Auto Update)

> Windows x64 / Windows ARM64 / macOS x64 — Stable 离线安装包，定时同步 Google Update 服务并发布到本仓库 Release。

[打开最新 Release](https://github.com/vaesn/get-chrome-installer/releases/latest)

## Latest Stable

| Platform | Version | Size | Google Direct | GitHub Release Mirror | SHA-256 |
| -------- | ------- | ---- | ------------- | --------------------- | ------- |
| **Windows x64** | `156.0.8078.48` | 502.71 MB | [dl.google.com](https://dl.google.com/release2/chrome/gqqkrczbgbi6dq5qhgethojfv4_156.0.8078.48/156.0.8078.48_chrome_installer_uncompressed.exe) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/x64_156.0.8078.48_chrome_installer_uncompressed.exe) | <details><summary><code>84e13e72c71a3b7d…</code></summary><code>84e13e72c71a3b7d767c115e8e94ec81cb563f9bf9a782407a54afceaa37f55a</code></details> |
| **Windows ARM64** | `156.0.8078.48` | 426.74 MB | [dl.google.com](https://dl.google.com/release2/chrome/pc3shryvqox3g3r47kcthpdl_156.0.8078.48/156.0.8078.48_chrome_installer_uncompressed.exe) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/arm64_156.0.8078.48_chrome_installer_uncompressed.exe) | <details><summary><code>b34cd2d1e0757263…</code></summary><code>b34cd2d1e07572633f1eefe8c589e3f0ea3cfd339094d9789ceefc0973bbdba9</code></details> |
| **macOS x64** | `156.0.8078.48` | 265.71 MB | [dl.google.com](https://dl.google.com/release2/chrome/acpz6fsjbxgnl2ylrkmukmxx2b7q_156.0.8078.48/GoogleChrome-156.0.8078.48.dmg) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/x64_GoogleChrome-156.0.8078.48.dmg) | <details><summary><code>0e013a010d9592c4…</code></summary><code>0e013a010d9592c4a905de0c81399ba3dc33ec0b4207befbecec85d67031301f</code></details> |

## 校验方法

点击表格 SHA-256 列展开完整哈希，下载后与本地计算结果比对。

<details>
<summary><strong>命令行校验（点击展开）</strong></summary>

### Windows x64

文件名：`x64_156.0.8078.48_chrome_installer_uncompressed.exe`

```text
84e13e72c71a3b7d767c115e8e94ec81cb563f9bf9a782407a54afceaa37f55a
```

PowerShell（在文件所在目录执行）：

```powershell
Get-FileHash .\x64_156.0.8078.48_chrome_installer_uncompressed.exe -Algorithm SHA256
```

CMD（可选）：

```bat
certutil -hashfile x64_156.0.8078.48_chrome_installer_uncompressed.exe SHA256
```

### Windows ARM64

文件名：`arm64_156.0.8078.48_chrome_installer_uncompressed.exe`

```text
b34cd2d1e07572633f1eefe8c589e3f0ea3cfd339094d9789ceefc0973bbdba9
```

PowerShell（在文件所在目录执行）：

```powershell
Get-FileHash .\arm64_156.0.8078.48_chrome_installer_uncompressed.exe -Algorithm SHA256
```

CMD（可选）：

```bat
certutil -hashfile arm64_156.0.8078.48_chrome_installer_uncompressed.exe SHA256
```

### macOS x64

文件名：`x64_GoogleChrome-156.0.8078.48.dmg`

```text
0e013a010d9592c4a905de0c81399ba3dc33ec0b4207befbecec85d67031301f
```

macOS / Linux：

```bash
shasum -a 256 x64_GoogleChrome-156.0.8078.48.dmg
```

</details>

## Notes

- 使用 7-Zip 解压并配合[chrome_plus](https://github.com/Bush2021/chrome_plus)以实现便携化使用。
- Tag 固定为 `latest`，每次版本更新时旧 Release 会被自动替换，仓库始终只保留一个 Release。
- `data.json` 保存了全部 13 个渠道/架构的原始响应（Stable / Beta / Dev / Canary × win x86/x64/arm64 / mac x64）
