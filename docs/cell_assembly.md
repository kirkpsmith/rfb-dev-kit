---
Details:
    Time: Tens of minutes
    Skills:
      - Mechanical assembly
      - Using a torque wrench properly
---
<!-- There should be only one Header per page. You do not need to use all the keys -->
# Assembling the flow cell from components

Ensure you have the following components:
{{BOM}}

Refer to the following diagram for the cell assembly process.

![](../CAD/exports/Cell Assembly.pdf)

## Place the endplate on the cell assembly tool {pagestep}

Take the [cell assembly tool](fromstep){qty: 1} and place the [endplate with pins](fromstep){qty: 1} with the pins pointing upwards.


## Add the brass current collector {pagestep}

Make sure the large tubing holes of the [outer current collector with banana connector](fromstep){qty: 1} align with the endplate.

## Add the negative grafoil current collector {pagestep}

Make sure the large tubing holes of the [grafoil current collector][grafoil current collectors](fromstep){qty: 1} align with the brass current collector.


## Add the negative outer gasket {pagestep}

Place one [outer gasket][outer gaskets](fromstep){qty: 1} on top of the assembly, using the bolts to guide the gasket and align it with the fluid holes in the cell body.


## Add the negative flow frame {pagestep}

Place one [flow frame with tubing and adapters](fromstep){qty: 1} on top of the assembly, with the barbs and tubing facing downward into the cell assembly tool.


>? **Help Block** 
>?
>? The total combined thickess of the flow frames and (compressed) gaskets is key to achieving the desired results! There are multiple thickness options in the `flow-frames` folder and custom thicknesses can be genererated from the FreeCAD files. The graphite felt should be compressed to 70% of it's original thickness. The compression is fixed by the combined total thickness of the flow frame and two gaskets.

## Add the negative graphite felt{pagestep}

Place one [graphite felt][cut electrodes](fromstep){qty:1} on top of the assembly.


## Add the negative inner gasket{pagestep}

Take one [inner gasket][inner gaskets](fromstep){qty: 1} and add it to the assembly.


## Add the membranes {pagestep}

Take the three [cut membranes](fromstep){qty: 3} and add them to the assembly.



## Add the positive inner gasket{pagestep}

Take one [inner gasket][inner gaskets](fromstep){qty: 1} and add it to the assembly.


## Add the positive flow frame {pagestep}

Place one flow frame with tubing on top of the assembly, using the bolts to guide the flow frame.


## Add positive outer gasket {pagestep}

Place one [outer gasket][outer gaskets](fromstep){qty:1} on top of the assembly, using the bolts to guide the flow frame.


## Add positive graphite felt{pagestep}

Place one [graphite felt][cut electrodes](fromstep){qty:1} on top of the assembly, using the bolts to guide the flow frame.


## Add the positive grafoil current collector {pagestep}

Place the positive [grafoil current collector][grafoil current collectors](fromstep){qty: 1} over the flow frame.


## Add the positive brass current collector {pagestep}

Place the positive [current collector][brass current collectors](fromstep){qty: 1} on the cell as shown so the tab is facing opposite the negative current collector tab.

## Add the positive endplate {pagestep}

Place the second cell body (with barbs and brass plate installed) on top of the assembly and ensure all fluid holes are aligned. 

## Tighten with C-clamp {pagestep}


Progressively tighten the bolts to 5 N⋅m in a [4-bolt flange pattern](https://www.flangeboltchart.com/torque-patterns/4-bolt-torque-pattern) using a [torque wrench]{qty: 1, cat: tool, Note: to accept 5 mm allen key or 10 mm hex socket} fitted with a [10 mm socket]{qty: 1, cat: tool, Note: To fit torque wrench} and a [5mm hex key]{qty: 1,cat: tool}



-------------------------------------------------------------

**Nice work, now you have an [assembled flow cell]{output, qty:1}!**




