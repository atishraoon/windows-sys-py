import os
import sys
import getpass
import time 

def usage():
    os.system("cls")  
    print("""
        sys [shutdown sh|re [seconds] ][bios][..]
        re       : restart
        clean    : clean all temp files
        hide     : hide file or folder. hide [path | h_ps]
        uhide    : unhide the file and folder. uhide [path | uh_ps]
        password : to change the sys password 
    """)
    sys.exit(0)

def hide(path):
    if not os.path.exists(path):
        print(f"Path {path} does not exist.")
        return
    try:
        os.system(f"attrib +h +r +s {path}")
        print(f"Successfully hidden: {path}")
    except Exception as e:
        print(f"Unable to hide {path}. Error: {e}")

def uhide(path):
    if not os.path.exists(path):
        print(f"Path {path} does not exist.")
        return
    try:
        os.system(f"attrib -h -r -s {path}")
        print(f"Successfully unhidden: {path}")
    except Exception as e:
        print(f"Unable to unhide {path}. Error: {e}")

def shutdown(time=0):
    print(f"Shutdown in {time}s")
    os.system(f"shutdown -s -t {time}")

def restart(time=0):
    print(f"Restart in {time}s")
    os.system(f"shutdown -r -t {time}")

def bios(time=0):
    print(f"Ready for BIOS restart in {time}s")
    os.system(f"shutdown -r -fw -t {time}")

def h_ps():
    if not os.path.exists("data.dat"):
        print("data.dat file not found.")
        return
    with open("data.dat", "r") as file:
        for line in file:
            folder_path = line.strip()
            hide(folder_path)

def uh_ps():
    if not os.path.exists("data.dat"):
        print("data.dat file not found.")
        return
    with open("data.dat", "r") as file:
        for line in file:
            folder_path = line.strip()
            uhide(folder_path)

def clean():
    temp = "C:\\Windows\\Temp"
    prefetch = "C:\\Windows\\Prefetch"
    local_temp = "C:\\Users\\Dell\\AppData\\Local\\Temp"

    try:
        os.system(f"del /q /f /s {temp}\\*")
        os.system(f"del /q /f /s {prefetch}\\*")
        os.system(f"del /q /f /s {local_temp}\\*") 
        print('Cleaned successfully')
        os.system('cls')  
    except Exception as e:
        print(f"Error during cleaning: {e}")

def change_password():
    print(os.system("net user")) 
    try:
        user = input("enter user to modefy password :")
        # temp_password = getpass.getpass("Enter new password: ")
        # password = getpass.getpass("Confirm password: ")
        if user:  
            os.system(f"net user {user} * ")
            print("password change successfully")  
        else:
            print("user not found ")  
    except Exception as e:
        raise e



def main():
    if not len(sys.argv[1:]):
        usage()

    command = sys.argv[1].lower()

    if command == "hide":
        hide(sys.argv[2])

    elif command == "uhide":
        uhide(sys.argv[2])

    elif command == "h_ps":
        h_ps()
        
    elif command == "uh_ps":
        uh_ps()
      
    elif command == "shutdown" or command == "sh":
        try:
            time = int(sys.argv[2])
            shutdown(time)
        except:
            shutdown() 
  
    elif command == "restart" or command == "re":
        try:
            time = int(sys.argv[2])
            restart(time)
        except:
            restart()        

    elif command == "bios":
        try:
            time = int(sys.argv[2])
            bios(time)
        except:
            bios()        

    elif command == "clean":
        clean()

    elif command == "password":
        change_password()

    else:
        print("Unexpected argument")

if __name__ == "__main__":
    main()
