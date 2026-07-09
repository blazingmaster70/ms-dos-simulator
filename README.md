# MS-DOS Terminal Simulator

A high-fidelity, hardware-free MS-DOS 6.22 environment simulation built entirely using standard web technologies. This project replicates the classic command-line experience, complete with an isolated virtual file system (VFS), authentic terminal rendering, and a suite of core legacy executable behaviors.

**THIS IS WINDOWS ONLY**

Run it directly in the browser with zero dependencies or emulation overhead.

---

## 🖥️ Python File
Check out the Python file: **[Launch MS-DOS Simulator](ms-dos.py)**

---

## ⚡ Key Features

* **Hardware-Free Execution:** Runs entirely inside the browser sandbox using vanilla TypeScript/JavaScript; no actual x86 hardware or underlying disk images required.
* **Virtual File System (VFS):** Supports hierarchical structures (`CD`, `DIR`), file management, and reading contents via `TYPE`.
* **Authentic CRT Aesthetics:** Styled using precise CSS layouts featuring monospace typography, retro scanlines, and a blinking system cursor block.
* **Memory Management Diagnostics:** Includes a modeled `MEM` command mapping conventional, upper, and extended (XMS) structural layout pools.

---

## 🛠️ Core Commands Supported

| Command | Description |
| :--- | :--- |
| `DIR` | Lists all files and subdirectories within the current path. |
| `CD [dir]` | Changes the current working directory path within the VFS structure. |
| `TYPE [file]` | Outputs the raw text content of a specified target file. |
| `MEM` | Provides an architecture breakdown of simulated base/extended memory. |
| `VER` | Displays the current simulated MS-DOS version string. |
| `CLS` | Flushes the current display buffer and clears the screen terminal. |
...There is more. Use 'help' in MS-DOS Simulator for more commands.

---

## 📂 Architecture Overview

The system architecture cleanly decouples user interface interaction from the underlying operational logic:
