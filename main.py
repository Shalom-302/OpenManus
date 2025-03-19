# import asyncio

# from app.agent.manus import Manus
# from app.logger import logger

# # pas mal ça 
# async def main():
#     agent = Manus()
#     try:
#         prompt = input("Enter your prompt: ")
#         if not prompt.strip():
#             logger.warning("Empty prompt provided.")
#             return

#         logger.warning("Processing your request...")
#         await agent.run(prompt)
#         logger.info("Request processing completed.")
#     except KeyboardInterrupt:
#         logger.warning("Operation interrupted.")


# if __name__ == "__main__":
#     asyncio.run(main())


import asyncio
import streamlit as st
from app.agent.manus import Manus
from app.logger import logger

# Fonction asynchrone
async def async_main(st_logging_callback):
    agent = Manus()
    try:
        # Remplacer input() par un champ de texte Streamlit
        prompt = st.text_input("Enter your prompt: ")
        if not prompt.strip():
            st_logging_callback("Empty prompt provided.")
            return

        st_logging_callback("Processing your request...")
        await agent.run(prompt)
        st_logging_callback("Request processing completed.")
    except KeyboardInterrupt:
        st_logging_callback("Operation interrupted.")

# Fonction pour afficher les logs dans Streamlit
def st_logging_callback(message):
    st.text(message)

# Utilisation de Streamlit
if __name__ == "__main__":
    st.title("Async Streamlit Agent")
    
    if st.button("Start"):
        # Lancer le code asynchrone dans un thread séparé
        asyncio.run(async_main(st_logging_callback))
