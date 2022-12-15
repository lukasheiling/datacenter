# Userstory_schaff190163_userstory_00

## Devices

* device_ID(int)
* device_name(varchar)
* device_ip(varchar)
* Constraint PK(device_ID)

## Sockets

* socket_ID(int)
* Constraint PK(socket_ID)

## Rooms

* room_ID(int)
* Constraint PK(room_ID)

## Floors

* floor_ID(int)
* Constraint PK(floor_ID)

## Buildings

* building_ID(int)
* Constraint PK(building_ID)

## Device Location

* device_ID references Devices.device_ID
* socket_ID references Sockets.socket_ID
* room_ID references Rooms.room_ID
* floor_ID references Floors.floor_ID
* building_ID references Buildings.building_ID
