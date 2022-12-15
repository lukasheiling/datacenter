# User story configure VLAN

Configures VLAN on the network

## Actors

* Person (Role: Admin)

## Input

vlanID, innerTagProtocollID, innerVlanID, Building, Floor, Room number

## Internal state change

The vlan is configured into the system

## Output 

Done!

## Errors

* insufficient rights
* nonexistent building
* nonexistent floor
* nonexistent room 
* already existing vlanID
* system not vlan ready
* already to many vlans created