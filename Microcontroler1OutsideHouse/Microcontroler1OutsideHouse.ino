#include "CommonDefines.h"


bool motionSensorCurrentstate  = false;
bool motionSensorPreviousstate = false;

bool lightSensorCurrentstate  = false;
bool lightSensorPreviousstate = false;

char incomingByte = 0;
DIGITAL motionSensorVal = 0;
DIGITAL lightSensorVal = 0;      

void setup()
{
  pinMode(OUTSIDE_MOTION_SENSOR, INPUT);  // declare motion sensor pin as input
  pinMode(OUTSIDE_LIGHT_SENSOR, INPUT);  // declare motion sensor pin as input
  pinMode(OUTSIDE_MOTION_LED, OUTPUT);	  // declare led pin as output
  pinMode(OUTSIDE_MOTION_BUZZER, OUTPUT); // declare buzzer pin as ouput
  Serial.begin(9600); // Default communication rate of the Serial connection
}
void loop() 
{
  //////////////////// READ SENSOR VALUES ///////////////////////			
  motionSensorVal = digitalRead(OUTSIDE_MOTION_SENSOR);  // read input value
  lightSensorVal  = digitalRead(OUTSIDE_LIGHT_SENSOR);
  
  //////////////////// SEND SENSOR STATE THROUGH SERIAL ///////////////////////
  handleMotionSensor(motionSensorVal);
  handleLightSensor(lightSensorVal);
  
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
          digitalWrite(OUTSIDE_MOTION_LED, HIGH);
        }
        break;
      case '2':
        {
          digitalWrite(OUTSIDE_MOTION_LED, LOW);
        }
        break;
      case '3':
        {
          digitalWrite(OUTSIDE_MOTION_BUZZER, HIGH);
        }
        break;
      case '4':
        {
          digitalWrite(OUTSIDE_MOTION_BUZZER, LOW);
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
      Serial.println(O_MOTION_SENSOR_ON);
    }

  }
  else
  {
    motionSensorCurrentstate = false;
    if (motionSensorPreviousstate != motionSensorCurrentstate)
    {
      Serial.println(O_MOTION_SENSOR_OFF);
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
      Serial.println(O_LIGHT_SENSOR_HIGH);
    }

  }
  else
  {
    lightSensorCurrentstate = false;
    if (lightSensorPreviousstate != lightSensorCurrentstate)
    {
      Serial.println(O_LIGHT_SENSOR_LOW);
    }
  }
  lightSensorPreviousstate = lightSensorCurrentstate;
}
