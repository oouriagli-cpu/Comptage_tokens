* 🇫🇷 [Français](#français)
* 🇬🇧 [English](#english)

---

## Français

# 🔑 Guide Détaillé : Gestion & Obtention des Clés API

Ce guide explique étape par étape comment obtenir vos clés d'API pour les différents fournisseurs de modèles de langage (LLM) et comment les configurer en toute sécurité dans votre fichier local `.env`.
Les clés ne sont pas gratuites : tarif de départ 5 dollars US sauf pour la clé API Gemini mais avec une utilisation quotidienne restreinte.

---

### 📑 Sommaire
1. [Obtenir une clé API Google Gemini](#1-obtenir-une-clé-api-google-gemini)
2. [Obtenir une clé API Anthropic Claude](#2-obtenir-une-clé-api-anthropic-claude)
3. [Obtenir une clé API OpenAI ChatGPT](#3-obtenir-une-clé-api-openai-chatgpt)
4. [Configurer le fichier .env local](#4-configurer-le-fichier-env-local)
5. [Règles de sécurité et bonnes pratiques](#5-règles-de-sécurité-et-bonnes-pratiques)

---

### 1. Obtenir une clé API Google Gemini
1. Rendez-vous sur **[Google AI Studio](https://aistudio.google.com/)**.
2. Connectez-vous avec votre compte Google.
3. Cliquez sur le bouton **Get API key** (Obtenir une clé API).
4. Cliquez sur **Create API key in new project**.
5. Copiez la clé générée (elle commence par `AIzaSy...`).

---

### 2. Obtenir une clé API Anthropic Claude
1. Rendez-vous sur la **[Console Anthropic](https://console.anthropic.com/)**.
2. Créez un compte ou connectez-vous.
3. Accédez à la section **API Keys**.
4. Cliquez sur **Create Key**.
5. Donnez un nom à votre clé (ex: `Tests Token Counter`) et copiez la clé générée (elle commence par `sk-ant-api03-...`).

---

### 3. Obtenir une clé API OpenAI ChatGPT
1. Rendez-vous sur la **[Plateforme OpenAI](https://platform.openai.com/)**.
2. Connectez-vous à votre compte OpenAI.
3. Accédez à la section **API Keys** dans le menu de gauche.
4. Cliquez sur **Create new secret key**.
5. Copiez la clé générée (elle commence généralement par `sk-proj-...`).

---

### 4. Configurer le fichier `.env` local

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

### 5. Règles de sécurité et bonnes pratiques

- 🛑 **Ne partagez jamais vos clés privées** sur un dépôt public GitHub, forum ou Discord.
- 🛑 **Le fichier `.env` ne doit jamais être commité** dans Git. Vérifiez qu'il est bien listé dans votre fichier `.gitignore`.
- 💡 Le fichier `.env.example` sert uniquement de modèle sans vos clés réelles pour indiquer aux utilisateurs les variables à remplir.

---

## English

# 🔑 Detailed Guide: API Keys Management & Setup

This guide explains step by step how to get your API keys for different Large Language Model (LLM) providers and how to securely configure them in your local `.env` file.
Keys are not free: starting price is 5 US dollars except for the Gemini API key, which has a restricted daily usage tier.

---

### 📑 Table of Contents
1. [Get a Google Gemini API key](#1-get-a-google-gemini-api-key)
2. [Get an Anthropic Claude API key](#2-get-an-anthropic-claude-api-key)
3. [Get an OpenAI ChatGPT API key](#3-get-an-openai-chatgpt-api-key)
4. [Configure the local .env file](#4-configure-the-local-env-file)
5. [Security rules and best practices](#5-security-rules-and-best-practices)

---

### 1. Get a Google Gemini API key
1. Go to **[Google AI Studio](https://aistudio.google.com/)**.
2. Log in with your Google account.
3. Click the **Get API key** button.
4. Click **Create API key in new project**.
5. Copy the generated key (it starts with `AIzaSy...`).

---

### 2. Get an Anthropic Claude API key
1. Go to the **[Anthropic Console](https://console.anthropic.com/)**.
2. Create an account or log in.
3. Go to the **API Keys** section.
4. Click **Create Key**.
5. Name your key (e.g., `Token Counter Tests`) and copy the generated key (it starts with `sk-ant-api03-...`).

---

### 3. Get an OpenAI ChatGPT API key
1. Go to the **[OpenAI Platform](https://platform.openai.com/)**.
2. Log in to your OpenAI account.
3. Go to the **API Keys** section in the left menu.
4. Click **Create new secret key**.
5. Copy the generated key (it usually starts with `sk-proj-...`).

---

### 4. Configure the local `.env` file

In your project folder:

1. Duplicate the `.env.example` file to create your `.env` file:
   ```bash
   cp .env.example .env
   ```

2. Open the `.env` file with your code editor and replace the placeholder values with your keys:

```env
# Real API keys
GEMINI_API_KEY=AIzaSy...
ANTHROPIC_API_KEY=sk-ant-api03-...
OPENAI_API_KEY=sk-proj-...
```

---

### 5. Security rules and best practices

- 🛑 **Never share your private keys** on a public GitHub repository, forum, or Discord.
- 🛑 **The `.env` file must never be committed** to Git. Make sure it is listed in your `.gitignore` file.
- 💡 The `.env.example` file is only a template without your real keys to show users which variables to fill.
