import bpy

class create_editor_workspace_op(bpy.types.Operator):
    bl_idname = "object.createWorkspac"
    bl_label = "CreateWorkspace"
    bl_description = "Description that shows in blender tooltips"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        bpy.ops.workspace.add("Blenderworks")        
        return {"FINISHED"}
