from pathlib import Path
from data.graphdata import GraphData
from data.datahandling import read_data, print_data

# File localization path
INPUT_DATA_FILE = Path('src/input_data.json')


def main():
    """Main file to run the script."""    
    graph_data = GraphData(read_data(INPUT_DATA_FILE))
    print_data(graph_data)


if __name__ == '__main__':
    main()