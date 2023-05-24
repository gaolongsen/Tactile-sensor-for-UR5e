#include <SoftwareSerial.h>
SoftwareSerial BTserial(2, 3); // RX | TX

int pressureAnalogPin = 0; //pin where our pressure pad is located.
int pressureAnalogPin2 = 2;
int pressureReading; //variable for storing our reading
int pressureReading2; //variable for storing our reading
int force1;
int force2;
int N2F;
//Adjust these if required.
//int noPressure = 5; //max value for no pressure on the pad
//int lightPressure = 100; //max value for light pressure on the pad
//int mediumPressure = 200; //max value for medium pressure on the pad
 
void setup(void) {
  Serial.begin(9600);
  BTserial.begin(9600);
}
 
void loop(void) {
  pressureReading = analogRead(pressureAnalogPin);
  pressureReading2 = analogRead(pressureAnalogPin2);
  force1 = map(pressureReading, 0, 2048, 0, 1000); 
  force2 = map(pressureReading2, 0, 2048, 0, 1000);
  N2F = force1 + force2;
  BTserial.println(N2F);
  delay(10);
}
