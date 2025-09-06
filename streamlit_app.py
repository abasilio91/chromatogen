import streamlit as st
import matplotlib.pyplot as plt
import utils
import images

from threading import RLock

_lock = RLock()

plt.rcParams['font.family'] = 'Arial'

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:

    # Can be used wherever a "file-like" object is accepted:
    dataframe = utils.prepare_data(uploaded_file)
    st.write(dataframe)

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

        images.plot_first_xaxis_curve(ax, 
                                    xdata=x_UV, 
                                    ydata=y_UV, 
                                    xlabel='Volume (mL)', 
                                    ylabel='UV 280 nm (mAU)',
                                    color='#332288')
        
        if len(set(y_ConcB)) > 1:
            images.plot_second_xaxis_curve(ax, 
                                        xdata=x_ConcB, 
                                        ydata=y_ConcB, 
                                        ylabel='Buffer B Concentration (%)', 
                                        color="#CC6677")
            
        if "Fraction (Fraction)" in dataframe.columns:
            images.add_fraction_ticks(ax, 
                                    xdata=x_Fraction, 
                                    ydata=y_Fraction, 
                                    ymin=y_UV, 
                                    color='#882255')

        st.write(fig)
