#include "CommonDefines.h"


bool lightSensorCurrentstate  = false;
bool lightSensorPreviousstate = false;
int incomingByte = 0;

void setup() 
{
  pinMode(INSIDE_LIGHT_SENSOR, INPUT_PULLUP);// define pin as Input  sensor
  pinMode(INSIDE_LIGHT_LED, OUTPUT);    // declare led pin as output
  Serial.begin(9600); // Default communication rate of the Bluetooth module
}

void loop() 
{
  DIGITAL lightSensorValue = digitalRead(INSIDE_LIGHT_SENSOR);// read the sensor
  int tempSensorValue = analogRead(INSIDE_TEMP_SENSOR);

  handleTempSensor(tempSensorValue);
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

void handleTempSensor(int value) 
{
  double Temp;
  Temp = log(((10240000/value) - 10000));
  Temp = 1 / (0.001129148 + (0.000234125 + (0.0000000876741 * Temp * Temp ))* Temp );
  Temp = Temp - 273.15;// Convert Kelvin to Celcius
  Serial.print("I_TEMP_SESOR_VAL");
  Serial.println(Temp);
}
