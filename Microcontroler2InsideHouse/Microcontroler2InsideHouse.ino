#include "CommonDefines.h"

DIGITAL motionSensorVal =  0;
DIGITAL lightSensorValue = 0;
DIGITAL flameSensorValue = 0; 
int tempSensorValue;
int previousTempValue = 0 ;

bool lightSensorCurrentState  = false;
bool lightSensorPreviousState = false;

bool motionSensorCurrentState  = false;
bool motionSensorPreviousState = false;

bool flameSensorCurrentState  = false;
bool flameSensorPreviousstate = false;


char incomingByte = 0;

void setup() 
{
  pinMode(INSIDE_LIGHT_SENSOR,  INPUT); // define pin as Input  sensor
  pinMode(INSIDE_MOTION_SENSOR, INPUT);
  pinMode(INSIDE_FLAME_SENSOR,  INPUT);

  pinMode(INSIDE_LIGHT_LED,     OUTPUT);    // declare led pin as output
  pinMode(INSIDE_VENT_PIN,      OUTPUT);
  pinMode(INSIDE_HEATING_PIN,   OUTPUT);
  pinMode(INSIDE_FLAME_BUZZER,  OUTPUT);

  Serial.begin(9600); // Default communication rate of the Bluetooth module
}

void loop() 
{
  //////////////////// READ SENSOR VALUES ///////////////////////		
  lightSensorValue = digitalRead(INSIDE_LIGHT_SENSOR);// read the sensor
  motionSensorVal  = digitalRead(INSIDE_MOTION_SENSOR);  // read input value
  flameSensorValue = digitalRead(INSIDE_FLAME_SENSOR);
  
  tempSensorValue  = analogRead(INSIDE_TEMP_SENSOR);
  
  //////////////////// SEND SENSOR STATE THROUGH SERIAL ///////////////////////
  handleTempSensor(tempSensorValue);
  handleLightSensor(lightSensorValue);
  handleFlameSensor(flameSensorValue);

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
          digitalWrite(INSIDE_VENT_PIN, HIGH);
        }
        break;
        
      case '4':
        {
          digitalWrite(INSIDE_VENT_PIN, LOW);
        }
        break;

      case '5':
        {
          digitalWrite(INSIDE_HEATING_PIN, HIGH);
        }
        break;
      case '6':
        {
          digitalWrite(INSIDE_HEATING_PIN, LOW);
        }
        break;

      case '7':
        {
          digitalWrite(INSIDE_FLAME_BUZZER, HIGH);
        }
        break;

      case '8':
        {
          digitalWrite(INSIDE_FLAME_BUZZER, LOW);
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
    motionSensorCurrentState = true;
    if (motionSensorPreviousState != motionSensorCurrentState)
    {
      Serial.println(I_MOTION_SENSOR_ON);
    }

  }
  else
  {
    motionSensorCurrentState = false;
    if (motionSensorPreviousState != motionSensorCurrentState)
    {
      Serial.println(I_MOTION_SENSOR_OFF);
    }
  }
  motionSensorPreviousState = motionSensorCurrentState;
}

void handleLightSensor(DIGITAL value)
{
  if (value == HIGH)
  {
    lightSensorCurrentState = true;
    if (lightSensorPreviousState != lightSensorCurrentState)
    {
      Serial.println(I_LIGHT_SENSOR_HIGH);
    }
  }
  else
  {
    lightSensorCurrentState = false;
    if (lightSensorPreviousState != lightSensorCurrentState)
    {
      Serial.println(I_LIGHT_SENSOR_LOW);
    }
  }
  lightSensorPreviousState = lightSensorCurrentState;
}

void handleFlameSensor(DIGITAL value)
{
  if (value == HIGH)
  {
      flameSensorCurrentState = true;
    if (flameSensorPreviousstate != flameSensorCurrentState)
    {
      Serial.println(I_FLAME_SENSOR_HIGH);
    }
  }
  else
  {
    flameSensorCurrentState = false;
    if (flameSensorPreviousstate != flameSensorCurrentState)
    {
      Serial.println(I_FLAME_SENSOR_LOW);
    }
  }
  flameSensorPreviousstate = flameSensorCurrentState;
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
