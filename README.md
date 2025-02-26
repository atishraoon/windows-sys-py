# 🛠️ System Utility Script

A command-line utility to manage system operations like shutdown, restart, hiding/unhiding files, cleaning temp files, and changing user passwords.

## 🚀 Features
- 🔄 **Restart / Shutdown**: Schedule a system restart or shutdown with a timer.
- 🔧 **BIOS Restart**: Restart the system into BIOS mode.
- 🔒 **Hide & Unhide Files**: Securely hide or unhide files and folders.
- 🗑️ **Clean Temp Files**: Remove unnecessary temporary files to free up space.
- 🔑 **Change Password**: Modify user account passwords from the command line.

## 📌 Usage
Run the script with the desired command:

```bash
python script.py [command] [optional arguments]
script.exe [command] [optional arguments]
```

### 🔹 Commands
| Command       | Description |
|--------------|-------------|
| `shutdown [seconds]` | Shut down the system after a delay (default: 0s) |
| `restart [seconds]` | Restart the system after a delay (default: 0s) |
| `bios [seconds]` | Restart into BIOS mode after a delay |
| `hide [path]` | Hide a specific file or folder |
| `uhide [path]` | Unhide a specific file or folder |
| `h_ps` | Hide all paths listed in `data.dat` |
| `uh_ps` | Unhide all paths listed in `data.dat` |
| `clean` | Delete temporary files from system directories |
| `password` | Change the user password |

## ⚡ Examples
- Shutdown in 60 seconds:
  ```bash
  python script.py shutdown 60
  ```
- Restart immediately:
  ```bash
  python script.py restart
  ```
- Hide a folder:
  ```bash
  python script.py hide "C:\Users\YourName\SecretFolder"
  ```
- Change a user password:
  ```bash
  python script.py password
  ```

## 🔥 Requirements
- Windows OS (Tested on Windows 10/11)
- Python 3.x installed

## 🛡️ Disclaimer
This script performs system-level operations. Use it responsibly and ensure you have administrative privileges where necessary.

## 🎯 Future Enhancements
- Add GUI support for ease of use
- Implement logging for system operations

📌 **Enjoy using this tool!** 🚀

