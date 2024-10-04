---
Details:
    Thumbnail: images/printing.png
    Time: Hours
    Difficulty: Hard
    Skills:
      - 3D printing or milling
      - Drilling
      - Cutting

---
<!-- There should be only one Header per page. You do not need to use all the keys -->
# Fabricating cell components

## Bill of Materials

{{BOM}}

## Fabricate cell bodies {pagestep}

These are preferably milled from solid polypropylene with a [3-axis mill]{qty: 1, cat: tool}. The .STEP file of the below part is found [here](../CAD/exports/Cell Body with Two Flat-Bottom Ports.step), this is exported from the `flow_cell.FCStd` file.

![](../CAD/exports/Cell Body with Two Flat-Bottom Ports.pdf)

This makes two [cell bodies]{output, qty: 2}

## Print rigid cell components  {pagestep}

Using a [3D printer]{qty:1, cat:tool} loaded with chemically compatible polypropylene filament [3D printing feedstock]{qty: 200 g}, print two [reservoirs](../CAD/exports/Reservoir.3mf) and two [flow frames](../CAD/exports/flow-frames/2 sqcm 1.2 mm Flow Frame.stl).
![](../CAD/exports/Reservoir.stl)
![](../CAD/exports/flow-frames/2 sqcm 1.2 mm Flow Frame.stl)


>!! **Warning** 
>!!
>!! The total combined thickess of the flow frames and (compressed) gaskets is important! There are multiple thickness options in the `flow-frames` folder and custom thicknesses can be genererated from the FreeCAD files. The graphite felt should be compressed to 70% of it's original thickness. The compression is fixed by the combined total thickness of the flow frame and two gaskets.


>i **Prefer conventional machining?**
>i 
>i You could also fabricate the flow frames parts by milling/laser cutting them from a sheet of polypropylene.

## Post-process printed parts  {pagestep}
Remove brim, raft, support material from print (depending on printing method)

Sand down, with fine-grit [sandpaper]{qty:1 sheet, cat:tool}, both faces of each flow frame.

![](images/flow_frame.png)



This will produce two [flow frames]{output, qty: 2} and two [reservoirs]{output, qty: 2}.

## Cut gaskets {pagestep}

>i **Note:**
>i
>i Cutting the gaskets is most easily done with a vinyl cutter machine, but can also be done manually with a steady hand, utility blade, and appropriately sized punches.

1. Using a [vinyl cutter machine]{qty: 1, cat:tool, Note: or laser cutter or hand tools}, download the gasket file (as [svg](../CAD/exports/1 sqcm gaskets.svg), [dxf](../CAD/exports/1 sqcm gaskets.dxf), or [pdf](../CAD/exports/1 sqcm gaskets.pdf)) and cut a sheet of [gasket material][gasket sheet](gaskets.md){qty: 160 cm², note: "Dimensions must be at least enough to cut out approx. four 6 cm x 8 cm rectangles, an A4 sheet is enough" } to make the following four gaskets:

![pass-through gasket](../CAD/exports/1 sqcm gaskets.pdf)



 This will produce two [pass-through gaskets]{output, qty: 2} and two [blocking gaskets]{output, qty: 2}.

## Cut porous carbon electrodes {pagestep}

TODO

Cut two conductive felt electrodes into 10 mm x 10 mm square from a sheet of conductive felt[conductive felt](conductive_felt.md){qty: 10 cm²,cat: part}
## Cut separator membrane {pagestep}

TODO

Cut [separator sheet](separator_sheet.md){qty: A4 sheet,cat: part} into three rectangles

[cut membranes]{output, qty: 3}

## Cut grafoil current collectors {pagestep}

Cut [grafoil](grafoil.md){qty: 100 cm²} into two 5 cm by 5 cm squares to make [grafoil current collectors]{output, qty: 2}.

## Cut copper current collectors {pagestep}

Cut [copper sheet](copper.md){qty: 100 cm²} into two 5 cm by 5 cm squares to make [copper current collectors]{output, qty: 2}.

>!! **Warning to prevent leakage** 
>!!
>!! Make sure at least one orientation of the copper squares fits *exactly* the machined square recess in the cell bodies 

## Cut tubing

Cut [tubing](tubing.md){qty: 1 meter} into 6 15 centimeter lengths to make [cut tubing pieces]{output, qty: 6}
