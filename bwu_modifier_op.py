import bpy

class BWU_OT_Apply_All_Op(bpy.types.Operator):
    bl_idname = "object.apply_all_mods"
    bl_label = "Apply All"
    bl_description = "Apply all operators of the active object"

    
    @classmethod
    def poll(cls,context):
        obj = context.object
        if obj is not None:
            if obj.mode == "OBJECT":
                return True
        return False
            
    def execute(self,context):
            active_obj = context.view_layer.objects.active 
            
            for mod in active_obj.modifiers:
                bpy.ops.object.modifier_apply(modifier=mod.name)
            return { 'FINISHED' }
        
        
class BWU_OT_Remove_All_Op(bpy.types.Operator):
    bl_idname = "object.remove_all_mods"
    bl_label = "Remove All"
    bl_description = "Remove all operators of the active object"

    
    @classmethod
    def poll(cls,context):
        obj = context.object
        if obj is not None:
            if obj.mode == "OBJECT":
                return True
        return False
            
    def execute(self,context):
            active_obj = context.view_layer.objects.active 
            
            active_obj.modifiers.clear()
            
            return { 'FINISHED' }
        
        
