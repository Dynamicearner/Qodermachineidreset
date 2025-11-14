import os
import platform
import uuid

def change_machine_id():
    print("=" * 50)
    print("      Qoder Reset Machine ID")
    print("      Created by @ismartSumit")
    print("=" * 50)
    print()
    
    os_type = platform.system().lower()
    print(f"[+] Detected OS: {os_type}")
    
    if os_type == "windows":
        path = os.path.expandvars(r"%APPDATA%\Qoder\machineid")
        mode = 2
    elif os_type == "linux":
        path = os.path.expanduser("~/.config/Qoder/machineid")
        mode = 1
    else:
        print("[-] Unsupported OS")
        input("\nPress Enter to exit...")
        return
    
    old_id = None
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                old_id = f.read().strip()
            print(f"[+] Old Machine ID: {old_id}")
        except Exception as e:
            print(f"[-] Error reading old ID: {e}")
    else:
        print("[!] No existing machine ID found")
    
    print()
    input("Press Enter to reset Machine ID...")
    print()
    
    new_id = str(uuid.uuid4())
    print(f"[+] New Machine ID: {new_id}")
    
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    try:
        with open(path, "w") as f:
            f.write(new_id)
        print(f"[+] Machine ID successfully changed! (Mode {mode})")
        print(f"[+] File: {path}")
    except Exception as e:
        print(f"[-] Error writing file: {e}")
    
    print()
    input("Press Enter to exit...")

if __name__ == "__main__":
    change_machine_id()
