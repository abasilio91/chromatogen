import streamlit as st
import validador
import utils
import images

st.write("# Visualização de dados de cromatografia")
st.write("P.S.: não tá bonito, mas ta funcionando =P")

option = st.radio(
    "Escolha o tipo de gráfico que quer visualizar:",
    ["Afinidade","Desalting","Interação hidrofóbica","gel filtração analítica","calibração - gel filtração"]
)

radio_image_fun = {
    "Afinidade": images.plot_affinity,
    "Desalting": images.plot_desalting,
    "Interação hidrofóbica": images.plot_hydrophobic_interactions,
    "gel filtração analítica": images.plot_gel_filtration_analytical,
    "calibração - gel filtração": images.plot_calibration_gel_filtration
}

uploaded_file = st.file_uploader("Faça upload de um arquivo CSV contendo os dados de cromatografia para visualizar os gráficos correspondentes.")

try:
    st.write("Processando o arquivo...")
    dataframe = utils.prepare_data(uploaded_file)

    st.write("Validando o arquivo...")
    msg = validador.validate_file(dataframe, option)
    st.write(msg)

    if msg != "arquivo valido":
        st.stop()
    
    st.write("Exibindo os dados...")
    st.write(dataframe)

    st.write("Gerando o gráfico...")
    fig = radio_image_fun[option](dataframe)
    st.write(fig)
except Exception as e:
    st.error(f"Erro ao processar o arquivo: {e}")
    st.stop()