# RB-003.3 — Setup and backup verification record

**Date:** 2026-09-30  
**Repository branch:** `docs/repository-setup`  
**Tested commit:** `7f1457ede67972203d8fad58a723349af7465e67`

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
| Runnable macro available in repository | PASS | `sample_plate.FCMacro` is the tracked source macro. |
| Fresh-repository-copy verification | PASS | Fresh clone of `docs/repository-setup` at commit `7f1457ede67972203d8fad58a723349af7465e67`. Macro ran successfully in FreeCAD 1.1.3 on 2026-09-30. |
| Generated output | PASS | Macro created `sample_plate.FCStd`, `sample_plate.step` and `test_report.txt` in a dated `FreeCAD_Setup_Check` folder. |
| FreeCAD and STEP reopening | PASS | The generated FCStd and STEP files were opened by FreeCAD 1.1.3 without errors. |
| Backup and recovery | PASS | The fresh GitHub clone at the tested commit was used as the recovery copy. It contained the macro, FCStd, STEP, README and this verification record. |
| Credential check | PASS | Tracked-file content and filenames were checked for password, token, API-key, secret and `.env` indicators. No credential values or credential-like tracked filenames were identified. |

## Execution note

The fresh-copy test used the installed FreeCAD 1.1.3 command runner. The generated output folder was `FreeCAD_Setup_Check/20260930_123957` under a temporary test profile. The runner was executed from a fresh clone of the published branch, and the generated FCStd, STEP and report files were verified. The GUI macro route remains the normal interactive method described in the README.

## Scope

This record verifies only the initial FreeCAD/software setup sample. It does not verify robot assembly, wiring, motor performance, walking, durability or production readiness.
