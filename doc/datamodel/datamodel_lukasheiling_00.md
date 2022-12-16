# Datamodel monitor network usage in datacenter

## Datacenter
- id (primary key)
- name (varchar)
- address (varchar)
- floor_ids (foreign keys)

## Floor
- id (primary key)
- floornumber (int)
- room_ids (foreign keys)

## Room
- id (primary key)
- roomnumber (int)
- network_usage_ids (foreign keys)

## Network usage
- id (primary key)
- timestamp (int)
- traffic (int)
- active_connections (int)
- performance (int)
- datacenter_id (foreign key)
- floor_id (foreign key)
- room_id (foreign key)