# RaspTank


<h1 align="center">
	
  <br>
  <a href="http://www.amitmerchant.com/electron-markdownify"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Logo_Universit%C3%A9_Paris-Saclay.svg/2560px-Logo_Universit%C3%A9_Paris-Saclay.svg.png" alt="Saclay" width="200"></a>
</h1>
<h4 align="center">RaspTank Project - <a href="#" target="_blank">M2 Data Science</a>.</h4>
<img align="left" width="150" height="150" src="https://avatars.githubusercontent.com/ahmedrachid?s=150&v=1">
<img align="right" width="150" height="150" src="https://i.ibb.co/TwX0sDR/dddsadd.png">


<br><br>
- **Ahmed Rachid HAZOURLI ( LEFT )**
- **Anes MEKKI ( RIGHT )**

<br><br>

## Project Content: 
We have succeeded to develop all the parts of this project.  We participated in the race and won it as the first group 🎉. <br>

This project contains 3 servers which are connected to each other.

* [Main Server](https://github.com/ahmedrachid/RaspTank/blob/main/mainServer.py) 
* [Controller Server](https://github.com/ahmedrachid/RaspTank/blob/main/controllerServer.py) 
* [Robot Server](https://github.com/ahmedrachid/RaspTank/blob/main/robotServer.py)  

## General info
We have developed it in **Python Language** using standard libraires such as: 
* socket
* keyboard
* threading
* os


## Key Features

* Registration of Rasptank by RobotName
* Connection of Controller to the main server
* Link the Controller to its Robot
* Manage messages in a mutli-threading way between controller and the main server as well as between the main server and robot
* Keyboard buttons to actions
* Implemented these actions:
  - Move Forward ( Press W button )
  - Move Backward ( Press S button )
  - Move Left ( Press A button )
  - Move Right ( Press D button )
  - Stop Robot ( Press C button )
  - Increase speed ( Press ↑ button )
  - Decrease speed ( Press ↓ button )
  - Police Lights ON ( Press L button )
  - Bonus / Malus algorithm to Stop a random robot each 30 seconds.

## Work

**Ahmed Rachid HAZOURLI**: worked on the configuration of DHCP and HOSTAPD on the main server. Then, worked on developing code for main server by forwarding the received commands messages from the controllers to the robots and mapping them. Also, I worked on the movements and bonus / malus.

**Anes MEKKI**: worked on the controller code part by translating keyboard press buttons to messages and send them to the main server. Worked on main server part too and debugging code of movements / stop robots... 
	
## Setup
To run this project: <br>

**On the Main Server**
```
$ sudo hostapd /etc/hostapd/hostapd.conf
$ sudo python3 mainServer.py
```
Then, you should connect to the network broadcasted by the main server

**On the Robot**
```
$ sudo python3 robotServer.py
```

**On the Controller**
```
$ sudo python3 controllerServer.py
```

Once you execute this command, you can now press on the buttons to move forward / backward.... 
