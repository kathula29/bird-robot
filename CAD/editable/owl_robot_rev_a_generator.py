import os

import FreeCAD as App
import Mesh
import Part


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
EDITABLE = os.path.join(ROOT, "CAD", "editable")
STEP_DIR = os.path.join(ROOT, "CAD", "STEP")
STL_DIR = os.path.join(ROOT, "CAD", "STL")

os.makedirs(STEP_DIR, exist_ok=True)
os.makedirs(STL_DIR, exist_ok=True)

doc = App.newDocument("owl_robot_rev_a")

meta = doc.addObject("App::FeaturePython", "PlanningMetadata")
meta.Label = "PLANNING MODEL - NOT ENGINEERING RELEASE"
meta.addProperty("App::PropertyString", "DesignRevision", "Revision")
meta.DesignRevision = "owl_robot_rev_a"
meta.addProperty("App::PropertyString", "FreeCADVersion", "Revision")
meta.FreeCADVersion = "1.1.3"
meta.addProperty("App::PropertyString", "ModelStatus", "Revision")
meta.ModelStatus = "Basic planning model; dimensions provisional"
meta.addProperty("App::PropertyString", "ExternalGeometry", "Licence")
meta.ExternalGeometry = "No Microduck geometry imported"
meta.addProperty("App::PropertyString", "ApprovalStatus", "Licence")
meta.ApprovalStatus = "Pending founder and qualified engineering reviewer approval"


def add_part(name, label, shape, colour):
    obj = doc.addObject("Part::Feature", name)
    obj.Label = label
    obj.Shape = shape
    view = getattr(obj, "ViewObject", None)
    if view is not None:
        view.ShapeColor = colour
    return obj


cream = (0.92, 0.82, 0.62)
dark = (0.18, 0.18, 0.20)
orange = (0.95, 0.55, 0.12)

# Provisional layout only. Z is vertical and +Y is the front of the owl.
parts = []
parts.append(add_part("Body", "Body - provisional", Part.makeSphere(32, App.Vector(0, 0, 58)), cream))
parts.append(add_part("Head", "Head - provisional", Part.makeSphere(27, App.Vector(0, 0, 105)), cream))
parts.append(add_part("Neck", "Neck interface - provisional", Part.makeCylinder(14, 16, App.Vector(0, 0, 82)), dark))
parts.append(add_part("LeftWing", "Left wing - provisional", Part.makeSphere(18, App.Vector(-30, 0, 58)), cream))
parts.append(add_part("RightWing", "Right wing - provisional", Part.makeSphere(18, App.Vector(30, 0, 58)), cream))
parts.append(add_part("LeftLeg", "Left leg - provisional", Part.makeBox(11, 12, 38, App.Vector(-17, -6, 20)), dark))
parts.append(add_part("RightLeg", "Right leg - provisional", Part.makeBox(11, 12, 38, App.Vector(6, -6, 20)), dark))
parts.append(add_part("LeftFoot", "Left foot - provisional", Part.makeBox(24, 34, 10, App.Vector(-24, 4, 10)), cream))
parts.append(add_part("RightFoot", "Right foot - provisional", Part.makeBox(24, 34, 10, App.Vector(0, 4, 10)), cream))

# Beak is a simple prism made from a front-facing profile.
profile = [
    App.Vector(-14, 24, 103),
    App.Vector(14, 24, 103),
    App.Vector(0, 24, 92),
    App.Vector(-14, 24, 103),
]
beak_face = Part.Face(Part.makePolygon(profile))
parts.append(add_part("Beak", "Closed beak - provisional", beak_face.extrude(App.Vector(0, 14, 0)), orange))

parts.append(add_part("LeftEye", "Left eye reference", Part.makeSphere(4, App.Vector(-9, 24, 113)), dark))
parts.append(add_part("RightEye", "Right eye reference", Part.makeSphere(4, App.Vector(9, 24, 113)), dark))

doc.recompute()

fcstd_path = os.path.join(EDITABLE, "owl_robot_rev_a.FCStd")
step_path = os.path.join(STEP_DIR, "owl_robot_rev_a.step")
stl_path = os.path.join(STL_DIR, "owl_robot_rev_a.stl")

doc.saveAs(fcstd_path)
Part.export(parts, step_path)
Mesh.export(parts, stl_path)

print("Created:", fcstd_path)
print("Created:", step_path)
print("Created:", stl_path)
print("Status: planning model only; engineering validation and approval pending")
