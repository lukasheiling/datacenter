# Userstory_login

## Table 1: User
* User_id (integer)
* Username (string)
* Password (string)
* Constraint PK(User_id)

## Table 2: Login_attempt
* Login_attempt_id (integer)
* User_id (integer)
* Login_timestamp (datetime)
* Constraint PK(Login_attempt_id)
* Constraint FK(User_id) references User.User_id