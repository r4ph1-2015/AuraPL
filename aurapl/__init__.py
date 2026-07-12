import builtins
import os
import sys
import subprocess
import stat
import subprocess
import aurapl.pixelmdl as pixelmdl
from turtle import *

def create_aurapl_launcher_and_add_to_path():
    package_dir = os.path.dirname(os.path.abspath(__file__))

    if sys.platform == "win32":
        # ── Windows: create .bat ─────────────────────────────────────────
        launcher_path = os.path.join(package_dir, "aurapl.bat")
        content = f'@echo off\n"{sys.executable}" -c "import aurapl; aurapl.run()" %*\n'
        try:
            with open(launcher_path, "w") as f:
                f.write(content)
        except PermissionError:
            print(f"[aurapl] Could not write launcher to {launcher_path}. Try running as administrator.")

        # ── Windows: add to PATH via registry ────────────────────────────
        try:
            import winreg
            reg_key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r"Environment",
                0,
                winreg.KEY_READ | winreg.KEY_WRITE,
            )
            try:
                current_path, _ = winreg.QueryValueEx(reg_key, "PATH")
            except FileNotFoundError:
                current_path = ""
            path_entries = [p.strip() for p in current_path.split(";") if p.strip()]
            if package_dir not in path_entries:
                new_path = current_path.rstrip(";") + ";" + package_dir
                winreg.SetValueEx(reg_key, "PATH", 0, winreg.REG_EXPAND_SZ, new_path)
            winreg.CloseKey(reg_key)
            # Broadcast WM_SETTINGCHANGE so the new PATH takes effect immediately
            subprocess.run(
                ["powershell", "-NoProfile", "-Command",
                 "Add-Type -Namespace Win32 -Name NativeMethods "
                 "-MemberDefinition '[DllImport(\"user32.dll\")]public static extern "
                 "IntPtr SendMessageTimeout(IntPtr hWnd,uint Msg,UIntPtr wParam,"
                 "string lParam,uint fuFlags,uint uTimeout,out UIntPtr lpdwResult);';"
                 "$r=[UIntPtr]::Zero;"
                 "[Win32.NativeMethods]::SendMessageTimeout([IntPtr]0xffff,0x001A,"
                 "[UIntPtr]::Zero,'Environment',2,5000,[ref]$r)|Out-Null"],
                capture_output=True,
            )
        except Exception as e:
            print(f"[aurapl] Could not modify PATH automatically: {e}")
            print(f"[aurapl] Add this directory to PATH manually: {package_dir}")

    else:
        # ── macOS / Linux: create shell script ───────────────────────────
        launcher_path = os.path.join(package_dir, "aurapl")
        content = f'#!/bin/sh\nexec "{sys.executable}" -c "import aurapl; aurapl.run()" "$@"\n'
        try:
            with open(launcher_path, "w") as f:
                f.write(content)
            # Make it executable
            st = os.stat(launcher_path)
            os.chmod(launcher_path, st.st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)
        except PermissionError:
            print(f"[aurapl] Could not write launcher to {launcher_path}. Try running with sudo.")
            return

        # ── macOS / Linux: add to PATH via shell rc file ─────────────────
        if package_dir in os.environ.get("PATH", "").split(os.pathsep):
            return  # Already on PATH, nothing to do

        if sys.platform == "darwin":
            rc_files = [os.path.expanduser("~/.zshrc"), os.path.expanduser("~/.bash_profile")]
        else:
            rc_files = [os.path.expanduser("~/.bashrc"), os.path.expanduser("~/.profile")]

        export_line = f'\nexport PATH="{package_dir}:$PATH"  # added by aurapl\n'
        rc_file = next((f for f in rc_files if os.path.exists(f)), rc_files[0])

        try:
            with open(rc_file, "r") as f:
                existing = f.read()
            if package_dir not in existing:
                with open(rc_file, "a") as f:
                    f.write(export_line)
                print(f"[aurapl] Added to PATH in {rc_file}. Restart your shell or run: source {rc_file}")
        except Exception as e:
            print(f"[aurapl] Could not modify {rc_file}: {e}")
            print(f"[aurapl] Add this to PATH manually: {package_dir}")

create_aurapl_launcher_and_add_to_path()

# Run Command for Terminal
def cmdrun():
    print("[aurapl] AuraPL has been initialized. Expect Bugs and Incomplete Features. Use 'help' command for more info.")
    run()

def print(text):
    sys.stdout.write(text + "\n")

def square():
   
    def reset():
        clear()
        setx(0)
        sety(0)

    reset()
    pendown()

    times = 4
    for i in range(times):
        forward(100)
        left(90)

    print("Process has been completed, Review the output and close the windows to end the process.")
    print("Done!")
    done()

def triangle():
    def reset():
        clear()
        setx(0)
        sety(0)

    reset()
    pendown()

    times = 3
    for i in range(times):
        forward(100)
        left(120)

    print("Process has been completed, Review the output and close the windows to end the process.")
    print("Done!")
    done()

# Basic Run Command
def run():
    answer = input()
    if answer == "help":
       print("------AURAPL------")
       print("Commands:")
       print(" help - the command ""help"" is a command which shows a lot of information")
       print(" quiz - the command ""quiz"" is a command which runs a quiz using PixelMDL")
       print(" square - the command ""square"" is a command which draws a square using turtle graphics")
       print(" triangle - the command ""triangle"" is a command which draws a triangle using turtle graphics")
       print(" devmode - the command ""devmode"" is a command which loads Developer Mode, which is specifically meant for PixelMDL.")
       print(" More Commands Upcoming")
       print("How to program using AuraPL -")
       print(" All Possible Commands for coding -")
       print("  print() - prints the value in the brackets")
       print("  square() - draws a square")
       print("  triangle() - draws a triangle")
       print("  More Commands Upcoming")
       run()
    if answer == "square":
        square()
        run()
    if answer == "triangle":
        triangle()
        run()
    if answer == "quiz":
        if pixelmdl.disabled:
            print("Function \"quiz\" does not exist. Use Function \"devmode\" to enable PixelMDL Functions. Use the command 'help' for more information.")
        else:
            pixelmdl.quiz()
            print("The Quiz has been completed, You may now continue using AuraPL, Use the command 'help' for more information.")
        run()
    if answer == "devmode":
        pixelmdl.devmode()
        print("Developer Mode has been completed, You may now continue using AuraPL, Use the command 'help' for more information.")
        run()



