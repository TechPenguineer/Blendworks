import bpy

class change_lod(bpy.types.Operator):
    bl_idname = "object.change_lod"
    bl_label = "Polify"
    bl_description = "Make blender object poly"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        bpy.context.window.workspace=bpy.data.workspace[self.layoutItems1]
        return {"FINISHED"}
