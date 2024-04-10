const int IRSensorPins[4] = {A2, A3, A4, A5};

const int leftMotor1 = 4;
const int leftMotor2 = 5;
const int rightMotor1 = 11;
const int rightMotor2 = 10;
const int leftEn = 3;
const int rightEn = 9;

int leftSpeed = 0;
int rightSpeed = 0;

void setup() {
  Serial.begin(115200);
  for (int i = 0; i < 4; i++) {
    pinMode(IRSensorPins[i], INPUT);
  }

  pinMode(leftMotor1, OUTPUT);
  pinMode(leftMotor2, OUTPUT);
  pinMode(rightMotor1, OUTPUT);
  pinMode(rightMotor2, OUTPUT);
  pinMode(leftEn, OUTPUT);
  pinMode(rightEn, OUTPUT);

  digitalWrite(leftEn, LOW);
  digitalWrite(rightEn, LOW);

  pinMode(6, INPUT);
}

void loop() {
    
  int sensorValues[4] = {};
  for (int i = 0; i < 4; i++) {
    sensorValues[i] = digitalRead(IRSensorPins[i]);
  }

  if (sensorValues[1] == LOW || sensorValues[2] == LOW) {
    // Move forward
    digitalWrite(leftMotor1, HIGH);
    digitalWrite(leftMotor2, LOW);
    digitalWrite(rightMotor1, HIGH);
    digitalWrite(rightMotor2, LOW);
    leftSpeed = 160;
    rightSpeed = 160;
  } else if (sensorValues[3] == LOW){
    // Turn left
    digitalWrite(leftMotor1, LOW);
    digitalWrite(leftMotor2, HIGH);
    digitalWrite(rightMotor1, HIGH);
    digitalWrite(rightMotor2, LOW);
    leftSpeed =180;
    rightSpeed = 255;
  } else if (sensorValues[0] == LOW){
    // Turn right
    digitalWrite(leftMotor1, HIGH);
    digitalWrite(leftMotor2, LOW);
    digitalWrite(rightMotor1, LOW);
    digitalWrite(rightMotor2, HIGH);
    leftSpeed = 255;
    rightSpeed = 180;
  } else {
    // Stop
    digitalWrite(leftMotor1, LOW);
    digitalWrite(leftMotor2, LOW);
    digitalWrite(rightMotor1, LOW);
    digitalWrite(rightMotor2, LOW);
    leftSpeed = 0;
    rightSpeed = 0;
  }
  if(digitalRead(6)==HIGH){
  // Set the motor speeds
  analogWrite(leftEn, leftSpeed);
  analogWrite(rightEn, rightSpeed);
  }else{
    analogWrite(leftEn, 0);
    analogWrite(rightEn, 0);
    
  }
}
