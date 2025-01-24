<!-- There should be only one Header per page. You do not need to use all the keys -->
# Assembling the jig with electronics and flow cell![page thumbnail](images/Screenshot_20250102_190036.png "")

| Detail        | Value                       |
|---------------|-----------------------------|
| Time Required | None      |
| Skills        | Mechanical assembly      |




Gather the following components:


### Parts 

* 1 [assembled flow cell]{: Class="bom"} 
* 4 [cut tubing pieces]{: Class="bom"} 
* 1 [jig with pumps and power electronics]{: Class="bom"} 
* 2 [reservoirs]{: Class="bom"} 




## Step 1: Add reservoirs to jig {:id="add-reservoirs-to-jig" class="page-step"}

Insert the two [reservoirs] into the [jig with pumps and power electronics] as shown:


![](images/Screenshot_20250102_190203.png "")

> **Warning** 
> 
> One barb on each reservoir is slightly longer than the other barb. This longer barb is for electrolyte returning to the reservoir from the cell, and there is an internal channel in the reservoir that returns electrolyte to the top of the reservoir.
> 
> The short barb is for electrolyte going to the pumps from the reservoir, and it draws electrolyte from the bottom of the reservoir. 
> 
>!!![](images/Screenshot_20250102_190750.png "")

## Step 2: Add cell to jig and connect to tubing {:id="add-cell-to-jig-and-connect-to-tubing" class="page-step"}

Take the [assembled flow cell] and place it into the jig, connecting the tubing as described and shown:

Take the [cut tubing pieces] and connect the tubing as so, for both positive and negative half-cells:
- pump outlet to inlet of cell (on bottom)
- outlet of cell (on top) to long barb on reservoir
- short barb on reservoir to pump inlet

![Same tubing principles apply for peristaltic pumps](images/front.png "")



> **Warning** 
> 
> Avoid creating kinks and sharp bends in the tubing when assembling the cell. This can create issues with electrolyte flow.



> **Warning** 
> 
> Electrolyte flow must flow from bottom of the cell upwards to top, in order to clear out gas bubbles from the cell and ensure good liquid electrolyte flow

This makes an <a name="output__assembled-test-jig"></a>assembled test jig.
[reservoirs]:fabrication.md ""
[jig with pumps and power electronics]:electronics.md ""
[assembled flow cell]:cell_assembly.md ""
[cut tubing pieces]:fabrication.md ""

<!-- GitBuilding Nav -->
---

[Previous page](cell_assembly.md) | [Next page](leak_test.md)