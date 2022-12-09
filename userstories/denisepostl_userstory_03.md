# User story create VLAN.

Create VLAN and add it to system.

## Actors

* Person (Role: Admin)

## Input

Building, Floor, Room number, Switch number

## Internal state change

Active VLAN. Deactive VLAN.

## Output 

Acknowledgement. If the VLAN is active or not.

## Errors

* insufficient rights
* nonexistent building
* nonexistent floor
* nonexistent room 
* non existent switch number
* defect switch