import builtins
import os
import sys
import subprocess

def create_aurapl_bat_and_add_to_path():
    package_dir = os.path.dirname(os.path.abspath(__file__))
    bat_path = os.path.join(package_dir, "aurapl.bat")

    # ── 1. Create the .bat file ──────────────────────────────────────────────
    bat_content = f"""@echo off
"{sys.executable}" -c "import aurapl; aurapl.run()" %*
"""
    with open(bat_path, "w") as f:
        f.write(bat_content)

    # ── 2. Add to PATH ───────────────────────────────────────────────────────
    if sys.platform != "win32":
        print("[aurapl] PATH modification is only supported on Windows.")
        return

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

            subprocess.run(
                ["powershell", "-NoProfile", "-Command",
                 "[System.Environment]::GetEnvironmentVariable('PATH','User')"],
                capture_output=True,
            )
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

        winreg.CloseKey(reg_key)

    except Exception as e:
        print(f"[aurapl] Could not modify PATH automatically: {e}")
        print(f"[aurapl] Add this directory to PATH manually: {package_dir}")


create_aurapl_bat_and_add_to_path()

# Basic Run Command
def run():
    answer = input()
    if answer == "help":
       print("------AURAPL------")
       print("Commands:")
       print(" help - the command ""help"" is a command which shows a lot of information")
       print(" More Commands Upcoming")
       print("How to program using AuraPL -")
       print(" All Possible Commands for coding -")
       print("  val = (value) - sets the value for the next command")
       print("  print() - prints the value set by val")
       run()

def print(val):
    builtins.print(val)