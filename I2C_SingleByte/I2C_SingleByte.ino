/* 
 * Ollie Langhorst
 * Robotics Research under Dr. Krauss
 * November 23 2015
 * Reference the wire library at www.arduino.cc/en/Reference/Wire
 */

#include <Wire.h>
int SLAVE_ADDRESS = 0x04;
int ledPin = 13;
int inByte;
boolean ledOn = false;
int n;
int numBytes = 1;

void setup() 
{
    pinMode(ledPin, OUTPUT);
    Wire.begin(SLAVE_ADDRESS);
    Wire.onReceive(read_single_byte);
    Wire.onRequest(echo_single_byte);
    Serial.begin(115200);
    Serial.print("I2C Single Byte testing 400KHz\n");
    	
    // initialize digital pin 7 as an output.
	DDRD |= _BV(PD7);
}

void loop()
{
}

void read_single_byte(int numBytes){
	PORTD |= _BV(PD7); //Toggle pin 7 high
	n = Wire.read();
}


void echo_single_byte(){
	n = n*n;
	Wire.write(n);
	PORTD &= ~_BV(PD7);		//Toggle pin 7 low
}
