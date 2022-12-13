# **TranquilityVPN**
*Tranquility VPN is an OpenVPN client with 1 US test server. Written in Python, based on OpenVPN Connect.*

____
![Alt-текст](https://i.ibb.co/1RNd4BC/Tranquillity-Studo.png "Tranquility Studio")
## **Contents**

1. [Beginning](#Beginning)
2. [How to enable VPN?](#How-to-enable-VPN)
3. [How to disable VPN?](#How-to-disable-VPN)
4. [How to set up your OpenVPN profiles?](#How-to-set-up-your-OpenVPN-profiles)
5. [How to uninstall the program?](#How-to-uninstall-the-program)
6. [Questions and answers](#Questions-and-answers)
    1. [Why disable Windows Defender](#Why-disable-Windows-Defender)
    2. [Why does Windows Defender think your VPN client is a virus](#Why-does-Windows-Defender-think-your-VPN-client-is-a-virus)
    3. [Why does the program disable UAC while it is running](#Why-does-the-program-disable-UAC-while-it-is-running)
8. [Check list](#Check-list)
## **Beginning**
1. Disable Windows Defender
2. Run TranquilityVpnSetup.exe
3. Enjoy!
## **How to enable VPN**
1. Open TranquilityVPN.exe
2. Select the desired country from the dropdown list.
3. Turn the switch to the ON position
## **How to disable VPN**
1. Open TranquilityVPN.exe
2. Turn the switch to the OFF position
## **How to set up your OpenVPN profiles**
1. After starting TranquilityVPN, go to the path:  
```%AppData%\TranquilityVPN\bin\Profiles```  
2. Then move your OpenVPN profiles (.ovpn) to this folder  
3. Restart TranquilityVPN.exe (just close and reopen)  
## **How to uninstall the program**
1. Open TranquilityVPN.exe
2. In the lower right corner, click on the Trash can button
3. Click Yes button
4. Wait for the deletion to finish and click the Yes button at the end.
## **Questions and answers**
### *Why disable Windows Defender*
Because Windows Defender thinks my VPN client is a Trojan virus! :(
____
### *Why does Windows Defender think your VPN client is a virus*
Because my VPN client disables UAC while the program is running.
____
### *Why does the program disable UAC while it is running*
This is for your convenience. Because every time you enable/disable the VPN, it will ask for administrative permission.
____
[:arrow_up:Contents](#Contents)
## **Check list**

- [X] Functional
	- [X] Checks
        - [X] Is OpenVPN installed?
        - [X] Is the VPN running?
        - [X] Is UAC enabled?
        - [X] Is Ovpn installed?
        - [X] Are there .ovpn profiles?
        - [X] Is the Ovpn process running?
	- [X] Installation
        - [X] Installing OpenVPN
        - [X] Ending the OpenVPN Process
        - [X] Ovpn installation
        - [X] Disabling UAC
        - [X] Copy profiles (.ovpn)
        - [X] Removing OpenVPN connect from the start bar
        - [X] Removing OpenVPN connect from autostart (REGEDIT)
	- [X] Uninstallation
        - [X] Removing OpenVPN
        - [X] Ovpn removal
        - [X] Enable UAC
	- [X] Start 
        - [X] Setting the configuration (OpenVPN)
        - [X] Launch OpenVPN
        - [X] Write to Json - run parameter: True
	- [X] Stop
        - [X] Stop OpenVPN
        - [X] Clear the OpenVPN configuration file (OpenVPN)
        - [X] Write to Json - run parameter: False
	- [X] Interface
        - [X] Launch interface  
        - [X] Frames
            - [X] Frame under the TranquilityVPN logo
            - [X] Frame under country selection
            - [X] Frame below text: Refresh (Status)
            - [X] Frame under text: Status
            - [X] Frame below text: Installed
            - [X] Frame under text: UAC
            - [X] Frame below text: Run
            - [X] Frame under text: Switch
            - [X] Frame below text: Refresh (Response Time)
            - [X] Frame below text: Response Time
        - [X] Static Text
            - [X] Status - text 
            - [X] Installed - text
            - [X] Installed - value
            - [X] UAC - text
            - [X] UAC - value
            - [X] Run - text
            - [X] Run - value
            - [X] Switch - text
            - [X] Switch - value
            - [X] Response Time - text
            - [X] Response Time - new value
            - [X] Response Time - old value
        - [X] Buttons
            - [X] Program uninstall button
            - [X] Button that leads to GitHub
            - [X] TranquilityVPN logo
            - [X] Button update ResponseTime
            - [X] Update Status button
        - [X] Switches
            - [X] Enable/Disable VPN
        - [X] Drop text
            - [X] Country selection
        - [X] Interface Completion
	- [X] Interface functions
        - [X] Trash button - function
        - [X] GitHub button - function
        - [X] Country selection dropdown text - function
        - [X] Status update button - function
        - [X] VPN switch (ON/OFF) - function
        - [X] ResponseTime update button - function
	- [X] Top Level Window
        - [X] Launch Top Level Window
        - [X] Top Level Window functions
            - [X] Uninstalling a program
            - [X] Closing the Top Level window
        - [X] Top Level Window Completion
	- [ ] Ability to switch between different VPN services
        - [X] Ability to connect via OpenVPN
        - [ ] Ability to connect via WireGuard

- [X] Releases
    - [X] Version 1.0
    - [ ] Version 1.1
    - [ ] Version 1.X
____
[:arrow_up:Contents](#Contents)
