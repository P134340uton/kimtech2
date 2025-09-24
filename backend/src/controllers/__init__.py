from src.controllers.user_controller import api as user_ns
from src.controllers.person_controller import api as person_ns
from src.controllers.city_controller import api as city_ns
from src.controllers.role_controller import api as role_ns
from src.controllers.user_role_controller import api as user_role_ns
from src.controllers.permission_controller import api as permission_ns
from src.controllers.role_permission_controller import api as role_permission_ns
from src.controllers.vehicle_controller import api as vehicle_ns
from src.controllers.vehicle_state_controller import api as vehicle_state_ns
from src.controllers.repair_controller import api as repair_ns
from src.controllers.repair_status_controller import api as repair_status_ns
from src.controllers.repair_part_controller import api as repair_part_ns
from src.controllers.repair_checklist_item_controller import api as repair_checklist_item_ns
from src.controllers.maintenance_controller import api as maintenance_ns
from src.controllers.maintenance_status_controller import api as maintenance_status_ns
from src.controllers.maintenance_checklist_item_controller import api as maintenance_checklist_item_ns

namespaces = [
    (user_ns, "/users"),
    (person_ns, "/persons"),
    (city_ns, "/cities"),
    (role_ns, "/roles"),
    (user_role_ns, "/user_roles"),
    (permission_ns, "/permissions"),
    (role_permission_ns, "/role_permissions"),
    (vehicle_ns, "/vehicles"),
    (vehicle_state_ns, "/vehicle_states"),
    (repair_ns, "/repairs"),
    (repair_status_ns, "/repair_statuses"),
    (repair_part_ns, "/repair_parts"),
    (repair_checklist_item_ns, "/repair_checklist_items"),
    (maintenance_ns, "/maintenances"),
    (maintenance_status_ns, "/maintenance_statuses"),
    (maintenance_checklist_item_ns, "/maintenance_checklist_items")
]