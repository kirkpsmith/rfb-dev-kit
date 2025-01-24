# Building a benchtop flow battery test cell with a zinc-iodide electrolyte

![](images/cell.jpeg "")

> **Note** 
> 
> This kit is intended for educational and R&D use only, not for actual energy storage applications. That will happen later, check out our [roadmap](https://fbrc.dev/about.html#roadmap "") to see when.



### Parts 

* a small plate of [1 mm copper sheet]{: Class="bom"} 
* 2 [19/22 silicone septa]{: Class="bom"} 
* 1 [24 V DC power source]{: Class="missing"}    - Anything between 12 V and 24 V may work but the results achieved here use 24 V. Motor speeds may need calibration to match existing results
* 1 [Arduino UNO R3]{: Class="missing"}    - or equivalent microcontroller that can output two independent 5V PWM signals and connect to PC over USB serial
* 4 cm² of [conductive felt]{: Class="bom"} 
* 1 [current collector]{: Class="missing"} 
* 2 [cut nonconductive felt]{: Class="missing"} 
* 4 [cut tubing]{: Class="missing"} 
* 160 cm² of [gasket sheet]{: Class="bom"}    - Dimensions must be at least enough to cut out approx. four 6 cm x 8 cm rectangles, an A4 sheet is enough
* 100 cm² of [grafoil]{: Class="bom"} 
* 1 [grafoil current collector]{: Class="missing"} 
* 1 [L298N motor driver]{: Class="bom"} 
* 4 [M6 nuts with washers]{: Class="missing"} 
* 4 [M6 x 35 mm hex socket cap bolts with washers]{: Class="missing"} 
* several [male-to-male breadboard jumper cables]{: Class="missing"} 
* 1 [outer gasket]{: Class="missing"} 
* 4 [peristaltic pumps]{: Class="bom"} 
* some [polypropylene filament]{: Class="missing"}    - This can be substituted if you only plan to run water through the cell for testing things other than the chemistry
* several cm [polypropylene packing tape]{: Class="missing"} 
* A4 sheet [separator sheet]{: Class="bom"} 
* some [stiff filament]{: Class="missing"}    - PLA works
* 44 cm of [tubing]{: Class="bom"} 
* 1 [USB A-to-B cable]{: Class="missing"} 


### Tools 

* 1 [10 mm socket]{: Class="missing"}    - To fit torque wrench
* 1 [5 mL syringe]{: Class="missing"} 
* 1 [50 mL beaker]{: Class="missing"} 
* 2 [50 mL beakers]{: Class="missing"}    - or drip tray/other container to hold 10 mL of water
* 1 [5mm hex key]{: Class="missing"} 
* 1 [FDM printer]{: Class="missing"} 
* 1 [gasket cutter machine]{: Class="missing"}    - Vinyl/laser cutter or hand tools
* 1 [pair of chemical safety goggles]{: Class="missing"} 
* 1 [pair of nitrile gloves]{: Class="missing"} 
* 1 [PC]{: Class="missing"}    - Must be able to flash firmware to microcontroller and connect over USB serial to microcontroller and potentiostat
* 1 [potentiostat]{: Class="bom"}    - preferably the MYSTAT
* 1 [scale]{: Class="missing"} 
* 1 [stir bar]{: Class="missing"} 
* 1 [stir plate]{: Class="missing"} 
* 1 [torque wrench]{: Class="missing"}    - to accept 5 mm allen key or 10 mm hex socket
* 1 [utility knife]{: Class="missing"} 
* 1 [vial]{: Class="missing"}    - min. 20 mL
* 1 [weighing spatula]{: Class="missing"} 


### Chemicals 

* 10.0 grams of [8% vinegar/acetic acid]{: Class="missing"} 
* 10 mL of [deionized water]{: Class="missing"} 
* 3.0 grams of [potassium acetate]{: Class="missing"} 
* 6.6 grams of [potassium iodide]{: Class="missing"} 
* 2.8 grams of [zinc chloride]{: Class="missing"} 
[FDM printer]:missing.md ""
[stiff filament]:missing.md ""
[polypropylene filament]:missing.md ""
[gasket cutter machine]:missing.md ""
[gasket sheet]:gaskets.md ""
[utility knife]:missing.md ""
[conductive felt]:conductive_felt.md ""
[separator sheet]:separator_sheet.md ""
[grafoil]:grafoil.md ""
[1 mm copper sheet]:copper.md ""
[tubing]:tubing.md ""
[peristaltic pumps]:pumps.md ""
[PC]:missing.md ""
[potentiostat]:pstat.md ""
[Arduino UNO R3]:missing.md ""
[L298N motor driver]:drivers.md ""
[24 V DC power source]:missing.md ""
[male-to-male breadboard jumper cables]:missing.md ""
[USB A-to-B cable]:missing.md ""
[cut tubing]:missing.md ""
[polypropylene packing tape]:missing.md ""
[M6 x 35 mm hex socket cap bolts with washers]:missing.md ""
[current collector]:missing.md ""
[grafoil current collector]:missing.md ""
[outer gasket]:missing.md ""
[cut nonconductive felt]:missing.md ""
[M6 nuts with washers]:missing.md ""
[torque wrench]:missing.md ""
[10 mm socket]:missing.md ""
[5mm hex key]:missing.md ""
[deionized water]:missing.md ""
[50 mL beakers]:missing.md ""
[pair of chemical safety goggles]:missing.md ""
[pair of nitrile gloves]:missing.md ""
[50 mL beaker]:missing.md ""
[scale]:missing.md ""
[weighing spatula]:missing.md ""
[zinc chloride]:missing.md ""
[potassium iodide]:missing.md ""
[potassium acetate]:missing.md ""
[8% vinegar/acetic acid]:missing.md ""
[stir bar]:missing.md ""
[stir plate]:missing.md ""
[vial]:missing.md ""
[5 mL syringe]:missing.md ""
[19/22 silicone septa]:septa.md ""




This bill of materials can be found [here](index_BOM.md) ([![HTML](static/Icons/html.png "HTML Bill of Materials"){: .smallicon}](index_BOM.md), [![CSV](static/Icons/csv.png "CSV Bill of Materials"){: .smallicon}](index_BOM.csv)).

If you're starting from scratch, you need to [fabricate](fabrication.md "") and source everything needed for using this flow battery test cell.

If you already have all the required components and materials, you can directly [prepare the power electronics](electronics.md ""), [assemble the cell](cell_assembly.md ""), [assemble the jig](jig_assembly.md ""), prepare the [electrolyte](electrolyte.md ""), and then begin [testing](testing.md ""). After an experiment, you should [clean up](cleanup.md "") your setup and [analyze](analysis.md "") the data you obtained.

1. [Fabricating components](fabrication.md "")

2.  [Preparing the pumps and power electronics](electronics.md "")

3. [Assembling the flow cell from components](cell_assembly.md "")

4. [Assembling the jig with electronics and flow cell](jig_assembly.md "")

5. [Leak testing the cell](leak_test.md "")

6. [Preparing the electrolyte](electrolyte.md "")

7. [Operating and testing the cell](testing.md "")

8. [Stopping and disassembling the cell](cleanup.md "")

9. [Analyzing and storing the experimental data](analysis.md "")

<!-- GitBuilding Nav -->
---

[Next page](index_BOM.md)