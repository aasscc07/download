#include<Servo.h>

Servo servo;
const int  analogPin = A0;
const int  servoPin = 9; 
void setup() {

  // put your setup code here, to run once:
  servo.attach(servoPin);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    int command = Serial.parseInt();
    if (command == 1) {
      servo.write(90);
      delay(500);
      servo.write(0);
    }
    else if(command == 0) {
      servo.write(0);
    }
  }
  int sensorValue = analogRead(analogPin);
  Serial.println(sensorValue);
  delay(1000);
}
