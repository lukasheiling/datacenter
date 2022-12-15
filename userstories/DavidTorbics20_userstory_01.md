# User story locate every device.

Create a table containing every devices location

## Actors

* Person (Role: Admin)

## Input

Building, Floor, Room number, Socket numbers, Computers

## Internal state change

Saving enduser location to a list (the list with IPs)

## Output 

A list with IPs and the location of the devices

## Errors

* insufficient rights
* nonexistent building
* nonexistent floor
* nonexistent room
* no endusers found
* duplicate IPs
* duplicate location
