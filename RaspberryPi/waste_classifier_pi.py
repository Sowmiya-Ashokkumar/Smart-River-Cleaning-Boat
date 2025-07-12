import cv2
import RPi.GPIO as GPIO
import time

# Setup
PLASTIC_SERVO = 17
ORGANIC_SERVO = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(PLASTIC_SERVO, GPIO.OUT)
GPIO.setup(ORGANIC_SERVO, GPIO.OUT)

plastic_pwm = GPIO.PWM(PLASTIC_SERVO, 50)
organic_pwm = GPIO.PWM(ORGANIC_SERVO, 50)
plastic_pwm.start(0)
organic_pwm.start(0)

def classify_and_act(image):
    # Dummy classification based on color (blue = plastic, green = organic)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    plastic_mask = cv2.inRange(hsv, (100, 150, 0), (140, 255, 255))
    organic_mask = cv2.inRange(hsv, (40, 40, 40), (70, 255, 255))

    if cv2.countNonZero(plastic_mask) > 500:
        print("Plastic detected")
        activate_servo(plastic_pwm)
    elif cv2.countNonZero(organic_mask) > 500:
        print("Organic detected")
        activate_servo(organic_pwm)
    else:
        print("Unknown or no waste detected")

def activate_servo(pwm):
    pwm.ChangeDutyCycle(5)  # Move to position
    time.sleep(1.5)
    pwm.ChangeDutyCycle(0)  # Reset position
    time.sleep(0.5)

def main():
    cam = cv2.VideoCapture(0)
    try:
        while True:
            ret, frame = cam.read()
            if not ret:
                break
            classify_and_act(frame)
            cv2.imshow("Waste Camera", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cam.release()
        cv2.destroyAllWindows()
        GPIO.cleanup()

if __name__ == "__main__":
    main()
