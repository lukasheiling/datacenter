# Userstory_AddAccessPoint

## Table 1: Building
* Building_id (integer)
* Building_name (string)
* Constraint PK(Building_id)

## Table 2: Floor
* Floor_id (integer)
Building_id (integer)
Floor_number (integer)
Constraint PK(Floor_id)
Constraint FK(Building_id) references Building.Building_id

## Table 3: Room
Room_id (integer)
Floor_id (integer)
Room_number (string)
Constraint PK(Room_id)
Constraint FK(Floor_id) references Floor.Floor_id

## Table 4: AccessPoint
* AccessPoint_id (INTEGER)
* Room_id (INTEGER)
* AccessPoint_name (VARCHAR)
* AccessPoint_model (VARCHAR)
* AccessPoint_serialNumber (VARCHAR)
* Constraint PK(AccessPointId)
* Constraint FK(RoomId) references Room.RoomId