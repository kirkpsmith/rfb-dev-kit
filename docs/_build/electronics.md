<!-- There should be only one Header per page. You do not need to use all the keys -->
# Preparing the pumps and power electronics![page thumbnail](images/test.jpg "")

| Detail        | Value                       |
|---------------|-----------------------------|
| Difficulty    | Easy      |
| Time Required | Easy      |
| Skills        | Electronics breadboarding, Flashing firmware to an Arduino      |






### Parts 

* 1 [24 V DC power source]{: Class="missing"}    - Anything between 12 V and 24 V may work but the results achieved here use 24 V. Motor speeds may need calibration to match existing results
* 1 [Arduino UNO R3]{: Class="missing"}    - or equivalent microcontroller that can output two independent 5V PWM signals and connect to PC over USB serial
* 1 [jig]{: Class="bom"} 
* 1 [L298N motor driver]{: Class="bom"} 
* several [male-to-male breadboard jumper cables]{: Class="missing"} 
* 2 [peristaltic pumps]{: Class="bom"} 
* 1 [USB A-to-B cable]{: Class="missing"} 


### Tools 

* 1 [PC]{: Class="missing"}    - Must be able to flash firmware to microcontroller and connect over USB serial to microcontroller and potentiostat
* 1 [potentiostat]{: Class="bom"}    - preferably the MYSTAT




## System overview

A [PC]{: Class="missing"} communicates with both a charging/discharging device (typically a [potentiostat]) as well as an [Arduino UNO R3]{: Class="missing"}. These documents assume the use of a MYSTAT potentiostat and it's [modified control software](https://codeberg.org/FBRC/mystat/ "").

The Arduino is connected to an [L298N motor driver], which is powered by a [24 V DC power source]{: Class="missing"}. This is a simple dual H-bridge motor driver that allows the Arduino to control the speeds of the peristaltic pumps using pulse width modulation (PWM). There is no speed feedback; we only tell the motors which direction to turn and whether they run at 100% maximum speed, 0% speed (off), or anything in between. To know the speed (in rpm) or flowrate (in mL/min) of the peristaltic pumps, a separate measurement is required (like dispensing water into a graduated cylinder).

We use the open-source MYSTAT (with our own modifications to the control software), but any equivalent potentiostat or battery cycler will do. Our pump control system is based on the MYSTAT software, though, and can be used without the MYSTAT present.

With this hardware configuration, the MYSTAT software then allows for entire control of this electrochemical system: the applied currents and voltages as well as the speeds of the electrolyte pumps. 


## Step 1: Flash firmware to microcontroller {:id="flash-firmware-to-microcontroller" class="page-step"}

Using the Arduino IDE with the elapsedMillis library installed, upload the following code to the Arduino. The location of the code in the repository is [here](https://codeberg.org/FBRC/RFB-dev-kit/src/branch/main/firmware/ArduinoUnoR3_MotorControl.ino "")

## Step 2: Remove on-board jumpers from motor driver {:id="remove-on-board-jumpers-from-motor-driver" class="page-step"}

**Remove** the three on-board jumpers (highlighted in pink) from the motor driver board:

![](images/Screenshot_20240703_221706.png "")

## Step 3: Add Arduino and motor driver to the jig {:id="add-arduino-and-motor-driver-to-the-jig" class="page-step"}

There are standoffs made for the for the Arduino and motor driver on the back of the [jig] .

## Step 4: Add pumps to jig {:id="add-pumps-to-jig" class="page-step"}

Insert the two [peristaltic pumps] into their holders in the as shown:

![](images/Screenshot_20250102_190036.png "")


## Step 5: Connect cables between Arduino, motor driver, and power supply {:id="connect-cables-between-arduino-motor-driver-and-power-supply" class="page-step"}

Using [male-to-male breadboard jumper cables]{: Class="missing"} connect according to the below diagram, taking care to connect the negative terminal of the 24 V power supply lead to both the GND terminal of the motor driver (middle connection of the three-terminal screw connection header) **and** a GND pin of the Arduino, so that the Arduino's signals to the motor driver are in relation to the same fixed GND.
![](images/test.jpg "")

The wiring should look like this when you're done (feel free to make it tidier!)
![](images/IMG_20241116_155825.jpg "")

You now have a <a name="output__jig-with-pumps-and-power-electronics"></a>jig with pumps and power electronics.

## Connect microcontroller to PC and test pumps.

We are using the MYSTAT potentiostat and have modified the software to be able to control the pump speeds. If you have a different potentiostat, you can still use the MYSTAT software to control your pumps without having a MYSTAT connected.

Plug in the 24V power source to the H-bridge. Connect the Arduino to the PC with a [USB A-to-B cable]{: Class="missing"}

Run the MYSTAT [modified control software](https://codeberg.org/FBRC/mystat/ "").

Connect to the Arduino through the MYSTAT GUI. Briefly test each pump to make sure it spins (it can spin for a couple seconds dry without issues).
[PC]:missing.md ""
[potentiostat]:pstat.md ""
[Arduino UNO R3]:missing.md ""
[L298N motor driver]:drivers.md ""
[24 V DC power source]:missing.md ""
[jig]:fabrication.md ""
[peristaltic pumps]:pumps.md ""
[male-to-male breadboard jumper cables]:missing.md ""
[USB A-to-B cable]:missing.md ""

<!-- GitBuilding Nav -->
---

[Previous page](fabrication.md) | [Next page](cell_assembly.md)