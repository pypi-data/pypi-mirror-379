from decimal import Decimal

from src.vector_tompy.line2 import Line2
from src.vector_tompy.vector2 import Vector2, Vector2Injector


class Area2:

    def __init__(self, width: Decimal, height: Decimal) -> None:
        self._width: Decimal = width
        self._height: Decimal = height

    @property
    def width(self) -> Decimal:
        return self._width

    @property
    def height(self) -> Decimal:
        return self._height

    @property
    def area(self) -> Decimal:
        return self.width * self.height


def points_in_cone(points: list[Vector2], peak: Vector2, cut: Line2) -> list[Vector2]:
    # TODO: create "Cone" class from peak Vector2 and cut Line2
    points_in_cone_: list[Vector2] = []

    for point in points:
        local_point: Vector2 = point.global_to_local(basis=peak)
        local_start: Vector2 = cut.point0.global_to_local(basis=peak)
        local_end: Vector2 = cut.point1.global_to_local(basis=peak)

        is_point_left_of_right_segment: bool = local_point.cross(other=local_start) > 0.0
        is_point_right_of_left_segment: bool = local_point.cross(other=local_end) < 0.0
        is_point_inside_cone: bool = is_point_left_of_right_segment and is_point_right_of_left_segment

        if is_point_inside_cone:
            points_in_cone_.append(point)

    return points_in_cone_
