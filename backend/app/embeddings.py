import os
import time

from google import genai
from dotenv import load_dotenv
from google.genai.errors import ServerError

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def get_embedding(text):
    """
    Generate embedding with automatic retry.
    """

    MAX_RETRIES = 5

    for attempt in range(MAX_RETRIES):

        try:

            response = client.models.embed_content(
                model="gemini-embedding-001",
                contents=text
            )

            return response.embeddings[0].values

        except ServerError:

            wait_time = 2 ** attempt

            print(
                f"⚠️ Gemini temporarily unavailable."
                f" Retrying in {wait_time} seconds..."
            )

            time.sleep(wait_time)

    raise Exception("Failed after multiple retries.")