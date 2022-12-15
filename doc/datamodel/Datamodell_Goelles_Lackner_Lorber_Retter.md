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

## Room 

* ID(int)
* Name(varchar)
* Location(Varchar)
* constraint PK(ID)
* FloorNumber(FK)

## Floor

* ID(int)
* Floornumber(varchar)
* Building(FK)

## Building

* ID(int)
* Name(varchar)
* Address(varchar)

## Building/Floor

* Floornumber
* Building.ID

## Computer

* ID(int)
* Connection.ID

## Computer/Wall_sockets

* Computer.ID
* Wall_sockets.ID

## Room/Wall_sockets

* Room.ID
* Wall_sockets.ID

