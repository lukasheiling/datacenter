# User story add topology to system.

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
* VLAN_ID(INT)
* Room_ID(INT)
* Topology_ID(INT)
* Status_Network(boolean)
* Constraint PK(Switch_ID)
* Constraint FK(Room_ID) references Room.
Room_ID
* Constraint FK(Error_ID) references Errors.
Error_ID
* Constraint FK(VLAN_ID) references VLAN.
VLAN_ID
* Constraint FK(Topology_ID) references Topology.
Topology_ID


## Router 

* Router_ID(INT)
* Descripton(varchar)
* Error_ID(INT)
* VLAN_ID(INT)
* Status(boolean)
* Room_ID(INT)
* Topology_ID(INT)
* Status_Network(boolean)
* Constraint PK(Router_ID)
* Constraint FK(Room_ID) references Room.
Room_ID
* Constraint FK(Error_ID) references Errors.
Error_ID
* Constraint FK(VLAN_ID) references VLAN.
VLAN_ID
* Constraint FK(Topology_ID) references Topology.
Topology_ID

## Topology 

* Topology_ID(INT)
* Descripton(varchar)
* Error_ID(INT)
* Room_ID(INT)
* Constraint PK(Router_ID)
* Constraint FK(Room_ID) references Room.
Room_ID
* Constraint FK(Error_ID) references Error.
Error_ID


## VLAN 

* VLAN_ID(INT)
* Description(varchar)
* Status(boolean)
* Room_ID(INT)
* Constraint PK(VLAN_ID)
* Constraint FK(Room_ID) references Room.
Room_ID


## Errors

* Error_ID(INT)
* Error_Description(varchar)
* Constraint PK(Error_ID)
