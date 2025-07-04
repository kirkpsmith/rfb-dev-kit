---
Details:
    Thumbnail: images/Screenshot_2025-01-23-15-14-43-351_org.fossify.gallery_1.jpg
    Time: Hours
    Skills:
      - 3D printing or milling
      - Drilling
      - Cutting

---
<!-- There should be only one Header per page. You do not need to use all the keys -->
# Fabricating components

## Bill of Materials

{{BOM}}

You will need a [FDM printer]{qty:1, cat:tool} and at least two types of filament, [stiff filament]{qty: some, Note: PLA works} and [polypropylene filament]{qty: some, Note: This can be substituted if you only plan to run water through the cell for testing things other than the chemistry}.

## Print one jig and one cell assembly tool{pagestep}

Print the [jig]{output, qty: 1} and [cell assembly tool]{output, qty: 1} in PLA or whatever material you can print easily. It does not have to be chemically resistant or that strong, so you can use a low infill.

![](../CAD/exports/jig.stl)

![](../CAD/exports/Cell Assembly Tool.stl)

## Print Arduino Uno case parts

These parts can be done in PLA or similar filaments at low infill. They mount onto the back of the jig.

![](../CAD/exports/uno_case/uno_case_base.stl)
![](../CAD/exports/uno_case/uno_case_lid.stl)
![](../CAD/exports/uno_case/reset_button.stl)


>i **Note** 
>i
>i [3D Printed Case for Arduino Uno, Leonardo](https://github.com/zygmuntw/3D-Printed-Case-for-Arduino) by ZygmuntW is licensed under the Creative Commons - Attribution - Share Alike license.


## Print two endplates{pagestep}

These [endplates]{output, qty: 2} must be stiff, so print them with at least 60% infill in PLA or PETG. Try to avoid warping as they bottom need to be flat to seal the cell well.

![](../CAD/exports/Polymer Endplate.stl)

## Print wetted cell components in polypropylene{pagestep}
 
Print two [reservoirs]{output, qty: 2}, two [flow frames]{output, qty: 2}, and one [membrane frame]{output, qty:1} **in polypropylene**.

It's important these don't leak, so print them at 100% infill with 5 perimeters.

![](../CAD/exports/Reservoir.stl)

![](../CAD/exports/flow-frames/2 sqcm 0.7 mm wall Flow Frame.stl)

![](../CAD/exports/Membrane Frame.stl)


>!! **Warning** 
>!!
>!! The total combined thickess of the flow frames and (compressed) gaskets is important! There are multiple thickness options in the `flow-frames` folder and custom thicknesses can be genererated from the FreeCAD files. The graphite felt should be compressed to 70% of it's original thickness. The compression is fixed by the combined total thickness of the flow frame and two gaskets.

## Cut gaskets {pagestep}

>i **Note:**
>i
>i Cutting the gaskets is most easily done with a vinyl cutter machine or laser cutter, but can also be done manually with a steady hand, utility blade, and appropriately sized punches.

1. Using a [gasket cutter machine]{qty: 1, cat:tool, Note: Vinyl/laser cutter or hand tools}, download the gasket file and cut a sheet of [gasket material][gasket sheet](gaskets.md){qty: 160 cm², note: "Dimensions must be at least enough to cut out approx. four 6 cm x 8 cm rectangles, an A4 sheet is enough" } to make the following four gaskets:

![](../CAD/exports/Gasket Drawings.pdf)

This makes two [inner gaskets]{output, qty: 2} and two [outer gaskets]{output, qty: 2}.

## Cut porous electrodes {pagestep}

Cut two conductive graphite felt electrodes to fit inside the flow frames using scissors or a [utility knife]{qty: 1, cat:tool}. Our current standard test uses 2 cm² geometric area cells, so cut two squares each with a side length of 14.1 mm from a larger piece of [conductive felt](conductive_felt.md){qty: 4 cm², cat: part}.

![](images/electrodes.jpeg)

This makes two [cut electrodes]{output, qty: 2}.

## Cut separator membrane {pagestep}

Cut [separator sheet](separator_sheet.md){qty: A4 sheet,cat: part} into three 2.7 cm x 2.7 cm squares.

![](images/separators.jpeg)

This produces four [cut membranes]{output, qty: 3}

## Cut grafoil current collectors {pagestep}

Using a precut gasket as a guide, cut/punch [grafoil](grafoil.md){qty: 100 cm²} into the following shape to make [grafoil current collectors]{output, qty: 2}.

![](../CAD/exports/Grafoil Drawing.pdf)


## Cut brass current collectors {pagestep}

Using a router or a drill (press), cut some [1 mm brass sheet](brass.md){qty: a small plate of} according to the below drawing to make two [brass current collectors]{output, qty: 2}.

![](../CAD/exports/Current Collector Drawing.pdf)

## Cut tubing

Cut [tubing](tubing.md){qty: 55 cm} into the following lengths:

- 4x 5.5 cm pieces (flow frame connections)
- 2x 10 cm pieces (reservoir outlet to pump inlet)
- 2x 6.5 cm pieces (flow frame tubing connector to pump outlet)

[cut tubing]{output, qty: 1, hidden}

## Ensure correct tubing type is in peristaltic pumps

If you plan to test zinc-iodide chemistries, you need PTFE-lined peristaltic pump tubing loaded in your [peristaltic pumps](pumps.md){qty: 2} as shown. [peristaltic pumps with correct tubing]{output, qty:2, hidden}

>!! **Warning** 
>!!
>!! Your pump may not come with PTFE-lined tubing installed, you should verify what type is installed before running your first experiment

![](images/IMG_20250423_160923.jpg)




