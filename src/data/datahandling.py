import json
from pathlib import Path
from data.dataset import DataSet


def read_data(file_path: Path) -> dict:
    """Retrieves input data from input data file. Returns dictionary with input data that has been read."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except IOError as err:
        print('Input file error...\n', err)
        raise


def print_data(data: DataSet) -> None:
    """Optional method that prints retrieved data to terminal screen for checking."""
    print(f'\nSetname: {data.setname}')
    
    print('\nPoints:')
    for point in data.points:
        print(f'{point.label}: ({point.x}, {point.y})')

    print('\nLines:')
    for line in data.lines:
        print(f'{line.label}, lhv: {line.lhv}: ({line.x}, {line.y})')

    print('\nSections:')
    for section in data.sections:
        print(f'{section.label}: ({section.x}, {section.y}), color: {section.color}, style: {section.style}')