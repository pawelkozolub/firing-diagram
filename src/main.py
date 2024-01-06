from pathlib import Path
from data.datahandling import read_input, read_data, print_data
from graph.graph import graph
from data.dataset import DataSet


def main():
    """Main file to run the script."""    
    inputs = read_input(Path('src/input_data.json'))
    for input in inputs:
        graph_data = read_data(input)
        if graph_data != None:
            data_set = DataSet(graph_data)
            print_data(data_set)
            graph(data_set, input.stem)


if __name__ == '__main__':
    main()