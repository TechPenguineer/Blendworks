import bpy

bl_info = {
    "name" : "Blendworks",
    "author" : "TechPenguineer",
    "description" : "Blendworks is a plugin that makes Blender easier to use for beginers",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "Palm Beach, Florida",
    "warning" : "STLL UNDER DEVELOPMENT",
    "category" : "Generic",
    "repository": "https://github.com/TechPenguineer/Blendworks"
}

import bpy 

from . bwu_modifier_op import BWU_OT_Apply_All_Op, BWU_OT_Remove_All_Op
from . bwu_pnl import BWU_MOD_PANEL, BWU_PHYSICS_PANEL
from . physics.bwu_physics_op import BWU_OT_Add_Rigidbody_Op, BWU_OT_Add_Rigidbody_Passive_Op, BWU_OT_Remove_Rigidbody_Op,BWU_OT_Physics_Settings_Friction_Op,OBJECT_OT_pyhsics_settings
from . mesh.bwu_custom_mesh import createOcean
from . ObjectContext.context_main import BWU_CONTEXT_MENU_OP
classes = (BWU_OT_Apply_All_Op,BWU_OT_Remove_All_Op,BWU_MOD_PANEL, BWU_PHYSICS_PANEL, BWU_OT_Add_Rigidbody_Op, BWU_OT_Add_Rigidbody_Passive_Op, BWU_OT_Remove_Rigidbody_Op,
           BWU_OT_Physics_Settings_Friction_Op,OBJECT_OT_pyhsics_settings, createOcean, BWU_CONTEXT_MENU_OP)

def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in classes:
      bpy.utils.register_class(c)
