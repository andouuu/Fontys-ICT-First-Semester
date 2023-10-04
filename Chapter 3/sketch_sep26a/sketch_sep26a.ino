const int potentiometerPin=A0;
const int yellowLEDPin=7;
const int blueLEDPin=6;
const int greenLEDPin=5;

void setup() {
  // put your setup code here, to run once:
pinMode(yellowLEDPin,OUTPUT);
pinMode(blueLEDPin,OUTPUT);
pinMode(greenLEDPin,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
int potValue=analogRead(potentiometerPin);

if (potValue<450){
  digitalWrite(yellowLEDPin,HIGH);
  digitalWrite(blueLEDPin,LOW);
  digitalWrite(greenLEDPin,LOW);
}
else if(potValue>=450&&potValue<=550){
  digitalWrite(yellowLEDPin,LOW);
  digitalWrite(blueLEDPin,HIGH);
  digitalWrite(greenLEDPin,LOW);
}
else{
  digitalWrite(yellowLEDPin,LOW);
  digitalWrite(blueLEDPin,LOW);
  digitalWrite(greenLEDPin,HIGH);
}
}
