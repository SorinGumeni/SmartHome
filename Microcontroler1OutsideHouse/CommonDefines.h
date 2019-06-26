#ifndef _COMMONDEFINES_H    // Put these two lines at the top of your file.
#define _COMMONDEFINES_H    // (Use a suitable name, usually based on the file name.)

//DEFINES FOR BOARD PIN NUMBERS
#define OUTSIDE_MOTION_LED    2
#define OUTSIDE_MOTION_BUZZER 3
#define OUTSIDE_MOTION_SENSOR 4
#define OUTSIDE_LIGHT_SENSOR  5
#define OUTSIDE_HALL_SENSOR   6

//DEFINES FOR EVENTS SENT THROUGH SERIAL
#define O_MOTION_SENSOR_ON  "O_MOTION_SENSORON"
#define O_MOTION_SENSOR_OFF "O_MOTION_SENSORFF"
#define O_LIGHT_SENSOR_HIGH "O_LIGHT_SENSOR_HIGH"
#define O_LIGHT_SENSOR_LOW  "O_LIGHT_SENSOR_LOW"
#define O_HALL_SENSOR_HIGH  "O_HALL_SENSOR_HIGH"
#define O_HALL_SENSOR_LOW   "O_HALL_SENSOR_LOW"
//CUSTOM TYPES
typedef int DIGITAL;



#endif  _COMMONDEFINES_H    // Put this line at the end of your file.
