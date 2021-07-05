import bpy

def dump(obj, text):
    for attr in dir(obj):
        print("%r.%s = %s" % (obj, attr, getattr(obj, attr)))
    

class change_lod(bpy.types.Operator):
    bl_idname = "object.change_lod"
    bl_label = "Polify"
    bl_description = "Make blender object poly"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        return context.active_object is None

    def execute(self, context):
        value = getattr(context, "button_pointer", None)
        if value is not None:
                dump(value, "button_pointer")
        
        value=getattr( context, "button_prop", None)
        if value is not None:
            dump(value, "button_prop")
        
        value = getattr(context, "button_operator", None)
        if value is not None:
            dump(value, "button_operator")
                    
        return {"FINISHED"}
