# lackne190044_01
## Wall_sockets

* ID(int)
* constraint PK(ID)

## Switch

* ID(int)
* Number_of_ports(int)
* constraint PK(ID)

## Connection 

* ID(int)
* Wall_socket(Wall_socket)
* Switch(Switch)
* constraint PK(ID)
* constraint FK(Wall_socket) references Wall_sockets.ID
* constraint FK(Switch) references Switch.ID

