import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment
token = os.getenv("SECRET")

# Model settings
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-nano"

# Initialize OpenAI client
client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

print("🤖 Lietuviškai kalbantis dirbtinis intelektas paruoštas! (Įrašyk „exit“ išeiti)\n")

# Start console chat loop
while True:
    user_input = input("Tu: ")

    if user_input.lower() in ["exit", "quit"]:
        print("👋 Iki!")
        break

    try:
        # Send request to model
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "Tu esi naudingas padėjėjas, kuris visada atsako tik lietuviškai.",
                },
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            temperature=1.0,
            top_p=1.0,
            model=model
        )

        print("AI:", response.choices[0].message.content.strip())

    except Exception as e:
        print("⚠️ Klaida:", e)
