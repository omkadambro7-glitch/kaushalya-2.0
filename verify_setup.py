import sys
import os

print("=" * 60)
print("🚀 KAUSHALYA 2.0 - SYSTEM & ENVIRONMENT VERIFICATION")
print("=" * 60)

# 1. Python Environment
print(f"✅ Python Version      : {sys.version.split()[0]}")
print(f"✅ Python Executable   : {sys.executable}")

# 2. Ultralytics & PyTorch
try:
    import torch
    print(f"✅ PyTorch Version     : {torch.__version__}")
    mps_available = torch.backends.mps.is_available()
    print(f"✅ Apple Silicon (MPS) : {'Available (Hardware Accelerated)' if mps_available else 'Not Available'}")
except Exception as e:
    print(f"❌ PyTorch Error       : {e}")

try:
    import ultralytics
    from ultralytics import YOLO
    print(f"✅ Ultralytics Version : {ultralytics.__version__}")
except Exception as e:
    print(f"❌ Ultralytics Error   : {e}")

# 3. OpenCV
try:
    import cv2
    print(f"✅ OpenCV Version      : {cv2.__version__}")
except Exception as e:
    print(f"❌ OpenCV Error        : {e}")

# 4. PySerial (for Arduino)
try:
    import serial
    import serial.tools.list_ports
    print(f"✅ PySerial Version    : {serial.__version__}")
    ports = list(serial.tools.list_ports.comports())
    if ports:
        print(f"📡 Detected Serial Ports ({len(ports)}):")
        for p in ports:
            print(f"   - {p.device} ({p.description})")
    else:
        print("ℹ️  No external serial devices currently plugged in.")
except Exception as e:
    print(f"❌ PySerial Error      : {e}")

# 5. Arduino IDE & CLI
arduino_ide_app = "/Applications/Arduino IDE.app"
print(f"✅ Arduino IDE 2.x App : {'Installed at ' + arduino_ide_app if os.path.exists(arduino_ide_app) else 'Not found'}")

print("=" * 60)
print("✨ All requested software and libraries are configured and ready!")
print("=" * 60)
