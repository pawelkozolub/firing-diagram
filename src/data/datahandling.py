import json
from pathlib import Path
from data.dataset import DataSet


def read_input(file_path: Path) -> list:
    """Retrieves input data file location. Returns a list with input file paths."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        file_paths = []
        for filename in data['filenames']:
            file_paths.append(Path(data['input_dir'], filename + '.json'))
        return file_paths
    except IOError as err:
        print('\nError: Cannot read input_data.json file.\n', err)
        raise


def read_data(file_path: Path) -> dict:
    """Retrieves input data from input data file used for a graph creation. 
    Returns a dictionary with input data for graph preparation containing:
    - setname
    - points
    - lines
    - sections
    - axes settings

    If no file is found, returns None and skips file to next one.
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except:
        print(f'\nWarning: Cannot read data from file \'{file_path}\'. File skipped...\n')
        return None


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