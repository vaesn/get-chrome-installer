# Google Chrome Offline Installers (Auto Update)

> Windows x64 / Windows ARM64 / macOS x64 — Stable 离线安装包，以及整合 [chrome_plus](https://github.com/Bush2021/chrome_plus) 的 Windows 便携版 `.7z`，定时同步 Google Update 服务并发布到本仓库 Release。

[打开最新 Release](https://github.com/vaesn/get-chrome-installer/releases/latest)

## Latest Stable

| Platform | Version | Size | Google Direct | GitHub Release Mirror | SHA-256 |
| -------- | ------- | ---- | ------------- | --------------------- | ------- |
| **Windows x64** | `158.0.8127.37` | 511.63 MB | [dl.google.com](https://dl.google.com/release2/chrome/ad42hbny6imw7va3w7vi2faooxba_158.0.8127.37/158.0.8127.37_chrome_installer_uncompressed.exe) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/x64_158.0.8127.37_chrome_installer_uncompressed.exe) | <details><summary><code>e64285a90f7edb6e…</code></summary><code>e64285a90f7edb6e05b8178e6e5a0eca678a9fdd20e9f381416476829ba02a7a</code></details> |
| **Windows ARM64** | `158.0.8127.37` | 440.92 MB | [dl.google.com](https://dl.google.com/release2/chrome/acnf45ma7wksgqr74ua6ecjqei3q_158.0.8127.37/158.0.8127.37_chrome_installer_uncompressed.exe) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/arm64_158.0.8127.37_chrome_installer_uncompressed.exe) | <details><summary><code>9f408365bb33b709…</code></summary><code>9f408365bb33b709b79fae02ba156009e05a97f25db5801fa3340b7646b1376a</code></details> |
| **macOS x64** | `158.0.8127.37` | 275.87 MB | [dl.google.com](https://dl.google.com/release2/chrome/adjlqkdatakdaf7cb6umhxhjsp4q_158.0.8127.37/GoogleChrome-158.0.8127.37.dmg) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/x64_GoogleChrome-158.0.8127.37.dmg) | <details><summary><code>10d1268e3019190d…</code></summary><code>10d1268e3019190d7fd20d0a7a658a33cfaa5da5351ced1b46c16b7dfa7c5223</code></details> |
| **Windows x64 (Chrome++)** | `158.0.8127.37` | N/A | — | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/x64_158.0.8127.37_chrome.7z) | N/A |
| **Windows ARM64 (Chrome++)** | `158.0.8127.37` | N/A | — | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/arm64_158.0.8127.37_chrome.7z) | N/A |

> 带 **(Chrome++)** 后缀的行为整合 [chrome_plus](https://github.com/Bush2021/chrome_plus) 的便携版 `.7z`，由本仓库工作流在版本更新时自动打包，仅随 Release 提供；`Size` / `SHA-256` 请以 Release 附件实际信息为准。

## 校验方法

点击表格 SHA-256 列展开完整哈希，下载后与本地计算结果比对。

<details>
<summary><strong>命令行校验（点击展开）</strong></summary>

### Windows x64

文件名：`x64_158.0.8127.37_chrome_installer_uncompressed.exe`

```text
e64285a90f7edb6e05b8178e6e5a0eca678a9fdd20e9f381416476829ba02a7a
```

PowerShell（在文件所在目录执行）：

```powershell
Get-FileHash .\x64_158.0.8127.37_chrome_installer_uncompressed.exe -Algorithm SHA256
```

CMD（可选）：

```bat
certutil -hashfile x64_158.0.8127.37_chrome_installer_uncompressed.exe SHA256
```

### Windows ARM64

文件名：`arm64_158.0.8127.37_chrome_installer_uncompressed.exe`

```text
9f408365bb33b709b79fae02ba156009e05a97f25db5801fa3340b7646b1376a
```

PowerShell（在文件所在目录执行）：

```powershell
Get-FileHash .\arm64_158.0.8127.37_chrome_installer_uncompressed.exe -Algorithm SHA256
```

CMD（可选）：

```bat
certutil -hashfile arm64_158.0.8127.37_chrome_installer_uncompressed.exe SHA256
```

### macOS x64

文件名：`x64_GoogleChrome-158.0.8127.37.dmg`

```text
10d1268e3019190d7fd20d0a7a658a33cfaa5da5351ced1b46c16b7dfa7c5223
```

macOS / Linux：

```bash
shasum -a 256 x64_GoogleChrome-158.0.8127.37.dmg
```

### Windows x64 (Chrome++)

文件名：`x64_158.0.8127.37_chrome.7z`（由工作流整合 [chrome_plus](https://github.com/Bush2021/chrome_plus) 自动生成，SHA-256 以 Release 附件实际下载结果为准）

PowerShell（在文件所在目录执行）：

```powershell
Get-FileHash .\x64_158.0.8127.37_chrome.7z -Algorithm SHA256
```

CMD（可选）：

```bat
certutil -hashfile x64_158.0.8127.37_chrome.7z SHA256
```

### Windows ARM64 (Chrome++)

文件名：`arm64_158.0.8127.37_chrome.7z`（由工作流整合 [chrome_plus](https://github.com/Bush2021/chrome_plus) 自动生成，SHA-256 以 Release 附件实际下载结果为准）

PowerShell（在文件所在目录执行）：

```powershell
Get-FileHash .\arm64_158.0.8127.37_chrome.7z -Algorithm SHA256
```

CMD（可选）：

```bat
certutil -hashfile arm64_158.0.8127.37_chrome.7z SHA256
```

</details>

## Notes

- 使用 7-Zip 解压并配合[chrome_plus](https://github.com/Bush2021/chrome_plus)以实现便携化使用。
- Tag 固定为 `latest`，每次版本更新时旧 Release 会被自动替换，仓库始终只保留一个 Release。
- `data.json` 保存了全部 13 个渠道/架构的原始响应（Stable / Beta / Dev / Canary × win x86/x64/arm64 / mac x64）
