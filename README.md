# RFB-dev-kit

![FreeCAD view of assembled cell](image.png)

Initial repo for a benchtop flow battery development kit, possibly applicable to other electrochemical systems with flow.

Designed in FreeCAD 0.21.1 with the fasteners and A2plus workbenches.

## Features
- Geometric cell area of 1cm² to 16 cm²
- Flow-through electrodes by default

## Design Choices
- Minimize machining of metal and graphitic materials
- Flow-through carbon felt electrodes of variable thickness (at least down to 1 mm compressed in each half-cell compartment)
- Maximize off-the-shelf part availability (ie. 50x50x0.8 mm copper plate current collectors, available on-demand from Aliexpress or other suppliers)

## TODO
- [ ] decide on pump/tubing and connection methods for BOM
- [ ] (as needed) add ridges in printed parts to enhance sealing
- [ ] add functionality to easily modify design files for differing thicknesses of current collector and graphite gaskets
- [ ] decide on blocking gaskets and add them to assembly
- [ ] mark a first release and implement a [changelog](https://keepachangelog.com/en/1.1.0/)
- [ ] consolidate part naming for cell body/flow frame/spacer
- [ ] remove 4mm cell body version once 0.8mm current collectors arrive and are tested

## References/Inspiration
- White, R. E. Electrochemical Cell Design; Springer US: Boston, MA, 1984.
- O’Connor, H.; Bailey, J. J.; Istrate, O. M.; Klusener, P. A. A.; Watson, R.; Glover, S.; Iacoviello, F.; Brett, D. J. L.; Shearing, P. R.; Nockemann, P. An Open-Source Platform for 3D-Printed Redox Flow Battery Test Cells. Sustainable Energy Fuels 2022, 6 (6), 1529–1540. https://doi.org/10.1039/D1SE01851E.
- Arenas, L. F.; Walsh, F. C.; León, C. P. de. 3D-Printing of Redox Flow Batteries for Energy Storage: A Rapid Prototype Laboratory Cell. ECS J. Solid State Sci. Technol. 2015, 4 (4), P3080. https://doi.org/10.1149/2.0141504jss.
- https://codeberg.org/LibreWater/Acraea-Prototype
- https://github.com/opulo-inc/lumenpnp/tree/main
 


