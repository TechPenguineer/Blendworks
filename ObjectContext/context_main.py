import bpy

class BWU_CONTEXT_MENU_OP(bpy.types.Operator):
    bl_idname = "view3d.open_bwu_context"
    bl_label = "Blendworks"
    bl_description = "Blendworks Context Menu"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        
        return {"FINISHED"}
