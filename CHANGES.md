# Change Log

# 0.6.0 +  0.7.0 
- Added new actions:  `create_dhcp_lease_reservation`, `create_or_edit_ip`, `get_lifecycle_event_objects`, `suggest_next_ip`, `write_pxe_cfg`, 
- Added new action chain: `networking_lifecycle_automation`, `suggest_and_create_ip`
- Added new rules: `device_created_initial_lifecyle`, `networking_lifecycle_automation_rule`

# 0.5.0 

- Added 4 new actions: `get_device_by_id`, `get_lifecycle_events`, `update_device`, and `update_object_category_by_lifecycle_id`. 
- Added 1 new rule: `lifecycle_triggered_object_category_change`.  
- Added new API method putAPI to `lib/base_action.py` in order to handle PUT requests to Device42.  

# 0.4.0

- Updated action `runner_type` from `run-python` to `python-script`

# 0.3.0

- Rename `config.yaml` to `config.schema.yaml` and update to use schema.
