from manim import *

def draw_polyhedron(scene, points, edges, labels=True, dot_color=RED, line_color=BLUE, billboard=False):
    """
    Vẽ khối đa diện 3D với tùy chọn nhãn chữ luôn hướng màn hình (billboard).
    
    scene     : ThreeDScene
    points    : dict {"A": [x,y,z], ...}
    edges     : list [("A","B"),("B","C"),...]
    labels    : bool, có vẽ nhãn tên điểm không
    dot_color : màu chấm điểm
    line_color: màu cạnh
    billboard : bool, nếu True thì chữ luôn hướng camera
    """

    # Tạo Dot cho mỗi điểm
    dots = {name: Dot3D(np.array(coord), color=dot_color) for name, coord in points.items()}

    texts = {}
    if labels:
        for name, dot in dots.items():
            t = Text(name).scale(0.5).next_to(dot, OUT)

            if billboard:  
                # updater để chữ luôn hướng camera
                t.add_updater(lambda m, dot=dot: m.move_to(
                    scene.camera.project_point(dot.get_center())
                ))
            texts[name] = t

    # Tạo cạnh
    lines = [Line3D(dots[a].get_center(), dots[b].get_center(), color=line_color) for a, b in edges]

    # Add tất cả vào scene
    scene.add(*dots.values(), *texts.values(), *lines)