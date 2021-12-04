from manim import*

class Vector(Scene):
    def construct(self):
        q1 = Tex('Base vectors', font_size=72)
        q1.to_corner(UL)
        vectorplane = NumberPlane()
        origin1 = Dot(ORIGIN)
        self.add(q1, vectorplane)
        self.play(Write(origin1))
        vec1 = Arrow(ORIGIN, [1, 0, 0], buff=0)
        vec2 = Arrow(ORIGIN, [0, 1, 0], buff=0)
        vec1_text = MathTex("\hat{i}").next_to(vec1.get_edge_center(RIGHT))
        vec2_text = MathTex("\hat{j}").next_to(vec2.get_edge_center(LEFT))
        self.play(GrowFromCenter(vec1), Write(vec1_text))
        self.wait()
        self.play(GrowFromCenter(vec2), Write(vec2_text))
        self.wait(6)
        self.remove(vec1, vec2, vec2_text, vec1_text)

        q2 = Tex('Vector', font_size=72)
        q2.to_corner(UL)
        self.play(ReplacementTransform(q1, q2))
        origin2 = Dot(ORIGIN)
        vec3 = Arrow(ORIGIN, [2, 2, 0], buff=0)
        self.play(Write(origin2))
        self.play(ReplacementTransform(origin2, vec3))

        origin_text = Tex("(0, 0)").next_to(ORIGIN, DOWN)
        point3_text = Tex("(2, 2)").next_to(vec3.get_end(), UR)

        #vec3_text = MathTex('2\hat{i} + 2\hat{j}').next_to(vec3.get_edge_center(RIGHT), buff = 0)
        #make vec3text curly bracket point to 2i+2j
        self.play(Write(origin_text), Write(point3_text))
        self.wait(2)

        line1 = Line(ORIGIN, [2,0,0], buff=0).set_color(ORANGE)
        self.play(ReplacementTransform(origin2.copy(), line1))
        line1_text = MathTex('2\hat{i}', font_size=50).next_to(line1.get_center(), DR)
        self.play(FadeIn(line1_text))
        self.wait(3)

        line2 = Line([2, 0, 0], [2, 2, 0], buff=0).set_color(ORANGE)
        self.play(ReplacementTransform(origin2.copy(), line2))
        line2_text = MathTex('2\hat{j}', font_size=50).next_to(line2.get_center(), RIGHT)
        self.play(FadeIn(line2_text))
        self.wait(3)

        b3 = Brace(vec3, direction=vec3.copy().rotate(PI / 2).get_unit_vector())
        b3_text = b3.get_tex(r'\vec{v} = 2\hat{i} + 2\hat{j}')
        self.play(Write(b3), Write(b3_text))

        self.wait(2)

        self.remove(line1_text, line2_text)
        q3 = Tex('Resolution of Vector').to_corner(UL)
        self.play(ReplacementTransform(q2, q3))
        self.wait(2)

        line3 = Line(ORIGIN, [2,0,0], buff=0)
        a1 = Angle(vec3, line3, radius=0.4, quadrant=(1, 1), other_angle=True)
        a1_name = MathTex(r'\theta', font_size=45).next_to(a1, RIGHT)
        self.play(Write(a1), Write(a1_name))
        self.wait(2)

        line1_label = MathTex(r'vcos\theta', font_size=40).next_to(origin_text, RIGHT*1)
        self.play(Write(line1_label))

        line2_label = MathTex(r'vsin\theta').next_to(line2.get_center(), RIGHT)
        self.play(Write(line2_label))
        self.wait(4)

        rec_explain = Rectangle(color='#000000', width=4.5, height=2, fill_opacity=1).to_corner(DR)
        calc1 = MathTex(r'v = |\vec{v}|').move_to(rec_explain.get_center())
        calc2 = MathTex(r'v = \sqrt{ {v_x}^2 + {v_y}^2}').move_to(rec_explain.get_center())
        calc3 = MathTex(r'v = \sqrt{ 2^2 + 2^2}').move_to(rec_explain.get_center())
        calc4 = MathTex(r'v = 2\sqrt{2}').move_to(rec_explain.get_center())
        self.add(rec_explain)
        self.play(Write(calc1))
        self.wait(4)
        self.play(ReplacementTransform(calc1, calc2))
        self.wait(4)
        self.play(ReplacementTransform(calc2, calc3))
        self.wait(4)
        self.play(ReplacementTransform(calc3, calc4))
        self.wait(4)

        line1_label2 = MathTex(r'2\sqrt{2}cos\theta', font_size=40).next_to(origin_text, RIGHT*1)
        line2_label2 = MathTex(r'2\sqrt{2}sin\theta').next_to(line2.get_center(), RIGHT)
        self.play(ReplacementTransform(calc4.copy(), line1_label2), Unwrite(line1_label))#remove the text in this one itslef
        self.play(ReplacementTransform(calc4, line2_label2), Unwrite(line2_label), Unwrite(rec_explain))
        self.wait()

class Addition(Scene):
    def construct(self):
        q1 = Tex('Vector Addition', font_size=72)
        q1.to_corner(UL)
        vectorplane = NumberPlane()
        origin1 = Dot(ORIGIN)
        self.add(q1, vectorplane)
        self.play(Write(origin1))
        q2 = Tex('(Triangle)', font_size=50).next_to(q1, DOWN)
        self.play(Write(q2))


        vec1 = Arrow(ORIGIN, [1, 2, 0], buff=0)
        vec2 = Arrow(ORIGIN, [3, 1, 0], buff=0)
        vec3 = Arrow([-3,-1,-1], ORIGIN, buff=0)
        self.play(Write(vec1))
        self.play(Write(vec2))
        self.wait()
        self.play(ReplacementTransform(vec2, vec3))
        vec1_label = MathTex(r'\vec{A}').next_to(vec1.get_center(), RIGHT)
        vec2_label = MathTex(r'\vec{B}').next_to(vec2.get_center(), DOWN)
        self.play(Write(VGroup(vec1_label, vec2_label)))
        self.wait()

        vec4 = Arrow([-3,-1,-1], [1, 2, 0], buff=0)
        self.play(Write(vec4))
        vec4_label = MathTex(r'\vec{C}').next_to(vec4.get_center(), LEFT, buff=0.5)
        self.play(Write(vec4_label))
        self.wait()

        rec_explain = Rectangle(color='#000000', width=4.5, height=2, fill_opacity=1).to_corner(DR)
        calc1 = MathTex(r'\vec{A} + \vec{B} = \vec{C}').move_to(rec_explain.get_center())
        self.play(Write(rec_explain))
        self.play(Write(calc1))
        self.play(Unwrite(VGroup(vec1_label, vec1, vec2, vec2_label, vec3, vec4, vec4_label, rec_explain, calc1, q2)))

        q3 = Tex('(Polygon)', font_size=50).next_to(q1, DOWN)
        self.play(Write(q3))
        vec5 = Arrow(ORIGIN, [1,2,0], buff=0)
        vec6 = Arrow([1,2,0], [3,3,0], buff=0)
        vec7 = Arrow([3,3,0], [5, 2, 0], buff=0)

        self.play(Write(vec5))
        self.wait()
        self.play(Write(vec6))
        self.wait()
        self.play(Write(vec7))
        self.wait(2)

        vec5_label = MathTex(r'\vec{A}').next_to(vec5.get_center(), RIGHT)
        vec6_label = MathTex(r'\vec{B}').next_to(vec6.get_center(), UP)
        vec7_label = MathTex(r'\vec{C}').next_to(vec7.get_center(), UP)
        self.play(Write(vec5_label))
        self.play(Write(vec6_label))
        self.play(Write(vec7_label))

        vec8 = Arrow(ORIGIN, [5, 2, 0], buff=0)
        vec8_label = MathTex(r'\vec{D}').next_to(vec8.get_center(), RIGHT, buff=1)
        self.play(Write(vec8))
        self.play(Write(vec8_label))
        self.wait()

        rec_explain2 = Rectangle(color='#000000', width=4.5, height=2, fill_opacity=1).to_corner(DR)
        self.play(Write(rec_explain2))
        self.wait()
        calc2 = MathTex(r'\vec{A} + \vec{B} + \vec{C} = \vec{D}').move_to(rec_explain2.get_center())
        self.play(Write(calc2))
        self.wait(3)

        q4 = Tex('Vector Subtraction', font_size=72).to_corner(UL)
        remove1 = VGroup(vec7, vec7_label, vec8, vec8_label, rec_explain2, calc2, q3)
        self.play(ReplacementTransform(q1, q4), Unwrite(remove1))
        self.wait(3)

        # vec9 = Arrow([-2, -1, 0], ORIGIN, buff=0)
        # vec9_label = MathTex(r'\vec{B}').move_to(vec9.get_center(), UL)
        # self.play(ReplacementTransform(vec6, vec9), Unwrite(vec6_label))
        # self.play(Write(vec9_label))
        # self.wait(3)

        vec9 = Arrow([3,3,0], [1,2,0], buff=0)
        vec9_label = MathTex(r'-\vec{B}').move_to(vec9.get_center(), UL)
        self.play(ReplacementTransform(vec6, vec9), Unwrite(vec6_label))
        self.play(Write(vec9_label))
        self.wait(3)

        vec10 = Arrow([1, 2, 0], [-1,1,0], buff=0)
        vec10_label = MathTex(r'-\vec{B}').move_to(vec10.get_center(), UP*2)
        self.play(ReplacementTransform(vec9, vec10), ReplacementTransform(vec9_label, vec10_label))
        self.wait()

        vec11 = Arrow(ORIGIN, [-1, 1, 0], buff=0)
        vec11_label = MathTex(r'\vec{C}').move_to(vec11.get_center(), LEFT*3)
        self.play(Write(vec11))
        self.wait()
        self.play(Write(vec11_label))

        rec_explain3 = Rectangle(color='#000000', width=4.5, height=2, fill_opacity=1).to_corner(DR)
        calc3 = MathTex(r'\vec{C} = \vec{A} - \vec{B}').move_to(rec_explain3.get_center())

        self.play(Write(rec_explain3))
        self.play(Write(calc3))


        # vec9_label = MathTex(r'-\vec{B}').move_to(vec9.get_center(), UL)
        # self.play(ReplacementTransform(vec9, vec10), ReplacementTransform(vec9_label, vec10_label))
        # vec9 = Arrow([3,3,0], [1,2,0], buff=0)
        # self.play(ReplacementTransform(vec6, vec9))
        # vec9_label = MathTex(r'-\vec{B}').next_to(vec9.get_center(), UP)
        # self.play(ReplacementTransform(vec6_label, vec9_label))

        #vec5, vec5_label, vec6, vec6_label,
