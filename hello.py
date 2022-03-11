from manim import*

class Hello(Scene):
    def construct(self):
        a = Tex('Hello World!')
        self.play(Write(a))