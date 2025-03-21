import asyncio

from app.agent.manus import Manus
from app.logger import logger

async def run_manus_agent(prompt: str):
    """
    Fonction pour exécuter l'agent Manus avec un prompt donné et retourner la réponse.
    Cette fonction encapsule la logique principale de main.py pour être utilisée dans Streamlit.
    """
    agent = Manus()
    if not prompt.strip():
        logger.warning("Prompt vide fourni.")
        return "Prompt vide. Veuillez entrer une requête." # Retourner un message pour Streamlit

    logger.warning("Traitement de votre requête...")
    response = await agent.run(prompt) # Exécuter l'agent et récupérer la réponse
    logger.info("Traitement de la requête terminé.")
    return str(response) # Retourner la réponse (convertie en string) pour Streamlit


# La partie __name__ == "__main__": est supprimée ici, car ce fichier sera importé, pas exécuté directement.
# La boucle principale et l'appel à asyncio.run seront gérés dans streamlit_app.py