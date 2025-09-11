---
PartData:

    Suppliers:
        PCBWay:
            PartNo: Use this link
            Link: 'https://www.pcbway.com/project/shareproject/MyStat_Potentiostat_9df57df2.html'
---

# Potentiostat

The MYSTAT potentiostat allows you to control the voltage or current through the cell and record and plot both parameters. You can order the PCB including components through the PCBWay project linked above.

>i **Note**
>i
>i You can also use another battery cycler or galvanostat/potentiostat with appropriate specifications, but this documentation uses the MYSTAT.


>!! **Warning** 
>!!
>!! The potentiostat has two analog-digital converters. There are three options of components to choose from,one for 50Hz grids like in Europe, one for 60Hz grids like in US America and one that can do both. Be sure to upload a BOM with the correct version for your grid. The 50Hz version of the ADC is called MCP3550-50, the 60Hz one is called MCP3550-60 and the universal one is called MCP3553.

In order to get the potentiostat working, you first need to program it's PIC16 microcontroller using a special PIC programmer like the PICkit and the programming software by Microchip. The version needed for the voltage-range extended MYSTAT can be found [here](https://codeberg.org/FBRC/mystat/src/branch/master/firmware/firmware.hex).

The python-based control software can be found [here](https://codeberg.org/FBRC/mystat/src/branch/master/python), it serves both as a potentiostat and galvanostat control and visualization software but can also control the pumps.

>i **Note**
>i
>i You need to fabricate a cable that connects the potentiostat to the cell, based on a 2.5 mm audio jack cable with 4 leads exposed.

>!! **Warning**
>!! 
>!! Never connect or disconnect the jack-cable while the power is still connected as the jack connects to random leads during insertion or removal from the socket.

>i **Note**
>i
>i Be sure to connect the potentiostat to the power supply before you do the calibration or use it for measurement.

Once you can successfully connect to the potentiostat, you need to calibate it, this procedure is explained in the [MYSTAT paper](https://www.hardware-x.com/article/S2468-0672(20)30072-9/fulltext) and the [paper](https://www.hardware-x.com/article/S2468-0672(17)30031-7/fulltext) describing the predecessor of MYSTAT.