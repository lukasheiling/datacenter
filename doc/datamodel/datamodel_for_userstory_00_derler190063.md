# User story create account.

## User

-   Id INT
-   Firstname VARCHAR
-   Surename VARCHAR
-   Username VARCHAR
-   Password VARCHAR
-   Constraint PK(Id)

## Email

-   Id INT
-   EmailAddress VARCHAR
-   UserId INT
-   MainEmail BOOLEAN
-   Constraint PK(Id)
-   Constraint FK(UserId) references User.Id

## PhoneNumber

-   Id INT
-   PhoneNumber INT
-   UserId INT
-   Constraint PK(Id)
-   Constraint FK(UserId) references User.Id

## Address

-   Id INT
-   UserId INT
-   City
-   Street
-   Housenumber
-   Zipcode
-   Constraint PK(Id)
-   Constraint FK(UserId) references User.Id

## Role

-   Id INT
-   RoleName VARCHAR
-   Description VARCHAR
-   Constraint PK (Id)

## UserRole

-   Id INT
-   UserId INT
-   RoleId INT
-   Constraint PK (Id)
-   Constraint FK(UserId) references User.Id
-   Constraint FK(RoleId) references Role.Id

## DeviceTypes

-   Id INT
-   DeviceFunctionality VARCHAR

## Devices

-   Id INT
-   DeviceName VARCHAR
-   DeviceTypeId INT
-   Constraint PK(Id)
-   Constraint FK(DeviceTypeId) references DeviceType.Id

## Socket

-   Id INT
-   SocketName VARCHAR
-   FirstPortId INT
-   SecondPortId INT
-   RoomId INT
-   Constraint PK(Id)
-   Constraint FK(RoomId) references Room.Id
-   Constraint FK(FirstPortId) references Port.Id
-   Constraint FK(SecondPortId) references Port.Id

## Room

-   Id INT
-   RoomName VARHCAR
-   FloorId INT
-   Constraint PK(Id)
-   Constraint FK(FloorId) references Floor.Id

## Floor

-   Id INT
-   FloorName VARCHAR
-   BuildingId INT
-   Constraint PK(Id)
-   Constraint FK(BuildingId) references Building.Id

## Building

-   Id INT
-   BuildingName VARCHAR
-   Constraint PK(Id)

## Port

-   Id INT
-   IPAddress VARCHAR
-   MACAddress VARCHAR
-   DeviceId INT
-   VlanId INT
-   Constraint PK(Id)
-   Constraint FK(DeviceId) references Device.Id
-   Constraint FK(VlanId) references Vlan.Id

## Connection

-   Id INT
-   FirstPortId INT
-   SecondPortId INT
-   Constraint PK(Id)
-   Constraint FK(FirstPortId) references Port.Id
-   Constraint FK(SecondPortId) references Port.Id

## Vlan

-   Id INT
-   VlanName VARCHAR
-   VlanId INT
-   Constraint PK(Id)
