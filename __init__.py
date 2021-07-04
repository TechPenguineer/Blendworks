import bpy

bl_info = {
    "name" : "Blendworks",
    "author" : "TechPenguineer",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import bpy 

from . bwu_modifier_op import BWU_OT_Apply_All_Op, BWU_OT_Remove_All_Op
from . bwu_pnl import BWU_MOD_PANEL, BWU_PHYSICS_PANEL
from . physics.bwu_physics_op import BWU_OT_Add_Rigidbody_Op, BWU_OT_Add_Rigidbody_Passive_Op

classes = (BWU_OT_Apply_All_Op,BWU_OT_Remove_All_Op,BWU_MOD_PANEL, BWU_PHYSICS_PANEL, BWU_OT_Add_Rigidbody_Op, BWU_OT_Add_Rigidbody_Passive_Op)

def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in classes:
      bpy.utils.register_class(c)
