# 🧠 Real-Time Person Detection and Tracking (YOLOv8 + DeepSORT)

This project implements a real-time person detection and multi-object tracking system using [YOLOv8](https://github.com/ultralytics/ultralytics) for object detection and [DeepSORT](https://github.com/mikel-brostrom/Yolov5_DeepSort_Pytorch) for assigning consistent IDs to detected people across frames. It works with both webcam input and video files.

---

## 🎯 Features

- 🔍 Detects people using YOLOv8 (Ultralytics)
- 🆔 Tracks individuals with unique, persistent IDs using DeepSORT
- 🖥 Supports real-time video and webcam input
- 🎯 Filters only "person" class detections
- ✅ Displays ID and bounding box for each tracked person
- 📦 Lightweight and easy to customize

---

## 📂 Project Structure

Person-Detector-and-Tracking/
├── deepsort.py # Main person detection and tracking script
├── requirements.txt # Python dependencies (optional)
└── README.md # This documentation






💡 Technologies Used
🧠 YOLOv8 (Ultralytics)

📦 DeepSORT (deep-sort-realtime)

🧪 OpenCV

⚙ Python, NumPy, PyTorch


---

## ⚙ Installation

### ✅ Step 1: Create and activate a virtual environment (recommended)

bash
python -m venv yoloenv
.\yoloenv\Scripts\activate       # Windows
# OR
source yoloenv/bin/activate     # macOS/Linux



pip install ultralytics opencv-python deep-sort-realtime
pip install torch torchvision numpy





# 🧠 Real-Time Person Detection and Tracking (YOLOv8 + DeepSORT)

This project implements a real-time person detection and multi-object tracking system using [YOLOv8](https://github.com/ultralytics/ultralytics) for object detection and [DeepSORT](https://github.com/mikel-brostrom/Yolov5_DeepSort_Pytorch) for assigning consistent IDs to detected people across frames. It works with both webcam input and video files.

---

## 🎯 Features

- 🔍 Detects people using YOLOv8 (Ultralytics)
- 🆔 Tracks individuals with unique, persistent IDs using DeepSORT
- 🖥 Supports real-time video and webcam input
- 🎯 Filters only "person" class detections
- ✅ Displays ID and bounding box for each tracked person
- 📦 Lightweight and easy to customize

---

## 📂 Project Structure

Person-Detector-and-Tracking/
├── deepsort.py # Main person detection and tracking script
├── requirements.txt # Python dependencies (optional)
└── README.md # This documentation






💡 Technologies Used
🧠 YOLOv8 (Ultralytics)

📦 DeepSORT (deep-sort-realtime)

🧪 OpenCV

⚙ Python, NumPy, PyTorch


---

## ⚙ Installation

### ✅ Step 1: Create and activate a virtual environment (recommended)

bash
python -m venv yoloenv
.\yoloenv\Scripts\activate       # Windows
# OR
source yoloenv/bin/activate     # macOS/Linux



pip install ultralytics opencv-python deep-sort-realtime
pip install torch torchvision numpy
