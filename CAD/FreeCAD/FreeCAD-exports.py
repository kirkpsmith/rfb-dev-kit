# run script from terminal with ` ~/AppImages/freecad.appimage  FreeCAD-exports.py`

import Mesh, Import, TechDrawGui
from PySide import QtCore

def delayHack(timeout):
    ## following hack is from here: https://github.com/FreeCAD/FreeCAD/issues/19603
    # wait for threads to complete before checking result
    loop = QtCore.QEventLoop()

    timer = QtCore.QTimer()
    timer.setSingleShot(True)
    timer.timeout.connect(loop.quit)

    timer.start(timeout*1000)   # delay in ms
    loop.exec()

def exportTechDrawSVG(document, object, timeout, path):

    __objs__ = []
    __objs__.append(FreeCAD.getDocument(document).getObject(object))

    delayHack(timeout)

    if hasattr(TechDrawGui, "exportOptions"):
        options = TechDrawGui.exportOptions(path)
        TechDrawGui.export(__objs__, path, options)
    else:
        TechDrawGui.export(__objs__, path)
    del __objs__   

def exportTechDrawPDF(document, object, timeout, path):
    __objs__ = []
    __objs__.append(FreeCAD.getDocument(document).getObject(object))

    delayHack(timeout)

    TechDrawGui.export(__objs__, path)
    del __objs__

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

# Arduino Case

FreeCAD.openDocument('uno-case.FCStd')
__objs__ = []
__objs__.append(FreeCAD.getDocument("uno_case").getObject("Body"))
if hasattr(Mesh, "exportOptions"):
    options = Mesh.exportOptions(u"../exports/uno_case_base.stl")
    Mesh.export(__objs__, u"../exports/uno_case_base.stl", options)
else:
    Mesh.export(__objs__, u"../exports/uno_case_base.stl")
del __objs__

__objs__ = []
__objs__.append(FreeCAD.getDocument("uno_case").getObject("Body002"))
if hasattr(Mesh, "exportOptions"):
    options = Mesh.exportOptions(u"../exports/reset_button.stl")
    Mesh.export(__objs__, u"../exports/reset_button.stl", options)
else:
    Mesh.export(__objs__, u"../exports/reset_button.stl")
del __objs__

__objs__ = []
__objs__.append(FreeCAD.getDocument("uno_case").getObject("Body003"))
if hasattr(Mesh, "exportOptions"):
    options = Mesh.exportOptions(u"../exports/uno_case_lid.stl")
    Mesh.export(__objs__, u"../exports/uno_case_lid.stl", options)
else:
    Mesh.export(__objs__, u"../exports/uno_case_lid.stl")
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

delayHack()

## STEP file

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


## PDF

exportTechDrawPDF("outer_current_collector", "Page", 2, u"../exports/Current Collector Drawing.pdf")

App.closeDocument(App.ActiveDocument.Name)

# Outer Gasket

FreeCAD.openDocument('outer-gasket.FCStd')

exportTechDrawPDF("outer_gasket", "Page004", 2, u"../exports/Outer Gasket Drawing.pdf")

App.closeDocument(App.ActiveDocument.Name)

# Inner Gasket

FreeCAD.openDocument('inner-gasket.FCStd')

exportTechDrawPDF("inner_gasket", "Page004", 2, u"../exports/Inner Gasket Drawing.pdf")

App.closeDocument(App.ActiveDocument.Name)

# Grafoil

FreeCAD.openDocument('inner-current-collector.FCStd')

exportTechDrawPDF("inner_current_collector", "Page003", 2, u"../exports/Grafoil Drawing.pdf")

App.closeDocument(App.ActiveDocument.Name)


# Assembly

FreeCAD.openDocument('assembly.FCStd')


exportTechDrawSVG("assembly","Page",2,u"../exports/cell.svg")

exportTechDrawSVG("assembly","Page001",2,u"../exports/front.svg")

exportTechDrawSVG("assembly","Page002",2,u"../exports/back.svg")


App.closeDocument(App.ActiveDocument.Name)


exit()