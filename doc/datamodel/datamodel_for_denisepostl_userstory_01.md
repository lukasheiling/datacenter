# User story add router to system.

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

## Router 

* Router_ID(INT)
* Descripton(varchar)
* Room_ID(INT)
* Constraint PK(Router_ID)
* Constraint FK(Room_ID) references Room.
Room_ID
