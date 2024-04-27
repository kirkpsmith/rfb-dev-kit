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

## Fabricate cell bodies

These are preferably milled from solid polypropylene with a [3-axis mill]{qty: 1, cat: tool}

![](../CAD/exports/Cell Body with Two Flat-Bottom Ports.pdf)

This makes two [cell bodies]{output, qty: 2}


>i **If you don't have access to a mill** 
>i
>i You can try to FDM (in polypropylene) or resin print (in epoxy-based resin) this file, with built-in barbs:
>i ![](../CAD/exports/Cell Body with Two Barbed Fittings.stl)


## Print rigid cell components  {pagestep}

Using a [3D printer]{qty:1, cat:tool} loaded with chemically compatible polypropylen filament/epoxy resin [3D printing feedstock]{qty: 200 g}, print two [reservoirs](../CAD/exports/Reservoir.3mf) and two [flow frames](../CAD/exports/Flow Frame.3mf) (links are to .3mf files).
![](../CAD/exports/Reservoir.stl)
![](../CAD/exports/Flow Frame.stl)

>i **Prefer conventional machining?**
>i 
>i You can also fabricate these parts by milling them from a larger sheet of polypropylene

## Post-process printed parts  {pagestep}
1. Remove brim, raft, support material from print (depending on printing method)
* Sand down, with fine-grit [sandpaper]{qty:1 sheet, cat:tool}:
> 1. The sealing faces of each cell body
> ![](images/cell_body.png)
> * Both faces of each flow frame
> ![](images/flow_frame.png)
* Secure each cell body and flow frame in a [vise]{qty: 1, cat:tool} and drill out the alignment pin holes to their final diameter with a [drill]{qty: 1, cat:tool, note:"A hand drill or rotary tool (with steady hands) works, but a drill press is preferable"} and an [1/8" drill bit]{qty: 1, cat: tool}
> ![](images/cell_body_alignment_pins.png)
> 
> ![](images/flow_frame_alignment_pins.png)
>! **Caution**
>! 
>! Depending on the dimensional accuracy of your printed parts, you may need to additionally drill out the electrolyte inlet/outlet holes to the correct diameter with an appropriately sized drill bit (these inlet/outlet holes are located immediately on either side of the alignment pin holes)



This will produce one [cell body with four barbed fittings]{output, qty:1}, one [backing plate]{output, qty:1} and two [flow frames]{output, qty: 2}.

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
