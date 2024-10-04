# Assembling the flow cell from components

![](images/cell-assembly/composite_image.jpeg)

Ensure you have the following components:
{{BOM}}

Here is an overview of assembling an outdated version of the cell:


<!-- You can drag and drop your images directly here and use this template -->
![](images/cell-assembly/a.jpg)
![](images/cell-assembly/b.jpg)
![](images/cell-assembly/c.jpg)
![](images/cell-assembly/d.jpg)
![](images/cell-assembly/e.jpg)
![](images/cell-assembly/f.jpg)
![](images/cell-assembly/g.jpg)
![](images/cell-assembly/h.jpg)
![](images/cell-assembly/i.jpg)
![](images/cell-assembly/j.jpg)
![](images/cell-assembly/k.jpg)

## Attach the barbed fittings {pagestep}

Take the two [cell bodies](fromstep){qty: 2} and place one [o-ring][o-rings](orings.md){qty: 4} at the bottom of each threaded hole.

Then insert and carefully hand-thread the [barbed fittings](barbed_fittings.md){qty:4} to the bottom of the port.

## Insulate the bolts with packing tape {pagestep}

Wrap [polypropylene packing tape]{qty: several cm} around the shafts of the bolts, leaving the final 1 cm of threads exposed. 

>i **Note** 
>i
>i This prevents accidental short circuits of the cell from the bolt shafts contacting the grafoil.

## Insert the four bolts into one cell body {pagestep}

Take one cell body and insert the four [M6 x 60 mm hex socket cap bolts]{qty: 4} so that the socket caps are on the same side of the cell as the barbs.

## Add the first grafoil current collector {pagestep}

Take this same cell body and place one [grafoil current collector][grafoil current collectors](fromstep){qty: 2} on top of the copper plate.

## Add the first pass-through gasket {pagestep}

Place one [pass-through gasket][pass-through gaskets](fromstep){qty: 2} on top of the assembly, using the bolts to guide the gasket and align it with the fluid holes in the cell body.

>? **Help Block** 
>?
>? The total combined thickess of the flow frames and (compressed) gaskets is key to achieving the desired results! There are multiple thickness options in the `flow-frames` folder and custom thicknesses can be genererated from the FreeCAD files. The graphite felt should be compressed to 70% of it's original thickness. The compression is fixed by the combined total thickness of the flow frame and two gaskets.


Place one [flow frame][flow frames](fromstep){qty: 2} on top of the assembly, using the bolts to guide the flow frame and align it with the fluid holes in the gasket.

## Add the first blocking gasket {pagestep}

Place one [blocking gasket][blocking gaskets](fromstep){qty: 2} on top of the assembly, using the bolts to guide the gasket and align it with the fluid holes in the flow frame.

## Add the membranes {pagestep}

Take the three [cut membranes](fromstep){qty: 3} and add them to the assembly.

## Add the second blocking gasket {pagestep}

Place one blocking gasket on top of the assembly, using the bolts to guide the gasket.

## Add the second flow frame {pagestep}

Place one flow frame on top of the assembly, using the bolts to guide the flow frame.

## Add the second pass-through gasket {pagestep}

Place one pass-through gasket on top of the assembly, using the bolts to guide the gasket and align it with the fluid holes in the flow frame.

## Add the second grafoil current collector {pagestep}

Place one grafoil current collector on top of the pass-through gasket, so that it will align with the copper current collector of the second cell body in the next step.

## Add the second cell body {pagestep}

Place the second cell body (with barbs and copper plate installed) on top of the assembly and ensure all fluid holes are aligned. Hand-tighten four [M6 nuts]{qty: 4} onto the exposed threads of the bolts in order to lightly compress the cell and hold all the components in place.

## Tighten the bolts {pagestep}

Progressively tighten the bolts to 5 N⋅m in a [4-bolt flange pattern](https://www.flangeboltchart.com/torque-patterns/4-bolt-torque-pattern) using a [torque wrench]{qty: 1, cat: tool, Note: to accept 5 mm allen key or 10 mm hex socket} fitted with a [10 mm socket]{qty: 1, cat: tool, Note: To fit torque wrench} and a [5mm hex key]{qty: 1,cat: tool}


>i **Note** 
>i
>i Progressively tightening using a flange pattern is important to evenly compressing the cell and ensuring leak-free operation


## Add the barbed fittings

>!! **Warning** 
>!!
>!! Do not overtighten the barbed fittings, or else they can shear off inside of the cell body!

Add the o-rings to the bottom of the threaded cell ports. Insert the barbed fittings and thread to finger-tight, then turn with a wrench 90 degrees past finger-tight.


-------------------------------------------------------------

**Now you have an [assembled flow cell]{output, qty:1}!**
