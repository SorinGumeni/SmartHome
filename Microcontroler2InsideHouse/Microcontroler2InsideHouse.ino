#include "CommonDefines.h"

DIGITAL motionSensorVal = 0;
DIGITAL lightSensorValue = 0; 
int tempSensorValue;
int previousTempValue = 0 ;

bool lightSensorCurrentstate  = false;
bool lightSensorPreviousstate = false;

bool motionSensorCurrentstate  = false;
bool motionSensorPreviousstate = false;


char incomingByte = 0;

void setup() 
{
  pinMode(INSIDE_LIGHT_SENSOR, INPUT);// define pin as Input  sensor
  pinMode(INSIDE_MOTION_SENSOR, INPUT);
  pinMode(INSIDE_LIGHT_LED, OUTPUT);    // declare led pin as output
  Serial.begin(9600); // Default communication rate of the Bluetooth module
}

void loop() 
{
  //////////////////// READ SENSOR VALUES ///////////////////////		
  lightSensorValue = digitalRead(INSIDE_LIGHT_SENSOR);// read the sensor
  tempSensorValue = analogRead(INSIDE_TEMP_SENSOR);
  motionSensorVal = digitalRead(INSIDE_MOTION_SENSOR);  // read input value
  
  //////////////////// SEND SENSOR STATE THROUGH SERIAL ///////////////////////
  handleTempSensor(tempSensorValue);
  handleLightSensor(lightSensorValue);
  
    //////////////////// CHECK FOR SERIAL EVENTS ///////////////////////
  handleSerialEvent();
}

void handleSerialEvent()
{
    if (Serial.available())
  {
    incomingByte = Serial.read();
    switch (incomingByte)
    {
      case '1':
        {
          digitalWrite(INSIDE_LIGHT_LED, HIGH);
        }
        break;
        
      case '2':
        {
          digitalWrite(INSIDE_LIGHT_LED, LOW);
        }
        break;
        
      case '3':
        {
          
        }
        break;
        
      case '4':
        {
          
        }
        break;
      default:
        break;
    }
  }
}

void handleMotionSensor(DIGITAL value)
{
  if (value == HIGH)
  {
    motionSensorCurrentstate = true;
    if (motionSensorPreviousstate != motionSensorCurrentstate)
    {
      Serial.println(I_MOTION_SENSOR_ON);
    }

  }
  else
  {
    motionSensorCurrentstate = false;
    if (motionSensorPreviousstate != motionSensorCurrentstate)
    {
      Serial.println(I_MOTION_SENSOR_OFF);
    }
  }
  motionSensorPreviousstate = motionSensorCurrentstate;
}

void handleLightSensor(DIGITAL value)
{
  if (value == HIGH)
  {
    lightSensorCurrentstate = true;
    if (lightSensorPreviousstate != lightSensorCurrentstate)
    {
      Serial.println(I_LIGHT_SENSOR_HIGH);
    }
  }
  else
  {
    lightSensorCurrentstate = false;
    if (lightSensorPreviousstate != lightSensorCurrentstate)
    {
      Serial.println(I_LIGHT_SENSOR_LOW);
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
  int intTemp = (int) Temp;
  if(previousTempValue != intTemp)
  {
    Serial.print("I_TEMP_SESOR_VAL");
    Serial.println(intTemp);
    previousTempValue = intTemp;
  }
}
