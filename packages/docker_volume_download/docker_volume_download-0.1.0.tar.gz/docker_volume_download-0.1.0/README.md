# Docker Volume Backup (`dvpy`)

A lightweight CLI tool to **backup Docker volumes** and optionally upload them to **Google Drive**.  
Supports both **OAuth** and **Service Account** authentication.

---

## 📦 Features

- Backup Docker volumes to a local file.
- Upload backups directly to Google Drive.
- Support for OAuth and Service Account credentials.
- Simple CLI interface.

---

## 🔹 Getting Started

### 1. Install

Install the package directly:

```bash
    uv pip install docker_volume_download
```
### 2. Check Installation

```bash
    dvpy --version
```
### 3. User Guide
#### 1. Set up path to Client Secret

```bash
    dvpy --conf <path to credentials>
```
#### 2. Configure Google Drive Name
eg. https://drive.google.com/drive/folders/exampleid
```bash
    dvpy --folder <google-drive-folder-id>
```

#### 3.1  Download Docker Volume 
```bash
    dvpy -d <volume-name> <path-to-save>
```

### OR

#### 3.2  Download Docker Volume and Upload to Google Drive
```bash
    dvpy -d <volume-name> <path-to-save> --upload
```