# app.py
import streamlit as st

# Constantes
ELEMENTARY_CHARGE = 1.602176634e-19  # C (carga elementar exata)

st.set_page_config(page_title="Questões de Eletrostática", layout="centered")
st.title("Resolução de Questões de Eletrostática")

st.markdown(
    """
Este programa resolve dois tipos de problemas comuns:
1. **Íon** → dado nº de prótons, elétrons e nêutrons, calcular carga, sinal e nº de nêutrons.  
2. **Esferas condutoras** → dado duas cargas iniciais, calcular a carga final após contato.  
"""
)

# --- Seleção de tipo de questão ---
tipo = st.radio(
    "Selecione o tipo de questão:",
    ["Íon (prótons, elétrons, nêutrons)", 
     "Esferas condutoras idênticas"
     ]
)

# --- Caso 1: Íon ---
if tipo == "Íon (prótons, elétrons, nêutrons)":
    st.subheader("Cálculo da carga de um íon")
    p = st.number_input("Número de prótons (p)", min_value=0, value=20, step=1)
    e = st.number_input("Número de elétrons (e)", min_value=0, value=18, step=1)
    n = st.number_input("Número de nêutrons (n)", min_value=0, value=22, step=1)

    q = (p - e) * ELEMENTARY_CHARGE  # excesso de prótons ou elétrons
    sinal = "positivo" if q > 0 else "negativo" if q < 0 else "neutro"

    st.write(f"**Carga do íon:** {q:.3e} C ({sinal})")
    st.write(f"**Número de nêutrons:** {int(n)}")

# --- Caso 2: Esferas condutoras ---
elif tipo == "Esferas condutoras idênticas":
    st.subheader("Distribuição de cargas após contato")
    q1 = st.number_input("Carga da primeira esfera (C)", value=2.0)
    q2 = st.number_input("Carga da segunda esfera (C)", value=-3.0)

    q_final = (q1 + q2) / 2
    st.write(f"**Carga final em cada esfera:** {q_final:.2f} C")


