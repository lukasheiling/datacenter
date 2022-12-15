# User story add topology to system.

Create a topology and add it to system.

## Actors

* Person (Role: Admin)

## Input

Building, Floor, Room number, Switch number, Router number, Socket numbers

## Internal state change

The topology can be changed, deleted or a new one added.

## Output 

Acknowledgement. Topology which is used in specific rooms, floors, buildings. Which devices are involved.

## Errors

* insufficient rights
* nonexistent building
* nonexistent floor
* nonexistent room 
* nonexistent switch number
* nonexistent router number
* nonexistent socket number
* defect switch
* defect router
* deactivated vlan
* device with the same number used - used same device in topology