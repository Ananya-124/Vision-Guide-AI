# Vision-Guide-AI
# VisionGuide - AI Navigation Assistant for Visually Impaired

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue.svg">
  <img src="https://img.shields.io/badge/YOLOv8-ultralytics-green.svg">
  <img src="https://img.shields.io/badge/OpenCV-4.0+-red.svg">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg">
</div>

<br>

<div align="center">
  <h3>AI-Powered Real-Time Object Detection & Voice Alert System</h3>
  <p>Helping visually impaired individuals navigate safely using computer vision</p>
</div>

---

## 📋 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Demo](#-demo)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Project Structure](#-project-structure)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [Team](#-team)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

---

## 🔍 Overview

**VisionGuide** is an AI-powered navigation assistant designed to help visually impaired individuals navigate their surroundings safely. The system uses a webcam to detect obstacles in real-time and provides voice alerts, enabling users to move independently.

This project was developed for **SkyHack 2.0**, a national-level hackathon organized by Astrakshaya, with support from Duality AI and Stepcraft.

---

## ✨ Features

### Core Features
- **Real-time Object Detection** - Detects people, vehicles, chairs, and other obstacles
- **Voice Alerts** - Clear audio warnings when obstacles are detected
- **Smart Filtering** - Only alerts for relevant obstacles (ignores background objects)
- **Cooldown System** - Prevents repeated alerts (5 seconds between announcements)
- **Confidence Threshold** - Ignores low-confidence detections (≥50% confidence)
- **Visual Feedback** - Bounding boxes with labels and confidence scores

### Advanced Features (Optional Version)
- **Distance Estimation** - Calculates approximate distance to obstacles
- **Priority Alerts** - "Immediate danger" vs "Caution" based on proximity
- **Multi-object Detection** - Detects and announces multiple objects at once

### Target Objects Detected
| Category | Objects |
|----------|---------|
| 👤 People | person |
| 🚗 Vehicles | car, bus, truck, motorcycle, bicycle |
| 🪑 Furniture | chair, bench |

---

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.9+** | Core programming language |
| **YOLOv8 (Ultralytics)** | Object detection model |
| **OpenCV** | Camera capture & image processing |
| **pyttsx3** | Text-to-speech voice alerts |
| **NumPy** | Numerical operations |

## 🎥 Demo
[Watch the Demo Video](https://drive.google.com/file/d/1Bfaa2iqy9_k6JvGM9z26AsV-rW0DIS1N/view?usp=sharing)









