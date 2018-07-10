int leftWhisker = 5;
int rightWhisker = 7;

void setup(){
    Serial.begin(9600);
    pinMode(leftWhisker, INPUT);
    pinMode(rightWhisker, INPUT);
}

void loop(){
    int leftWhiskerValue = digitalRead(leftWhisker);
    int rightWhiskerValue = digitalRead(rightWhisker);


    Serial.print("Left: ");
    Serial.print(leftWhiskerValue);
    Serial.print("Right: ");
    Serial.print(rightWhiskerValue);

    if (leftWhiskerValue == 0 && rightWhiskerValue == 0) {
        Serial.print("Left and Right pressed.");
    } else if (leftWhiskerValue == 0) {
        Serial.print("Left whisker pressed.");
    } else if (rightWhiskerValue == 0) {
        Serial.print("Right whisker pressed.");
    } else {
        Serial.print("No whiskers are pressed.");
    }
    Serial.println("");

    delay(100);
}
