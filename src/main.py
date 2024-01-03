from pathlib import Path
from data.datahandling import read_data, print_data
from graph.graph import graph
from data.dataset import DataSet

# File localization path
INPUT_DATA_FILE = Path('src/input_data.json')


def main():
    """Main file to run the script."""    
    graph_data = DataSet(read_data(INPUT_DATA_FILE))
    print_data(graph_data)
    graph(graph_data)


if __name__ == '__main__':
    main()