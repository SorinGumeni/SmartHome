#include "CommonDefines.h"


bool lightSensorCurrentstate  = false;
bool lightSensorPreviousstate = false;
int incomingByte = 0;

void setup() {
  pinMode(INSIDE_LIGHT_SENSOR, INPUT_PULLUP);// define pin as Input  sensor
  pinMode(INSIDE_LIGHT_LED, OUTPUT);    // declare led pin as output
  Serial.begin(9600); // Default communication rate of the Bluetooth module
}

void loop() {
  DIGITAL lightSensorValue = digitalRead(INSIDE_LIGHT_SENSOR);// read the sensor

  handleLightSensor(lightSensorValue);
}

void handleSerialEvent()
{
    if (Serial.available())
  {
    incomingByte = Serial.read();
    switch (incomingByte)
    {
      case 1:
        {
          digitalWrite(INSIDE_LIGHT_LED, HIGH);
        }
        break;
      case 2:
        {
          digitalWrite(INSIDE_LIGHT_LED, LOW);
        }
        break;
      case 3:
        {
          
        }
        break;
      case 4:
        {
          
        }
        break;
      default:
        break;
    }
  }
}

void handleLightSensor(DIGITAL value)
{
  if (value == HIGH)
  {
    lightSensorCurrentstate = true;
    if (lightSensorPreviousstate != lightSensorCurrentstate)
    {
      Serial.println("I_LIGHT_SENSORON");
    }
  }
  else
  {
    motionSensorCurrentstate = false;
    if (lightSensorPreviousstate != lightSensorCurrentstate)
    {
      Serial.println("I_LIGHT_SENSOROFF");
    }
  }
  lightSensorPreviousstate = lightSensorCurrentstate;
}
