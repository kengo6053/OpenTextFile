import webbrowser

import bpy

from .register_class import _get_cls


class COU_OT_open_text_file(bpy.types.Operator):
    bl_idname = "object.open_text_file"
    bl_label = "Open Text File"
    bl_description = "Open the URL of a text object."

    def execute(self, context):  # noqa: PLR6301
        lst = list(bpy.data.objects)
        if context.view_layer.objects.active:
            lst = [context.view_layer.objects.active, *lst]
        lst = [obj for obj in lst if obj.type == "FONT" and obj.data.body.startswith("http")]
        if lst:
            webbrowser.open(lst[0].data.body)
        return {"FINISHED"}


# 自動的にこのモジュールのクラスを設定
ui_classes = _get_cls(__name__)


def draw_item(self, _context):
    """メニューの登録と削除用"""
    for ui_class in ui_classes:
        self.layout.operator(ui_class.bl_idname)


def register():
    """追加登録用(クラス登録は、register_class内で実行)"""
    bpy.types.TEXT_MT_text.append(draw_item)


def unregister():
    """追加削除用(クラス削除は、register_class内で実行)"""
    bpy.types.TEXT_MT_text.remove(draw_item)
