from decimal import Decimal

from angle_tompy.angle_decimal import Angle

from .line2 import Line2
from .vector2 import Vector2


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
        # TODO: include check for whether point is inside/outside cone "cap/end/top" line
        #       by checking whether point is closer than line intersection point
        is_point_inside_cone: bool = is_point_left_of_right_segment and is_point_right_of_left_segment

        if is_point_inside_cone:
            points_in_cone_.append(point)

    return points_in_cone_


def is_inside_cone(apex_to_axis_point: Line2, other: Vector2, sweep: Angle) -> bool:
    half_sweep: Angle = sweep / 2
    right_sweep: Vector2 = apex_to_axis_point.point1.revolve(angle=-half_sweep, basis=apex_to_axis_point.point0)
    left_sweep: Vector2 = apex_to_axis_point.point1.revolve(angle=half_sweep, basis=apex_to_axis_point.point0)
    local_other: Vector2 = other.global_to_local(basis=apex_to_axis_point.point0)
    local_right: Vector2 = right_sweep.global_to_local(basis=apex_to_axis_point.point0)
    local_left: Vector2 = left_sweep.global_to_local(basis=apex_to_axis_point.point0)
    is_point_to_left_of_right_sweep: bool = local_right.cross(other=local_other) > 0.0
    is_point_to_right_of_left_sweep: bool = local_left.cross(other=local_other) < 0.0
    is_point_in_cone: bool = is_point_to_left_of_right_sweep and is_point_to_right_of_left_sweep
    return is_point_in_cone


def is_inside_n_gon_margin(point: Vector2, edges: list[Line2], margin: Decimal) -> bool:
    # This assumes that the point is already known to be inside the polygon.

    edge_distances: list[Decimal] = [edge.perpendicular_distance(point=point)
                                     for edge in edges]

    is_all_distances_inside_margin: bool = any(distance <= margin for distance in edge_distances)

    return is_all_distances_inside_margin
