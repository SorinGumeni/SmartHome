#ifndef _COMMONDEFINES_H    // Put these two lines at the top of your file.
#define _COMMONDEFINES_H    // (Use a suitable name, usually based on the file name.)

#define INSIDE_TEMP_SENSOR   0 //Temperature sensor from inside the house
#define INSIDE_LIGHT_SENSOR  2 // Light sensor from inside the house
#define INSIDE_LIGHT_LED     3 // Led triggered by the sensor from inside the house
#define INSIDE_MOTION_SENSOR 4

#define I_MOTION_SENSOR_ON  "I_MOTION_SENSORON"
#define I_MOTION_SENSOR_OFF "I_MOTION_SENSORFF"
#define I_LIGHT_SENSOR_HIGH "I_LIGHT_SENSOR_HIGH"
#define I_LIGHT_SENSOR_LOW  "I_LIGHT_SENSOR_LOW"

//CUSTOM TYPES
typedef int DIGITAL;

#endif  _COMMONDEFINES_H    // Put this line at the end of your file.
