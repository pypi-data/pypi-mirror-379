from visuscript.mixins import (
    Drawable,
    ShapeMixin,
    FillMixin,
    StrokeMixin,
    OpacityMixin,
    Color,
)
from visuscript.primatives.protocols import HasShape
from visuscript.segment import Path
from visuscript.drawable import Drawing, Pivot
from visuscript.primatives import Vec2
from visuscript.constants import LineTarget
from visuscript.config import ConfigurationDeference, DEFER_TO_CONFIG, config
from visuscript.math_utility import magnitude
from visuscript.animation import (
    fade_in,
    fade_out,
    sequence,
    bundle,
    run,
    Animation,
)

from abc import abstractmethod
from typing import Tuple, Callable, Iterable
import itertools

__all__ = [
    "Connector",
    "Line",
    "Arrow",
    "Edges",
]


class Connector(Drawable, ShapeMixin, FillMixin, StrokeMixin, OpacityMixin):
    """A connector visually connects one object to another or one location to another."""

    POSITIVE = 1
    NEGATIVE = -1

    def __init__(
        self,
        *,
        source: Vec2 | HasShape,
        destination: Vec2 | HasShape,
        source_target: LineTarget = LineTarget.RADIAL,
        destination_target: LineTarget = LineTarget.RADIAL,
    ):
        super().__init__()
        if isinstance(source, Vec2):
            source = Pivot().translate(source)
        if isinstance(destination, Vec2):
            destination = Pivot().translate(destination)
        self._source: HasShape = source
        self._destination: HasShape = destination

        self._source_target = source_target
        self._destination_target = destination_target

    def calculate_height(self) -> float:
        return abs(self._destination.shape.center[1] - self._source.shape.center[1])

    def calculate_width(self) -> float:
        return abs(self._destination.shape.center[0] - self._source.shape.center[0])

    def calculate_top_left(self) -> Vec2:
        return Vec2(
            min(
                self._destination.shape.center[0],
                self._source.shape.center[0],
            ),
            min(
                self._destination.shape.center[1],
                self._source.shape.center[1],
            ),
        )

    @property
    def _unit_between(self) -> Vec2:
        diff = self._destination.shape.center - self._source.shape.center
        eps = 1e-16
        return diff / max(magnitude(diff), eps)

    def _get_vec2(self, element: HasShape, target: LineTarget, offset_sign: int):
        if target == LineTarget.CENTER:
            return element.shape.center
        elif target == LineTarget.RADIAL:
            center = element.shape.center
            return (
                center
                + offset_sign * element.shape.circumscribed_radius * self._unit_between
            )

    @property
    def source(self) -> Vec2:
        """The (x,y) source for this Connector, updated to the source's global Shape."""
        return self._get_vec2(self._source, self._source_target, Line.POSITIVE)

    @property
    def destination(self) -> Vec2:
        """The (x,y) destination for this Connector, updated to the destination's global Shape."""
        return self._get_vec2(
            self._destination, self._destination_target, Line.NEGATIVE
        )

    @property
    def overlapped(self) -> bool:
        """True if and only if the source and destination are overlapped."""
        distance = 0
        if self._source_target == LineTarget.RADIAL:
            distance += self._source.shape.circumscribed_radius
        if self._destination_target == LineTarget.RADIAL:
            distance += self._destination.shape.circumscribed_radius

        return (
            magnitude(self._destination.shape.center - self._source.shape.center)
            < distance
        )

    def draw(self):
        return self.get_connector(
            source=self.source,
            destination=self.destination,
            stroke=self.stroke,
            stroke_width=self.stroke_width,
            fill=self.fill,
            opacity=self.opacity,
            overlapped=self.overlapped,
        ).draw()

    @abstractmethod
    def get_connector(
        self,
        source: Vec2,
        destination: Vec2,
        stroke: Color,
        stroke_width: float,
        fill: Color,
        opacity: float,
        overlapped: bool,
    ) -> Drawable:
        """Returns a drawable connector from source to destination"""
        ...


class Line(Connector):
    """A Line is a straight-line :class:`Connector`."""

    def get_connector(
        self,
        source: Vec2,
        destination: Vec2,
        stroke: Color,
        stroke_width: float,
        fill: Color,
        opacity: float,
        overlapped: bool,
    ) -> Drawing:
        return (
            Drawing(Path().M(*source).L(*destination))
            .set_stroke(stroke)
            .set_stroke_width(stroke_width)
            .set_fill(fill)
            .set_opacity(0.0 if overlapped else opacity)
        )


class Arrow(Connector):
    """An Arrow is a straight-line :class:`Connector` with an optional arrowhead on either side."""

    def __init__(
        self,
        *,
        start_size: float = 0,
        end_size: float | ConfigurationDeference = DEFER_TO_CONFIG,
        source: Vec2 | HasShape,
        destination: Vec2 | HasShape,
        source_target: LineTarget = LineTarget.RADIAL,
        destination_target: LineTarget = LineTarget.RADIAL,
    ):
        super().__init__(
            source=source,
            destination=destination,
            source_target=source_target,
            destination_target=destination_target,
        )
        self._start_size = start_size
        self._end_size = (
            config.element_stroke_width * 5
            if isinstance(end_size, ConfigurationDeference)
            else end_size
        )

    def get_connector(
        self,
        source: Vec2,
        destination: Vec2,
        stroke: Color,
        stroke_width: float,
        fill: Color,
        opacity: float,
        overlapped: bool,
    ) -> Drawing:
        unit = self._unit_between
        diff = destination - source
        dist = max(magnitude(diff), 1e-16)
        unit = diff / dist
        ortho = Vec2(-unit.y, unit.x)

        line_start = source + unit * self._start_size
        line_end = source + unit * (dist - self._end_size)

        return (
            Drawing(
                (
                    Path()
                    .M(*source)
                    .L(*(line_start - ortho * self._start_size / 2))
                    .M(*source)
                    .L(*(line_start + ortho * self._start_size / 2))
                    .L(*line_start)
                    .L(*line_start)
                    .L(*line_end)
                    .L(*(line_end + ortho * self._end_size / 2))
                    .L(*(source + unit * dist))
                    .L(*(line_end - ortho * self._end_size / 2))
                    .L(*line_end)
                ),
            )
            .set_stroke(stroke)
            .set_stroke_width(stroke_width)
            .set_fill(fill)
            .set_opacity(0.0 if overlapped else opacity)
        )


class ElementsAlreadyConnectedError(ValueError):
    pass


class ElementsNotConnectedError(ValueError):
    pass


class Edges(Drawable):
    """A collection of :class:`Line` objects that are drawn to connect specified objects."""

    def __init__(self):
        super().__init__()
        self._edges: dict[Tuple[HasShape, HasShape], Line] = dict()
        self._fading_away: set[Line] = set()

    def connect_by_rule(
        self,
        rule: Callable[[HasShape, HasShape], bool],
        elements: Iterable[HasShape],
        duration: float | ConfigurationDeference = DEFER_TO_CONFIG,
    ) -> Animation:
        """Connects every pair of input elements that satisfy a rule,
        disconnecting those that break the rule.

        :param rule: A function that takes two objects and returns True if they are to be
            connected and False otherwise.
        :param elements: The group of objects from which pairs will be taken.
        :return: An Animation fading in/out all of the edges
        """
        a_bundle = bundle()

        for e1, e2 in itertools.combinations(elements, 2):
            should_be_connected = rule(e1, e2)
            if should_be_connected and not self.connected(e1, e2):
                a_bundle.push(self.connect(e1, e2, duration=duration))
            elif self.connected(e1, e2) and not should_be_connected:
                a_bundle.push(self.disconnect(e1, e2, duration=duration))

        return a_bundle

    def get_edge(self, element1: HasShape, element2: HasShape) -> Connector:
        """Gets the :class:`Connector` connecting two objects."""
        if not self.connected(element1, element2):
            raise ElementsNotConnectedError(
                f"Elements {element1} and {element2} are not connected"
            )
        return (
            self._edges.get((element1, element2)) or self._edges[(element2, element1)]
        )

    def connected(self, element1: HasShape, element2: HasShape) -> bool:
        """Returns whether two objects are connected."""
        return (element1, element2) in self._edges or (
            element2,
            element1,
        ) in self._edges

    def connect(
        self,
        element1: HasShape,
        element2: HasShape,
        *,
        duration: float | ConfigurationDeference = DEFER_TO_CONFIG,
    ) -> Animation:
        """Connects two objects and returns an animation fading in the connecting edge."""
        if self.connected(element1, element2):
            raise ElementsAlreadyConnectedError(
                f"Elements {element1} and {element2} are already connected"
            )
        if element1 is element2:
            raise ValueError("Cannot connect an element to itself")

        edge = Line(source=element1, destination=element2).set_opacity(0.0)
        self._edges[(element1, element2)] = edge

        return fade_in(edge, duration=duration)

    def disconnect(
        self,
        element1: HasShape,
        element2: HasShape,
        *,
        duration: float | ConfigurationDeference = DEFER_TO_CONFIG,
    ) -> Animation:
        """Disconnects two objects and returns an animation fading out th eedge that had connected them."""
        if not self.connected(element1, element2):
            raise ElementsNotConnectedError(
                f"Elements {element1} and {element2} are not connected"
            )
        if (element1, element2) in self._edges:
            edge = self._edges.pop((element1, element2))
        else:
            edge = self._edges.pop((element2, element1))

        self._fading_away.add(edge)

        return sequence(
            fade_out(edge, duration=duration),
            run(self._fading_away.remove, edge),
        )

    def draw(self):
        drawing = ""
        for edge in self._edges.values():
            drawing += edge.draw()
        for edge in self._fading_away:
            drawing += edge.draw()
        return drawing

    def lines_iter(self) -> Iterable[Tuple[Vec2, Vec2]]:
        yield from map(lambda x: (x.source, x.destination), self._edges.values())
