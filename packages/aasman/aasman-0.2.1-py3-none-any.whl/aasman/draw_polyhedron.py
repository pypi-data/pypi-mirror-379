from manim import *

def draw_polyhedron(scene, points, edges, labels=True, dot_color=RED, line_color=BLUE):
    """
    Vẽ khối đa diện 3D bằng Manim
    
    scene  : ThreeDScene đang hoạt động
    points : dict, ví dụ {"A": [0,0,0], "B": [2,0,0], "C": [0,2,0], "S": [0,0,3]}
    edges  : list, các cạnh nối 2 điểm, ví dụ [("A","B"),("B","C"),("C","A"),("S","A"),("S","B"),("S","C")]
    labels : bool, có vẽ nhãn tên điểm không
    dot_color : màu chấm điểm
    line_color: màu cạnh
    """

    # Tạo Dot cho mỗi điểm
    dots = {name: Dot3D(np.array(coord), color=dot_color) for name, coord in points.items()}

    # Tạo nhãn
    if labels:
        texts = {name: Text(name).scale(0.5).next_to(dots[name], OUT) for name in points}
    else:
        texts = {}

    # Tạo cạnh
    lines = [Line3D(dots[a].get_center(), dots[b].get_center(), color=line_color) for a, b in edges]

    # Add tất cả vào scene
    scene.add(*dots.values(), *texts.values(), *lines)