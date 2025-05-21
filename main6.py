import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
token = os.getenv("SECRET")

# Check for missing API key
if not token:
    print("❌ Klaida: Nerastas API raktas. Įsitikinkite, kad .env faile yra SECRET=...")
    sys.exit(1)

# Model settings
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-nano"

# Initialize client
client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

# Welcome message
print("\n🤖 Sveiki atvykę! Tai – AI padėjėjas, atsakantis lietuviškai.")
print("✍️  Įveskite klausimą ir paspauskite Enter.")
print("❌ Norėdami išeiti, parašykite „exit“ arba paspauskite Ctrl+C.\n")

# Chat loop
try:
    while True:
        user_input = input("👤 Tu: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("👋 Iki pasimatymo!")
            break

        if not user_input:
            print("⚠️ Prašome įvesti klausimą.")
            continue

        # Get response from model
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "Tu esi naudingas padėjėjas, kuris visada atsako tik lietuviškai."},
                {"role": "user", "content": user_input}
            ],
            model=model,
            temperature=1.0,
            top_p=1.0
        )

        ai_response = response.choices[0].message.content.strip()
        print(f"🤖 AI: {ai_response}\n")

except KeyboardInterrupt:
    print("\n👋 Išėjote iš programos. Gero vakaro!")
    sys.exit(0)
