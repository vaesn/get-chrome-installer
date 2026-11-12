# Google Chrome Offline Installers (Auto Update)

> Windows x64 / Windows ARM64 / macOS x64 — Stable 离线安装包，以及整合 [chrome_plus](https://github.com/Bush2021/chrome_plus) 的 Windows 便携版 `.7z`，定时同步 Google Update 服务并发布到本仓库 Release。

[打开最新 Release](https://github.com/vaesn/get-chrome-installer/releases/latest)

## Latest Stable

| Platform | Version | Size | Google Direct | GitHub Release Mirror | SHA-256 |
| -------- | ------- | ---- | ------------- | --------------------- | ------- |
| **Windows x64** | `157.0.8103.79` | 504.44 MB | [dl.google.com](https://dl.google.com/release2/chrome/acab3swyzqgszbsf6npoanqbvgvq_157.0.8103.79/157.0.8103.79_chrome_installer_uncompressed.exe) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/x64_157.0.8103.79_chrome_installer_uncompressed.exe) | <details><summary><code>acb77d39d1759408…</code></summary><code>acb77d39d1759408ad6f9874081c25e68cd042f1de6145064bbc9c2be4ad733e</code></details> |
| **Windows ARM64** | `157.0.8103.79` | 433.23 MB | [dl.google.com](https://dl.google.com/release2/chrome/acq6idvhxkcwr5otpuozd2yp6bia_157.0.8103.79/157.0.8103.79_chrome_installer_uncompressed.exe) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/arm64_157.0.8103.79_chrome_installer_uncompressed.exe) | <details><summary><code>b9342a5e718678ee…</code></summary><code>b9342a5e718678ee56ac876900672a54f7eff205c9178072b8a833d2bd09c910</code></details> |
| **macOS x64** | `157.0.8103.79` | 269.89 MB | [dl.google.com](https://dl.google.com/release2/chrome/adnzqttux77ny5bapr5n3fiap5cq_157.0.8103.79/GoogleChrome-157.0.8103.79.dmg) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/x64_GoogleChrome-157.0.8103.79.dmg) | <details><summary><code>eed1522d8c9ad5e8…</code></summary><code>eed1522d8c9ad5e86b51e76df01af451c7c2480cdb0d00a98794e546f9248a46</code></details> |
| **Windows x64 (Chrome++)** | `157.0.8103.79` | N/A | — | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/x64_157.0.8103.79_chrome.7z) | N/A |
| **Windows ARM64 (Chrome++)** | `157.0.8103.79` | N/A | — | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/arm64_157.0.8103.79_chrome.7z) | N/A |

> 带 **(Chrome++)** 后缀的行为整合 [chrome_plus](https://github.com/Bush2021/chrome_plus) 的便携版 `.7z`，由本仓库工作流在版本更新时自动打包，仅随 Release 提供；`Size` / `SHA-256` 请以 Release 附件实际信息为准。

## 校验方法

点击表格 SHA-256 列展开完整哈希，下载后与本地计算结果比对。

<details>
<summary><strong>命令行校验（点击展开）</strong></summary>

### Windows x64

文件名：`x64_157.0.8103.79_chrome_installer_uncompressed.exe`

```text
acb77d39d1759408ad6f9874081c25e68cd042f1de6145064bbc9c2be4ad733e
```

PowerShell（在文件所在目录执行）：

```powershell
Get-FileHash .\x64_157.0.8103.79_chrome_installer_uncompressed.exe -Algorithm SHA256
```

CMD（可选）：

```bat
certutil -hashfile x64_157.0.8103.79_chrome_installer_uncompressed.exe SHA256
```

### Windows ARM64

文件名：`arm64_157.0.8103.79_chrome_installer_uncompressed.exe`

```text
b9342a5e718678ee56ac876900672a54f7eff205c9178072b8a833d2bd09c910
```

PowerShell（在文件所在目录执行）：

```powershell
Get-FileHash .\arm64_157.0.8103.79_chrome_installer_uncompressed.exe -Algorithm SHA256
```

CMD（可选）：

```bat
certutil -hashfile arm64_157.0.8103.79_chrome_installer_uncompressed.exe SHA256
```

### macOS x64

文件名：`x64_GoogleChrome-157.0.8103.79.dmg`

```text
eed1522d8c9ad5e86b51e76df01af451c7c2480cdb0d00a98794e546f9248a46
```

macOS / Linux：

```bash
shasum -a 256 x64_GoogleChrome-157.0.8103.79.dmg
```

### Windows x64 (Chrome++)

文件名：`x64_157.0.8103.79_chrome.7z`（由工作流整合 [chrome_plus](https://github.com/Bush2021/chrome_plus) 自动生成，SHA-256 以 Release 附件实际下载结果为准）

PowerShell（在文件所在目录执行）：

```powershell
Get-FileHash .\x64_157.0.8103.79_chrome.7z -Algorithm SHA256
```

CMD（可选）：

```bat
certutil -hashfile x64_157.0.8103.79_chrome.7z SHA256
```

### Windows ARM64 (Chrome++)

文件名：`arm64_157.0.8103.79_chrome.7z`（由工作流整合 [chrome_plus](https://github.com/Bush2021/chrome_plus) 自动生成，SHA-256 以 Release 附件实际下载结果为准）

PowerShell（在文件所在目录执行）：

```powershell
Get-FileHash .\arm64_157.0.8103.79_chrome.7z -Algorithm SHA256
```

CMD（可选）：

```bat
certutil -hashfile arm64_157.0.8103.79_chrome.7z SHA256
```

</details>

## Notes

- 使用 7-Zip 解压并配合[chrome_plus](https://github.com/Bush2021/chrome_plus)以实现便携化使用。
- Tag 固定为 `latest`，每次版本更新时旧 Release 会被自动替换，仓库始终只保留一个 Release。
- `data.json` 保存了全部 13 个渠道/架构的原始响应（Stable / Beta / Dev / Canary × win x86/x64/arm64 / mac x64）
