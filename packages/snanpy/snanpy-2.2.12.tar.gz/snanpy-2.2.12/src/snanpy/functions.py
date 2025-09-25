from matplotlib import pyplot as plt
import matplotlib as mpl

mpl.rcParams.update(mpl.rcParamsDefault)
plt.rcParams.update({'font.size': 19})
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

def figax(figsize=(8,6), xlim=None, ylim=None, xlabel=None, ylabel=None, title=None):
    fig, ax = plt.subplots(figsize=figsize, dpi=200, constrained_layout=True)
    ax.grid(linewidth=0.5) 
    if xlim is not None:
        ax.set_xlim(xlim)  
    if ylim is not None:
        ax.set_ylim(ylim) 
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel) 

    return fig, ax
