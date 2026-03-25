def afinity(dataframe) -> str:
    if not "Conc B (%)" in dataframe.columns:
        msg = "O gráfico de afinidade requer a coluna 'Conc B (%)' no arquivo CSV."
        return msg
    return "arquivo valido"

def desalting(dataframe) -> str:
    if not "Cond (mS/cm)" in dataframe.columns:
        msg = "O gráfico de desalting requer a coluna 'Cond (mS/cm)' no arquivo CSV."
        return msg
    return "arquivo valido"

def hydrophobic_interaction(dataframe) -> str:
    if not "Cond (mS/cm)" in dataframe.columns:
        msg = "O gráfico de interação hidrofóbica requer a coluna 'Cond (mS/cm)' no arquivo CSV."
        return msg
    return "arquivo valido"

def gel_filtration_analysis(dataframe) -> str:
    if not "Cond (mS/cm)" in dataframe.columns:
        msg = "O gráfico de filtração em gel requer a coluna 'Cond (mS/cm)' no arquivo CSV."
        return msg
    return "arquivo valido"

def gel_filtration_calibration(dataframe) -> str:
    return "arquivo valido"

def validate_file(dataframe, radio_option) -> str:
    radio = {"Afinidade ou troca iônica": afinity, 
             "Desalting": desalting, 
             "Interação hidrofóbica": hydrophobic_interaction, 
             "gel filtração analítica": gel_filtration_analysis, 
             "calibração - gel filtração": gel_filtration_calibration}

    msg = radio[radio_option](dataframe)
    return msg