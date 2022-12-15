# User story Add IP-Address of Device and try to Identify it.

Add a Device and its IP-Address. When the administrator is looking
for the Device with the specific IP-Address then he/she should get
informations about this device.

## Actors

* Person (Role: Admin)

## Input

Building, Floor, Room number, IP-Address

## Internal state change

If a device is defect, then it should be removed. Maybe the
IP-Address can be used for a new one. 
The IP-Address of a specific device should be the same as long the device works properly.

## Output 

Acknowledgement. Location of Device (Building, Room-/Floor-/Number).
Is the Device in a VLAN/Topology involved.

## Errors

* non existent IP-Address
* duplicate IP-Address
