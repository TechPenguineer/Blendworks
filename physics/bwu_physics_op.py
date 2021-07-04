import bpy 

class MyClassName(bpy.types.Operator):
    bl_idname = "object.apply_rigidbody"
    bl_label = "Apply Rigidbody"
    bl_description = "Description that shows in blender tooltips"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        
        return {"FINISHED"}
