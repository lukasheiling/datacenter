# User story find active network device.

## Building

* Building_ID(INT) 
* Description(varchar)
* Constraint PK(Building_ID)


## Floor

* Floor_ID(INT)
* Description(varchar)
* Building_ID(INT)
* Constraint PK(Floor_ID)
* Constraint FK(Building_ID) references Building.Building_ID


## Room 

* Room_ID(INT)
* Description(varchar)
* Floor_ID(INT)
* Constraint PK(Room_ID)
* Constraint FK(Floor_ID) references Floor.Floor_ID


## Switch 

* Switch_ID(INT)
* Descripton(varchar)
* Error_ID(INT)
* Room_ID(INT)
* Status_Network(boolean)
* Constraint PK(Switch_ID)
* Constraint FK(Room_ID) references Room.
Room_ID
* Constraint FK(Status_Network) references ActiveNetworks.
ActiveNetworks_ID
* Constraint FK(Error_ID) references Errors.
Error_ID


## Router 

* Router_ID(INT)
* Descripton(varchar)
* Error_ID(INT)
* Status(boolean)
* Room_ID(INT)
* Status_Network(boolean)
* Constraint PK(Router_ID)
* Constraint FK(Room_ID) references Room.
Room_ID
* Constraint FK(Status_Network) references ActiveNetworks.
ActiveNetworks_ID
* Constraint FK(Error_ID) references Errors.
Error_ID


## Active Networks 

* ActiveNetworks_ID(INT)
* Status(boolean)
* Room_ID(INT)
* Constraint PK(ActiveNetworks_ID)
* Constraint FK(Room_ID) references Room.
Room_ID

## Errors

* Error_ID(INT)
* Error_Description(varchar)
* Constraint PK(Error_ID)
