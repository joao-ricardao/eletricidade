import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Valores de tensão
v = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

st.title("Gráfico de Tensão vs Corrente para duas Resistências")

# Sliders para selecionar dois valores de resistência
r1 = st.slider("Selecione o valor da Resistência R1 (Ω):", 1, 100, 10)
r2 = st.slider("Selecione o valor da Resistência R2 (Ω):", 1, 100, 20)

# Calcular correntes para cada resistência
i1 = [valor/r1 for valor in v]
i2 = [valor/r2 for valor in v]

# Criar DataFrame para mostrar os dados
df = pd.DataFrame({
    "Tensão (V)": v,
    f"Corrente R1 = {r1} Ω": i1,
    f"Corrente R2 = {r2} Ω": i2
})

# Mostrar tabela
st.dataframe(df)

# Plotar gráfico
fig, ax = plt.subplots()
ax.plot(v, i1, marker='o', linestyle='-', label=f"R1 = {r1} Ω")
ax.plot(v, i2, marker='s', linestyle='--', label=f"R2 = {r2} Ω")
ax.set_xlabel("Tensão (V)")
ax.set_ylabel("Corrente (A)")
ax.set_title("Curvas V-I para duas Resistências")
ax.legend()
ax.grid()

st.pyplot(fig)


