# Google Chrome Offline Installers (Auto Update)

> Windows x64 / Windows ARM64 / macOS x64 — Stable 离线安装包，定时同步 Google Update 服务并发布到本仓库 Release。

[打开最新 Release](https://github.com/vaesn/get-chrome-installer/releases/latest)

## Latest Stable

| Platform | Version | Size | Google Direct | GitHub Release Mirror | SHA-256 |
| -------- | ------- | ---- | ------------- | --------------------- | ------- |
| **Windows x64** | `156.0.8078.80` | 500.97 MB | [dl.google.com](https://dl.google.com/release2/chrome/aczq54y7kwp55hzkkdtm7qgz2x6a_156.0.8078.80/156.0.8078.80_chrome_installer_uncompressed.exe) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/x64_156.0.8078.80_chrome_installer_uncompressed.exe) | <details><summary><code>43cca215206b634b…</code></summary><code>43cca215206b634b89d226ed71522c7f58c5430b8559b92e782dd7bd77add7cc</code></details> |
| **Windows ARM64** | `156.0.8078.80` | 426.87 MB | [dl.google.com](https://dl.google.com/release2/chrome/acpvmvph6azmnleo3any6quriw6a_156.0.8078.80/156.0.8078.80_chrome_installer_uncompressed.exe) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/arm64_156.0.8078.80_chrome_installer_uncompressed.exe) | <details><summary><code>f7a5713fcc6594e0…</code></summary><code>f7a5713fcc6594e006b0a73730bb1f846d09f92834cc0397ca692b61cb18461d</code></details> |
| **macOS x64** | `156.0.8078.80` | 266.08 MB | [dl.google.com](https://dl.google.com/release2/chrome/hmx6fwnspbytmrtkulm2cctvey_156.0.8078.80/GoogleChrome-156.0.8078.80.dmg) | [GitHub Release](https://v4.gh-proxy.org/https://github.com/vaesn/get-chrome-installer/releases/latest/download/x64_GoogleChrome-156.0.8078.80.dmg) | <details><summary><code>f805340c73f5e569…</code></summary><code>f805340c73f5e569124d0fd5e0c0b9a3eba81b76016198ea7703b349c0006d9a</code></details> |

## 校验方法

点击表格 SHA-256 列展开完整哈希，下载后与本地计算结果比对。

<details>
<summary><strong>命令行校验（点击展开）</strong></summary>

### Windows x64

文件名：`x64_156.0.8078.80_chrome_installer_uncompressed.exe`

```text
43cca215206b634b89d226ed71522c7f58c5430b8559b92e782dd7bd77add7cc
```

PowerShell（在文件所在目录执行）：

```powershell
Get-FileHash .\x64_156.0.8078.80_chrome_installer_uncompressed.exe -Algorithm SHA256
```

CMD（可选）：

```bat
certutil -hashfile x64_156.0.8078.80_chrome_installer_uncompressed.exe SHA256
```

### Windows ARM64

文件名：`arm64_156.0.8078.80_chrome_installer_uncompressed.exe`

```text
f7a5713fcc6594e006b0a73730bb1f846d09f92834cc0397ca692b61cb18461d
```

PowerShell（在文件所在目录执行）：

```powershell
Get-FileHash .\arm64_156.0.8078.80_chrome_installer_uncompressed.exe -Algorithm SHA256
```

CMD（可选）：

```bat
certutil -hashfile arm64_156.0.8078.80_chrome_installer_uncompressed.exe SHA256
```

### macOS x64

文件名：`x64_GoogleChrome-156.0.8078.80.dmg`

```text
f805340c73f5e569124d0fd5e0c0b9a3eba81b76016198ea7703b349c0006d9a
```

macOS / Linux：

```bash
shasum -a 256 x64_GoogleChrome-156.0.8078.80.dmg
```

</details>

## Notes

- 使用 7-Zip 解压并配合[chrome_plus](https://github.com/Bush2021/chrome_plus)以实现便携化使用。
- Tag 固定为 `latest`，每次版本更新时旧 Release 会被自动替换，仓库始终只保留一个 Release。
- `data.json` 保存了全部 13 个渠道/架构的原始响应（Stable / Beta / Dev / Canary × win x86/x64/arm64 / mac x64）
