#include <Servo.h>

Servo servo;
Servo servo2;
char grado = 90;


 
void setup(){
  Serial.begin(9600);
  servo.attach(6);
  servo2.attach(8);
  servo2.write(90);
  servo.write(grado);  
}
 
void loop(){
  
  if (Serial.available()>0){
   grado = Serial.read();

   }
       servo.write(grado);

}
