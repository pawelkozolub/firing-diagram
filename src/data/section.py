from data.point import Point


class Section:
    """Definition of a section data."""
    def __init__(self, section: dict, section_begin: Point, section_end: Point) -> None:
        self._label = section['label']
        self._color = section['color']
        self._style = section['style']
        self._x = []
        self._y = []
        self._update_section_by_point(section_begin)
        self._update_section_by_point(section_end)

    def _update_section_by_point(self, point: Point) -> None:
        self._x.append(point.x)
        self._y.append(point.y)

    @property
    def label(self) -> str:
        return self._label
    
    @property
    def color(self) -> str:
        return self._color
    
    @property
    def style(self) -> str:
        return self._style
    
    @property
    def x(self) -> float:
        return self._x
    
    @property
    def y(self) -> float:
        return self._y