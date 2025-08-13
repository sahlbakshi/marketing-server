import os
from dotenv import load_dotenv
from supabase import create_client, Client
from openai import OpenAI

# Load .env into environment variables
load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_KEY")
ELEVENLABS_KEY = os.getenv("ELEVENLABS_KEY")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SECRET_KEY = os.getenv("SUPABASE_SECRET_KEY")
AUDIO_CACHE_BUCKET = "audio-cache"

# Consider moving this to a client file for better practice
supabase: Client = create_client(SUPABASE_URL, SUPABASE_SECRET_KEY)
openai = OpenAI(api_key=OPENAI_KEY)
