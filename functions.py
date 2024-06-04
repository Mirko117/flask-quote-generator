from dotenv import load_dotenv
import os

load_dotenv()

PIXABAY_API_KEY = os.environ.get("PIXABAY_API_KEY")

print(".env variables loaded")
