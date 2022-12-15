# Userstory_Add_RJ45_port

## Table 1: Building
* Building_id (integer)
* Building_name (string)
* Constraint PK(Building_id)

## Table 2: Floor
* Floor_id (integer)
* Building_id (integer)
* Floor_number (integer)
* Constraint PK(Floor_id)
* Constraint FK(Building_id) references Building. Building_id

## Table 3: Room
* Room_id (integer)
* Floor_id (integer)
* Room_number (string)
* Constraint PK(Room_id)
* Constraint FK(Floor_id) references Floor.Floor_id

## Table 4: RJ45 port
* Port_id (integer)
* Room_id (integer)
* Port_number (integer)
* Data_transfer_rate (integer)
* Cable_type (string)
* PoE (boolean)
* Network_management_protocols (string)
* Constraint PK(Port_id)
* Constraint FK(Room_id) references Room.Room_id