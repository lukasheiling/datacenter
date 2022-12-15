# Userstory_MH1224578_07

# Building
- id: integer
- name: string
- address: string

# Floor
- id: integer
- building_id: integer (foreign key to Building)
- level: integer

# Room
- id: integer
- floor_id: integer (foreign key to Floor)
- name: string

# Server
- id: integer
- room_id: integer (foreign key to Room)
- name: string
- socket_number: string

# PatchPanel
- id: integer
- server_id: integer (foreign key to Server)
- number: integer
- port_number: integer

# PatchCable
- id: integer
- patch_panel_id: integer (foreign key to PatchPanel)
- number: integer

# Switch
- id: integer
- server_id: integer (foreign key to Server)
- number: integer
- port_number: integer