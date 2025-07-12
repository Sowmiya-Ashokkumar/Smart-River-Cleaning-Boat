# 🌊 Smart River Cleaning Boat with Waste Segregation

A gesture-controlled smart boat designed to clean floating waste from water bodies and segregate it in real time using Raspberry Pi and Arduino.

---

## 🎯 Project Overview

This project tackles river and lake pollution through an embedded, remote-operated boat.  
It uses gesture control via mobile, real-time image processing, and an onboard segregation system powered by Arduino and Raspberry Pi.

---

## 🧠 System Architecture

- **Gesture Control:** J-Robot mobile app sends commands to Arduino via Bluetooth.
- **Motion Control:** Arduino handles DC motors and conveyor operation.
- **Image Processing:** Raspberry Pi classifies waste using OpenCV.
- **Waste Segregation:** Servo motors sort waste into bins.
- **Expandable Features:** Optional GPS, solar, and IoT monitoring.

---

## 🔩 Hardware Components

| Component              | Function                                              |
|------------------------|-------------------------------------------------------|
| Arduino Uno            | Controls motors, actuators and receives BT signals   |
| Raspberry Pi 3/4       | Image capture, OpenCV processing, GPIO control       |
| HC-05 Bluetooth Module | Gesture control communication                        |
| L298N Motor Driver     | Drives DC motors for movement                        |
| DC Motors              | Boat propulsion                                       |
| Servo Motor            | Waste segregation control                            |
| Pi Camera Module       | Captures real-time footage                           |
| IR/Ultrasonic Sensors  | (Optional) Obstacle detection                        |

---

## ⚙️ Working Process

1. Gesture from mobile → Bluetooth → Arduino  
2. Arduino drives motors and conveyor belt  
3. Raspberry Pi analyzes waste using camera and OpenCV  
4. Servo motor segregates waste into correct compartment

---

## 🧪 Raspberry Pi Detection Logic

- Captures image stream using Pi Camera  
- Applies basic color or shape-based filtering (OpenCV)  
- Classifies object type (e.g., plastic vs organic)  
- Uses GPIO to activate servo motors  
- Optionally expandable with ML (TensorFlow Lite)

---

## 💡 Key Features

- ✅ Multi-controller system: Arduino + Raspberry Pi  
- ✅ Gesture-based smart navigation  
- ✅ Real-time waste classification  
- ✅ Modular, portable, scalable  
- ✅ Compatible with solar and IoT extensions

---

## 🔭 Future Scope

- Solar-powered upgrades for energy autonomy  
- GPS-guided autonomous navigation  
- Live data monitoring via IoT dashboard  
- Enhanced object recognition using AI/ML  
- Collaboration with smart cities & river projects

---

## 📸 Media & Presentation

- 🎞️ **Demo Video:** _[To be uploaded]_  
- 📊 **Presentation Slides:** Smart_River_Cleaning_Boat_PPT.pptx  
- 🖼️ **System Diagrams & Flowcharts:** _[To be added]_  

---

## 📁 Project Structure

# Smart-River-Cleaning-Boat
A gesture-controlled river cleaning robot with Raspberry Pi-based waste detection and segregation.
