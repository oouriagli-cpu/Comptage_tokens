* 🇫🇷 [Français](#français)
* 🇬🇧 [English](#english)

---

## Français

# Scripts de Comptage de Tokens & Benchmarks LLM

Ce dépôt contient des scripts Python légers permettant de calculer le nombre de tokens pour des prompts de test sur différents modèles d'IA (**Google Gemini**, **Anthropic Claude**, et **OpenAI ChatGPT**).

---

### ⚡ Démarrage Rapide

#### 1. Installation des dépendances
```bash
pip install python-dotenv google-genai anthropic openai
```

#### 2. Configuration des Clés API
Dupliquez le fichier d'exemple et renseignez vos clés dans votre fichier `.env` local :
```bash
cp .env.example .env
```

Pour consulter le guide détaillé étape par étape sur la création et la sécurité des clés API, consulter le [guide de démarrage](./Guide.md)*.

---

### Scripts disponibles

* **Google Gemini** : `count_tokens_Flash38.py`
* **Anthropic Claude** : `count_tokens_Opus5.py`
* **OpenAI ChatGPT** : `count_tokens_Sol56.py`

Pour changer le nom du modèle, entrez son nom technique dans la variable 'selected_model' du script Python.

---

### 📁 Fichiers du projet

* `README.md` : Présentation du projet.
* `GUIDE.md` : Guide détaillé pour obtenir et configurer les clés API.
* `.env.example` : Modèle de configuration exemple.
* `.gitignore` : Protection des fichiers sensibles.

---

## English

# Token Counting Scripts & LLM Benchmarks

This repository contains lightweight Python scripts to calculate the number of tokens for test prompts across different AI models (**Google Gemini**, **Anthropic Claude**, and **OpenAI ChatGPT**).

---

### ⚡ Quick Start

#### 1. Install dependencies
```bash
pip install python-dotenv google-genai anthropic openai
```

#### 2. Configure API Keys
Duplicate the example file and fill in your keys in your local `.env` file:
```bash
cp .env.example .env
```

To view the detailed step-by-step guide on creating and securing API keys, check out the [getting started guide](./Guide.md)*.

---

### Available scripts

* **Google Gemini**: `count_tokens_Flash38.py`
* **Anthropic Claude**: `count_tokens_Opus5.py`
* **OpenAI ChatGPT**: `count_tokens_Sol56.py`

To change the model name, enter its technical name in the 'selected_model' variable of the Python script.

---

### 📁 Project files

* `README.md`: Project overview.
* `GUIDE.md`: Detailed guide for obtaining and configuring API keys.
* `.env.example`: Example configuration template.
* `.gitignore`: Protection for sensitive files.
