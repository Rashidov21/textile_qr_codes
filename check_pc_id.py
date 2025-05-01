import subprocess
import winreg

def get_windows_uuid():
    try:
        result = subprocess.check_output(
            ["powershell", "(Get-CimInstance -Class Win32_ComputerSystemProduct).UUID"],
            text=True
        ).strip()
        return result
    except:
        return None


def get_machine_guid():
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Cryptography")
        value, _ = winreg.QueryValueEx(reg_key, "MachineGuid")
        winreg.CloseKey(reg_key)
        return value
    except Exception as e:
        return f"Ошибка: {e}"

print("Machine GUID:", get_machine_guid())
