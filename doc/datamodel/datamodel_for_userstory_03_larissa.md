# Userstory_add_patch_wire_in_patch_pannel

## Building

* building_id int
* name Text
* Constraint PK(building_id)

## Room-number

* room_id int
* name Text
* Constraint PK(room_id)
* Constraint FK(building_id) references Building.building_id
* Constraint FK(floor_id) references Floor.floor_id

## Floor

* floor_id int
* Constraint PK(floor_id)

## Patch-Panel-Number

* patchPanel_id int
* name Text
* Constraint PK(patchPanel_id)
* Constraint FK(room_id) references Room-Number.room_id
* Constraint FK(error_id) references Error.error_id
* Constraint FK(error_id) references Wire.wire_id

## Wire

* wire_id int
* name Text
* Constraint PK(wire_id)

## Error

* error_id int
* name Text
* Constraint PK(error_id)