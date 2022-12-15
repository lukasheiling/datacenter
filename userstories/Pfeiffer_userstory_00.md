User story Implement MiktroTik.

Add a end device with its IP-Address and add it to system.
Actors

    Person (Role: Admin)

Input

Building, Floor, Room number
Internal state change

The end device can be active or not. It should stay at the same place.
Output

Acknowledgement.
Errors

    insufficient rights
    nonexistent building
    nonexistent floor
    nonexistent room
    if IP-Address static: check duplicate IP-Address --> duplicate IP-Address
