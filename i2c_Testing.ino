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
int ids[] =  {1 ,  3 , 8 , 13 , 16 , 24 ,
        28 , 30 , 42 , 52 , 53 , 61 ,
        65 , 68 , 72 , 74 , 78 , 83 , 87 ,
        90 , 94 , 99 , 100 , 111 , 114 , 
        159 , 169 , 170 , 172 , 193 , 200 ,
        233 , 234 , 235 , 236 , 258 , 263 ,
        272 , 281 , 284 , 294 , 323 , 324 ,
        332 , 334 , 354 , 363 , 367 , 377 ,
        395 , 418 , 505 , 509 , 512 , 535 , 
        538 , 602 , 630 , 632 , 656 , 706 , 
        739 , 752 , 759 , 765 , 831 , 846 ,
        866 , 888 , 889 , 916 , 920 , 998};

void setup() {
  Wire.begin(); // join i2c bus (address optional for master)
  Serial.begin(9600);
  radio.begin();
  radio.openReadingPipe(1,pipe);
  radio.startListening();
}

byte x = 0;

void loop() {

  Reading r;
  r.id = float(ids[random(0 , 73)]);
  r.measurement = float(random(25 , 255));
  Serial.print(r.id);
  Serial.print(" ");
  Serial.println(r.measurement);
  sendReading(r);
  delay(60000);
}


void sendReading(Reading r){
  Wire.beginTransmission(GATEWAY_ADDR); // transmit to device #8
  Wire.write((byte *) &r, sizeof(r));
  Wire.endTransmission();    // stop transmitting
}
