#include <elapsedMillis.h>
#define LED_BUILTIN 17

#define RIGHT_MOTOR_PWM_PIN 10 // 490 Hz
#define LEFT_MOTOR_PWM_PIN 3 // 490 Hz
#define In1 9
#define In2 8
#define In3 7
#define In4 6

// INPUT PUMP SPEED/DUTY CYCLE, 0-255 is 0-100%, PUMPS MAY NOT SPIN UNTIL MINUMUM DUTY CYCLE IS MET
int speed1P = 0;
int speed1N = 0;

// OUTPUT PUMP SPEED

unsigned long rpm1P = 0;
unsigned long rpm1N = 0;

//PUMP COUNTERS

unsigned long count1P = 0;
unsigned long count1N = 0;

const byte buffSize = 40;
char inputBuffer[buffSize];
const char startMarker = '<';
const char endMarker = '>';
byte bytesRecvd = 0;
boolean readInProgress = false;
boolean newDataFromPC = false;
char messageFromPC[buffSize] = {0};
char cmd;
String val;

const int updateInterval = 1000; // serial update time period (ms)
elapsedMillis updateTimer = 0;

bool ledState = LOW;

// Pumps are off on board startup/reset
int RIGHT_MOTOR_SPEED = 0;
int LEFT_MOTOR_SPEED = 0;

void parseData()
{
  cmd = strtok(inputBuffer, ",")[0];
  val = strtok(NULL, ",");
  Serial.print(cmd);
  Serial.print(',');
  Serial.println(val);
}

void recieveFromPC()
{

  // receive data from PC and save it into inputBuffer

  if (Serial.available() > 0)
  {

    char x = Serial.read();
    // the order of these IF clauses is significant

    if (x == endMarker)
    {
      readInProgress = false;
      newDataFromPC = true;
      inputBuffer[bytesRecvd] = 0;
      parseData();
    }

    if (readInProgress)
    {
      inputBuffer[bytesRecvd] = x;
      bytesRecvd++;
      if (bytesRecvd == buffSize)
      {
        bytesRecvd = buffSize - 1;
      }
    }

    if (x == startMarker)
    {
      bytesRecvd = 0;
      readInProgress = true;
    }
  }
}

void ISR_1P()
{
  count1P++;
}
void ISR_1N()
{
  count1N++;
}

void setup()
{
  Serial.begin(9600);

  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, ledState);

  pinMode(RIGHT_MOTOR_PWM_PIN, OUTPUT);
  pinMode(LEFT_MOTOR_PWM_PIN, OUTPUT);
  pinMode(In1, OUTPUT);
  pinMode(In2, OUTPUT);
  pinMode(In3, OUTPUT);
  pinMode(In4, OUTPUT);

  digitalWrite(In1, HIGH);
  digitalWrite(In2, LOW);

  digitalWrite(In3, HIGH);
  digitalWrite(In4, LOW);

  analogWrite(RIGHT_MOTOR_PWM_PIN, RIGHT_MOTOR_SPEED);
  analogWrite(LEFT_MOTOR_PWM_PIN, LEFT_MOTOR_SPEED);
}

void controlPumps()
{
  if (newDataFromPC)
  {
    switch (cmd)
    {
    case 'a':
      RIGHT_MOTOR_SPEED = val.toInt();
      analogWrite(RIGHT_MOTOR_PWM_PIN, RIGHT_MOTOR_SPEED);
      break;
    case 'b':
      LEFT_MOTOR_SPEED = val.toInt();
      analogWrite(LEFT_MOTOR_PWM_PIN, LEFT_MOTOR_SPEED);
      break;
    case 'c':
      LEFT_MOTOR_SPEED = val.toInt();
      RIGHT_MOTOR_SPEED = val.toInt();
      analogWrite(LEFT_MOTOR_PWM_PIN
      , LEFT_MOTOR_SPEED);
      analogWrite(RIGHT_MOTOR_PWM_PIN, RIGHT_MOTOR_SPEED);
      break;
    }
  }
}

void loop()
{
  recieveFromPC();
  controlPumps();
}
