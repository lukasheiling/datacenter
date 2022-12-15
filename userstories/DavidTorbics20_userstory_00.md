# User story get existing IPs.

Receive the IP address of every enduser in the network 

## Actors

* Person (Role: Admin)

## Input

Building, Floor, Room number, Socket numbers, Computers

## Internal state change

Saving enduser IP to a list

## Output 

A list of IP addresses

## Errors

* insufficient rights
* nonexistent building
* nonexistent floor
* nonexistent room
* no endusers found
* duplicate IPs