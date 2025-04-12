from subprocess import run
import bpy
from .register_class import _get_cls


class COT_OT_open_text_file(bpy.types.Operator):
    bl_idname = "object.open_text_file"
    bl_label = "Open Text File"
    bl_description = "Open the file of bpy.data.texts."

    def execute(self, context):
        # VS Code の実行ファイル（Code.exe）のフルパスを指定
        code_exe_path = "C:/Users/hoike/AppData/Local/Programs/Microsoft VS Code/Code.exe"
        for text in bpy.data.texts:
            if s := text.filepath:
                # ファイルパスを出力して変数の中身を確認
                print("Opening file:", s)
                run([code_exe_path, s])
        return {"FINISHED"}
s

# 自動的にこのモジュールのクラスを設定
ui_classes = _get_cls(__name__)


def draw_item(self, context):
    """メニューの登録と削除用"""
    for ui_class in ui_classes:
        self.layout.operator(ui_class.bl_idname)


def register():
    """追加登録用（クラス登録は、register_class内で実行）"""
    bpy.types.TEXT_MT_text.append(draw_item)


def unregister():
    """追加削除用（クラス削除は、register_class内で実行）"""
    bpy.types.TEXT_MT_text.remove(draw_item)
