import streamlit as st
import asyncio # Importez asyncio même si pas utilisé directement ici, Streamlit peut en avoir besoin
from manuswrap import run_manus_agent # <-- Importez la fonction wrapper


import streamlit as st
import asyncio # Importez asyncio même si pas utilisé directement ici, Streamlit peut en avoir besoin
st.title("OpenManus - Prototype Streamlit")

if "agent_response" not in st.session_state: # Initialiser l'état de session pour la réponse
    st.session_state.agent_response = None

prompt = st.text_input("Entrez votre prompt :")

if prompt:
    st.session_state.agent_response = asyncio.run(run_manus_agent(prompt))
if st.session_state.agent_response: # Afficher la réponse si elle existe
    st.write("Réponse de OpenManus :")
    st.code(st.session_state.agent_response, language="json") # Afficher la réponse dans st.code (JSON pour commencer)