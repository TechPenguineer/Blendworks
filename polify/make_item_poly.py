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
        bpy.ops.workspace.add("Blenderworks Polify")
        bpy.ops.workspace.reorder_to_front()
        return {"FINISHED"}
