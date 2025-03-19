
# 👋 OpenManus

Manus est un agent d'intelligence artificielle révolutionnaire qui, grâce à son architecture modulaire, permet de transformer des réponses générées par un modèle de langage (LLM) en actions concrètes. Contrairement à d'autres agents qui se limitent à la réponse textuelle, OpenManus orchestre l'exécution d'outils spécialisés (ex. : génération de code, visualisation via navigateur) pour créer un résultat tangible.

L'objectif de ce projet est de permettre à chacun de déployer, comprendre et personnaliser un agent IA performant, tout en se basant sur une documentation détaillée de son fonctionnement interne.

---

## Table des Matières

- [Démo du Projet](#démo-du-projet)
- [Installation](#installation)
  - [Méthode 1 : Utilisation de conda](#méthode-1--utilisation-de-conda)
  - [Méthode 2 : Utilisation de uv (recommandée)](#méthode-2--utilisation-de-uv-recommandée)
- [Configuration](#configuration)
- [Démarrage Rapide](#démarrage-rapide)
- [Reverse Engineering du Workflow d'Exécution de Manus](#reverse-engineering-du-workflow-dexécution-de-manus)
  - [Workflow Global](#workflow-global)
  - [Analyse Technique du Module `toolcall.py`](#analyse-technique-du-module-toolcallpy)
- [Création et Personnalisation de Votre Propre Agent](#création-et-personnalisation-de-votre-propre-agent)
- [Contribuer](#contribuer)
- [Communauté](#communauté)
- [Historique des Étoiles](#historique-des-étoiles)
- [Citer](#citer)

---

## Démo du Projet

<video src="https://private-user-images.githubusercontent.com/61239030/420168772-6dcfd0d2-9142-45d9-b74e-d10aa75073c6.mp4" controls muted class="d-block rounded-bottom-2 border-top width-fit" style="max-height:640px; min-height: 200px"></video>

---

## Installation

### Méthode 1 : Utilisation de conda

1. Créez un nouvel environnement conda :
   ```bash
   conda create -n open_manus python=3.12
   conda activate open_manus
   ```

2. Clonez le dépôt :
   ```bash
   git clone https://github.com/mannaandpoem/OpenManus.git
   cd OpenManus
   ```

3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

### Méthode 2 : Utilisation de uv (Recommandée)

1. Installez uv (un installateur Python rapide et résolveur de dépendances) :
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Clonez le dépôt :
   ```bash
   git clone https://github.com/mannaandpoem/OpenManus.git
   cd OpenManus
   ```

3. Créez et activez un nouvel environnement virtuel :
   ```bash
   uv venv --python 3.12
   source .venv/bin/activate  # Sur Unix/macOS
   # Ou sur Windows :
   # .venv\Scripts\activate
   ```

4. Installez les dépendances :
   ```bash
   uv pip install -r requirements.txt
   ```

---

## Configuration

OpenManus nécessite une configuration pour les API du LLM utilisé. Pour configurer votre environnement :

1. Copiez le fichier de configuration exemple :
   ```bash
   cp config/config.example.toml config/config.toml
   ```

2. Modifiez `config/config.toml` pour ajouter vos clés API et personnaliser les paramètres :
   ```toml
   [llm]
   model = "gpt-4o"
   base_url = "https://api.openai.com/v1"
   api_key = "sk-..."  # Remplacez par votre clé API
   max_tokens = 4096
   temperature = 0.0

   [llm.vision]
   model = "gpt-4o"
   base_url = "https://api.openai.com/v1"
   api_key = "sk-..."  # Remplacez par votre clé API
   ```

---

## Démarrage Rapide

Pour lancer OpenManus, exécutez simplement :
```bash
python main.py
```

Vous pouvez ensuite entrer votre commande dans le terminal, par exemple :
```
un site de ecommerce responsive avec du HTML CSS et JAVASCRIPT
```

---

## Reverse Engineering du Workflow d'Exécution de Manus

Ce section décrit en détail comment OpenManus exécute une tâche, depuis la réception de la demande jusqu'à l'affichage du résultat, afin de mieux comprendre la chaîne d'opérations et vous permettre de créer votre propre agent.

### Workflow Global

1. **Initialisation**  
   - **Configuration du Logging et Activation de la Télémétrie Anonyme**  
     Au démarrage, OpenManus initialise le système de logging et active la télémétrie anonyme pour suivre l'exécution tout en garantissant la confidentialité.

2. **Réception de la Demande**  
   - **Saisie de la Commande Utilisateur**  
     L'utilisateur saisit sa demande. Par exemple :
     ```
     un site de ecommerce responsive avec du HTML CSS et JAVASCRIPT
     ```

3. **Appel au Modèle de Langage (LLM)**  
   - **Interrogation et Traitement**  
     L'agent envoie l'historique des messages et un prompt système au LLM pour générer une réponse initiale. Ce processus inclut la gestion de la consommation de tokens pour chaque étape.

4. **Sélection et Activation des Outils**  
   - **Choix de l'Outil Approprié**  
     D'après la réponse du LLM, l'agent sélectionne un ou plusieurs outils à utiliser. Dans notre exemple :
     - `python_execute` est d'abord activé pour générer le code HTML, CSS et JavaScript.
   - **Exécution de l'Outil**  
     L'outil sélectionné est exécuté, par exemple, pour créer un fichier HTML contenant le code généré.

5. **Visualisation avec BrowserUse**  
   - **Affichage du Résultat**  
     Après l'exécution, l'outil `browser_use` est appelé pour ouvrir le fichier généré dans un navigateur, permettant à l'utilisateur de visualiser le résultat final.

6. **Itération et Affinage (si nécessaire)**  
   - **Processus Itératif**  
     Selon la demande, l'agent peut poursuivre avec d'autres étapes pour affiner le résultat ou intégrer des modifications supplémentaires.

### Analyse Technique du Module `toolcall.py`

Le fichier `toolcall.py` joue un rôle crucial dans l'orchestration des appels aux outils. Voici les points essentiels :

- **Héritage et Objectif**  
  La classe `ToolCallAgent` hérite de `ReActAgent` et gère la transformation de la réponse du LLM en actions concrètes via des appels de fonctions (tool calls).

- **Méthode `think`**  
  - Ajoute un prompt de prochaine étape aux messages.
  - Interroge le LLM via `ask_tool` en passant les messages, le prompt système et la liste des outils disponibles.
  - Extrait et loggue les tool calls générés (les outils sélectionnés et leur ordre d'exécution).

- **Méthode `act`**  
  - Pour chaque appel d'outil, exécute la méthode `execute_tool`.
  - Agrège les résultats et les enregistre dans la mémoire de l'agent pour constituer la réponse finale.
  - Loggue l'issue de chaque appel d'outil avec des messages détaillés.

- **Méthode `execute_tool`**  
  - Valide et parse les arguments (au format JSON) de l'appel.
  - Active l'outil correspondant à partir d'une collection d'outils disponibles.
  - Gère les erreurs et formate le résultat pour l'afficher (ex. : « Observed output of cmd `python_execute` executed: ... »).

- **Gestion des Outils Spéciaux**  
  La méthode `_handle_special_tool` vérifie si un outil particulier (comme `Terminate`) nécessite un traitement spécial, par exemple pour terminer l'exécution de l'agent.

Ces mécanismes, combinés aux logs détaillés (incluant la consommation de tokens et l'ordre des étapes), offrent une vision claire du fonctionnement interne d'OpenManus et facilitent le reverse engineering pour créer et personnaliser votre propre agent.

---

## Création et Personnalisation de Votre Propre Agent

En vous appuyant sur l'analyse ci-dessus, vous pouvez adapter OpenManus à vos besoins :

1. **Étude du Workflow**  
   - Analysez les logs d'exécution pour comprendre comment l'agent décide, sélectionne et exécute des outils.
   - Identifiez les modules clés (comme `toolcall.py`, `ReActAgent`, etc.) pour déterminer où intervenir.

2. **Ajout ou Modification d'Outils**  
   - Étendez la collection d'outils en ajoutant de nouvelles classes dans `ToolCollection`.
   - Intégrez des fonctionnalités supplémentaires, par exemple, la communication en temps réel via Gemini Live.

3. **Personnalisation de la Logique de Décision**  
   - Modifiez la méthode `think` pour adapter la logique de sélection des outils selon vos critères.
   - Ajoutez des messages de log pour une meilleure traçabilité et analyse.

4. **Tests et Itérations**  
   - Testez chaque modification en observant les logs et le comportement de l'agent.
   - Affinez la gestion des erreurs et l'optimisation des appels aux API pour garantir un fonctionnement fluide.

---

