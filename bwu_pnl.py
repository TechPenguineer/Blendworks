import bpy;


class BWU_MOD_PANEL(bpy.types.Panel):
    bl_label = "Modifier Controllers"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Blendworks"

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        col = layout.column()
        
        col.operator("object.apply_all_mods", text="Apply All")
        
        col =  row.column()
        col.operator("object.remove_all_mods", text="Cancel All")




class BWU_PHYSICS_PANEL(bpy.types.Panel, bpy.types.PropertyGroup):
    bl_label = "Physics"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Blendworks"

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        col = layout.column()
        
        col.operator("object.apply_rigidbody", text="Add Physics Object")
        
        col =  row.column()
        col.operator("object.apply_passive_rigidbody", text="Make Collider")

        row = layout.row()
        col =  row.column()
        col.operator("object.remove_rigidbody", text="Remove Physics Object")
        
