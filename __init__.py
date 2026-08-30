# =========================================================================
# BACKWARD COMPATIBILITY HEADER (Required for Blender 4.1 and older)
# =========================================================================
bl_info = {
    "name": "StarchVSE",
    "author": "Pedro Cardoso",
    "version": (1, 0, 0),
    "blender": (4, 0, 0), # Enables support on older versions
    "location": "Properties > Output > Frame Range",
    "description": "Auto-sets timeline start and end frames to fit all active VSE media strips.",
    "warning": "",
    "doc_url": "",
    "category": "Sequencer",
}

import bpy

# Relative import targeting our subfolder module 'src'
from .src import starch_panel

def register():
    # Register the Operator inside src/starch_panel.py
    bpy.utils.register_class(starch_panel.SEQUENCER_OT_fit_timeline_to_strips)
    
    # Append the drawing layout inside src/starch_panel.py
    bpy.types.RENDER_PT_frame_range.append(starch_panel.draw_vse_range_helper)

def unregister():
    # Clean up the injected layout
    bpy.types.RENDER_PT_frame_range.remove(starch_panel.draw_vse_range_helper)
    
    # Unregister the Operator class
    bpy.utils.unregister_class(starch_panel.SEQUENCER_OT_fit_timeline_to_strips)