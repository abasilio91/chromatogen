import matplotlib.pyplot as plt
from threading import RLock

_lock = RLock()
plt.rcParams['font.family'] = 'Arial'

def plot_affinity(dataframe) -> plt.Figure:
    x_UV = list(dataframe["UV 1_280 (ml)"])
    y_UV = list(dataframe["UV 1_280 (mAU)"])
    x_ConcB = list(dataframe["Conc B (ml)"])
    y_ConcB = list(dataframe["Conc B (%)"])
    x_Fraction = list(dataframe["Fraction (ml)"])

    if "Fraction (Fraction)" in dataframe.columns:
        y_Fraction = list(dataframe["Fraction (Fraction)"])

    with _lock:
        fig, ax = plt.subplots(figsize=(16, 8), dpi=300)
        fig.patch.set_facecolor('none')

        plot_first_xaxis_curve(ax, 
                               xdata=x_UV, 
                               ydata=y_UV, 
                               xlabel='Volume (mL)', 
                               ylabel='UV 280 nm (mAU)',
                               color='#332288')
        
        if len(set(y_ConcB)) > 1:
            plot_second_xaxis_curve(ax, 
                                    xdata=x_ConcB, 
                                    ydata=y_ConcB, 
                                    ylabel='Buffer B Concentration (%)', 
                                    color="#CC6677")
            
        if "Fraction (Fraction)" in dataframe.columns:
            add_fraction_ticks(ax, 
                               xdata=x_Fraction, 
                               ydata=y_Fraction, 
                               ymin=y_UV, 
                               color='#882255')
    return fig

def plot_desalting(dataframe):
    x_UV = list(dataframe["UV 1_280 (ml)"])
    y_UV = list(dataframe["UV 1_280 (mAU)"])
    x_cond = list(dataframe["Cond (ml)"])
    y_cond = list(dataframe["Cond (mS/cm)"])
    x_Fraction = list(dataframe["Fraction (ml)"])
    x_injection = list(dataframe["Injection (ml)"])
    y_injection = [0, 1]

    if "Fraction (Fraction)" in dataframe.columns:
        y_Fraction = list(dataframe["Fraction (Fraction)"])

    with _lock:
        fig, ax = plt.subplots(figsize=(16, 8), dpi=300)
        fig.patch.set_facecolor('none')

        plot_first_xaxis_curve(ax, 
                               xdata=x_UV, 
                               ydata=y_UV, 
                               xlabel='Volume (mL)', 
                               ylabel='UV 280 nm (mAU)',
                               color='#332288')
        
        if len(set(y_cond)) > 1:
            plot_second_xaxis_curve(ax, 
                                    xdata=x_cond, 
                                    ydata=y_cond, 
                                    ylabel='Condutividade (mS/cm)', 
                                    color="#CC6677")
            
        if "Fraction (Fraction)" in dataframe.columns:
            add_fraction_ticks(ax, 
                               xdata=x_Fraction, 
                               ydata=y_Fraction, 
                               ymin=y_UV, 
                               color='#882255')
        
        add_injection_ticks(ax,
                            xdata=x_injection, 
                            ydata=y_injection, 
                            ymin=y_UV, 
                            color='#44AA99')

    return fig

def plot_hydrophobic_interactions(dataframe):
    pass

def plot_gel_filtration_analytical(dataframe):
    pass

def plot_calibration_gel_filtration(dataframe):
    x_UV = list(dataframe["UV 1_280 (min)"])
    y_UV = list(dataframe["UV 1_280 (mAU)"])

    with _lock:
        fig, ax = plt.subplots(figsize=(16, 8), dpi=300)
        fig.patch.set_facecolor('none')

        plot_first_xaxis_curve(ax, 
                               xdata=x_UV, 
                               ydata=y_UV, 
                               xlabel='Tempo (min)', 
                               ylabel='UV 280 nm (mAU)',
                               color='#332288')
            
    return fig

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