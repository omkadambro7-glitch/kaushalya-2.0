# Kaushalya 2.0

Project workspace for Computer Vision (Ultralytics YOLO) and Arduino IoT integration.

## 🛠️ Installed Environment

- **Python**: 3.14 (Virtual Environment in `.venv/`)
- **Ultralytics**: 8.4.198 (YOLOv8 / YOLOv11)
- **PyTorch**: 2.15.0 with Apple Silicon MPS Hardware Acceleration
- **OpenCV**: 5.0.0
- **PySerial**: 3.5 (Arduino USB Communication)
- **Arduino IDE**: 2.3.10 (`/Applications/Arduino IDE.app`)
- **Arduino CLI**: 1.5.1 (`/opt/homebrew/bin/arduino-cli`)

## 🚀 Quick Start

1. **Verify Setup**:
   ```bash
   .venv/bin/python verify_setup.py
   ```

2. **Run YOLO & Arduino Bridge**:
   ```bash
   .venv/bin/python arduino_yolo_bridge.py
   ```

## 🔌 VS Code & Antigravity Configuration

- Automatically configured via [`.vscode/settings.json`](.vscode/settings.json).
- Default Python interpreter set to `${workspaceFolder}/.venv/bin/python`.
- Official Python & Arduino extensions installed in VS Code.
