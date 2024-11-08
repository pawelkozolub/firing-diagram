class Line:
    """Definition of a line data."""
    def __init__(self, line: dict, axes: list) -> None:
        self._label = line['label']
        self._lhv = line['lhv']
        self._x = []
        self._y = []
        self._update_line(axes)
        self._label_offset_x = line['label_offset_x']
        self._label_offset_y = line['label_offset_y']

    def _update_line(self, axes: list) -> None:
        for axis in axes:
            if axis['label'] == 'y_axis':
                y_min = axis['y_min']
                y_max = axis['y_max']

                self._x.append(y_min / self._lhv * 3.6)
                self._x.append(y_max / self._lhv * 3.6)

                self._y.append(y_min)
                self._y.append(y_max)

    @property
    def label(self) -> str:
        return self._label
    
    @property
    def lhv(self) -> float:
        return self._lhv
    
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