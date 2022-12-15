# Userstory_cabling_ethernet

## Building

* building_id int
* name Text
* Constraint PK(building_id)

## Room

* room_id int
* name Text
* Constraint PK(room_id)
* Constraint FK(building_id) references Building.building_id
* Constraint FK(wall_id) references Wall.wall_id

## Wall

* wall_id int
* Constraint PK(wall_id)

## Patch Panel

* patchPanel_id int
* name Text
* Constraint PK(patchPanel_id)
* Constraint FK(room_id) references Room.room_id
* Constraint FK(error_id) references Error.error_id

## Wall-Socket

* wallSocket_id int
* name Text
* Constraint PK(wallSocket_id)
* Constraint FK(wall_id) references Wall.wall_id

## Error

* error_id int
* name Text
* Constraint PK(error_id)