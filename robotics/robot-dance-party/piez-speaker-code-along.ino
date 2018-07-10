


int piezoSensor = A0;
int threshold = 150;
int sensorReading = 0

void setup(){
    Serial.begin(9600);
}

void loop(){
    sensorReading = analogRead(piezoSensor);

    Serial.println(sensorReading);

    if (sensorReading >= threshold){
        Serial.println("Being pressed");
    } else {
        Serial.printlin("Not being pressed!");
    }
}
