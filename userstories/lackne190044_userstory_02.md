# User story to connect a switch to another

Connect a switch with another switch.

## Actors

* Person (Role:Admin)

## Input

switch1 number, port1, switch2 number, port2

## Internal state change

The connection is persisted into the system.

## Output

Acknowledgement

## Errors

* insufficient rights
* nonexistend switch
* nonexistend port
* port already used
