// Wire Master Writer
// by Nicholas Zambetti <http://www.zambetti.com>

// Demonstrates use of the Wire library
// Writes data to an I2C/TWI slave device
// Refer to the "Wire Slave Receiver" example for use with this

// Created 29 March 2006

// This example code is in the public domain.

#define GATEWAY_ADDR 9

#include <Wire.h>
struct Reading{
  float id;
  float measurement;
};

void setup() {
  Wire.begin(); // join i2c bus (address optional for master)
  Serial.begin(9600);
}

byte x = 0;

void loop() {
  Reading r;
  r.id = random(0 , 25);
  r.measurement = random(20 , 50);
  sendReading(r);
  delay(2000);
}


void sendReading(Reading r){
  Wire.beginTransmission(GATEWAY_ADDR); // transmit to device #8
  Wire.write((byte *) &r, sizeof(r));
  Wire.endTransmission();    // stop transmitting
}
