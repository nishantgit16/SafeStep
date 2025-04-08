#  SafeStep: Smart Wearable Navigation System for Deafblind Users

**SafeStep** is an intelligent wearable system designed to assist **deafblind individuals** in safely navigating both **indoor and outdoor** environments. It combines real-time **object detection**, **ultrasonic sensing**, and **haptic feedback** to ensure obstacle-free movement without relying on auditory or visual cues.

##  Project Overview

SafeStep consists of two wearable modules:

-  **Waist-Worn Belt**:
  - Equipped with a **Raspberry Pi Camera**, **ultrasonic sensors**, and a **Raspberry Pi 5**
  - Captures live video and distance data to detect and classify obstacles
  - Processes information to determine whether the path is clear or blocked
  - Decides the path based on the processed information whether to re-route the path or continue on current path

-  **Wristband Feedback Unit**:
  - Contains a **vibration motor** and **Bluetooth/serial module**
  - Delivers real-time haptic feedback based on the user's surroundings and intended direction

##  Key Features

-  Real-time obstacle detection (camera + ultrasonic sensors)
-  Supports **dynamic or predefined paths**
-  Differentiates between **static** and **movable** obstacles
-  Provides intuitive **vibrational feedback**:
  - **Long Vibration** → STOP (movable obstacle like a person or vehicle)
  - **Single Short Vibration** → MOVE LEFT
  - **Double Short Vibration** → MOVE RIGHT
  - **Fast Double Vibration** → MOVE FORWARD
-  Haptic guidance for **both indoor and outdoor** navigation
-  Automatic re-routing when static obstacles are detected
-  Modular and easy-to-wear design


