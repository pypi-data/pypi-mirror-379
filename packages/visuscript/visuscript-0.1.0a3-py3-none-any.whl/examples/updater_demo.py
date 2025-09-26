"""An example that demonstrates Updaters."""

from visuscript import *

with Scene() as s:
    circle = (
        Circle(20)
        .add_child(Rect(10, 10).set_fill("green").set_stroke("green"))
        .set_stroke("blue")
    )
    rectangle = (
        Rect(40, 40)
        .translate(*s.ushape.bottom_left + [20, -40])
        .set_stroke("red")
        .add_child(Text("E"))
    )

    crosshair = (
        Drawing(Path().M(0, -5).L(0, 5).M(-5, 0).L(5, 0))
        .set_anchor(Anchor.CENTER)
        .set_opacity(0.5)
    )

    for color, (xp, yp) in zip(
        ["red", "blue", "green", "yellow"],
        [(0.25, 0.25), (0.25, 0.75), (0.75, 0.25), (0.75, 0.75)],
    ):
        s << Rect(10, 10).translate(*s.xy(xp, yp)).set_fill(color)

    s << [rectangle, circle, crosshair]

    s.updaters << TranslationUpdater(
        rectangle.transform, circle.transform, max_speed=300, acceleration=200
    )
    s.updaters << TranslationUpdater(s.transform, circle.transform, acceleration=500)
    s.updaters << TranslationUpdater(crosshair.transform, s.transform)

    s.animations << sequence(
        animate_path(
            circle.transform,
            Path()
            .M(*circle.ushape.center)
            .Q(*(s.ushape.center + s.ushape.right) / 2 + UP * 80, *s.ushape.right)
            .Q(*s.ushape.center + DOWN * 80, *s.ushape.left)
            .L(*s.ushape.top_left)
            .l(120, 0)
            .l(150, 80)
            .L(*s.ushape.bottom_right)
            .Q(
                *(s.ushape.bottom_right + s.ushape.center) / 2 + UP * 50 + RIGHT * 50,
                *s.ushape.center,
            ),
            duration=7,
            easing_function=easing.linear_easing,
        ),
        wait(),
    )
