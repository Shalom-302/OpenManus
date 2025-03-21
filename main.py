# import asyncio

# from app.agent.manus import Manus
# from app.logger import logger


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

from app.agent.manus import Manus
from app.logger import logger

async def main():
    agent = Manus() # <-- L'AGENT EST CRÉÉ *UNE SEULE FOIS, EN DEHORS DE LA BOUCLE*
    print("🤖 OpenManus est prêt. Tapez 'exit' ou 'quit' pour arrêter.") # Message de démarrage

    while True: # <-- BOUCLE INFINIE AJOUTÉE
        prompt = input("Enter your prompt: ")
        if prompt.lower() in ["exit", "quit"]: # <-- GESTION DE LA COMMANDE DE SORTIE
            print("👋 Arrêt de OpenManus...")
            break # Sortir de la boucle infinie

        if not prompt.strip(): # Gestion des prompts vides (comme dans votre code actuel)
            logger.warning("Empty prompt provided.")
            continue # Retour au début de la boucle (attendre un nouveau prompt)


        logger.warning("Processing your request...")
        await agent.run(prompt)
        logger.info("Request processing completed.\n") # Ajout d'un retour à la ligne pour plus de clarté

    print("OpenManus a été arrêté.") # Message de fin (après la sortie de la boucle)


if __name__ == "__main__":
    try: # On garde le bloc try...except pour KeyboardInterrupt, mais il englobe maintenant toute la boucle main()
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.warning("Opération interrompue par l'utilisateur.")
        print("\nOpenManus a été interrompu par l'utilisateur.") # Message plus clair pour interruption manuelle
