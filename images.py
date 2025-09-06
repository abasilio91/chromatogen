def plot_first_xaxis_curve(ax, xdata, ydata, xlabel, ylabel, color):
    ax.plot(xdata, ydata, '-', color=color, label=ylabel)
    ax.set_ylabel(ylabel, color=color, fontweight='bold')
    ax.tick_params('y', colors=color)
    ax.set_xlabel(xlabel, fontweight='bold')
    ax.set_xlim(left=-1, right=max(xdata)*1.01)
    ax.tick_params(axis='both', labelsize=16)
    ax.set_ylabel(ax.get_ylabel(), fontsize=18)
    ax.set_xlabel(ax.get_xlabel(), fontsize=18)

def plot_second_xaxis_curve(ax, xdata, ydata, ylabel, color):
    ax2 = ax.twinx()
    ax2.plot(xdata, ydata, '--', color=color, label=ylabel)
    ax2.set_ylabel(ylabel, color=color, fontweight='bold')
    ax2.tick_params('y', colors=color)
    ax2.set_ylim(bottom=-5, top=105)
    ax2.tick_params(axis='both', labelsize=16)
    ax2.set_ylabel(ax2.get_ylabel(), fontsize=18)

def add_fraction_ticks(ax, xdata, ydata, ymin, color):
    for event, label in zip(xdata, ydata):
        ax.axvline(x=event, color=color, linestyle='-', ymax=0.05)
        ax.text(event, min(ymin), label, color=color, rotation=90, va='bottom',fontsize=12)