import pyray as pr

from iterable_tompy.exceptions import EmptyIterableError
from iterable_tompy.head import head


def pr_draw_concave_polygon(points: list[pr.Vector3], color: pr.Color, is_ordered: bool = True) -> None:
    if not is_ordered:
        # TODO: Order points anti-clockwise based on centroid point
        #       derive centroid from points list
        #       find normal vector or up vector from centroid point
        #       imagine sweeping cylinder around normal vector at centroid
        #       sort points list based on rotation angle in cylinder
        pass

    try:
        start = head(points)
        for point0, point1 in zip(points[1:-1], points[2:]):
            pr.draw_triangle_3d(start, point0, point1, color)
    except EmptyIterableError:
        pass
