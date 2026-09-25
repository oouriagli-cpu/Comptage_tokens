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

Pour consulter le guide détaillé étape par étape sur la création et la sécurité des clés API, consulter le [guide de démarrage](./Guide.md)*.

---

## Scripts disponibles

* **Google Gemini** : `count_tokens_Flash38.py`
* **Anthropic Claude** : `count_tokens_Opus5.py`
* **OpenAI ChatGPT** : `count_tokens_Sol56.py`

Pour changer le nom du modèle, entrer son nom technique.

---

## 📁 Fichiers du projet

* `README.md` : Présentation du projet.
* `GUIDE.md` : Guide détaillé pour obtenir et configurer les clés API.
* `.env.example` : Modèle de configuration exemple.
* `.gitignore` : Protection des fichiers sensibles.
