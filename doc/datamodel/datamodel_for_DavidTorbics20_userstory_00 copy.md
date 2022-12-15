# Userstory_00

## IPv4AddressList

* ID INT
* Computer_ID INT
* IPv4 VARCHAR
* Error_Message TEXT
* Contraint PK(ID)
* Constraint FK(Computer_ID) references Computers.ID

## Buildings

* ID INT
* Name TEXT
* Address (which I dont want to explain any further) TEXT
* Constraint PK(ID)

## Floors

* ID INT
* Name TEXT
* Building_ID INT 
* Constraint PK(ID)
* Constraint FK(Building_ID) references Buildings.ID

## Rooms

* ID INT
* Name TEXT
* Floor_ID INT 
* Constraint PK(ID)
* Constraint FK(Floor_ID) references Floors.ID

## Sockets

* ID INT
* Name TEXT
* Room_ID INT 
* Constraint PK(ID)
* Constraint FK(Room_ID) references Room.ID


## Computers

* ID INT
* Name TEXT
* IPv4 VARCHAR
* Socket_ID INT 
* Constraint PK(ID)
* Constraint FK(Room_ID) references Socket.ID
