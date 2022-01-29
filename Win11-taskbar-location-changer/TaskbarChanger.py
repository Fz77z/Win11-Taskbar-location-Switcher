import os
from pick import pick
import ctypes, sys
import wmi
import time
import subprocess

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def restart_taskbar():
    f = wmi.WMI()
    print("pid   Process name")

    # Iterating through all the running processes
    for process in f.Win32_Process():

      # Displaying the P_ID and P_Name of the process
      # print(f"{process.ProcessId:<10} {process.Name}")     

      if process.Name == "explorer.exe":
          os.system("taskkill /f /im  explorer.exe")
    time.sleep(1) # Sleep for 1 seconds
    FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
    subprocess.run([FILEBROWSER_PATH])
    


def is_top():
        os.system("bkp_registro_win11-top.reg") # path to top-windows task bar reg file
        restart_taskbar()
        
    

def is_bottom():
        os.system("bkp_registro_win11-bottom.reg") # path to top-windows task bar reg file
        restart_taskbar()


if is_admin():

    # Code of your program here
    
    title = 'Please choose a location for your windows 11 taskbar:  '
    options = ['Top', 'Bottom']

    option, index = pick(options, title, indicator='=>', default_index=0)


    if option == 'Top':
        is_top()

    elif option =='Bottom':
        is_bottom()
    else:
        print(is_admin()) 



else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)





































 #def chooseLocation():
  #  while True:
  #      top = 1
  #      bottom = 2
  #      print("Please choose a location for your windows 11 taskbar: ")
  #      print("[ 1.] Bottom ")
  #      print("[ 2.] Top  ")
  #      locationInput = (input(""))
  #      try:
  #          locationInput = float(locationInput)
  #          if locationInput > 0 and locationInput <= 2 :
  #              return(locationInput)
  #          if locationInput < 0 or locationInput > 2 :
  #              print("ERROR YOU NEED TO CHOOSE A LOCATION")
  #              return(chooseLocation())
  #          break;
  #      except ValueError:
  #            print("[ERROR]: Please enter a 1 or 2 without text/symbols.")







