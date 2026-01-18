import random
import time

def mood_detector():
    moods = [
        "focused",
        "confused",
        "dangerously productive",
        "pretending to work",
        "about to google something obvious"
    ]
    
    print("Analyzing system vibes...")
    time.sleep(1.5)

    mood = random.choice(moods)
    confidence = random.randint(42, 99)

    print(f"Current mood detected: {mood}")
    print(f"Confidence level: {confidence}%")

    if confidence < 60:
        print("Recommendation: coffee.")
    else:
        print("Recommendation: ship the code.")

if __name__ == "__main__":
    mood_detector()
