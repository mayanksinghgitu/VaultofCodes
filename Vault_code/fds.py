import os, dotenv
from openai import OpenAI

dotenv.load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("Using Key:", os.getenv("OPENAI_API_KEY")[:10] + "...")

try:
    res = client.models.list()
    print("✅ API key works!")
except Exception as e:
    print("❌ Error:", e)
