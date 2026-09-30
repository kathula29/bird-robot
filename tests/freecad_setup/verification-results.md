# RB-003.3 — Setup and backup verification record

**Date:** 2026-09-30  
**Repository branch:** `docs/repository-setup`  
**Tested commit:** Pending — update after the verification commit is pushed.

## Test procedure

1. Create a fresh local clone of the `docs/repository-setup` branch.
2. Open `tests/freecad_setup/sample_plate.FCMacro` in FreeCAD 1.1.3 and run it.
3. Confirm that FreeCAD shows a 40 × 30 × 3 mm plate with four 3 mm holes.
4. Open the generated `sample_plate.FCStd` and `sample_plate.step` files.
5. Confirm that the generated report is present.
6. Treat the fresh clone as the recovery copy and confirm the tracked macro, CAD files, STEP file, README and this verification record are available.
7. Search tracked files and filenames for password, token, API-key, secret and `.env` indicators. Record only the result; never record credentials.

## Results

| Check | Result | Evidence / notes |
| --- | --- | --- |
| Runnable macro available in repository | Pending execution | `sample_plate.FCMacro` is the tracked source macro. |
| Fresh-repository-copy verification | Pending execution | Run only from a newly cloned copy of the review branch. |
| FreeCAD model and STEP reopening | Previously reported successful | Original `sample_plate.FCStd` and `sample_plate.step` are in this folder. |
| Backup and recovery | Pending execution | Fresh clone will be used as the recovery copy. |
| Credential check | Pending execution | Record method and result after the search. |

## Scope

This record verifies only the initial FreeCAD/software setup sample. It does not verify robot assembly, wiring, motor performance, walking, durability or production readiness.
