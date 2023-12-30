class GraphData:
    def __init__(self, data: dict) -> None:
        self._setname = data['setname']
        self._points = data['points']
        self._lines = data['lines']

    @property
    def setname(self) -> str:
        return self._setname
    
    @property
    def points(self) -> list:
        return self._points
    
    @property
    def lines(self) -> list:
        return self._lines