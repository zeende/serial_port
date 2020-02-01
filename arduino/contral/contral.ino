int a=12;
int b=13;
int c=15;
void setup(){
   Serial.begin(9600);
 }
 void loop(){
   Serial.print(a);
   Serial.print(",");
   Serial.print(b);
   Serial.print(",");
   Serial.println(c);
   delay(1);
 }
