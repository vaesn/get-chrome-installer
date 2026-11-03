# Google Chrome Offline Installers (Auto Update)

> Windows x64 / Windows ARM64 / macOS x64 — Stable 离线安装包，定时同步 Google Update 服务并发布到本仓库 Release。

[打开最新 Release](https://github.com/vaesn/get-chrome-installer/releases/latest)

## Latest Stable

| Platform | Version | Size | Google Direct | GitHub Release Mirror | SHA-256 |
| -------- | ------- | ---- | ------------- | --------------------- | ------- |
| **Windows x64** | `157.0.8103.39` | 505.67 MB | [dl.google.com](https://dl.google.com/release2/chrome/lzz46e6auim6sx75xrn7xp5hza_157.0.8103.39/157.0.8103.39_chrome_installer_uncompressed.exe) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/x64_157.0.8103.39_chrome_installer_uncompressed.exe) | <details><summary><code>389b9e21de9a520a…</code></summary><code>389b9e21de9a520a6e24ba807ee8760409ccc837457bbcc460d2fdce0d5e8df5</code></details> |
| **Windows ARM64** | `157.0.8103.39` | 433.2 MB | [dl.google.com](https://dl.google.com/release2/chrome/b5nkgc5ojnyxf6fup2lbg7wu2i_157.0.8103.39/157.0.8103.39_chrome_installer_uncompressed.exe) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/arm64_157.0.8103.39_chrome_installer_uncompressed.exe) | <details><summary><code>b78eb6f41328178f…</code></summary><code>b78eb6f41328178fe5051959daf3a4193b10721e89bb7932228911a9f4b36fca</code></details> |
| **macOS x64** | `157.0.8103.39` | 269.53 MB | [dl.google.com](https://dl.google.com/release2/chrome/lj4mgpdwdwirchvgzajx46etji_157.0.8103.39/GoogleChrome-157.0.8103.39.dmg) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/x64_GoogleChrome-157.0.8103.39.dmg) | <details><summary><code>c4cd9a7c35b60ae0…</code></summary><code>c4cd9a7c35b60ae05ddb7f1ec3fce4911636e1bad0cacb99e1a2ea1ff2013105</code></details> |

## 校验方法

点击表格 SHA-256 列展开完整哈希，下载后与本地计算结果比对。

<details>
<summary><strong>命令行校验（点击展开）</strong></summary>

### Windows x64

文件名：`x64_157.0.8103.39_chrome_installer_uncompressed.exe`

```text
389b9e21de9a520a6e24ba807ee8760409ccc837457bbcc460d2fdce0d5e8df5
```

PowerShell（在文件所在目录执行）：

```powershell
Get-FileHash .\x64_157.0.8103.39_chrome_installer_uncompressed.exe -Algorithm SHA256
```

CMD（可选）：

```bat
certutil -hashfile x64_157.0.8103.39_chrome_installer_uncompressed.exe SHA256
```

### Windows ARM64

文件名：`arm64_157.0.8103.39_chrome_installer_uncompressed.exe`

```text
b78eb6f41328178fe5051959daf3a4193b10721e89bb7932228911a9f4b36fca
```

PowerShell（在文件所在目录执行）：

```powershell
Get-FileHash .\arm64_157.0.8103.39_chrome_installer_uncompressed.exe -Algorithm SHA256
```

CMD（可选）：

```bat
certutil -hashfile arm64_157.0.8103.39_chrome_installer_uncompressed.exe SHA256
```

### macOS x64

文件名：`x64_GoogleChrome-157.0.8103.39.dmg`

```text
c4cd9a7c35b60ae05ddb7f1ec3fce4911636e1bad0cacb99e1a2ea1ff2013105
```

macOS / Linux：

```bash
shasum -a 256 x64_GoogleChrome-157.0.8103.39.dmg
```

</details>

## Notes

- 使用 7-Zip 解压并配合[chrome_plus](https://github.com/Bush2021/chrome_plus)以实现便携化使用。
- Tag 固定为 `latest`，每次版本更新时旧 Release 会被自动替换，仓库始终只保留一个 Release。
- `data.json` 保存了全部 13 个渠道/架构的原始响应（Stable / Beta / Dev / Canary × win x86/x64/arm64 / mac x64）
