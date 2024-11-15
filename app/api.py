import os
import openai
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_phrase(cefr_level=None, topic=None):
    """
    Generate a new phrase using OpenAI's GPT-3.5 model based on the specified CEFR level and topic.
    """
    try:
        # Construct the prompt with CEFR level and topic
        prompt = "Generate a European Portuguese phrase"
        if cefr_level:
            prompt += f" at the {cefr_level} level"
        if topic:
            prompt += f" about {topic}"
        prompt += "."

        # Make the API call to generate the phrase
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates European Portuguese phrases."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.7,
        )

        # Extract and return the generated phrase
        generated_phrase = response.choices[0].message['content'].strip()
        return generated_phrase

    except Exception as e:
        # Log the error and return None to trigger fallback
        print(f"Error generating phrase: {e}")
        return None

