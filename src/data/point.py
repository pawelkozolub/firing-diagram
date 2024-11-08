class Point:
    """Definition of a point data."""
    def __init__(self, point: dict) -> None:
        self._label = point['label']
        self._x = point['x']
        self._y = point['y']
        self._label_offset_x = point['label_offset_x']
        self._label_offset_y = point['label_offset_y']

    @property
    def label(self) -> str:
        return self._label
    
    @property
    def x(self) -> float:
        return self._x
    
    @property
    def y(self) -> float:
        return self._y
    
    @property
    def label_offset_x(self) -> float:
        return self._label_offset_x
    
    @property
    def label_offset_y(self) -> float:
        return self._label_offset_y