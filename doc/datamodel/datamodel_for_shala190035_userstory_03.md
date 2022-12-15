# Userstory_AddAccessPoint

## Table 1: Building
* BuildingId (INTEGER)
* BuildingName (VARCHAR)
* Constraint PK(BuildingId)

## Table 2: Floor
* FloorId (INTEGER)
* BuildingId (INTEGER)
* FloorNumber (INTEGER)
* Constraint PK(FloorId)
* Constraint FK(BuildingId) references Building.* BuildingId

## Table 3: Room
* RoomId (INTEGER)
* FloorId (INTEGER)
* RoomNumber (INTEGER)
* Constraint PK(RoomId)
* Constraint FK(FloorId) references Floor.FloorId

## Table 4: AccessPoint
* AccessPointId (INTEGER)
* RoomId (INTEGER)
* AccessPointName (VARCHAR)
* AccessPointModel (VARCHAR)
* AccessPointSerialNumber (VARCHAR)
* Constraint PK(AccessPointId)
* Constraint FK(RoomId) references Room.RoomId