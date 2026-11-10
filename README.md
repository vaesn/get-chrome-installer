# Google Chrome Offline Installers (Auto Update)

> Windows x64 / Windows ARM64 / macOS x64 — Stable 离线安装包，以及整合 [chrome_plus](https://github.com/Bush2021/chrome_plus) 的 Windows 便携版 `.7z`，定时同步 Google Update 服务并发布到本仓库 Release。

[打开最新 Release](https://github.com/vaesn/get-chrome-installer/releases/latest)

## Latest Stable

| Platform | Version | Size | Google Direct | GitHub Release Mirror | SHA-256 |
| -------- | ------- | ---- | ------------- | --------------------- | ------- |
| **Windows x64** | `157.0.8103.51` | 505.67 MB | [dl.google.com](https://dl.google.com/release2/chrome/hhb3n3my4axozv7qmzlcqqaspi_157.0.8103.51/157.0.8103.51_chrome_installer_uncompressed.exe) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/x64_157.0.8103.51_chrome_installer_uncompressed.exe) | <details><summary><code>cc7aca3546b69255…</code></summary><code>cc7aca3546b69255ecc2419c2cbfd51a21ed47837e953cf9d84ab60eca758d57</code></details> |
| **Windows ARM64** | `157.0.8103.51` | 433.2 MB | [dl.google.com](https://dl.google.com/release2/chrome/joakxwrgjhhcrkplqg7sgj2g2u_157.0.8103.51/157.0.8103.51_chrome_installer_uncompressed.exe) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/arm64_157.0.8103.51_chrome_installer_uncompressed.exe) | <details><summary><code>b6c2d0b1bcf0df79…</code></summary><code>b6c2d0b1bcf0df79d6d8940c64d8c29b966fc57c0ef989808529498a348fb0c1</code></details> |
| **macOS x64** | `157.0.8103.51` | 269.55 MB | [dl.google.com](https://dl.google.com/release2/chrome/n4ityugm3nsrjwv6gqod5juq4a_157.0.8103.51/GoogleChrome-157.0.8103.51.dmg) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/x64_GoogleChrome-157.0.8103.51.dmg) | <details><summary><code>0038dacc39b2cc4d…</code></summary><code>0038dacc39b2cc4d45ae7f4d2e70d2ef105277acff0100fa77be686a7813f60f</code></details> |
| **Windows x64 (Chrome++)** | `157.0.8103.51` | N/A | — | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/x64_157.0.8103.51_chrome.7z) | N/A |
| **Windows ARM64 (Chrome++)** | `157.0.8103.51` | N/A | — | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/arm64_157.0.8103.51_chrome.7z) | N/A |

> 带 **(Chrome++)** 后缀的行为整合 [chrome_plus](https://github.com/Bush2021/chrome_plus) 的便携版 `.7z`，由本仓库工作流在版本更新时自动打包，仅随 Release 提供；`Size` / `SHA-256` 请以 Release 附件实际信息为准。

## 校验方法

点击表格 SHA-256 列展开完整哈希，下载后与本地计算结果比对。

<details>
<summary><strong>命令行校验（点击展开）</strong></summary>

### Windows x64

文件名：`x64_157.0.8103.51_chrome_installer_uncompressed.exe`

```text
cc7aca3546b69255ecc2419c2cbfd51a21ed47837e953cf9d84ab60eca758d57
```

PowerShell（在文件所在目录执行）：

```powershell
Get-FileHash .\x64_157.0.8103.51_chrome_installer_uncompressed.exe -Algorithm SHA256
```

CMD（可选）：

```bat
certutil -hashfile x64_157.0.8103.51_chrome_installer_uncompressed.exe SHA256
```

### Windows ARM64

文件名：`arm64_157.0.8103.51_chrome_installer_uncompressed.exe`

```text
b6c2d0b1bcf0df79d6d8940c64d8c29b966fc57c0ef989808529498a348fb0c1
```

PowerShell（在文件所在目录执行）：

```powershell
Get-FileHash .\arm64_157.0.8103.51_chrome_installer_uncompressed.exe -Algorithm SHA256
```

CMD（可选）：

```bat
certutil -hashfile arm64_157.0.8103.51_chrome_installer_uncompressed.exe SHA256
```

### macOS x64

文件名：`x64_GoogleChrome-157.0.8103.51.dmg`

```text
0038dacc39b2cc4d45ae7f4d2e70d2ef105277acff0100fa77be686a7813f60f
```

macOS / Linux：

```bash
shasum -a 256 x64_GoogleChrome-157.0.8103.51.dmg
```

### Windows x64 (Chrome++)

文件名：`x64_157.0.8103.51_chrome.7z`（由工作流整合 [chrome_plus](https://github.com/Bush2021/chrome_plus) 自动生成，SHA-256 以 Release 附件实际下载结果为准）

PowerShell（在文件所在目录执行）：

```powershell
Get-FileHash .\x64_157.0.8103.51_chrome.7z -Algorithm SHA256
```

CMD（可选）：

```bat
certutil -hashfile x64_157.0.8103.51_chrome.7z SHA256
```

### Windows ARM64 (Chrome++)

文件名：`arm64_157.0.8103.51_chrome.7z`（由工作流整合 [chrome_plus](https://github.com/Bush2021/chrome_plus) 自动生成，SHA-256 以 Release 附件实际下载结果为准）

PowerShell（在文件所在目录执行）：

```powershell
Get-FileHash .\arm64_157.0.8103.51_chrome.7z -Algorithm SHA256
```

CMD（可选）：

```bat
certutil -hashfile arm64_157.0.8103.51_chrome.7z SHA256
```

</details>

## Notes

- 使用 7-Zip 解压并配合[chrome_plus](https://github.com/Bush2021/chrome_plus)以实现便携化使用。
- Tag 固定为 `latest`，每次版本更新时旧 Release 会被自动替换，仓库始终只保留一个 Release。
- `data.json` 保存了全部 13 个渠道/架构的原始响应（Stable / Beta / Dev / Canary × win x86/x64/arm64 / mac x64）
