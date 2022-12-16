# Userstory datamodel Paul, Jonas, Simon, Matthias 00

## Building
* ID(int) pk
* Name (varchar)
* Location (varchar)   

## Floor
* ID(int) pk
* building_ID(int) fk
* number(int)

## Room
* ID(int) pk
* floor_ID(int) fk Floor.ID
* number(int)

## Socket
* ID(int)
* device_ID(int) fk Device.ID

## Device
* ID(int) pk
* Name(varchar)

## Errors
* eID
* ErrorType(varchar)

## Permissions
* pmID(INT)
* Permission(varchar)
* UserID(INT)
* ErrorID(INT)
* Constrain FK(UserID) references Users.uID
* Constraint PK(pmID)
* Constrain FK(ErrorID) references Error.eID


## Config

## Users
* uID(INT) PK 
* UserName(varchar)
* security(hash)