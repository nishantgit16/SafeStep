import pygame

def give_haptic_feedback(action):
    vibration_patterns = {
        "STOP": (1, 2000),  # Long vibration
        "MOVE LEFT": (1, 500),  # Short single
        "MOVE RIGHT": (2, 500),  # Double short
        "MOVE FORWARD": (2, 300),  # Speedy double
    }

    if action in vibration_patterns:
        count, duration = vibration_patterns[action]
        for _ in range(count):
            print(f"🔔 Haptic Feedback: {action}")
            pygame.time.wait(duration)
