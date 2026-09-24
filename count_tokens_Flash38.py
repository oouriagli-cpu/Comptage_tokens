import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()

print("=== Étape 0 : Lecture complète du fichier externe ===")
try:
    with open("10000_prompts_en.txt", "r", encoding="utf-8") as f:
        file_content = f.read()
    print("Fichier chargé avec succès d'un seul bloc.\n")
except Exception as e:
    print(f"Erreur lors de la lecture du fichier de prompts : {e}\n")
    file_content = ""

# Sélection du modèle Gemini récent 
selected_model = "gemini-3.8-flash"

print(f"=== Étape 1 : Comptage global des tokens avec le modèle Gemini '{selected_model}' ===\n")

total_tokens_count = 0

if file_content:
    try:
        response = client.models.count_tokens(
            model=selected_model,
            contents=file_content
        )
        total_tokens_count = response.total_tokens
        print("Comptage effectué d'un trait avec succès.\n")
    except Exception as e:
        print(f"Erreur lors du comptage global des tokens : {e}\n")

print("=" * 50)
print(f"TOTAL GEMINI ({selected_model}) : {total_tokens_count} tokens d'entrée.")
print("=" * 50)
