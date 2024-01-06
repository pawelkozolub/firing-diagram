import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from data.dataset import DataSet


OUTPUT_DIR = 'output/'
FIG_EXT = '.png'


def graph(data: DataSet, fig_name: str) -> None:
    """Create graph/plot function from data provided."""
    plt.rcParams['figure.figsize'] = [7.50, 5.00]
    plt.rcParams['figure.autolayout'] = True
    plt.title('Firing diagram: ' + data.setname)

    # Adjusting x-axis
    plt.xlabel('Fuel Flow, t/h')
    x_min = data.axes[0]['x_min']
    x_max = data.axes[0]['x_max']
    x_step = data.axes[0]['x_step']   
    plt.xticks(np.arange(x_min, x_max, x_step))
    plt.xlim([x_min, x_max])
    
    # Adjusting y-axis
    plt.ylabel('Heat Input, MW')
    y_min = data.axes[1]['y_min']
    y_max = data.axes[1]['y_max']
    y_step = data.axes[1]['y_step'] 
    plt.yticks(np.arange(y_min, y_max, y_step))
    plt.ylim([y_min, y_max])

    # Plotting data for lines
    x_offset = -1.5
    y_offset = -y_step    
    for line in data.lines:
        plt.plot(
            line.x, 
            line.y, 
            linestyle='--', linewidth=1.0, color='steelblue', alpha=0.5)   

        plt.text(
            line.x[1] + x_offset, 
            line.y[1] + y_offset, 
            line.label, fontdict={'color':'steelblue'})

    # Plotting data for sections
    for section in data.sections:
        plt.plot(
            section.x, 
            section.y, 
            linestyle=section.style, linewidth=2.0, color=section.color, alpha=1.0) 
    
    # Plotting data for points
    x_offset = -1.5
    y_offset = 1.5
    for point in data.points:
        plt.plot(
            point.x, 
            point.y, 
            marker='o', markersize=5, linewidth=0, color='k')
        plt.text(point.x + x_offset, point.y + y_offset, point.label)

    # Showing plot in external window
    # plt.show()
        
    # Saving plot to file
    fig_to_save = Path(OUTPUT_DIR + fig_name + FIG_EXT)
    plt.savefig(fig_to_save)
    print('\n' + str(fig_to_save) + ' ...Saved')
    plt.close()