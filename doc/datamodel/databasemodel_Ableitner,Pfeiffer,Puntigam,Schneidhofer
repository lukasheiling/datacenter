Pfeiffer:
Building:

    building_id (pk)
    building_name (varchar)
    building_address (varchar)

Floor:

    floor_id (primary key)
    building_id (foreign key -> building_id)
    floor_name  (varchar)

Room:

    room_id (primary key)
    floor_id (foreign key -> floor_id)
    room_name (varchar)
    room_number (varchar)

Device table:

    device_id (primary key)
    room_id (foreign key -> room_id)
    device_name (varchar)
    device_ip (varchar)
    device_status (active/inactive)
    device_uptime (integer)

User table:

    user_id (primary key)
    username  (varchar)
    password  (varchar)
    email (varchar)
    permissions (admin/non-admin -> bool)

Error table:

    error_id (primary key)
    error_type (varchar)
    error_message (varchar)


Userstory Puntigam

Person:

    person_id   (primary key)
    name    (varchar)
    role    (varchar)

Errors:
    
    error_id    (primary key)
    error_message   (varchar)
    error_type    (varchar)
    
Userstory:

    story_id    (primary key)
    story   (varchar)
    input   (varchar)
    output  (varchar)
    person_id   (foreign key -> person_id)
    
StoryError:

    PK    (primary key)
    userstory_id    (foreign key -> userstory_id)
    error_id    (foreign key -> error_id)
