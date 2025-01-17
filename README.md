# RFB-dev-kit

![Exploded view of cell](CAD/exports/exploded.webp)
Exploded view of cell

![View of assembled cell in jig](CAD/exports/front.png)
View of assembled cell in jig

![View of electronics in jig](CAD/exports/back.png)
View of electronics in jig

--------------------------------------------------------------------------------
A benchtop flow battery development kit, extendable to other electrochemical systems with flow.
Designed in [FreeCAD](https://www.freecad.org/).

Developed by the [Flow Battery Research Collective](https://opencollective.com/fbrc).

## Documentation

Documentation, which includes the BOM, is available [here](https://fbrc.codeberg.page/rfb-dev-kit/). This is the contents of the `docs` subfolder of this repository rendered as a static website, using [GitBuilding](https://gitbuilding.io/).

## Features
- Geometric cell area from 1 cm² to 10 cm²

## Design Choices
- Minimize machining of metal and graphitic materials
- Flow-through porous carbon electrodes of variable thickness
- Maximize off-the-shelf component and material availability
- Manufacturable by multiple methods, e.g. FDM/SLA/SLS printing, conventional subtractive machining, etc.

## Repository Structure

- `CAD` directory: FreeCAD design files
    - `exports` directory: files for manufacturing cell components
    - `imports` directory: files imported by FreeCAD for creating assembly
- `docs` directory: documentation written with [GitBuilding](https://gitbuilding.io/)
- `firmware` directory: code for pump speed controllers based on Arduino Uno R3


## References/Inspiration/Collaborators/Conspirators (in no particular order)
- [FAIR Battery project](https://github.com/SanliFaez/FAIR-Battery) (collaborators)
- White, R. E. Electrochemical Cell Design; Springer US: Boston, MA, 1984.
- O’Connor, H.; Bailey, J. J.; Istrate, O. M.; Klusener, P. A. A.; Watson, R.; Glover, S.; Iacoviello, F.; Brett, D. J. L.; Shearing, P. R.; Nockemann, P. An Open-Source Platform for 3D-Printed Redox Flow Battery Test Cells. Sustainable Energy Fuels 2022, 6 (6), 1529–1540. https://doi.org/10.1039/D1SE01851E.
- Arenas, L. F.; Walsh, F. C.; León, C. P. de. 3D-Printing of Redox Flow Batteries for Energy Storage: A Rapid Prototype Laboratory Cell. ECS J. Solid State Sci. Technol. 2015, 4 (4), P3080. https://doi.org/10.1149/2.0141504jss.
- https://codeberg.org/LibreWater/Acraea-Prototype
- https://github.com/opulo-inc/lumenpnp/tree/main
- https://openflexure.org/