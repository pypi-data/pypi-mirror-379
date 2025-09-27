from manim import *

class _BillboardText(VGroup):
    def __init__(self, text, point, scene, scale=0.5, buff=0.2, **kwargs):
        super().__init__()
        self.text = Text(text, **kwargs).scale(scale)
        self.point = point
        self.scene = scene
        self.buff = buff
        self.add(self.text)

        self.text.add_updater(self._update_text)

    def _update_text(self, mobj):
        pos = self.point.get_center() + self.buff * OUT
        mobj.move_to(pos)

        # Reset rotation để luôn đối diện camera
        mobj.set_orientation(np.array([0, 0, 1]))  # mặt chữ hướng ra ngoài
        mobj.rotate(-self.scene.camera.theta, axis=OUT)
        mobj.rotate(-self.scene.camera.phi, axis=RIGHT)
        return mobj
    
def draw_polyhedron(scene, points, edges, labels=True, dot_color=RED, line_color=BLUE, billboard=False):
    # Tạo Dot cho mỗi điểm
    dots = {name: Dot3D(np.array(coord), color=dot_color) for name, coord in points.items()}

    texts = {}
    if labels:
        for name, dot in dots.items():
            if billboard:
                texts[name] = _BillboardText(name, dot, scene, scale=0.5)
            else:
                texts[name] = Text(name).scale(0.5).next_to(dot, OUT)

    # Tạo cạnh
    lines = [Line3D(dots[a].get_center(), dots[b].get_center(), color=line_color) for a, b in edges]

    scene.add(*dots.values(), *texts.values(), *lines)