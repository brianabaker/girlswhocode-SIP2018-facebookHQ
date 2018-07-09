#include<Servo.h>
Servo servoLeft;
Servo servoRight;
void setup() {
  // put your setup code here, to run once:
    pinMode(10, INPUT);  pinMode(9, OUTPUT);   // Left IR LED & Receiver
    pinMode(3, INPUT);  pinMode(2, OUTPUT);    //Right

    Serial.begin(9600);
//    servoLeft.attach(13);
    servoRight.attach(12);
//    servoLeft.writeMicroseconds(1500);
    servoRight.writeMicroseconds(1500);

}
void loop() {
  // put your main code here, to run repeatedly:
  int irLeft = irDetect(9, 10, 20000);       // Check for object
  Serial.println(irLeft);                    // Display 1/0 no detect/detect
  delay(100);                                // 0.1 second delay
  int irRight = irDetect(3, 2, 20000);
  Serial.println(irRight);
  delay(100);

  servoLeft.writeMicroseconds(1700);         // Left wheel counterclockwise
  servoRight.writeMicroseconds(1300);        // Right wheel clockwise
  delay(3000);

// if((irLeft == 0) && (irRight == 0))        // If both sides detect
// {
//   backward(1000);                          // Back up 1 second
//   turnLeft(800);                           // Turn left about 120 degrees
// }
// else if(irLeft == 0)                       // If only left side detects
// {
//   backward(1000);                          // Back up 1 second
//   turnRight(400);                          // Turn right about 60 degrees
// }
// else if(irRight == 0)                      // If only right side detects
// {
//   backward(1000);                          // Back up 1 second
//   turnLeft(400);                           // Turn left about 60 degrees
// }
// else                                       // Otherwise, no IR detected
// {
//   forward(20);                             // Forward 1/50 of a second
// }
}
int irDetect(int irLedPin, int irReceiverPin, long frequency)
{
 tone(irLedPin, frequency, 8);              // IRLED 38 kHz for at least 1 ms
 delay(1);                                  // Wait 1 ms
 int ir = digitalRead(irReceiverPin);       // IR receiver -> ir variable
 delay(1);                                  // Down time before recheck
 return ir;                                 // Return 1 no detect, 0 detect
}
void forward(int time)                       // Forward function
{
 servoLeft.writeMicroseconds(1700);         // Left wheel counterclockwise
 servoRight.writeMicroseconds(1300);        // Right wheel clockwise
 delay(time);                               // Maneuver for time ms
}
void turnLeft(int time)                      // Left turn function
{
 servoLeft.writeMicroseconds(1300);         // Left wheel clockwise
 servoRight.writeMicroseconds(1300);        // Right wheel clockwise
 delay(time);                               // Maneuver for time ms
}
void turnRight(int time)                     // Right turn function
{
 servoLeft.writeMicroseconds(1700);         // Left wheel counterclockwise
 servoRight.writeMicroseconds(1700);        // Right wheel counterclockwise
 delay(time);                               // Maneuver for time ms
}
void backward(int time)                      // Backward function
{
 servoLeft.writeMicroseconds(1300);         // Left wheel clockwise
 servoRight.writeMicroseconds(1700);        // Right wheel counterclockwise
 delay(time);                               // Maneuver for time ms
}
