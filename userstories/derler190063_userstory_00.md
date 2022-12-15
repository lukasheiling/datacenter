# User story create account.

Create a new user that has access to the system.

## Actors

-   Person (Role: Admin)

## Input

Firstname, surename, email, phone number, initial password, role, address

## Internal state change

A new user is created on the system.

## Output

Acknowledgement

## Errors

-   insufficient rights
-   firstname field not filled in
-   surename field not filled in
-   email field not filled in
-   phone number field not filled in
-   initial password field not filled in
-   role field not filled in
-   address field is not filled in
-   address is invalid

## User

-   Id INT
-   Firstname VARCHAR
-   Surename VARCHAR
-   Password VARCHAR
-   Constraint PK(Id)

## Email

-   Id INT
-   EmailAddress VARCHAR
-   UserId INT
-   MainEmail BOOLEAN
-   Constraint PK(Id)
-   Constraint FK(UserId) references User.Id

## PhoneNumber

-   Id INT
-   PhoneNumber INT
-   UserId INT
-   Constraint PK(Id)
-   Constraint FK(UserId) references User.Id

## Address

-   Id INT
-   UserId INT
-   City
-   Street
-   Housenumber
-   Zipcode
-   Constraint PK(Id)
-   Constraint FK(UserId) references User.Id

## Role

-   Id INT
-   RoleName INT
-   Constraint PK (Id)

## UserRole

-   Id INT
-   UserId INT
-   RoleId INT
-   Constraint PK (Id)
-   Constraint FK(UserId) references User.Id
-   Constraint FK(RoleId) references Role.Id
