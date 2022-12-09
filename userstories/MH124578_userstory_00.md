# User story add company building.

Add a company building

## Actors

* Building (Role: Contain floors)

## Input

Building

## Internal state change

The building is persisted into the company network

## Output 

Acknowledgement

## Errors

* nonexistent floor
* nonexistent room


# User story add floor.

Add a new floor to the building

## Actors

* Floor (Role: Contain rooms)

## Input

Building, Floor

## Internal state change

The floor is persisted into the building

## Output 

Acknowledgement

## Errors

* nonexistent room



# User story add room.

Add a room to the floor

## Actors

* Room (Role: Contain sockets)

## Input

Building, Floor, Room number

## Internal state change

The room is persisted into the floor

## Output 

Acknowledgement

## Errors

* nonexistent socket



# User story add wall socket.

Add a network wall socket to the system

## Actors

* Person (Role: Admin)

## Input

Building, Floor, Room number, Socket numbers, 

## Internal state change

The socket is persisted into the system

## Output 

Acknowledgement

## Errors

* insufficient rights
* nonexistemt patch panel
* already existent socket number



# User story add patch panel.

Add a patch panel to the system

## Actors

* Patch panel (Role: Use patch cord)

## Input

Building, Floor, Room number, Socket numbers, Patch panel numbers, Patch panel port numbers

## Internal state change

The socket is persisted into the system

## Output 

Acknowledgement

## Errors

* already used patch panel port
* nonexistent patch cable
* nonexistent server



# User story add patch cable.

Add a patch cable to the system

## Actors

* Patch cable (Role: Connect to switch)

## Input

Building, Floor, Room number, Socket numbers, Patch panel numbers, Patch panel port numbers, Patch cable

## Internal state change

The patch cable is persisted into the system

## Output 

Acknowledgement

## Errors


* nonexistent siwitch port



# User story add switch.

Add a switch to the system

## Actors

* Switch (Role: Connect devices)

## Input

Building, Floor, Room number, Socket numbers, Patch panel numbers,  Patch panel port numbers, Patch cable, Switch numbers, Switch port numbers

## Internal state change

The switch is persisted into the system

## Output 

Acknowledgement

## Errors

* already used switch port
* nonexistent patch cable
* nonexistent server



# User story add server.

Add a server to the room

## Actors

* Server (Role: Contain patch panels and switches)

## Input

Building, Floor, Room number, Socket numbers, Patch panel numbers,  Patch panel port numbers, Patch cable, Switch numbers, Switch port numbers, Server number

## Internal state change

The server is persisted into the room

## Output 

Acknowledgement

## Errors

* nonexistent server room