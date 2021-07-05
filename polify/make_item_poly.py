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
        for area in bpy.data.screen["Blendworks Polify"].screens[0].areas: 
            if area.type == 'VIEW_3d':
                for spaces in area.spaces:
                    area.spaces.active.clip_start = 0.1
        return {"FINISHED"}
