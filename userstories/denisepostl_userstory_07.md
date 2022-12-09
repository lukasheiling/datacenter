# User story add patch wire in patch panel.

Add patch wire in patch pannel and add it to system.

## Actors

* Person (Role: Admin)

## Input

Building, Floor, Room number, Patchpanel number

## Internal state change

Patch wire should be persistent in patch panel. 
If its defect then it have to be replaced.

## Output 

Acknowledgement. How much patch wires are in patch panel

## Errors

* insufficient rights
* nonexistent building
* nonexistent floor
* nonexistent room 
* nonexistent patch panel
* defect patch wire