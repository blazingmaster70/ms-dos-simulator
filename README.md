# MS-DOS Terminal Simulator

A Python program that simulates the Microsoft MS-DOS 6.22 command-line environment. It features a classic startup sequence, a DOS-style prompt, directory navigation, and a collection of simulated MS-DOS commands.

**Windows Only**

---

## Requirements

- Python 3
- Windows

The program uses Python's built-in `winsound` module, so it is designed to run on Windows.

---

## Running

```bash
python ms-dos.py
```

---

## Features

- Classic MS-DOS 6.22 boot sequence
- DOS-style command prompt
- PC speaker startup beep
- Simulated directory structure
- Directory navigation
- Simulated file system
- Directory listings
- File viewing
- Environment variable simulation
- Volume label support
- Memory information
- Built-in help command
- Screen clearing
- DOS version information

---

## Directory Structure

```
C:\
├── DOS
│   ├── HIMEM.SYS
│   ├── MEM.EXE
│   ├── FORMAT.COM
│   ├── CHKDSK.EXE
│   ├── EDIT.COM
│   ├── XCOPY.EXE
│   ├── ATTRIB.EXE
│   ├── TREE.COM
│   ├── LABEL.EXE
│   ├── PATH.COM
│   ├── SETVER.EXE
│   ├── UNDELETE.EXE
│   ├── DEFRAG.EXE
│   ├── FDISK.EXE
│   └── SYS.COM
└── GAMES
    └── DOOM
        ├── DOOM.EXE
        └── DEFAULT.CFG
```

---

## Supported Commands

- ATTRIB
- CD / CHDIR
- CHKDSK
- CLS
- COPY
- DATE
- DEL / ERASE
- DIR
- ECHO
- EXIT
- FDISK
- FORMAT
- HELP
- LABEL
- MD / MKDIR
- MEM
- MOVE
- PATH
- PROMPT
- RD / RMDIR
- REN / RENAME
- SET
- SYS
- TIME
- TREE
- TYPE
- VER
- VOL

---

## Notes

This project is a simulator created for fun and learning. It does not emulate a real MS-DOS operating system or execute DOS programs.

Microsoft, MS-DOS, and Windows are trademarks of Microsoft Corporation. This project is not affiliated with or endorsed by Microsoft.
