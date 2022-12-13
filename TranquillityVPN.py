#IMPORTS /// ИМПОРТЫ
import os
import json
import time
import psutil
import struct
import subprocess
import webbrowser
import customtkinter
from tkinter import *
from PIL import Image,ImageTk
import win32com.shell.shell as shell

#PATH VARIABLES /// ПЕРЕМЕННЫЕ ПУТИ
binpath = "\\TranquillityVPN\\bin"
profiles = "\\TranquillityVPN\\bin\\Profiles"
mainicon = "\\TranquillityVPN\\bin\\ICOns\\vpn.ico"
all_delete_end = '\\TranquillityVPN" && unins000.exe'
ovpn = "\\TranquillityVPN\\OpenVPN\\ovpnconnector.exe"
trashicon = "\\TranquillityVPN\\bin\\Images\\trash.png"
phototrash = "\\TranquillityVPN\\bin\\Images\\trash.png"
githubicon = "\\TranquillityVPN\\bin\\Images\\github.png"
status_json = "\\TranquillityVPN\\bin\\JSON\\status.json"
OvpnCfg = "\\TranquillityVPN\\OpenVPN\\ovpnconnector.cfg"
openvpn = "\\TranquillityVPN\\OpenVPN\\OpenVPNConnect.exe"
openvpn_delete_panel_2 = "C:\\Users\\Public\\Desktop\\OpenVPN Connect.lnk"
traquillitystudioicon = "\\TranquillityVPN\\bin\\Images\\TranquillityStudo.png"
copy_profiles_end = '\\TranquillityVPN\\bin\\Profiles" "%AppData%\\TranquillityVPN\\OpenVPN"'
openvpn_delete_panel_1 = "C:\\ProgramData\Microsoft\\Windows\\Start Menu\\Programs\\OpenVPN Connect"

#CMD VARIABLES /// ПЕРЕМЕННЫЕ CMD
stopOVPN = "stop"
startOVPN = "start"
installOVPN = "install"
uninstallOVPN = "remove"
setConfigOVPN_end = ".ovpn"
all_delete_start = 'cd /d "'
copy_profiles_start = 'xcopy "'
openvpn_install_start = "cd /d "
unsetconfig = "unset-config profile"
setConfigOVPN_start = "set-config profile "
all_program_kill = "taskkill /IM TranquillityVPN.exe /F"
pathOVPN = "cd %appdata%\TranquillityVPN\OpenVPN && ovpnconnector.exe "
openvpn_install_middle = '\\TranquillityVPN\\bin\\Installers && msiexec /i "OpenVPN'
uninstallOpenVPN = 'wmic product where name="OpenVPN Connect" call uninstall /nointeractive'
openvpn_install_end = '.msi" /quiet /qn /norestart APPLICATIONROOTDIRECTORY="%AppData%\\TranquillityVPN\\OpenVPN"'

#REGEDIT VARIABLES /// ПЕРЕМЕННЫЕ РЕЕСТРА
uac_write_start = "Reg Add "
uac_read_start = "Reg Query "
uac_write_end_0 = " /t REG_DWORD /d 0 /f"
uac_write_end_1 = " /t REG_DWORD /d 1 /f"
uac_regedit = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA"
openvpn_delete_autostart = "REG DELETE HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v org.openvpn.client /f"

#OTHERS VARIABLES /// ОСТАЛЬНОЕ ПЕРЕМЕННЫЕ
responseold = 0
appdata = "APPDATA"
openvpnexe = "OpenVPNConnect.exe"
github = "https://github.com/TeaGG2020"

#Class with the required information /// Класс с нужной информацией
class Info:
    #Sending the necessary commands to CMD /// Отправка нужных команд в CMD
    def cmd(command,runas,output):
        if runas == True and output == False:
            shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+command)
        elif runas == False and output == False: 
            shell.ShellExecuteEx(lpFile='cmd.exe', lpParameters='/c '+command)
        elif runas == False and output == True:
            outputs = subprocess.getoutput(command)
            uac_regedits = outputs.split()
            return uac_regedits[3]
        elif runas == True and output == True:
            pass
        
    #Path to environment variable (To get the path to the Roaming folder) /// Путь к переменной среды (Для того, чтобы получить путь к папке Roaming)
    def varPath(variable):
        for key in os.environ:
            key, '=>', os.environ[key] 
        return os.environ[variable]

    #Check for the presence/absence of a file /// Проверка на присутствие/отсутствие файла
    def existFile(path_is_file):
        return os.path.isfile(path_is_file)

    #Checking the presence/absence of files with the desired extension in the directory /// Проверка присутствие/отсутствие файлов с нужным расширением в директорие
    def existFileExpansion(path_to_files,expansion):
        if any(File.endswith(expansion) for File in os.listdir(path_to_files)):
            return True
        else: 
            return False
    
    #Changing parameters in JSON /// Изменение параметров в JSON
    def setJson(path_to_json,variables,value):
        with open(path_to_json) as f:
            data = json.load(f)
        data[variables] = value
        with open(path_to_json, 'w') as outfile:
            json.dump(data, outfile,indent=4)

    #Reading parameters in JSON /// Чтение параметров в JSON
    def readJson(path_to_jsons,value):
        with open(path_to_jsons) as f:
            data = json.load(f)
            return data[value]

    #Is the process running? /// Запущен ли процесс?
    def isRunProcess(name_process):
        for proc in psutil.process_iter():
            name = proc.name()
            if name == name_process:
                return True

    #Terminating a process /// Завершение процесса
    def terminateProcess(name_proces):
        for proc in psutil.process_iter():
            if proc.name() == name_proces:
                proc.kill()         
    
    #Write available profiles (.ovpn) to an array /// Запись доступных профилей (.ovpn) в массив
    def arrayProfiles(path_to_profiles):
        myListRaw = os.listdir(path_to_profiles)
        myListFinished = [] * len(myListRaw)
        for i in range(len(myListRaw)): 
            myListFinished.append(myListRaw[0].replace(".ovpn",""))
            myListRaw.remove(myListRaw[0])
        return myListFinished

    #64 bit Windows? /// 64 бита Windows?
    def is64Bit():
        if struct.calcsize('P') * 8 != 64:
            return "32"
        else:
            return "64"

    #Deleting a file/folder /// Удаление файла/папки
    def deletedFile(path_to_delete_file,IsCatalog):
        if IsCatalog == False:
            Info.cmd('ERASE /f /q "'+path_to_delete_file+'"',True,False)
        else:
            Info.cmd('RD /q "'+path_to_delete_file+'"',True,False)

    #Ping the desired ip /// Ping нужного ip
    def pingToIp(ip):
        ping = os.popen("ping "+ip).read().split(sep=None, maxsplit=-1)
        return ping[len(ping)-2]

    #Opening the default browser with the desired link /// Открытие браузера по умолчанию с нужной ссылкой
    def openBrowser(link):
        webbrowser.open_new_tab(link)

#VPN readiness class /// Класс проверки готовности VPN
class Check:
    def jsonMain():
        #Is OpenVPN installed? /// Установлен ли OpenVPN?
        if Info.existFile(Info.varPath(appdata)+openvpn) and Info.existFile(Info.varPath(appdata)+ovpn) == True:
            Info.setJson(Info.varPath(appdata)+status_json,"installed",True)
        else:
            Info.setJson(Info.varPath(appdata)+status_json,"installed",False)

        #Is the VPN running? /// Запущен ли VPN?
        if Info.isRunProcess("ovpnconnector.exe") == True:
            Info.setJson(Info.varPath(appdata)+status_json,"run",True)
        else:
            Info.setJson(Info.varPath(appdata)+status_json,"run",False)
        
        #Is UAC enabled? /// Включён ли UAC?
        if Info.cmd(uac_read_start + uac_regedit,False,True) == "0x0":
            Info.setJson(Info.varPath(appdata)+status_json,"uacison",False)
        else:
            Info.setJson(Info.varPath(appdata)+status_json,"uacison",True)

        #Is Ovpn installed? /// Установлен ли Ovpn?
        if Info.existFile(Info.varPath(appdata)+OvpnCfg) == True:
            Info.setJson(Info.varPath(appdata)+status_json,"ovpninstalled",True)
        else:
            Info.setJson(Info.varPath(appdata)+status_json,"ovpninstalled",False)

        #Are there .ovpn profiles? /// Есть ли профили .ovpn?
        if Info.existFileExpansion(Info.varPath(appdata)+profiles,".ovpn") == True:
            Info.setJson(Info.varPath(appdata)+status_json,"anyprofiles",True)
        else:
            Info.setJson(Info.varPath(appdata)+status_json,"anyprofiles",False)

    #Is the ovpn process running? /// Запущен ли процесс ovpn? 
    def lastConnection():
        if Info.readJson(Info.varPath(appdata)+status_json,"installed") == True and Info.readJson(Info.varPath(appdata)+status_json,"run") == True:
            return Info.readJson(Info.varPath(appdata)+status_json,"selectcountry")
        else:
            return "None"

#OpenVPN installation class /// Класс установки OpenVPN
class Install:
    #Installing OpenVPN /// Установка OpenVPN
    def installOpenVPN():
        Info.cmd(openvpn_install_start+Info.varPath(appdata)+openvpn_install_middle+Info.is64Bit()+openvpn_install_end,True,False)
        time.sleep(15)

    #Ending the OpenVPN Process /// Завершение процесса OpenVPN
    def terminateOpenVPN(): 
        isLaunch = False
        while (isLaunch != True):                                            
            if Info.isRunProcess(openvpnexe) == True:
                Info.terminateProcess(openvpnexe)
                time.sleep(3)
                isLaunch = True
    
    #OVPN installation /// Установка OVPN
    def installOvpn():
        Info.cmd(pathOVPN+installOVPN,True,False) 

    #Disabling UAC /// Отключение UAC
    def disabledUAC():
        Info.cmd(uac_write_start+uac_regedit+uac_write_end_0,True,False)

    #Copy profiles (.ovpn) /// Копирование профилей (.ovpn)
    def copyProfiles():
        Info.cmd(copy_profiles_start+Info.varPath(appdata)+copy_profiles_end,False,False)
    
    #Removing OpenVPN connect from the start bar /// Удаление OpenVPN connect из панели пуска 
    def removeFromLaunch(): 
        Info.deletedFile(openvpn_delete_panel_1,False)
        Info.deletedFile(openvpn_delete_panel_2,False)

    #Removing OpenVPN connect from autostart (REGEDIT) /// Удаление OpenVPN connect из автостарта (REGEDIT)
    def removeFromAutoStart(): 
        Info.cmd(openvpn_delete_autostart,True,False)

#OpenVPN Deletion Class /// Класс удаление OpenVPN
class Uninstall: 
    #Removing OpenVPN /// Удаление OpenVPN
    def uninstallOpenVPN():
        Info.cmd(uninstallOpenVPN,True,False) 
        time.sleep(25)
    
    #OVPN Removal /// Удаление OVPN
    def uninstallOvpn():
        Info.cmd(pathOVPN+uninstallOVPN,True,False)

    #Enable UAC /// Включение UAC
    def enabledUAC():
        Info.cmd(uac_write_start+uac_regedit+uac_write_end_1,True,False)

#VPN start class /// Класс запуска VPN
class Start:
    #Setting the configuration /// Установка конфигурации
    def setConfig(country):
        Info.cmd(pathOVPN+setConfigOVPN_start+country+setConfigOVPN_end,True,False)

    #Launch VPN /// Запуск VPN
    def runOvpn():
        Info.cmd(pathOVPN+startOVPN,True,False)

    #Write to Json run  - parameter: True /// Запись в Json параметра run: True
    def runJsonOn():
        Info.setJson(Info.varPath(appdata)+status_json,"run",True)

#VPN stop class /// Класс остановки VPN
class Stop:
    #Stop OpenVPN /// Остановить OpenVPN 
    def stopOvpn():
        Info.cmd(pathOVPN+stopOVPN,True,False)

    #Clear the OpenVPN configuration file /// Очистить файл конфигурации OpenVPN 
    def unSetConfig():
        Info.cmd(pathOVPN+unsetconfig,True,False)

    #Write to Json run - parameter: False /// Запись в Json параметра run: False
    def runJsonOff():
        Info.setJson(Info.varPath(appdata)+status_json,"run",False)

#Interface /// Интерфейс
class Interface:
    #Launch interface /// Запуск интерфейса
    def start(): 
        global window
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")
        window = customtkinter.CTk()
        window.geometry("300x400")
        window.resizable(width=False, height=False)
        window.title('TranquillityVPN')
        window.iconbitmap(Info.varPath(appdata)+mainicon)

    #FRAMES /// ФРЕЙМЫ

    #Frame under the TranquilityVPN logo /// Frame под логотипом TranquillityVPN
    def frameUnderLogo():
        frame = customtkinter.CTkFrame(master=window,width=290,height=80,border_color="white",border_width=0.9,corner_radius=7)
        frame.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

    #Frame under country selection /// Frame под выбором страны
    def frameUnderSelectCountry(): 
        frame = customtkinter.CTkFrame(master=window,width=290,height=40,border_color="white",border_width=0.9,corner_radius=7)
        frame.place(relx=0.5, rely=0.275, anchor=customtkinter.CENTER)

    #Frame below text: Refresh (Status) /// Frame под текстом: Refresh (Status)
    def frameUnderRefreshStatusText(): 
        frame = customtkinter.CTkFrame(master=window,width=145,height=235,border_color="white",border_width=0.9,corner_radius=7)
        frame.place(relx=0.255, rely=0.65, anchor=customtkinter.CENTER)

    #Frame under text: Status /// Frame под текстом: Status
    def frameUnderStatusText(): 
        frame = customtkinter.CTkFrame(master=window,width=145,height=30,border_color="white",border_width=0.9,corner_radius=7)
        frame.place(relx=0.255, rely=0.39, anchor=customtkinter.CENTER)

    #Frame below text: Installed /// Frame под текстом: Installed
    def frameUnderInstalledText(): 
        frame = customtkinter.CTkFrame(master=window,width=145,height=60,border_color="white",border_width=0.9,corner_radius=7)
        frame.place(relx=0.255, rely=0.5, anchor=customtkinter.CENTER)

    #Frame under text: UAC /// Frame под текстом: UAC
    def frameUnderUACText(): 
        frame = customtkinter.CTkFrame(master=window,width=145,height=60,border_color="white",border_width=0.9,corner_radius=7)
        frame.place(relx=0.255, rely=0.645, anchor=customtkinter.CENTER)

    #Frame below text: Run /// Frame под текстом: Run
    def frameUnderRunText(): 
        frame = customtkinter.CTkFrame(master=window,width=145,height=60,border_color="white",border_width=0.9,corner_radius=7)
        frame.place(relx=0.255, rely=0.78, anchor=customtkinter.CENTER)    

    #Frame under text: Switch /// Frame под текстом: Switch
    def frameUnderSwitchText(): 
        frame = customtkinter.CTkFrame(master=window,width=145,height=118,border_color="white",border_width=0.9,corner_radius=7)
        frame.place(relx=0.75, rely=0.5, anchor=customtkinter.CENTER)    

    #Frame below text: Refresh (Response Time) /// Frame под текстом: Refresh (Response Time)
    def frameUnderRefreshResponseTimeText(): 
        frame = customtkinter.CTkFrame(master=window,width=145,height=110,border_color="white",border_width=0.9,corner_radius=7)
        frame.place(relx=0.75, rely=0.77, anchor=customtkinter.CENTER) 

    #Frame below text: Response Time /// Frame под текстом: Response Time
    def frameUnderResponseTimeText(): 
        frame = customtkinter.CTkFrame(master=window,width=145,height=80,border_color="white",border_width=0.9,corner_radius=7)
        frame.place(relx=0.75, rely=0.735, anchor=customtkinter.CENTER)  

    #STATIC TEXT /// СТАТИЧНЫЙ ТЕКСТ

    #Status - text /// Статус - текст
    def labelStatusText(): 
        label = customtkinter.CTkLabel(master=window, text="Status:",bg_color="#2e2e2e",text_font="Gotham 15",fg_color="#2e2e2e",corner_radius=7,text_color="white")
        label.place(relx=0.26, rely=0.39, anchor=CENTER)

    #Installed - text /// Установлен - текст
    def labelStatusInstalledText(): 
        label = customtkinter.CTkLabel(master=window, text="Installed:",bg_color="#2e2e2e",text_font="Gotham 14",text_color="white")
        label.place(relx=0.26, rely=0.465, anchor=CENTER)

    #Installed - value /// Установлен - значение
    def labelStatusInstalledValue(): 
        global StatusInstalledValue
        StatusInstalledValue = customtkinter.CTkLabel(master=window, text="Waiting Refresh",bg_color="#2e2e2e",text_font="Gotham 14",text_color="lightblue")
        StatusInstalledValue.place(relx=0.26, rely=0.53, anchor=CENTER)

    #UAC - text /// UAC - текст
    def labelStatusUacText(): 
        label = customtkinter.CTkLabel(master=window, text="UAC:",bg_color="#2e2e2e",text_font="Gotham 14",text_color="white")
        label.place(relx=0.26, rely=0.61, anchor=CENTER)

    #UAC - value /// UAC - значение 
    def labelStatusUacValue():
        global StatusUacValue
        StatusUacValue = customtkinter.CTkLabel(master=window, text="Waiting Refresh",bg_color="#2e2e2e",text_font="Gotham 14",text_color="lightblue")
        StatusUacValue.place(relx=0.26, rely=0.67, anchor=CENTER)

    #Run - text /// Run - текст
    def labelStatusRunText(): 
        label = customtkinter.CTkLabel(master=window, text="Run:",bg_color="#2e2e2e",text_font="Gotham 14",text_color="white")
        label.place(relx=0.26, rely=0.755, anchor=CENTER)

    #Run - value /// Run - значение
    def labelStatusRunValue(): 
        global StatusRunValue
        StatusRunValue = customtkinter.CTkLabel(master=window, text="Waiting Refresh",bg_color="#2e2e2e",text_font="Gotham 14",text_color="lightblue")
        StatusRunValue.place(relx=0.26, rely=0.815, anchor=CENTER)

    #Switch - text /// Switch - текст
    def labelSwitchText(): 
        label = customtkinter.CTkLabel(master=window, text="Switch:",bg_color="#2e2e2e",text_font="Gotham 15",text_color="white")
        label.place(relx=0.75, rely=0.39, anchor=CENTER)

    #Switch - value /// Switch - значение
    def labelSwitchTextValue(): 
        global SwitchTextValue
        if Info.readJson(Info.varPath(appdata)+status_json,"run") == False:
            SwitchTextValue = customtkinter.CTkLabel(master=window, text="Off",bg_color="#2e2e2e",text_font="Gotham 15",text_color="firebrick")
        else:
            SwitchTextValue = customtkinter.CTkLabel(master=window, text="On",bg_color="#2e2e2e",text_font="Gotham 15",text_color="darkgreen")
        SwitchTextValue.place(relx=0.75, rely=0.6, anchor=CENTER)

    #Response Time - text /// Response Time - текст
    def labelResponseText(): 
        label = customtkinter.CTkLabel(master=window, text="Response time:",bg_color="#2e2e2e",text_font="Gotham 14",text_color="white")
        label.place(relx=0.75, rely=0.674, anchor=CENTER)

    #Response Time - new value /// Response Time - новое значение
    def labelResponseValue(): 
        global ResponseValue
        ResponseValue = customtkinter.CTkLabel(master=window, text="Waiting Refresh",bg_color="#2e2e2e",text_font="Gotham 13",text_color="lightblue")
        ResponseValue.place(relx=0.75, rely=0.735, anchor=CENTER)
    
    #Response Time - old value /// Response Time - старое значение
    def labelResponseOldValue(): 
        global ResponseOldValue
        ResponseOldValue = customtkinter.CTkLabel(master=window, text="Waiting Refresh",bg_color="#2e2e2e",text_font="Gotham 13",text_color="lightblue")
        ResponseOldValue.place(relx=0.75, rely=0.798, anchor=CENTER)

    #BUTTONS /// КНОПКИ

    #Program uninstall button /// Кнопка удаления программы
    def buttonTrash(): 
        trash = (Image.open(Info.varPath(appdata)+trashicon))
        resized_image = trash.resize((25,35), Image.ANTIALIAS)
        trash = ImageTk.PhotoImage(resized_image)
        button = customtkinter.CTkButton(master=window, width=1,text_color="#2e2e2e", fg_color="#2e2e2e",border_color="white",border_width=0.6,corner_radius=5,hover=None,image=trash,text=" ",command=InterfaceFunctions.trashButtonFunction)
        button.place(relx=0.975, rely=0.96, anchor=customtkinter.CENTER)

    #Button that leads to GitHub /// Кнопка которая ведёт на GitHub
    def buttonGitHub(): 
        github_image = (Image.open(Info.varPath(appdata)+githubicon))
        resized_image = github_image.resize((20,20), Image.ANTIALIAS)
        github_image = ImageTk.PhotoImage(resized_image)
        button = customtkinter.CTkButton(window, width=1, text_color="white", fg_color="#2e2e2e",border_width=0.9,corner_radius=7, hover=None, text="Created by MrTeaGG",text_font="Gotham 10",image=github_image,command=InterfaceFunctions.githubFunction)
        button.place(relx=0.5, rely=0.98, anchor=customtkinter.CENTER)
        button.bind("<Enter>", lambda event: button.configure(text_color="lightblue"))
        button.bind("<Leave>", lambda event: button.configure(text_color="white"))

    #TranquilityVPN logo + add website link in the future /// Лого TranquillityVPN + добавить в будущем ссылку на сайт
    def buttonLogoTranquillity(): 
        tranquillity_image = (Image.open(Info.varPath(appdata)+traquillitystudioicon))
        resized_image3 = tranquillity_image.resize((270,65), Image.ANTIALIAS)
        tranquillity_image = ImageTk.PhotoImage(resized_image3)
        button = customtkinter.CTkButton(master=window, width=1,text_color="#2e2e2e", fg_color="#2e2e2e",border_color="white",border_width=0,corner_radius=0,hover=None,image=tranquillity_image,text="")
        button.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

    #Button update ResponseTime /// Кнопка обновление ResponseTime
    def buttonRefreshResponse(): 
        button = customtkinter.CTkButton(master=window, width=1,height=1,text_color="white", fg_color="#2e2e2e",border_color="white",border_width=0,corner_radius=0,hover=None,text="Refresh",command=InterfaceFunctions.refreshButtonResponseFunction,text_font="Gotham 13")
        button.place(relx=0.75, rely=0.8735, anchor=customtkinter.CENTER)
        button.bind("<Enter>", lambda event: button.configure(text_color="lightblue"))
        button.bind("<Leave>", lambda event: button.configure(text_color="white"))

    #Update Status button /// Кнопка обновление Status(а)
    def buttonRefreshStatus(): 
        button = customtkinter.CTkButton(master=window, width=1,text_color="white", fg_color="#2e2e2e",border_color="white",border_width=0,corner_radius=0,hover=None,text="Refresh",command=InterfaceFunctions.refreshButtonStatusFunction,text_font="Gotham 15")
        button.place(relx=0.26, rely=0.9, anchor=customtkinter.CENTER)
        button.bind("<Enter>", lambda event: button.configure(text_color="lightblue"))
        button.bind("<Leave>", lambda event: button.configure(text_color="white"))

    #SWITCHES /// ПЕРЕКЛЮЧАТЕЛИ 
      
    #Enable/Disable VPN /// Включение/Отключение VPN
    def switchVPN(): 
        global switch_var
        if Info.readJson(Info.varPath(appdata)+status_json,"run") == True:
            switch_var = customtkinter.StringVar(value="on")
        else:
            switch_var = customtkinter.StringVar(value="off")
        switch = customtkinter.CTkSwitch(master=window, text="", command=InterfaceFunctions.vpnSwitchFunction,width=125,height=45,progress_color="gray",button_color="deepskyblue",button_hover_color="skyblue",bg_color="#2e2e2e",fg_color="#1f1f1f",variable=switch_var, onvalue="on", offvalue="off")
        switch.place(relx=0.755, rely=0.5, anchor=CENTER)

    #DROP TEXT /// ВЫПАДАЮЩИЙ ТЕКСТ

    #Country selection /// Выбор страны
    def comboboxSelectCountry(): 
        global combobox
        if Info.readJson(Info.varPath(appdata)+status_json,"anyprofiles") == True:
            combobox = customtkinter.CTkOptionMenu(master=window,fg_color="#2e2e2e",bg_color="#2e2e2e",button_color="#2e2e2e",button_hover_color="#2e2e2e",dropdown_color="#2e2e2e",dropdown_text_font="Gotham 15",dropdown_text_color="white",values=Info.arrayProfiles(Info.varPath(appdata)+profiles),width=270,height=30,text_font="Gotham 15",text_color="white",text_color_disabled="white",command=InterfaceFunctions.selectCountryFunction)
            combobox.place(relx=0.5, rely=0.275, anchor=customtkinter.CENTER)
            combobox.set(Check.lastConnection())
        else:
            combobox = customtkinter.CTkOptionMenu(master=window,fg_color="#2e2e2e",bg_color="#2e2e2e",button_color="#2e2e2e",button_hover_color="#2e2e2e",dropdown_color="#2e2e2e",dropdown_text_font="Gotham 15",dropdown_text_color="red",values=["NO","PROFILES","INSTALLED"],width=270,height=30,text_font="Gotham 15",text_color="white",text_color_disabled="red")
            combobox.place(relx=0.5, rely=0.275, anchor=customtkinter.CENTER)
            combobox.set("OPEN ME")

    #Interface Completion /// Завершение интерфейса
    def stop():
        global window 
        window.mainloop()

#Interface functions /// Функции интерфейса
class InterfaceFunctions:
    #Trash button - function /// Кнопка мусорки - функция
    def trashButtonFunction():
            topLevels.topLevel()

    #GitHub button - function /// Кнопка GitHub - функция
    def githubFunction():
            Info.openBrowser(github)

    #Country selection dropdown text - function /// Выпадающий текст выбора стран - функция
    def selectCountryFunction(choise):
        Info.setJson(Info.varPath(appdata)+status_json,"selectcountry",choise)

    #Status update button - function /// Кнопка обновления статуса - функция
    def refreshButtonStatusFunction():
        if Info.readJson(Info.varPath(appdata)+status_json,"installed") == True:
            StatusInstalledValue.configure(text="Yes",text_color="darkgreen")
        else:
            StatusInstalledValue.configure(text="No",text_color="firebrick")
        if Info.readJson(Info.varPath(appdata)+status_json,"uacison") == True:
            StatusUacValue.configure(text="On",text_color="firebrick")
        else:
            StatusUacValue.configure(text="Off",text_color="darkgreen")
        if Info.readJson(Info.varPath(appdata)+status_json,"run") == True:
            StatusRunValue.configure(text="Yes",text_color="darkgreen")
        else:
            StatusRunValue.configure(text="No",text_color="firebrick")

    #VPN switch (ON/OFF) - function /// Переключатель VPN (ON/OFF) - функция
    def vpnSwitchFunction():
        #Are there any profiles (.ovpn) in the folder? /// Есть ли какие-то профили (.ovpn) в папке?
        if Info.readJson(Info.varPath(appdata)+status_json,"anyprofiles") == True:
            if switch_var.get() == "off":
                SwitchTextValue.configure(text="Off",text_color="firebrick")
                combobox.set("None")
                Stop.stopOvpn()
                Stop.unSetConfig()
                Stop.runJsonOff()
            elif switch_var.get() == "on":
                SwitchTextValue.configure(text="On",text_color="darkgreen")
                Start.setConfig(Info.readJson(Info.varPath(appdata)+status_json,"selectcountry"))
                combobox.set(Info.readJson(Info.varPath(appdata)+status_json,"selectcountry"))
                Start.runOvpn()
                Start.runJsonOn()
        else:
            if switch_var.get() == "on":
                combobox.set("CLICK ON ME")
                combobox.configure(text_color="red")
            else:
                combobox.set("OPEN ME")
                combobox.configure(text_color="aqua")
            
    #ResponseTime update button - function /// Кнопка обновления ResponseTime - функция
    def refreshButtonResponseFunction():
        global responseold
        response = Info.pingToIp("1.1.1.1")
        responseInt = int(response)
        responseStr = str(response)
        responseold = str(responseold)
        if responseold != "0":
            ResponseValue.configure(text="Before "+responseold+" ms",text_color="aqua")
        if responseInt <= 100:     
            ResponseOldValue.configure(text="After "+responseStr+" ms",text_color="lightgreen") #до 100
        elif responseInt > 100 and responseInt <= 150:
            ResponseOldValue.configure(text="After "+responseStr+" ms",text_color="green") #от 100 до 150
        elif responseInt > 150 and responseInt <= 250:
            ResponseOldValue.configure(text="After "+responseStr+" ms",text_color="green") #от 150 до 250
        elif responseInt > 250 and responseInt <= 350:
            ResponseOldValue.configure(text="After "+responseStr+" ms",text_color="orange") #от 250 до 350
        elif responseInt > 350 and responseInt <= 500:
            ResponseOldValue.configure(text="After "+responseStr+" ms",text_color="darkorange") #от 350 до 500
        elif responseInt > 500 and responseInt <= 750: 
            ResponseOldValue.configure(text="After "+responseStr+" ms",text_color="red") #от 500 до 750
        elif responseInt > 750 and responseInt <= 1000:
            ResponseOldValue.configure(text="After "+responseStr+" ms",text_color="firebrick") #от 750 до 1000
        elif responseInt > 1000:
            ResponseOldValue.configure(text="After "+responseStr+" ms",text_color="darkred") #от 1000
        responseold = response    

#TOPLEVEL WINDOW /// TOPLEVEL ОКНО
class topLevels:
    def topLevel():
        global top
        top = Toplevel()
        top.geometry("300x100")
        top.resizable(width=False, height=False)
        top.title('TranquillityVPN')
        top["bg"] = "#1f1f1f"
        top.iconbitmap(Info.varPath(appdata)+mainicon)
        top.frame = customtkinter.CTkFrame(top,width=285,height=30,border_color="white",border_width=0.9,corner_radius=7)
        top.frame.place(relx=0.5, rely=0.25, anchor=customtkinter.CENTER)   
        top.label = customtkinter.CTkLabel(top, text="Are you sure you want to uninstall the program?",fg_color="#2e2e2e")
        top.label.place(relx=0.5, rely=0.25, anchor=CENTER)
        top.button = customtkinter.CTkButton(top, text="Yes", command=topLevels.yes,width=75,height=30,fg_color="green",hover_color="#2e2e2e",text_font="Gotham 13",border_color="white")
        top.button.place(relx=0.25, rely=0.7, anchor=CENTER)
        top.button = customtkinter.CTkButton(top, text="No", command=topLevels.no,width=75,height=30,fg_color="firebrick",hover_color="#2e2e2e",text_font="Gotham 13",border_color="white")
        top.button.place(relx=0.75, rely=0.7, anchor=CENTER)   

    #FUNCTIONS FOR TOPLEVEL WINDOWS /// ФУНКЦИИ ДЛЯ TOPLEVEL ОКНА

    #Uninstalling a program /// Удаление программы
    def yes():
        Uninstall.uninstallOvpn()
        Uninstall.uninstallOpenVPN()
        Info.deletedFile(Info.varPath(appdata)+binpath,False)
        Info.deletedFile(Info.varPath(appdata)+binpath,True)
        Info.cmd(all_delete_start+Info.varPath(appdata)+all_delete_end,True,False)
        Info.cmd(all_program_kill,True,False)

    #Closing the TOPLEVEL window /// Закрытие TOPLEVEL окна         
    def no():
        top.destroy()
        top.update()

#Start order interface function /// Порядок запуска функция интерфейса
def InterfaceSequence():
        #Launch interface /// Запуск интерфейса
        Interface.start()
        
        #FRAMES /// ФРЕЙМЫ
        Interface.frameUnderLogo()
        Interface.frameUnderSelectCountry()
        Interface.frameUnderRefreshStatusText()
        Interface.frameUnderStatusText()
        Interface.frameUnderInstalledText()
        Interface.frameUnderUACText()
        Interface.frameUnderRunText()
        Interface.frameUnderSwitchText()
        Interface.frameUnderRefreshResponseTimeText()
        Interface.frameUnderResponseTimeText()
        
        #STATIC TEXT /// СТАТИЧНЫЙ ТЕКСТ
        Interface.labelStatusText()
        Interface.labelStatusInstalledText()
        Interface.labelStatusInstalledValue()
        Interface.labelStatusUacText()
        Interface.labelStatusUacValue()
        Interface.labelStatusRunText()
        Interface.labelStatusRunValue()
        Interface.labelSwitchText()
        Interface.labelSwitchTextValue()
        Interface.labelResponseText()
        Interface.labelResponseValue()
        Interface.labelResponseOldValue()
        
        #BUTTONS /// КНОПКИ
        Interface.buttonTrash()
        Interface.buttonGitHub()
        Interface.buttonLogoTranquillity()
        Interface.buttonRefreshResponse()
        Interface.buttonRefreshStatus()
        
        #SWITCHES /// ПЕРЕКЛЮЧАТЕЛИ
        Interface.switchVPN()
        
        #DROP TEXT /// ВЫПАДАЮЩИЙ ТЕКСТ
        Interface.comboboxSelectCountry()
        
        #Interface Completion /// Завершение интерфейса
        Interface.stop()

#Main function /// Главная функция
def main():
    #Checking the status of everything and writing to JSON /// Проверяем состояние всего и записываем в JSON
    Check.jsonMain()
    
    #Remember the initial UAC parameter /// Запоминаем начальный параметр UAC
    statusUAC = Info.cmd(uac_read_start + uac_regedit,False,True)
    
    #We read JSON and perform the necessary actions /// Считываем JSON и выполняем нужные действия
    if Info.readJson(Info.varPath(appdata)+status_json,"isfirstlaunch") == True or Info.readJson(Info.varPath(appdata)+status_json,"installed") == False:
        #First installation /// Первая установка
        Install.installOpenVPN()
        Install.terminateOpenVPN()
        Install.installOvpn()
        if statusUAC != "0x0":
            Install.disabledUAC()
        Install.removeFromLaunch()
        Install.removeFromAutoStart()
        Info.setJson(Info.varPath(appdata)+status_json,"isfirstlaunch",False)
        time.sleep(5)
        Check.jsonMain()
    
    #OVPN installed? /// Установлен OVPN?
    elif Info.readJson(Info.varPath(appdata)+status_json,"ovpninstalled") == False:
        #Ovpn installation /// Установка Ovpn
        Install.installOvpn()
        time.sleep(5)
        Check.jsonMain()
    
    #Is UAC disabled? /// Выключен UAC?
    elif Info.readJson(Info.varPath(appdata)+status_json,"uacison") == True:
        #Turn off UAC /// Выключение UAC
        Install.disabledUAC()
        time.sleep(5)
        Check.jsonMain()
    
    #Checking for the presence of profiles in bin\Profiles /// Проверка на присутствие профилей в bin\Profiles
    if Info.readJson(Info.varPath(appdata)+status_json,"anyprofiles") == True:
        #Copy profiles to OpenVPN folder /// Копирование профилей в папку с OpenVPN
        Install.copyProfiles()
    
    #Launching the interface /// Запускаем интерфейс
    InterfaceSequence()
    
    #Return UAC to initial parameter /// Возвращаем UAC к начальному параметру
    if statusUAC != "0x0":
        Uninstall.enabledUAC()
 
#Program launch /// Запуск программы
main()