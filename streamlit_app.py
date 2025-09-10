import streamlit as st
import plotly.graph_objects as go

st.set_page_config(layout="wide")

# Layout met twee kolommen
col1, col2 = st.columns([1,2])

with col1:
    st.header("Voer je Python-code in")
    user_code = st.text_area("Typ of plak hier je code:", height=300, placeholder="Bijvoorbeeld: maak een 3D-kubus met Plotly")
    run_button = st.button("Run")

with col2:
    st.header("Output")
    if run_button and user_code.strip() != "":
        try:
            # Sandbox voor de code-uitvoer
            local_vars = {}
            exec(user_code, {"go": go}, local_vars)

            # Verwacht dat de code een figuur-object maakt met naam 'fig'
            if "fig" in local_vars:
                st.plotly_chart(local_vars["fig"], use_container_width=True)
            else:
                st.warning("Geen variabele 'fig' gevonden. Zorg dat je code een fig = ... aanmaakt.")
        except Exception as e:
            st.error(f"Fout bij uitvoeren van code: {e}")
