from manim import *

class MatrixVectorMultiplication(Scene):
    def construct(self):
        # Define the matrix and vector
        matrix = MathTex(r"\begin{bmatrix} 2 & 0 \\ 0 & 1 \end{bmatrix}")
        vector = MathTex(r"\begin{bmatrix} 1 \\ 1 \end{bmatrix}")
        equals = MathTex("=")
        result = MathTex(r"\begin{bmatrix} 2 \\ 1 \end{bmatrix}")

        # Arrange the components
        equation = VGroup(matrix, vector, equals, result).arrange(RIGHT)

        # Add equation to the scene
        self.play(Write(equation))

        # Explain multiplication process
        arrow = Arrow(start=LEFT, end=RIGHT).next_to(vector, UP)
        self.play(Create(arrow))
        self.wait(1)

        # Animate the transformation
        self.play(Transform(vector, result))
        self.wait(1)

        # Show geometrical interpretation
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            axis_config={"include_numbers": True},
        ).shift(2 * DOWN)
        self.play(Create(axes))

        # Add original and transformed vectors
        original_vector = Vector([1, 1], color=BLUE).shift(2 * DOWN)
        transformed_vector = Vector([2, 1], color=GREEN).shift(2 * DOWN)

        self.play(GrowArrow(original_vector))
        self.play(Transform(original_vector, transformed_vector))
        self.wait(2)
