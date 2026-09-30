# FreeCAD Sample Setup Check

**Task:** RB-003.3 — Verify setup and backups  
**Owner:** Prashant  
**Location:** [tests/freecad_setup](https://github.com/kathula29/bird-robot/tree/docs/repository-setup/tests/freecad_setup)

This folder contains the FreeCAD sample used to check the development environment for the original owl-inspired robot project. It is a software setup sample, not a validated robot component.

## Design specification

| Property | Nominal value |
| --- | --- |
| Length | 40 mm |
| Width | 30 mm |
| Thickness | 3 mm |
| Number of holes | 4 |
| Hole diameter | 3 mm |
| Hole-centre distance from adjacent edges | 5 mm |
| FreeCAD version used | 1.1.3 |

These values describe the CAD design, not physical measurements.

## Folder contents

| File | Description |
| --- | --- |
| `sample_plate.FCMacro` | Runnable FreeCAD source macro. |
| `sample_plate.FCStd` | Editable FreeCAD model created in the original check. |
| `sample_plate.step` | STEP export created in the original check. |
| `sample_plate.20260925-142049.FCBak` | Automatically generated FreeCAD backup. |
| `sample_plate` | Additional original file; its exact format remains unconfirmed. |
| `verification-results.md` | Fresh-copy, recovery and credential-check record. |

## Run the check from a fresh repository copy

1. Clone the `docs/repository-setup` branch into a new folder.
2. Open FreeCAD 1.1.3.
3. Use **Macro → Macros…**, choose `sample_plate.FCMacro`, and run it.
4. Confirm that a 40 × 30 × 3 mm plate with four 3 mm holes appears in the 3D view.
5. Open the dated `FreeCAD_Setup_Check` folder created in the current user's home folder. It must contain `sample_plate.FCStd`, `sample_plate.step` and `test_report.txt`.
6. Reopen the generated FCStd and STEP files in FreeCAD.
7. Record the tested commit and results in `verification-results.md`.

## Scope

This sample covers initial CAD and development-environment verification only. It does not demonstrate robot assembly, wiring, motor performance, walking, durability or production readiness.

