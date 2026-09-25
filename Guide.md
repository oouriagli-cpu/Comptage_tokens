# 🔑 Guide Détaillé : Gestion & Obtention des Clés API

Ce guide explique étape par étape comment obtenir vos clés d'API pour les différents fournisseurs de modèles de langage (LLM) et comment les configurer en toute sécurité dans votre fichier local `.env`.
Les clés ne sont pas gratuites : tarif de départ 5 dollars US sauf pour la clé API Gemini mais avec une utilisation quotidienne restreinte.

---

## 📑 Sommaire
1. [Obtenir une clé API Google Gemini](#1-obtenir-une-clé-api-google-gemini)
2. [Obtenir une clé API Anthropic Claude](#2-obtenir-une-clé-api-anthropic-claude)
3. [Obtenir une clé API OpenAI ChatGPT](#3-obtenir-une-clé-api-openai-chatgpt)
4. [Configurer le fichier .env local](#4-configurer-le-fichier-env-local)
5. [Règles de sécurité et bonnes pratiques](#5-règles-de-sécurité-et-bonnes-pratiques)

---

## 1. Obtenir une clé API Google Gemini
1. Rendez-vous sur **[Google AI Studio](https://aistudio.google.com/)**.
2. Connectez-vous avec votre compte Google.
3. Cliquez sur le bouton **Get API key** (Obtenir une clé API).
4. Cliquez sur **Create API key in new project**.
5. Copiez la clé générée (elle commence par `AIzaSy...`).

---

## 2. Obtenir une clé API Anthropic Claude
1. Rendez-vous sur la **[Console Anthropic](https://console.anthropic.com/)**.
2. Créez un compte ou connectez-vous.
3. Accédez à la section **API Keys**.
4. Cliquez sur **Create Key**.
5. Donnez un nom à votre clé (ex: `Tests Token Counter`) et copiez la clé générée (elle commence par `sk-ant-api03-...`).

---

## 3. Obtenir une clé API OpenAI ChatGPT
1. Rendez-vous sur la **[Plateforme OpenAI](https://platform.openai.com/)**.
2. Connectez-vous à votre compte OpenAI.
3. Accédez à la section **API Keys** dans le menu de gauche.
4. Cliquez sur **Create new secret key**.
5. Copiez la clé générée (elle commence généralement par `sk-proj-...`).

---

## 4. Configurer le fichier `.env` local

Dans le dossier de votre projet :

1. Dupliquez le fichier `.env.example` pour créer votre fichier `.env` :
   ```bash
   cp .env.example .env
   ```

2. Ouvrez le fichier `.env` avec votre éditeur de code et remplacez les valeurs fictives par vos clés :

```env
# Clés API réelles
GEMINI_API_KEY=AIzaSy...
ANTHROPIC_API_KEY=sk-ant-api03-...
OPENAI_API_KEY=sk-proj-...
```

---

## 5. Règles de sécurité et bonnes pratiques

- 🛑 **Ne partagez jamais vos clés privées** sur un dépôt public GitHub, forum ou Discord.
- 🛑 **Le fichier `.env` ne doit jamais être commité** dans Git. Vérifiez qu'il est bien listé dans votre fichier `.gitignore`.
- 💡 Le fichier `.env.example` sert uniquement de modèle sans vos clés réelles pour indiquer aux utilisateurs les variables à remplir.
