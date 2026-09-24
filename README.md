# Scripts de Comptage de Tokens & Benchmarks LLM

Ce dépôt contient des scripts Python légers permettant de calculer le nombre de tokens pour des prompts de test sur différents modèles d'IA (**Google Gemini**, **Anthropic Claude**, et **OpenAI ChatGPT**).

---

## ⚡ Démarrage Rapide

### 1. Installation des dépendances
```bash
pip install python-dotenv google-genai anthropic openai
```

### 2. Configuration des Clés API
Dupliquez le fichier d'exemple et renseignez vos clés dans votre fichier `.env` local :
```bash
cp .env.example .env
```

Pour consulter le guide détaillé étape par étape sur la création et la sécurité des clés API, consultez **[GUIDE.md](./GUIDE.md)**.

---

## Exécution des scripts

* **Google Gemini** : `python count_prompts_Flash38.py`
* **Anthropic Claude** : `python count_prompts_Opus5.py`
* **OpenAI ChatGPT** : `python count_prompts_Sol56.py`

---

## 📁 Fichiers du projet

* `README.md` : Présentation du projet.
* `GUIDE.md` : Guide détaillé pour obtenir et configurer les clés API.
* `.env.example` : Modèle de configuration exemple.
* `.gitignore` : Protection des fichiers sensibles.
