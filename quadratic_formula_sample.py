from manim import *

class Test(Scene):
    def construct(self):
        equation1 = MathTex(r"\therefore",r"\text{When }",r"ax^2 + bx + c = 0").to_edge(UP, buff = 3)
        equation13 = MathTex(r"x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}").move_to(DOWN)
        self.play(Write(equation1), Write(equation13), run_time = 2)
        self.wait()