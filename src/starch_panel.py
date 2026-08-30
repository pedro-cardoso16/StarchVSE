import bpy


class SEQUENCER_OT_fit_timeline_to_strips(bpy.types.Operator):
    bl_idname = "sequencer.fit_timeline_to_strips"
    bl_label = "Fit Timeline to Strips"
    bl_description = "Auto-adjust start and end frames to fit all VSE media"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return (context.scene.sequence_editor is not None and
                len(context.scene.sequence_editor.sequences) > 0)

    def execute(self, context):
        scene = context.scene
        seq_editor = scene.sequence_editor

        if seq_editor is None:
            self.report(
                {'WARNING'}, "VSE is not initialized! Add a strip first.")
            return {'CANCELLED'}

        all_strips = seq_editor.sequences
        if len(all_strips) == 0:
            self.report({'WARNING'}, "No strips found in the timeline.")
            return {'CANCELLED'}

        start_frames = [strip.frame_final_start for strip in all_strips]
        end_frames = [strip.frame_final_end - 1 for strip in all_strips]

        scene.frame_start = int(min(start_frames))
        scene.frame_end = int(max(end_frames))

        self.report(
            {'INFO'}, f"Timeline fitted: {scene.frame_start} to {scene.frame_end}")
        return {'FINISHED'}


def draw_vse_range_helper(self, context):
    layout = self.layout
    layout.separator()
    layout.operator("sequencer.fit_timeline_to_strips",
                    icon='FULLSCREEN_ENTER')
