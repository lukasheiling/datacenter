# Userstory_add_a_server

## Building

* building_id int
* name Text
* Constraint PK(building_id)

## Room

* room_id int
* name Text
* Constraint PK(room_id)
* Constraint FK(building_id) references Building.building_id

## Server

* server_id int
* name Text
* state-change Text
* Constraint PK(server_id)
* Constraint FK(room_id) references Room.room_id
* Constraint FK(error_id) references Error.error_id

## Error

* error_id int
* name Text
* Constraint PK(error_id)
