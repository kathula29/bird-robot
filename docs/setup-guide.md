# Development Environment Setup Guide

## RB-003.2 — Install and record development tools

**Owner:** Prashant
**Last updated:** 2026-10-01
**Status:** In review

This guide records the Windows development environment used for the bird-robot prototype. It documents the installed tools and the setup path used for the controller software. Fresh-copy execution, CAD reopening and backup recovery are recorded separately under RB-003.3.

## Windows computer

| Item | Recorded value | Evidence/status |
| --- | --- | --- |
| Operating system | Windows 11 Pro | User-supplied system information |
| Windows version | 25H2 | User-supplied system information |
| OS build | 26200.9457 | User-supplied system information |
| Processor | Intel Core i9-14900KS, 3.20 GHz | User-supplied system information |
| Installed RAM | 64.0 GB; 63.7 GB usable | User-supplied system information |
| System type | 64-bit operating system, x64-based processor | User-supplied system information |
| Dedicated graphics | NVIDIA GeForce RTX 3050, 6 GB | User-supplied system information |
| Integrated graphics | Intel UHD Graphics | User-supplied system information |
| Installation drive | C: | Drive containing the recorded Windows development-tool installation |
| Free space on installation drive | 166 GB free of 735 GB | Measured in File Explorer on 1 October 2026 |

The earlier 932 GB total / 572 GB used values describe the reported storage device and are not used as the installation-drive free-space record. The final record must be the free space on the drive containing the installed tools.

## Installed software and controller packages

| Tool/package | Installed version | Status / evidence |
| --- | --- | --- |
| Python | 3.14.2, 64-bit CPython | Confirmed from the supplied Python startup output |
| Git | 2.51.0.windows.1 | Confirmed from the supplied Git version output |
| Arduino IDE | 2.3.10 | Installed version recorded |
| FreeCAD | 1.1.3 | Installed version recorded; sample CAD check is in RB-003.3 |
| MuJoCo | 3.14.0 | Installed and import-verified in the project Python 3.14 virtual environment at `C:\Users\Android\Desktop\bird-robot\.venv\Scripts\python.exe` |
| GitHub Desktop | 3.6.6 (x64) | User-reported installed version; the older 3.22.0 entry in `docs/revisions.md` has been reconciled |
| OpenRB-150 board package | OpenRB-150, version 0.2.1 | Installed board package recorded |
| Controller library | Dynamixel2Arduino, version 0.8.1 | Library used by the working sketch and recorded in the licence register |

The versions above describe the local development setup. They do not by themselves approve a firmware release or a hardware power test.

## Setup steps used

### 1. Python and Git

1. Install 64-bit Python for Windows and confirm the interpreter with `python --version`.
2. Create and use the project virtual environment with `py -3.14 -m venv .venv`, then activate it with `.\.venv\Scripts\activate`.
3. Confirm Git with `git --version`.
4. Use GitHub Desktop 3.6.6 to clone the repository, select the `docs/repository-setup` branch, review changes and publish commits.

The selected MuJoCo environment is `C:\Users\Android\Desktop\bird-robot\.venv\Scripts\python.exe`. It uses Python 3.14.2 (64-bit).

### 2. Arduino IDE and OpenRB-150

1. Install Arduino IDE 2.3.10.
2. Open **Boards Manager**, search for the ROBOTIS OpenRB-150 package, and install/select OpenRB-150 package version 0.2.1.
3. Connect the OpenRB-150 to the Windows computer by USB and select the detected COM port. The recorded port was COM3; Windows may assign a different port later.
4. Open **Library Manager**, search for `Dynamixel2Arduino`, and install version 0.8.1.
5. Compile/upload the project controller sketch using the selected OpenRB-150 board and the recorded library.
6. Keep USB and controller evidence separate from the later powered-motor tests; the existing USB evidence is linked below.

### 3. FreeCAD

1. Install FreeCAD 1.1.3.
2. Open the project CAD files with FreeCAD.
3. Use the repository's documented sample macro and CAD verification under RB-003.3 for fresh-copy execution and reopening results.

### 4. MuJoCo

1. From `C:\Users\Android\Desktop\bird-robot`, create the Python 3.14 environment with `py -3.14 -m venv .venv` and activate it with `.\.venv\Scripts\activate`.
2. Install the package with `python -m pip install mujoco`.
3. Verify the installed version and environment with `python -c "import mujoco, sys; print(mujoco.__version__); print(sys.executable)"`.
4. Verified result: MuJoCo 3.14.0 installed at `C:\Users\Android\Desktop\bird-robot\.venv\Lib\site-packages`; import succeeded using `C:\Users\Android\Desktop\bird-robot\.venv\Scripts\python.exe`.
5. Do not claim that a robot simulation has been validated by this setup ticket; simulation work is recorded separately.

## OpenRB-150 USB/controller record

| Item | Recorded value |
| --- | --- |
| Selected board | OpenRB-150 |
| Detected COM port | COM3 |
| Board-package version | 0.2.1 |
| Controller library | Dynamixel2Arduino |
| Library version | 0.8.1 |
| USB data connection | Previously checked using Arduino IDE with the OpenRB-150 and XL330-M288-T |
| Evidence | [Existing Zoho RB-003.2 comment and attachment](https://projects.zoho.in/portal/nestackdotcom#zp/projects/215875000001685046/tasks/custom-view/215875000000028003/list/task-detail/215875000001689092?group_by=tasklist), dated 2026-09-25 (`WIN_20260922_14_52_03_Pro.jpg`) |

The USB evidence is a reference to the existing Zoho comment and attachment; the test is not repeated here. COM3 is the port observed on this computer and may change on another USB port or computer.

## External reference links

- [Arduino IDE installation guide](https://docs.arduino.cc/software/ide-v2/tutorials/getting-started/ide-v2-downloading-and-installing/)
- [MuJoCo Python installation reference](https://mujoco.readthedocs.io/en/stable/python.html)
- [FreeCAD installation reference](https://www.geeksforgeeks.org/installation-guide/how-to-install-freecad-on-windows/)

These links are general references. The recorded versions and project-specific steps above are the authoritative setup record.

## Mac status

The Mac check is blocked because Mac access is unavailable. The founder must either provide access or agree to defer this check. No Mac specifications or installed-tool claims are made in this record.

## Scope boundary

Sample-script execution, CAD/STEP reopening, fresh-copy recovery and repository credential checks belong to RB-003.3 and are recorded there. This ticket records the development environment and setup instructions only.

## Finalisation items

- Obtain the founder's decision on Mac access or deferral.
- Attach or link the updated guide in Zoho for review.
