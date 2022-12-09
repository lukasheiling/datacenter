# User story to add connection of socket to switch

Connect a network wall socket with a switch.

## Actors

* Person (Role:Admin)

## Input

Socket number, switch number, port number

## Internal state change

The connection is persisted into the system.

## Output

Acknowledgement

## Errors

* insufficient rights
* nonexistend socket
* nonexistend switch
* nonexistend port
* port already used
* socket already connected
