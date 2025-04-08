import time
from object_detection import detect_objects_live
from haptic_feedback import give_haptic_feedback

# Predefined path: (direction, duration in sec)
PREDEFINED_PATH = [
    ("FORWARD", 5),
    ("RIGHT", 3),
    ("FORWARD", 4),
    ("LEFT", 2),
    ("FORWARD", 6),
]

def navigate():
    print("🚶 Navigating predefined path...\n")

    for step, (direction, duration) in enumerate(PREDEFINED_PATH):
        print(f"➡️ Step {step+1}: Move {direction} for {duration} sec")
        
        obstacle = detect_objects_live()
        
        if obstacle:
            print(f"⚠️ Obstacle detected: {obstacle}")
            handle_obstacle(obstacle)
        else:
            give_haptic_feedback(direction)
            time.sleep(duration)

    print("\n✅ Destination Reached!")

def handle_obstacle(obstacle):
    if obstacle in ["person", "vehicle"]:
        print("🔴 Auto-movable object detected. STOP!")
        give_haptic_feedback("STOP")
    else:
        print("🔄 Static obstacle detected. Re-routing...")
        give_haptic_feedback("LEFT")  # Example: Move left
