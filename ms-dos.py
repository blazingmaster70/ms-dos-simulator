import time
import os
import winsound

notice = input("WARNING: This is not affiliated with the official Microsoft or MS-DOS companies. This is a program that simulates MS-DOS commands For more information, visit www.github.com/blazingmaster70/ms-dos-simulator/readme.md. Press ENTER to continue: ")
print()

frequency = 896
duration = 100

winsound.Beep(frequency, duration)

print("Starting MS-DOS...")
time.sleep(2)
print()
print("HIMEM: DOS XMS Driver, Version 3.10 - 09/30/93 Copyright 1986, 1993 Microsoft Corp.")
print()
print("HIMEM is testing extended memory...", end="", flush=True)
time.sleep(1.5)
print("done.")
print()
print("MS-DOS Prompt")
print()
print("Microsoft(R) MS-DOS(R) Version 6.22 (C)Copyright Microsoft Corp 1981-1994.")
print()

current_dir = "C:\\"
drive_label = None
echo_on = True
prompt_value = "$P$G"
path_value = "C:\\DOS"

dirs = {"C:\\", "C:\\DOS", "C:\\GAMES", "C:\\GAMES\\DOOM"}

help_commands = [
    "ASSIGN", "ATTRIB", "BACKUP", "BREAK", "CALL", "CD/CHDIR", "CHCP", "CHKDSK",
    "CHKNTFS", "CLS", "CMD", "COMMAND", "COMP", "COMPACT", "COPY", "CTTY",
    "DATE", "DEBUG", "DEFRAG", "DEL/ERASE", "DELTREE", "DIR", "DISKCOMP",
    "DISKCOPY", "DOSKEY", "DRIVER.SYS", "DOSSHELL", "ECHO", "EDLIN", "EDIT",
    "EXIT", "EXPAND", "FASTHELP", "FC", "FDISK", "FIND", "FOR", "FORMAT",
    "GOTO", "GRAFTABL", "HELP", "IF", "JOIN", "KEYB", "LABEL", "LOADFIX",
    "LOADHIGH/LH", "LOCK", "MD/MKDIR", "MEM", "MEMMAKER", "MODE", "MORE",
    "MOVE", "MSAV", "MSCDEX", "MSD", "NLSFUNC", "PATH", "PAUSE", "PRINT",
    "PROMPT", "QBASIC", "RD/RMDIR", "RENAME/REN", "REPLACE", "RESTORE", "SET",
    "SETVER", "SHARE", "SORT", "SUBST", "SYS", "TIME", "TREE", "TYPE",
    "UNDELETE", "UNFORMAT", "VER", "VERIFY", "VOL", "XCOPY",
    "APPEND", "ARJ", "BASIC", "BASICA", "BUFFERS", "CACLS", "CHOICE", "CLIP",
    "COMMAND /C", "COMPRESS", "CONFIG", "CONVERT", "COPY CON", "DBLSPACE",
    "DELOLDOS", "DISABLE", "DRVSPACE", "EGA", "EMM386", "EXE2BIN", "FCBS",
    "FINDSTR", "GRAPHICS", "IMKDIR", "INSTALL", "INTERLNK", "INTERSVR",
    "LASTDRIVE", "LISTS", "LZEXE", "RECOVER", "SMARTDRV", "STACKS", "SWITCHES",
    "UNLOCK", "VSAFE"
]

help_commands = help_commands[:135]

def prompt_path():
    return current_dir + ">"

def norm_path(path):
    path = path.strip().replace("/", "\\")
    if path in ["", "."]:
        return current_dir
    if path == "..":
        if current_dir == "C:\\GAMES\\DOOM":
            return "C:\\GAMES"
        if current_dir in ["C:\\DOS", "C:\\GAMES"]:
            return "C:\\"
        return current_dir
    if path in ["\\", "C:\\"]:
        return "C:\\"
    if path.startswith("C:\\"):
        return path.rstrip("\\")
    if current_dir == "C:\\":
        if path.lower() == "dos":
            return "C:\\DOS"
        if path.lower() == "games":
            return "C:\\GAMES"
    if current_dir == "C:\\GAMES" and path.lower() == "doom":
        return "C:\\GAMES\\DOOM"
    return (current_dir + path).rstrip("\\")

def show_dir(path):
    print(" Volume in drive C has no label.")
    print(" Volume Serial Number is 1AC2-34EF")
    if path == "C:\\":
        print(" Directory of C:\\\n")
        print("DOS          <DIR>     05-12-94  6:22p")
        print("COMMAND  COM   54,645  05-31-94  6:22p")
        print("AUTOEXEC BAT       25  06-01-94  1:10a")
        print("CONFIG   SYS       38  06-01-94  1:12a")
        print("GAMES        <DIR>     07-15-94  8:45p")
        print("         3 file(s)         54,708 bytes")
        print("         2 dir(s)      14,204,928 bytes free\n")
    elif path == "C:\\DOS":
        print(" Directory of C:\\DOS\n")
        print(".            <DIR>     05-12-94  6:22p")
        print("..           <DIR>     05-12-94  6:22p")
        print("HIMEM    SYS   14,208  09-30-93  6:22p")
        print("MEM      EXE   32,150  05-31-94  6:22p")
        print("FORMAT   COM   22,771  05-31-94  6:22p")
        print("CHKDSK   EXE   37,120  05-31-94  6:22p")
        print("EDIT     COM   45,312  05-31-94  6:22p")
        print("XCOPY    EXE   58,240  05-31-94  6:22p")
        print("ATTRIB   EXE   18,944  05-31-94  6:22p")
        print("TREE     COM   16,384  05-31-94  6:22p")
        print("LABEL    EXE   11,264  05-31-94  6:22p")
        print("PATH     COM   10,240  05-31-94  6:22p")
        print("SETVER   EXE   21,504  05-31-94  6:22p")
        print("UNDELETE EXE   24,576  05-31-94  6:22p")
        print("DEFRAG   EXE   52,224  05-31-94  6:22p")
        print("FDISK    EXE   34,816  05-31-94  6:22p")
        print("SYS      COM   12,288  05-31-94  6:22p")
        print("         15 file(s)        435,231 bytes")
        print("         2 dir(s)      14,204,928 bytes free\n")
    elif path == "C:\\GAMES":
        print(" Directory of C:\\GAMES\n")
        print("DOOM     <DIR>         12-10-93  1:10a")
        print("         0 file(s)              0 bytes")
        print("         1 dir(s)      14,204,928 bytes free\n")
    elif path == "C:\\GAMES\\DOOM":
        print(" Directory of C:\\GAMES\\DOOM\n")
        print("DOOM     EXE  245,311  12-10-93  1:10a")
        print("DEFAULT  CFG    1,024  12-11-93  4:20p")
        print("         2 file(s)        246,335 bytes")
        print("         0 dir(s)      14,204,928 bytes free\n")

def show_help():
    print("\nFor more information on a specific command, type HELP command-name\n")
    for cmd in help_commands:
        print(cmd)
    print()

while True:
    user_input = input(prompt_path() + " ")
    user = user_input.strip()
    lower = user.lower()

    if lower == "":
        continue
    elif lower == "dir":
        show_dir(current_dir)
    elif lower.startswith("cd") or lower.startswith("chdir"):
        parts = user_input.split(maxsplit=1)
        if len(parts) == 1:
            print(current_dir + "\n")
        else:
            new_dir = norm_path(parts[1])
            if new_dir in dirs:
                current_dir = new_dir
            else:
                print("Invalid directory\n")
    elif lower == "cls":
        os.system("cls" if os.name == "nt" else "clear")
    elif lower == "ver":
        print("\nMicrosoft(R) MS-DOS(R) Version 6.22\n")
    elif lower == "vol":
        print(" Volume in drive C has no label.")
        print(" Volume Serial Number is 1AC2-34EF\n")
    elif lower.startswith("label"):
        parts = user_input.split(maxsplit=1)
        if len(parts) == 1:
            print(f" Volume in drive C is {drive_label if drive_label else 'no label'}.\n")
        else:
            drive_label = parts[1].strip()
            print(" Volume label changed.\n")
    elif lower == "date":
        print("Current date is Thu 07-09-2026\n")
    elif lower == "time":
        print("Current time is 12:35:00.00a\n")
    elif lower == "echo":
        print(f"ECHO is {'on' if echo_on else 'off'}")
    elif lower.startswith("echo "):
        print(user_input[5:])
    elif lower == "mem":
        print("\nMemory Type        Total       Used       Free")
        print("----------------  --------  ---------  ---------")
        print("Conventional          640K        45K       595K")
        print("Upper                   0K         0K         0K")
        print("Extended (XMS)     15,360K     2,048K    13,312K")
        print("Total memory       16,000K     2,093K    13,907K\n")
    elif lower == "help":
        show_help()
    elif lower.startswith("help "):
        print("Help topic not available.\n")
    elif lower.startswith("md ") or lower.startswith("mkdir "):
        print("The system cannot create the directory.\n")
    elif lower.startswith("rd ") or lower.startswith("rmdir "):
        print("The system cannot remove the directory.\n")
    elif lower.startswith("del ") or lower.startswith("erase "):
        print("File deleted.\n")
    elif lower.startswith("ren ") or lower.startswith("rename "):
        print("1 file(s) renamed.\n")
    elif lower.startswith("copy "):
        print("        1 file(s) copied.\n")
    elif lower.startswith("move "):
        print("        1 file(s) moved.\n")
    elif lower.startswith("attrib "):
        print("File attributes changed.\n")
    elif lower == "path":
        print(f"PATH={path_value}\n")
    elif lower.startswith("path "):
        path_value = user_input[5:].strip()
        print("Path changed.\n")
    elif lower == "prompt":
        print(f"PROMPT {prompt_value}\n")
    elif lower.startswith("prompt "):
        prompt_value = user_input[7:].strip()
        print("Prompt changed.\n")
    elif lower == "set":
        print("COMSPEC=C:\\COMMAND.COM")
        print(f"PATH={path_value}\n")
    elif lower.startswith("set "):
        print("Environment variable set.\n")
    elif lower.startswith("chkdsk"):
        print("Volume C:")
        print("  14,204,928 bytes free")
        print("  0 bad sectors")
        print("  0 hidden files")
        print("  0 directories")
        print("  4,096 bytes in each allocation unit\n")
    elif lower.startswith("format"):
        print("Formatting 100.0 percent complete.\n")
    elif lower.startswith("fdisk"):
        print("Fixed Disk Setup Program\n")
    elif lower.startswith("sys"):
        print("System transferred.\n")
    elif lower.startswith("tree"):
        print("\nC:\\")
        print("├── DOS")
        print("└── GAMES")
        print("    └── DOOM\n")
    elif lower.startswith("type "):
        filename = lower[5:].strip()
        if current_dir == "C:\\" and filename == "autoexec.bat":
            print("@ECHO OFF\nPROMPT $P$G\nPATH C:\\DOS\nLH SMARTDRV.EXE\n")
        elif current_dir == "C:\\" and filename == "config.sys":
            print("DEVICE=C:\\DOS\\HIMEM.SYS\nDOS=HIGH,UMB\nBUFFERS=15,0\nFILES=30\n")
        elif current_dir == "C:\\GAMES\\DOOM" and filename == "default.cfg":
            print("mouse_enable=1\nsound=1\nskill=2\n")
        else:
            print("File not found\n")
    elif lower == "exit":
        break
    else:
        print("Bad command or file name\n")
