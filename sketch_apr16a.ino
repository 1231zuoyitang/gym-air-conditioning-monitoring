#include <Wire.h>
#include "Adafruit_SHT31.h"

Adafruit_SHT31 sht31 = Adafruit_SHT31();

void setup() {
  Serial.begin(9600);

  if (!sht31.begin(0x44)) {
    Serial.println("SHT31 not found");
    while (1) delay(1);
  }

  Serial.println("SHT31 ready");
}

void loop() {
  float t = sht31.readTemperature();
  float h = sht31.readHumidity();

  if (!isnan(t) && !isnan(h)) {
    Serial.print(t);
    Serial.print(",");
    Serial.println(h);
  } else {
    Serial.println("NaN,NaN");
  }

  delay(5000);
}