Person
  PK              int
  Name            string
  Role            string
 
Errors
  PK              int
  Error_masage    string
  Error_type      string
  
Userstory
  PK              int
  story           string
  input           string
  output          string
  person_id       foreign_key, Person
  
  
StoryError
  PK              int
  Userstory_id    foreign_key, Userstory
  Error_id        foreign_key, Errors
