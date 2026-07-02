import bpy #bpyとは、Blender全体のAPI（オブジェクトとかシーンとか）
import bmesh #メッシュの内部構造(頂点、辺、面のトポロジーなど)を編集するためのモジュール
#bpy.date側にあるメッシュデータは「保存用の静的なデータ」で、そのままではトポロジーを走らせにくい
#bmeshで一時的に「編集可能な生のメッシュ表現」に変換する。
#よくわからない！

def find_ngons(obj):
    if obj.type != 'MESH':
        return []

    #まず空のbmeshインスタンスを作る。
    bm = bmesh.new()

    #メッシュのデータブロックの中身をこの箱にコピーする。ここで頂点だとかをはじめて読み込む
    bm.from_mesh(obj.data)

    #BlenderAPI特有の癖。
    #bmeshは内部にインデックス番号でアクセスできる「テーブル」を持つわけですが、
    #メッシュを変更した後はテーブル古くなる（invalidate）
    #するとIndexErrorになったり、f.indexがわけわからん数値になる。
    #Blenderでアドオンを作る際のお作法
    bm.faces.ensure_lookup_table()

    #bm.facesを一つずつfとして見て、f.verts(その面を構成する頂点のリスト)の長さが4より大きい
    #つまり五角形以上のものを抽出！
    ngon_indices = [f.index for f in bm.faces if len(f.verts) > 4]

    #短いけど超大事な一文
    #bmesh.new()で確保したメモリはBlenderのガベージコレクタが自動で開放してくれない。
    #何度も使ううちにメモリにたまり続けるので、ここでメモリをリセットしないといけない。
    #Blender特有
    bm.free()
    return ngon_indices

def select_ngons_in_editmode(obj):
    """指定のオブジェクトを編集モードにしてNgonnだけを選択状態にする"""
    # オブジェクトを編集モードに切り替える
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode='EDIT')

    bm = bmesh.from_edit_mesh(obj.data)
    bm.faces.ensure_lookup_table()

    for f in bm.faces:
        f.select = False  # すべての面を非選択状態にする

    for e in bm.edge:
        e.select = False  # すべての辺を非選択状態にする
    
    for v in bm.faces:
        v.select = False

    for f in bm.faces:
        if len(f.verts) > 4:
            f.select = True  # Ngonの面を選択状態にする

    bmesh.update_edit_mesh(obj.data)  # 編集モードのメッシュを更新する

#   実行部分
obj = bpy.context.active_object

if obj and obj.type == 'MESH' and find_ngons(obj):
    select_ngons_in_editmode(obj)
