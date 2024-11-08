from data.point import Point
from data.line import Line
from data.section import Section

class DataSet:
    "Class that aggregates data retrieved from an input file."
    def __init__(self, data: dict) -> None:
        self._setname = data['setname']
        self._settings = data['settings']
        self._points = []
        self._lines = []
        self._sections = []
        self._update_points(data['points'])
        self._update_lines(data['lines'], self.settings)
        self._update_sections(data['sections'], self.points)

    def _update_points(self, points: list) -> None:
        for point in points:
            self._points.append(Point(point))

    def _update_lines(self, lines: list, settings: list) -> None:
        for line in lines:
            self._lines.append(Line(line, settings))

    def _update_sections(self, sections: list, points: list) -> None:
        for section in sections:
            label = section['label'].split('-', 1)
            section_begin = self._find_point_by_label(label[0])
            section_end = self._find_point_by_label(label[1])
            self._sections.append(Section(section, section_begin, section_end))

    def _find_point_by_label(self, label: str) -> Point:
        for point in self.points:
            if point.label == label:
                return point
        return None

    @property
    def setname(self) -> str:
        return self._setname
    
    @property
    def settings(self) -> list:
        return self._settings
    
    @property
    def points(self) -> Point:
        return self._points
    
    @property
    def lines(self) -> Line:
        return self._lines
    
    @property
    def sections(self) -> Section:
        return self._sections