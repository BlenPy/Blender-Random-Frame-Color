bl_info = {
    "name": "Random Node Frame Colorizer",
    "blender": (4, 2, 0),
    "category": "Node",
    "version": (1, 0),
    "author": "BlenDev",
    "description": "Automatically assigns random colors to selected Frames in any node editor.",
    "location": "Node Editor",
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
}

import bpy
import random

class NODE_OT_random_frame_color(bpy.types.Operator):
    """Randomly colorize selected frame nodes"""
    bl_idname = "node.random_frame_color"
    bl_label = "Apply Random Frame Color"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        # Access the node tree of the current node editor
        node_tree = context.space_data.node_tree
        
        if not node_tree:
            self.report({'WARNING'}, "No node tree found or the node editor is not active.")
            return {'CANCELLED'}
        
        frame_count = 0
        
        # Iterate over selected nodes to apply random color
        for node in node_tree.nodes:
            if isinstance(node, bpy.types.NodeFrame) and node.select:
                frame_count += 1
                
                # Generate and assign a random color to the frame node
                node.color = (random.random(), random.random(), random.random())
                
                # Ensure the custom color is enabled
                node.use_custom_color = True

        # Feedback message based on action success
        if frame_count == 0:
            self.report({'WARNING'}, "No selected frame nodes found.")
        else:
            self.report({'INFO'}, f"Random colors applied to {frame_count} selected frame(s).")
        
        return {'FINISHED'}

class NODE_PT_random_frame_color_panel(bpy.types.Panel):
    """Creates a panel in the node editor UI"""
    bl_label = "Random Frame Colorizer"
    bl_idname = "NODE_PT_random_frame_colorizer"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Frame Color"

    def draw(self, context):
        layout = self.layout
        layout.operator("node.random_frame_color")

def register():
    bpy.utils.register_class(NODE_OT_random_frame_color)
    bpy.utils.register_class(NODE_PT_random_frame_color_panel)

def unregister():
    bpy.utils.unregister_class(NODE_OT_random_frame_color)
    bpy.utils.unregister_class(NODE_PT_random_frame_color_panel)

if __name__ == "__main__":
    register()
