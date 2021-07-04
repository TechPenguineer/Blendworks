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
            active_obj = context.view_layer.objects.active 
            
            obNameList=[]
            for objs in active_obj:
                obNameList.append(objs.name) 
                bpy.context.rigid_body.type = 'ACTIVE'
                bpy.context.space_data.context = 'PHYSICS'
                bpy.ops.rigidbody.object_add(objs.name)
            
            return { 'FINISHED' }
