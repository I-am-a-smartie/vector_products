from manim import*

class twod(Scene):
    def construct(self):
        q1 = Tex('2D plane', font_size=72)
        q1.to_corner(UL)
        vectorplane = NumberPlane()
        origin1 = Dot(ORIGIN)
        p1 = Dot([0, 1, 0])
        p1_label = Tex('(0, 1)').next_to(p1, UP)
        origin_label = Tex('(0, 0)').next_to(origin1, UR)
        x = Dot([7,0,0])
        y = Dot([0,4,0])
        x_label = MathTex('x').next_to(x, DOWN, buff=0.2)
        y_label = MathTex('y').next_to(y, DR*0.5)
        self.add(vectorplane, origin1, p1, p1_label, origin_label, x_label, y_label)

class threed(ThreeDScene):
    def construct(self):
        ax = ThreeDAxes()
        self.set_camera_orientation(phi= 2 * PI / 5, theta=-PI / 4)
        x_axis = ax.get_x_axis_label(Tex("$z$-axis"))
        y_axis = ax.get_y_axis_label(Tex("$z$-axis"))
        z_axis = ax.get_z_axis_label(Tex("$z$-axis"))
        self.add(ax, z_axis, x_axis, y_axis)



