# Preparing the power electronics

## System overview

A [PC]{cat:tool, qty:1, Note:Must be able to flash firmware to microcontroller and connect over USB serial to microcontroller and potentiostat} communicates with both a charging/discharging device (typically a [potentiostat](pstat.md){cat:tool, qty:1}) as well as an [Arduino UNO R3]{qty:1, Note:or equivalent microcontroller that can output two independent 5V PWM signals and connect to PC over USB serial}. These documents assume the use of a MYSTAT potentiostat and it's [modified control software](https://codeberg.org/FBRC/mystat/).

The Arduino is connected to an [L298N motor driver](drivers.md){cat:part, qty:1}, which is powered by a [24 V DC power source]{cat: part, qty: 1, Note: Anything between 12 V and 24 V may work but the results achieved here use 24 V. Motor speeds may need calibration to match existing results}. This is a simple dual H-bridge motor driver that allows the Arduino to control the speeds of the peristaltic pumps using pulse width modulation (PWM). There is no speed feedback; we only tell the motors which direction to turn and whether they run at 100% maximum speed, 0% speed (off), or anything in between. To know the speed (in rpm) or flowrate (in mL/min) of the peristaltic pumps, a separate measurement is required (like dispensing water into a graduated cylinder).

With this hardware configuration, the MYSTAT software then allows for entire control of this electrochemical system: the applied currents and voltages as well as the speeds of the electrolyte pumps.
{{BOM}}

## Flash firmware to microcontroller {pagestep}

Using the Arduino IDE with the elapsedMillis library installed, upload the following code to the Arduino. The location of the code in the repository is [here](https://codeberg.org/FBRC/RFB-dev-kit/src/branch/main/firmware/ArduinoUnoR3_MotorControl.ino)

```{.c++}
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

```

## Remove on-board jumpers from motor driver {pagestep}

**Remove** the three on-board jumpers (hig hlighted in pink) from the motor driver board:

![](images/Screenshot_20240703_221706.png)

## Connect cables between Arduino, motor driver, and power supply {pagestep}

Connect according to the below diagram, taking care to connect the negative terminal of the 24 V power supply lead to both the GND terminal of the motor driver (middle connection of the three-terminal screw connection header) **and** a GND pin of the Arduino, so that the Arduino's signals to the motor driver are in relation to the same fixed GND.
![](images/test.jpg)

## Connect microcontroller to PC

TODO



