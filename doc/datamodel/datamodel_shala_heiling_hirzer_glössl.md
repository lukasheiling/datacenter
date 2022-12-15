# Userstory_Server

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

## Table 4: Server
* Server_id: integer
* Server_Name: string
* Constraint FK(Room_id) references Room.Room_id


# Userstory_Monitor_network_usage_in_datacenter

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

## Table 4: Datacenter
* Datacenter_id (primary key)
* Datacenter_name (varchar)
* Address (varchar)
* Constraint PK(Datacenter_id)
* Constraint FK(Room_id) references Room.Room_id

## Table 5: Network usage
* NetworkUsage_id (primary key)
* Timestamp (int)
* Traffic (int)
* Active_connections (int)
* Performance (int)
* Constraint PK(NetworkUsage_id)
* Constraint FK(Datacenter_id) references Datacenter.Datacenter_id
* Constraint FK(Room_id) references Room.Room_id

# Userstory_login

## Table 1: User
* User_id (integer)
* Username (string)
* Password (string)
* Constraint PK(User_id)

## Table 2: Login_attempt
* Login_attempt_id (integer)
* User_id (integer)
* Login_timestamp (datetime)
* Constraint PK(Login_attempt_id)
* Constraint FK(User_id) references User.User_id

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
* AccessPoint_id (integer)
* Room_id (integer)
* AccessPoint_name (string)
* AccessPoint_model (string)
* AccessPoint_serialNumber (string)
* Constraint PK(AccessPointId)
* Constraint FK(RoomId) references Room.RoomId