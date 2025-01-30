# RFB-dev-kit

--------------------------------------------------------------------------------
## About

This kit is for testing flow battery components and electrolytes at small-scales (1-5 cm²) with an affordable, reproducible setup.

Developed by the [Flow Battery Research Collective](https://fbrc.dev).

![](CAD/exports/cell-assembled.png)

Assembled cell

![Exploded view of cell](CAD/exports/cell.png)


![View of assembled cell in jig](CAD/exports/front.png)


![View of electronics in jig](CAD/exports/back.png)


## Documentation

Documentation to build the kit, which includes the BOM, is available [here (latest version, with file previews)](https://fbrc.codeberg.page/rfb-dev-kit/), or locally in the repo [here (current version, without file previews)](docs/_site/index.html).

## Design Choices

- Maximize off-the-shelf component and material availability.
- Impervious graphite or polymer-graphite composite materials are hard to source. Instead we use graphite foil, which is affordable, easily sourceable and works well enough to perform cycling experiments at this scale.
- No flow fields. We use flow-through graphite felt porous electrodes, and the design is parametric to handle differents thicknesses
- No machining of graphite and minimizing machining of plastic.

## Repository Structure

- `CAD` directory: FreeCAD design files
    - `exports` directory: files for manufacturing cell components
    - `imports` directory: files imported by FreeCAD for creating assembly
- `docs` directory: documentation written with [GitBuilding](https://gitbuilding.io/)
- `firmware` directory: code for pump speed controllers based on Arduino Uno R3

## Contributing

Please see the [contributing guide](https://fbrc.dev/contributing.html) on our website!

## Community

Discussion about the project happens on the [FBRC forum](https://fbrc.nodebb.com/)!


## References/Inspiration/Collaborators/Conspirators (in no particular order)
- [FAIR Battery project](https://github.com/SanliFaez/FAIR-Battery) (collaborators)
- White, R. E. Electrochemical Cell Design; Springer US: Boston, MA, 1984.
- O’Connor, H.; Bailey, J. J.; Istrate, O. M.; Klusener, P. A. A.; Watson, R.; Glover, S.; Iacoviello, F.; Brett, D. J. L.; Shearing, P. R.; Nockemann, P. An Open-Source Platform for 3D-Printed Redox Flow Battery Test Cells. Sustainable Energy Fuels 2022, 6 (6), 1529–1540. https://doi.org/10.1039/D1SE01851E.
- Arenas, L. F.; Walsh, F. C.; León, C. P. de. 3D-Printing of Redox Flow Batteries for Energy Storage: A Rapid Prototype Laboratory Cell. ECS J. Solid State Sci. Technol. 2015, 4 (4), P3080. https://doi.org/10.1149/2.0141504jss.
- https://codeberg.org/LibreWater/Acraea-Prototype
- https://github.com/opulo-inc/lumenpnp/tree/main
- https://openflexure.org/
