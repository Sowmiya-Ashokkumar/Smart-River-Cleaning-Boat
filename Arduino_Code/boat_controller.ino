#include <Servo.h>
#include <SoftwareSerial.h>

#define LEFT_MOTOR_FORWARD  9
#define RIGHT_MOTOR_FORWARD 10
#define SERVO_PIN 6

Servo wasteServo;
SoftwareSerial bluetooth(2, 3); // RX, TX

char command;

void setup() {
  pinMode(LEFT_MOTOR_FORWARD, OUTPUT);
  pinMode(RIGHT_MOTOR_FORWARD, OUTPUT);
  bluetooth.begin(9600);
  wasteServo.attach(SERVO_PIN);
  wasteServo.write(90); // Neutral position
}

void loop() {
  if (bluetooth.available()) {
    command = bluetooth.read();
    handleGesture(command);
  }
}

void handleGesture(char cmd) {
  switch (cmd) {
    case 'F': // Forward
      digitalWrite(LEFT_MOTOR_FORWARD, HIGH);
      digitalWrite(RIGHT_MOTOR_FORWARD, HIGH);
      break;
    case 'S': // Stop
      digitalWrite(LEFT_MOTOR_FORWARD, LOW);
      digitalWrite(RIGHT_MOTOR_FORWARD, LOW);
      break;
    case 'L': // Turn Left
      digitalWrite(LEFT_MOTOR_FORWARD, LOW);
      digitalWrite(RIGHT_MOTOR_FORWARD, HIGH);
      break;
    case 'R': // Turn Right
      digitalWrite(LEFT_MOTOR_FORWARD, HIGH);
      digitalWrite(RIGHT_MOTOR_FORWARD, LOW);
      break;
    case 'D': // Dump Waste
      wasteServo.write(0);   // Move servo to dump bin
      delay(1500);
      wasteServo.write(90);  // Reset
      break;
  }
}
