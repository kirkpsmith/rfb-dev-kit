# run script from terminal with `<path-to-FreeCAD> --console export-stl.py`

import Mesh, Import, TechDrawGui
from PySide import QtCore

# Endplate (Hole)

FreeCAD.openDocument('endplate-hole.FCStd')
__objs__ = []
__objs__.append(FreeCAD.getDocument("endplate_hole").getObject("Body004"))
if hasattr(Mesh, "exportOptions"):
    options = Mesh.exportOptions(u"../exports/Endplate-Hole.stl")
    Mesh.export(__objs__, u"../exports/Endplate-Hole.stl", options)
else:
    Mesh.export(__objs__, u"../exports/Endplate-Hole.stl")
del __objs__
App.closeDocument(App.ActiveDocument.Name)


# Endplate (Pin)

FreeCAD.openDocument('endplate-pin.FCStd')
__objs__ = []
__objs__.append(FreeCAD.getDocument("endplate_pin").getObject("Body004"))
if hasattr(Mesh, "exportOptions"):
    options = Mesh.exportOptions(u"../exports/Endplate-Pin.stl")
    Mesh.export(__objs__, u"../exports/Endplate-Pin.stl", options)
else:
    Mesh.export(__objs__, u"../exports/Endplate-Pin.stl")
del __objs__
App.closeDocument(App.ActiveDocument.Name)


# Membrane Frame

FreeCAD.openDocument('membrane-frame.FCStd')
__objs__ = []
__objs__.append(FreeCAD.getDocument("membrane_frame").getObject("Body007"))
if hasattr(Mesh, "exportOptions"):
    options = Mesh.exportOptions(u"../exports/Membrane-Frame.stl")
    Mesh.export(__objs__, u"../exports/Membrane-Frame.stl", options)
else:
    Mesh.export(__objs__, u"../exports/Membrane-Frame.stl")
del __objs__
App.closeDocument(App.ActiveDocument.Name)

# Flow Frame

FreeCAD.openDocument('flow-frame.FCStd')
__objs__ = []
__objs__.append(FreeCAD.getDocument("flow_frame").getObject("Body"))
if hasattr(Mesh, "exportOptions"):
    options = Mesh.exportOptions(u"../exports/Flow-Frame.stl")
    Mesh.export(__objs__, u"../exports/Flow-Frame.stl", options)
else:
    Mesh.export(__objs__, u"../exports/Flow-Frame.stl")
del __objs__
App.closeDocument(App.ActiveDocument.Name)


# Double Reservoir

try:
    FreeCAD.openDocument('double-reservoir.FCStd')
except ModuleNotFoundError:
    print("uh oh")
finally:
    __objs__ = []
    __objs__.append(FreeCAD.getDocument("double_reservoir").getObject("Connect"))
    if hasattr(Mesh, "exportOptions"):
        options = Mesh.exportOptions(u"../exports/Double-Reservoir.stl")
        Mesh.export(__objs__, u"../exports/Double-Reservoir.stl", options)
    else:
        Mesh.export(__objs__, u"../exports/Double-Reservoir.stl")
    del __objs__
App.closeDocument(App.ActiveDocument.Name)


# Jig

FreeCAD.openDocument('jig.FCStd')
__objs__ = []
__objs__.append(FreeCAD.getDocument("jig").getObject("Body"))
if hasattr(Mesh, "exportOptions"):
    options = Mesh.exportOptions(u"../exports/Jig.stl")
    Mesh.export(__objs__, u"../exports/Jig.stl", options)
else:
    Mesh.export(__objs__, u"../exports/Jig.stl")
del __objs__
App.closeDocument(App.ActiveDocument.Name)


# Cell Assembly Tool

FreeCAD.openDocument('cell-assembly-tool.FCStd')
__objs__ = []
__objs__.append(FreeCAD.getDocument("cell_assembly_tool").getObject("Body005"))
if hasattr(Mesh, "exportOptions"):
    options = Mesh.exportOptions(u"../exports/Cell-Assembly-Tool.stl")
    Mesh.export(__objs__, u"../exports/Cell-Assembly-Tool.stl", options)
else:
    Mesh.export(__objs__, u"../exports/Cell-Assembly-Tool.stl")
del __objs__
App.closeDocument(App.ActiveDocument.Name)

# Outer Current Collector

FreeCAD.openDocument('outer-current-collector.FCStd')

__objs__ = []
__objs__.append(FreeCAD.getDocument("outer_current_collector").getObject("Body002"))

if hasattr(Import, "exportOptions"):
    options = Import.exportOptions(u"../exports/Current-Collector.step")
    Import.export(__objs__, u"../exports/Current-Collector.step", options)
else:
    Import.export(__objs__, u"../exports/Current-Collector.step")
del __objs__

__objs__ = []
__objs__.append(FreeCAD.getDocument("outer_current_collector").getObject("Page"))


## following hack is from here: https://github.com/FreeCAD/FreeCAD/issues/19603
# wait for threads to complete before checking result
loop = QtCore.QEventLoop()

timer = QtCore.QTimer()
timer.setSingleShot(True)
timer.timeout.connect(loop.quit)

timer.start(2000)   #2 second delay
loop.exec_()

##

if hasattr(TechDrawGui, "exportOptions"):
    options = TechDrawGui.exportOptions(u"../exports/Current Collector Drawing.svg")
    TechDrawGui.export(__objs__, u"../exports/Current Collector Drawing.pdf", options)
else:
    TechDrawGui.export(__objs__, u"../exports/Current Collector Drawing.pdf")
del __objs__

App.closeDocument(App.ActiveDocument.Name)




## Assembly

FreeCAD.openDocument('assembly.FCStd')

__objs__ = []
__objs__.append(FreeCAD.getDocument("assembly").getObject("Page"))
import TechDrawGui, FreeCADGui


if hasattr(TechDrawGui, "exportOptions"):
    options = TechDrawGui.exportOptions(u"../exports/assembly-Page123.svg")
    TechDrawGui.export(__objs__, u"../exports/assembly-Page123.svg", options)
else:
    TechDrawGui.export(__objs__, u"../exports/assembly-Page123.svg")
del __objs__


App.closeDocument(App.ActiveDocument.Name)


exit()