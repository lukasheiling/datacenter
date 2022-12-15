# Userstory_XYZ

## Permissions

* pmID(INT)
* Permission(Text)
* UserID(INT)
* ErrorID(INT)
* Constrain FK(UserID) references Users.uID
* Constraint PK(pmID)
* Constrain FK(ErrorID) references Error.eID

## Users

* uID(INT)
* UserName(Text)
* security(hash)
* Constraint PK(uID)


## Vlans

* vID(INT)
* PermissionID(INT)
* LocationID(INT)
* innerTagProtocoll(Text)
* innerVlan(Text)
* Constraint PK(vID)
* Constraint FK (PermissionID) references Permissions.pmID
* Constrain FK(LocationID) references Location.loID

## Location

* loID(INT)
* Floor(INT)
* Room(INT)
* Building(INT)
* Switch(INT)

## Errors

* eID
* ErrorType(Text)




