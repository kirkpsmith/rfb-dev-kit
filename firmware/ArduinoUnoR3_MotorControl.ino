#include <elapsedMillis.h>
#define LED_BUILTIN 17

// WHITE WIRES, SPEED CONTROL

#define PIN_1P_PWM 10
#define PIN_1N_PWM 5
#define In1 9
#define In2 8
#define In3 7
#define In4 6

// INPUT PUMP SPEED/DUTY CYCLE, 0-255 is 0-100%, PUMPS MINIMUM SPEED STARTS FROM ~3.8 - 7.6 %
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

int set1P = 160;
int set1N = 160;

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

  pinMode(PIN_1P_PWM, OUTPUT);
  pinMode(PIN_1N_PWM, OUTPUT);
  pinMode(In1, OUTPUT);
  pinMode(In2, OUTPUT);
  pinMode(In3, OUTPUT);
  pinMode(In4, OUTPUT);

  digitalWrite(In1, HIGH);
  digitalWrite(In2, LOW);

  digitalWrite(In3, HIGH);
  digitalWrite(In4, LOW);

  analogWrite(PIN_1P_PWM, set1P);
  analogWrite(PIN_1N_PWM, set1N);
}

void controlPumps()
{
  if (newDataFromPC)
  {
    switch (cmd)
    {
    case 'a':
      set1P = val.toInt();
      analogWrite(PIN_1P_PWM, set1P);
      break;
    case 'b':
      set1N = val.toInt();
      analogWrite(PIN_1N_PWM, set1N);
      break;
    case 'c':
      set1N = val.toInt();
      set1P = val.toInt();
      analogWrite(PIN_1N_PWM
      , set1N);
      analogWrite(PIN_1P_PWM, set1P);
      break;
    }
  }
}

void loop()
{
  recieveFromPC();
  controlPumps();
}
