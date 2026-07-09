# MS-DOS Terminal Simulator

A Python-based MS-DOS terminal simulator that recreates the look and feel of the classic MS-DOS command prompt. It runs directly in your terminal and includes several built-in DOS-style commands.

**Windows is recommended.**

---

## 🐍 Python File

Run the simulator:

```bash
python ms-dos.py
```

If you have multiple Python versions installed:

```bash
python3 ms-dos.py
```

---

## Features

- MS-DOS-style terminal interface
- Classic boot sequence
- DOS-inspired commands
- Simulated file system
- Simple command prompt
- No external libraries required (unless your code uses them)

---

## Supported Commands

| Command | Description |
|---------|-------------|
| `DIR` | Lists files and folders. |
| `CD` | Changes the current directory (simulated). |
| `TYPE` | Displays the contents of a text file. |
| `CLS` | Clears the screen. |
| `VER` | Displays the simulated MS-DOS version. |
| `HELP` | Shows available commands. |
| `MEM` | Displays simulated memory information. |

*(The available commands depend on the features implemented in your Python code.)*

---

## Requirements

- Python 3.8 or newer
- Windows (recommended)

If your program imports extra modules such as `keyboard`, install them with:

```bash
pip install keyboard
```

---

## Running

Clone the repository:

```bash
git clone <repository-url>
cd <repository-folder>
```

Run:

```bash
python ms-dos.py
```

---

## Project Structure

```
ms-dos.py      # Main simulator
README.md      # Project documentation
```

---

## Notes

This project is a simulator made for fun and learning. It does **not** emulate a real MS-DOS system or run DOS software.

Microsoft, MS-DOS, and Windows are trademarks of Microsoft Corporation. This project is not affiliated with or endorsed by Microsoft.
