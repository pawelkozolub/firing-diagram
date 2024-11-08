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
    plt.title(data.setname)

    # Adjusting x-axis
    plt.xlabel('Fuel Flow, t/h')
    x_min = data.settings[0]['x_min']
    x_max = data.settings[0]['x_max']
    x_step = data.settings[0]['x_step']   
    plt.xticks(np.arange(x_min, x_max, x_step))
    plt.xlim([x_min, x_max])
    
    # Adjusting y-axis
    plt.ylabel('Heat Input, MW')
    y_min = data.settings[1]['y_min']
    y_max = data.settings[1]['y_max']
    y_step = data.settings[1]['y_step'] 
    plt.yticks(np.arange(y_min, y_max, y_step))
    plt.ylim([y_min, y_max])

    # Plotting data for lines
    color = data.settings[2]['color']
    fontsize = data.settings[2]['fontsize']
    fontweight = 'bold' if data.settings[2]['bold'] == 'yes' else 'normal'   
    for line in data.lines:
        plt.plot(
            line.x, 
            line.y, 
            linestyle='--', linewidth=1.0, color='steelblue', alpha=0.5)   

        plt.text(
            line.x[1] + line.label_offset_x, 
            line.y[1] + line.label_offset_y, 
            line.label, 
            fontdict={'color':color, 'fontsize':fontsize, 'fontweight':fontweight})

    # Plotting data for sections
    for section in data.sections:
        plt.plot(
            section.x, 
            section.y, 
            linestyle=section.style, linewidth=2.0, color=section.color, alpha=1.0) 
    
    # Plotting data for points 
    color = data.settings[3]['color']
    fontsize = data.settings[3]['fontsize']
    fontweight = 'bold' if data.settings[3]['bold'] == 'yes' else 'normal'   
    for point in data.points:
        plt.plot(
            point.x, 
            point.y, 
            marker='o', markersize=5, linewidth=0, color='k')
        plt.text(
            point.x + point.label_offset_x, 
            point.y + point.label_offset_y, 
            point.label,
            fontdict={'color':color, 'fontsize':fontsize, 'fontweight':fontweight})

    # Showing plot in external window
    # plt.show()
        
    # Saving plot to file
    fig_to_save = Path(OUTPUT_DIR + fig_name + FIG_EXT)
    plt.savefig(fig_to_save)
    print('\n' + str(fig_to_save) + ' ...Saved')
    plt.close()