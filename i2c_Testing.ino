// Wire Master Writer
// by Nicholas Zambetti <http://www.zambetti.com>

// Demonstrates use of the Wire library
// Writes data to an I2C/TWI slave device
// Refer to the "Wire Slave Receiver" example for use with this

// Created 29 March 2006

// This example code is in the public domain.
#include <SPI.h>
#include "nRF24L01.h"
#include "RF24.h"
#include <Wire.h>

#define GATEWAY_ADDR 9
int msg[1];
RF24 radio(9,10);
const uint64_t pipe = 0xE8E8F0F0E1LL;

struct Reading{
  float id;
  float measurement;
};

void setup() {
  Wire.begin(); // join i2c bus (address optional for master)
  Serial.begin(9600);
  radio.begin();
  radio.openReadingPipe(1,pipe);
  radio.startListening();
}

byte x = 0;

void loop() {
  if (radio.available()){
    int done = 0;    
    while (done == 0){
      radio.read(msg, 1);     
      done = 1;
      // display recieved data, mapping is done for my water container
      Serial.print("Water Level: "); 
      Serial.print(-5*(msg[0]-17));
      Serial.println("%");
      delay(10);
    }
  }





  
  Reading r;
  r.id = random(0 , 25);
  r.measurement = (float) msg[0];
  sendReading(r);
  delay(2000);
}


void sendReading(Reading r){
  Wire.beginTransmission(GATEWAY_ADDR); // transmit to device #8
  Wire.write((byte *) &r, sizeof(r));
  Wire.endTransmission();    // stop transmitting
}
