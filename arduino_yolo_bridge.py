"""
Kaushalya 2.0 - Ultralytics YOLO & Arduino Communication Bridge
--------------------------------------------------------------
This script demonstrates:
1. Loading an Ultralytics YOLO model.
2. Detecting objects via webcam / image stream.
3. Sending trigger signals to Arduino over Serial.
"""

import time
import cv2
import serial
import serial.tools.list_ports
from ultralytics import YOLO

def find_arduino_port():
    """Auto-detect connected Arduino / USB serial port."""
    ports = serial.tools.list_ports.comports()
    for port in ports:
        # Common identifiers for Arduino on macOS
        if "usbmodem" in port.device.lower() or "usbserial" in port.device.lower() or "arduino" in port.description.lower():
            return port.device
    return None

def main():
    print("🔹 Initializing Kaushalya 2.0 Vision System...")
    
    # 1. Load YOLO model (pretrained nano model for lightweight real-time inference)
    print("🔹 Loading YOLOv8 nano model...")
    model = YOLO("yolov8n.pt")
    
    # 2. Check Arduino connection
    port = find_arduino_port()
    arduino = None
    if port:
        print(f"🔌 Connected to Arduino on port: {port}")
        arduino = serial.Serial(port, baudrate=9600, timeout=1)
        time.sleep(2)  # Wait for Arduino reboot
    else:
        print("⚠️  No physical Arduino detected right now. Running in Simulation / Vision mode.")

    print("🚀 System Ready! Open webcam or feed images to model.")

if __name__ == "__main__":
    main()
