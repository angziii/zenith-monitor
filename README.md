# 🧘 Zenith Monitor - AI Focus Tracking Assistant

> **Empower your concentration with AI. Make distractions visible.**

Zenith Monitor is a futuristic productivity tool built with Computer Vision (AI) and system monitoring. It real-time tracks your posture, gaze, and screen content to intelligently determine if you're in a "Deep Work" state or "Slacking Off."

---

## ✨ Core Features

*   **🤖 AI Gaze Tracking**: Powered by MediaPipe Face Mesh, it detects head orientation and eye direction in real-time.
*   **📱 Glance Detection**: Optimized algorithms to catch "stealthy" phone usage. Even if your head remains still, looking down triggers a focus penalty.
*   **🖥️ Active Window Monitoring**: Real-time integration with macOS to identify the frontmost app. Slacking apps like YouTube, Bilibili, or Steam cause scores to plummet instantly.
*   **📊 Cyberpunk Dashboard**: A premium, glassmorphic web UI with smooth animations and instant visual alerts.
*   **🔌 Smart Heartbeat**: Backend automatically releases system resources and ports 30 seconds after the webpage is closed.

## 🛠️ Tech Stack

*   **Backend**: Python 3.12 + FastAPI
*   **Vision Engine**: MediaPipe Face Landmarker (Tasks API)
*   **Frontend**: HTML5 + Vanilla CSS3 (Glassmorphism) + JavaScript
*   **System Bridge**: AppleScript (for macOS window tracking)

---

## 🚀 Quick Start (macOS)

Designed for users with zero programming background.

### 1. Prerequisites
Ensure you have **Python 3** installed on your Mac.

### 2. Launch the Project
1. Clone or download this repository.
2. Locate the file **`start.command`** in the project folder.
3. **Double-click** to run. The script will automatically install dependencies, download the AI model, and open the dashboard in your browser.
4. Grant **Camera** and **Accessibility** permissions when prompted.

### 3. Usage
*   **Green State**: Stay focused on the screen; scores remain above 80%.
*   **Slacking Alerts**: Looking away, staring at your phone, or switching to recreational apps triggers the red **SLACKING DETECTED** warning.

---

## ⚙️ Customization

Tailor the monitor to your needs:

*   **Slacking Apps**: Edit the `self.slacking_apps` list in `screen_monitor.py`.
*   **Sensitivity**: Adjust `yaw_threshold` or `eye_penalty` in `vision_engine.py`.

---

## 🔒 Privacy

*   **100% Local**: All AI calculations are performed on your machine. **No** image or video data is ever uploaded to the cloud.
*   **Open Source**: Transparent code for full auditability.

---

# 🧘 Zenith Monitor - AI 摸鱼监测助手

> **用 AI 守护你的专注力，让摸鱼无所遁形。**

Zenith Monitor 是一款基于计算机视觉（AI）和系统监控的有趣工具。它能够通过摄像头实时监测你的坐姿、视线以及电脑屏幕内容，自动判断你是在专注工作还是在悄悄“摸鱼”。

---

## ✨ 核心功能

*   **🤖 AI 视线追踪**：利用 MediaPipe 脸部网格技术，实时检测你的头部朝向和眼神位置。
*   **📱 低头检测**：专门针对“低头看手机”行为进行了算法优化，即使头不动，眼神游离也会被发现。
*   **🖥️ 屏幕应用监控**：实时获取 macOS 当前活动窗口，当你打开 Bilibili、Steam 或 YouTube 时，专注分值会暴跌。
*   **📊 赛博朋克仪表盘**：全动态网页设计，支持实时分值显示、平滑动画和摸鱼预警。
*   **🔌 智能启停**：后端具备自动心跳检测，关闭网页 30 秒后自动释放系统资源和端口。

## 🛠️ 技术栈

*   **后端**: Python 3.12 + FastAPI
*   **视觉算法**: MediaPipe Face Landmarker (Tasks API)
*   **前端**: HTML5 + CSS3 (Glassmorphism / 玻璃拟态设计) + Vanilla JavaScript
*   **系统交互**: AppleScript (用于 macOS 应用监控)

---

## 🚀 快速开始 (macOS)

为了让普通用户也能快速上手，我们提供了点击即用的脚本。

### 1. 准备工作
请确保你的 Mac 已安装 **Python 3**。

### 2. 启动项目
1. 下载或克隆本项目到本地。
2. 打开文件夹，找到 **`start.command`** 文件。
3. **双击运行**。脚本会自动帮你安装所有依赖并打开浏览器，你只需在系统提示时允许“摄像头”和“辅助功能”权限。

### 3. 使用方法
*   **绿色状态**: 盯着屏幕工作，分值保持在 80% 以上。
*   **复警报**: 当你完全看向侧面、低头玩手机或打开了预设的“摸鱼 App”时，屏幕会闪红并提示 **SLACKING DETECTED**。

---

## ⚙️ 自定义配置

你可以通过修改以下文件来个性化你的监测助手：

*   **摸鱼 App 列表**: 修改 `screen_monitor.py` 中的 `self.slacking_apps`。
*   **监测灵敏度**: 在 `vision_engine.py` 中调整 `yaw_threshold` 和 `eye_penalty` 参数。

---

## 🔒 隐私声明

*   本工具的所有 AI 运算均在本地完成，**不会**上传任何图像或视频数据到云端。

---

*Made with ❤️ for Productive People.*
