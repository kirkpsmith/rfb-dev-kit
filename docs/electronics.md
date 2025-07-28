---
Details:
    Thumbnail: images/Screenshot_20250609_150903.png
    Time: Tens of minutes
    Difficulty: Easy
    Skills:
      - Electronics breadboarding
      - Flashing firmware to an Arduino 

---
<!-- There should be only one Header per page. You do not need to use all the keys -->
# Preparing the pumps and power electronics

{{BOM}}

## System overview

A [PC]{cat:tool, qty:1, Note:Must be able to flash firmware to microcontroller and connect over USB serial to microcontroller and potentiostat} communicates with both a charging/discharging device (typically a [potentiostat](pstat.md){cat:tool, qty:1, note: preferably the MYSTAT}) as well as an [Arduino UNO R3]{qty:1, Note:or equivalent microcontroller that can output two independent 5V PWM signals and connect to PC over USB serial}. These documents assume the use of a MYSTAT potentiostat and it's [modified control software](https://codeberg.org/FBRC/mystat/).

The Arduino is connected to two peristaltic pumps which have internal stepper motor drivers, and are powered by a [24 V DC power source]{cat: part, qty: 1}. To know the flowrate (in mL/min) of the peristaltic pumps, a separate measurement is required (like dispensing water into a graduated cylinder).

We use the open-source MYSTAT (with our own modifications to the control software), but any equivalent potentiostat or battery cycler will do. Our pump control system is based on the MYSTAT software, though, and can be used without the MYSTAT present.

With this hardware configuration, the MYSTAT software then allows for entire control of this electrochemical system: the applied currents and voltages as well as the speeds of the electrolyte pumps. 


## Flash firmware to microcontroller {pagestep}

Using the Arduino IDE with the elapsedMillis library installed, upload the following code to the Arduino. The location of the code in the repository is [here](https://codeberg.org/FBRC/RFB-dev-kit/src/branch/main/firmware/ArduinoUnoR3_MotorControl.ino)

## Add pumps to jig {pagestep}

Insert the two [peristaltic pumps with correct tubing](fromstep){qty:2} into their holders in the as shown:

![](images/Screenshot_20250610_105323.png)

## Add case, Arduino UNO to the jig{pagestep}

There are holes for the for the Arduino and its case on the back of the [jig](fromstep){qty: 1} . Using four [self-tapping screws]{qty: 4,cat: part} inserted from the front of the jig, attach the case and Arduino to the jig.

![](images/Screenshot_20250609_151049.png)


>i **Note** 
>i
>i The reset button is placed with the large end *inside* the case, as visible in the original designer's [photos](https://www.thingiverse.com/thing:628929)


## Connect cables between Arduino, motors, and power supply{pagestep}

Using [male-to-male breadboard jumper cables]{qty: several, cat: part} connect according to the below diagram:

![](../CAD/exports/schematic.pdf)

Positive pump:

- Red wire to DC power jack positive terminal
- Black wire to DC power jack negative terminal
- Yellow wire (PWM speed control) to Arduino pin 2
- White wire (Tacho / speed measurement) to Arduino pin 10
- Green wire (reverse) to Arduino GND

Negative pump:

- Red wire to DC power jack positive terminal
- Black wire to DC power jack negative terminal
- Yellow wire (PWM speed control) to Arduino pin 3
- White wire (Tacho / speed measurement) to Arduino pin 11
- Green wire (reverse) leave unconnected

Misc.

- Connect DC power jack negative terminal to Arduino GND


![](images/Screenshot_20250610_105535.png)


[][jig with pumps and power electronics]{output, qty:1}

##Connect microcontroller to PC and test pumps{pagestep}


We are using the MYSTAT potentiostat and have modified the software to be able to control the pump speeds. If you have a different potentiostat, you can still use the MYSTAT software to control your pumps without having a MYSTAT connected.

Plug in the 24V power source to the H-bridge. Connect the Arduino to the PC with a [USB A-to-B cable]{qty: 1,cat: part}

Run the MYSTAT [modified control software](https://codeberg.org/FBRC/mystat/).

Connect to the Arduino through the MYSTAT GUI. Briefly test each pump to make sure it spins (it can spin for a couple seconds dry without issues).






