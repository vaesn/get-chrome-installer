# Google Chrome Offline Installers (Auto Update)

> Windows x64 / Windows ARM64 / macOS x64 — Stable 离线安装包，以及整合 [chrome_plus](https://github.com/Bush2021/chrome_plus) 的 Windows 便携版 `.7z`，定时同步 Google Update 服务并发布到本仓库 Release。

[打开最新 Release](https://github.com/vaesn/get-chrome-installer/releases/latest)

## Latest Stable

| Platform | Version | Size | Google Direct | GitHub Release Mirror | SHA-256 |
| -------- | ------- | ---- | ------------- | --------------------- | ------- |
| **Windows x64** | `158.0.8127.89` | 511.64 MB | [dl.google.com](https://dl.google.com/release2/chrome/cegotz2vlsfimli3uv34l7ztzm_158.0.8127.89/158.0.8127.89_chrome_installer_uncompressed.exe) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/x64_158.0.8127.89_chrome_installer_uncompressed.exe) | <details><summary><code>e94768730a55bfe6…</code></summary><code>e94768730a55bfe698d65899a9aa43d498a8816e7ce3b307bd9d07ac230a9371</code></details> |
| **Windows ARM64** | `158.0.8127.89` | 440.93 MB | [dl.google.com](https://dl.google.com/release2/chrome/ads3hjcdxv4d63a4tvmbe5agceea_158.0.8127.89/158.0.8127.89_chrome_installer_uncompressed.exe) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/arm64_158.0.8127.89_chrome_installer_uncompressed.exe) | <details><summary><code>587aaf6bc0be6a2e…</code></summary><code>587aaf6bc0be6a2e481534537af43d591764b2704b2cf029a6f7535b7fa8e643</code></details> |
| **macOS x64** | `158.0.8127.89` | 275.86 MB | [dl.google.com](https://dl.google.com/release2/chrome/adgy6ceswc76i2cvcaufmkulok6q_158.0.8127.89/GoogleChrome-158.0.8127.89.dmg) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/x64_GoogleChrome-158.0.8127.89.dmg) | <details><summary><code>f54426133e03ea9b…</code></summary><code>f54426133e03ea9bf8dfd2d0f9226265fba2974dddc26e8bf99cf2890de6821e</code></details> |
| **Windows x64 (Chrome++)** | `158.0.8127.89` | N/A | — | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/x64_158.0.8127.89_chrome.7z) | N/A |
| **Windows ARM64 (Chrome++)** | `158.0.8127.89` | N/A | — | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/arm64_158.0.8127.89_chrome.7z) | N/A |

> 带 **(Chrome++)** 后缀的行为整合 [chrome_plus](https://github.com/Bush2021/chrome_plus) 的便携版 `.7z`，由本仓库工作流在版本更新时自动打包，仅随 Release 提供；`Size` / `SHA-256` 请以 Release 附件实际信息为准。

## 校验方法

点击表格 SHA-256 列展开完整哈希，下载后与本地计算结果比对。

<details>
<summary><strong>命令行校验（点击展开）</strong></summary>

### Windows x64

文件名：`x64_158.0.8127.89_chrome_installer_uncompressed.exe`

```text
e94768730a55bfe698d65899a9aa43d498a8816e7ce3b307bd9d07ac230a9371
```

PowerShell（在文件所在目录执行）：

```powershell
Get-FileHash .\x64_158.0.8127.89_chrome_installer_uncompressed.exe -Algorithm SHA256
```

CMD（可选）：

```bat
certutil -hashfile x64_158.0.8127.89_chrome_installer_uncompressed.exe SHA256
```

### Windows ARM64

文件名：`arm64_158.0.8127.89_chrome_installer_uncompressed.exe`

```text
587aaf6bc0be6a2e481534537af43d591764b2704b2cf029a6f7535b7fa8e643
```

PowerShell（在文件所在目录执行）：

```powershell
Get-FileHash .\arm64_158.0.8127.89_chrome_installer_uncompressed.exe -Algorithm SHA256
```

CMD（可选）：

```bat
certutil -hashfile arm64_158.0.8127.89_chrome_installer_uncompressed.exe SHA256
```

### macOS x64

文件名：`x64_GoogleChrome-158.0.8127.89.dmg`

```text
f54426133e03ea9bf8dfd2d0f9226265fba2974dddc26e8bf99cf2890de6821e
```

macOS / Linux：

```bash
shasum -a 256 x64_GoogleChrome-158.0.8127.89.dmg
```

### Windows x64 (Chrome++)

文件名：`x64_158.0.8127.89_chrome.7z`（由工作流整合 [chrome_plus](https://github.com/Bush2021/chrome_plus) 自动生成，SHA-256 以 Release 附件实际下载结果为准）

PowerShell（在文件所在目录执行）：

```powershell
Get-FileHash .\x64_158.0.8127.89_chrome.7z -Algorithm SHA256
```

CMD（可选）：

```bat
certutil -hashfile x64_158.0.8127.89_chrome.7z SHA256
```

### Windows ARM64 (Chrome++)

文件名：`arm64_158.0.8127.89_chrome.7z`（由工作流整合 [chrome_plus](https://github.com/Bush2021/chrome_plus) 自动生成，SHA-256 以 Release 附件实际下载结果为准）

PowerShell（在文件所在目录执行）：

```powershell
Get-FileHash .\arm64_158.0.8127.89_chrome.7z -Algorithm SHA256
```

CMD（可选）：

```bat
certutil -hashfile arm64_158.0.8127.89_chrome.7z SHA256
```

</details>

## Notes

- 使用 7-Zip 解压并配合[chrome_plus](https://github.com/Bush2021/chrome_plus)以实现便携化使用。
- Tag 固定为 `latest`，每次版本更新时旧 Release 会被自动替换，仓库始终只保留一个 Release。
- `data.json` 保存了全部 13 个渠道/架构的原始响应（Stable / Beta / Dev / Canary × win x86/x64/arm64 / mac x64）
