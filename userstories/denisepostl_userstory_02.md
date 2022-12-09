# User story find active network device.

Find an active network device which is in system by room number, floor, building or device number(Swich numbers, Router numbers).

## Actors

* Person (Role: Admin)

## Input

Building, Floor, Room number, Switch numbers, Router numbers

## Internal state change

The Network Device can be replaced or doesn't exist anymore.

## Output 

Return the number of the active network devices.

## Errors

* insufficient rights
* nonexistent building
* nonexistent floor
* nonexistent room 
* nonexistent switch
* nonexistent router
* defect switch
* defect router