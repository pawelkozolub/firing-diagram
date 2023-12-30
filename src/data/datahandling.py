import json
from pathlib import Path
from data.graphdata import GraphData


def read_data(file_path: Path) -> dict:
    """Retrieves input data from input data file. Returns dictionary with input data that has been read."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except IOError as err:
        print('Input file error...\n', err)
        raise


def print_data(graph_data: GraphData) -> None:
    """Optional method that prints retrieved data to terminal screen for checking."""
    print(f'\nSetname: {graph_data.setname}')
    
    print('\nPoints:')
    for point in graph_data.points:
        label = point['label']
        x = point['x']
        y = point['y']
        print(f'{label}: ({x}, {y})')

    print('\nLines:')
    for line in graph_data.lines:
        label = line['label']
        x = line['x']
        y = line['y']
        print(f'{label}: ({x}, {y})')