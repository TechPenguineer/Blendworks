import bpy 

class  BWU_OT_Add_Rigidbody_Op(bpy.types.Operator):
    bl_idname = "object.apply_rigidbody"
    bl_label = "Apply Rigidbody"
    bl_description = "Adds a rigidbody to the selected object(s)"

    @classmethod
    def poll(cls,context):
        obj = context.object
        if obj is not None:
            if obj.mode == "OBJECT":
                return True
        return False
            
    def execute(self,context):
            selected_objects = bpy.context.selected_objects
            
            obNameList=[]
            context = bpy.context
            scene = context.scene
            for objs in selected_objects:
                bpy.ops.rigidbody.object_add(type='ACTIVE')
            
            return { 'FINISHED' }

class  BWU_OT_Add_Rigidbody_Passive_Op(bpy.types.Operator):
    bl_idname = "object.apply_passive_rigidbody"
    bl_label = "Make Passive"
    bl_description = "Adds a passive rigidbody to the selected object(s)"

    @classmethod
    def poll(cls,context):
        obj = context.object
        if obj is not None:
            if obj.mode == "OBJECT":
                return True
        return False
            
    def execute(self,context):
            selected_objects = bpy.context.selected_objects
            
            obNameList=[]
            context = bpy.context
            scene = context.scene
            for objs in selected_objects:
                bpy.ops.rigidbody.object_add(type='PASSIVE')
            
            return { 'FINISHED' }


class  BWU_OT_Remove_Rigidbody_Op(bpy.types.Operator):
    bl_idname = "object.remove_rigidbody"
    bl_label = "Remove Physics Object"
    bl_description = "Removes the rigidbody from the selected object(s)"

    @classmethod
    def poll(cls,context):
        obj = context.object
        if obj is not None:
            if obj.mode == "OBJECT":
                return True
        return False
            
    def execute(self,context):
            selected_objects = bpy.context.selected_objects
            
            obNameList=[]
            context = bpy.context
            scene = context.scene
            for objs in selected_objects:
                bpy.ops.rigidbody.object_remove()
            
            return { 'FINISHED' }