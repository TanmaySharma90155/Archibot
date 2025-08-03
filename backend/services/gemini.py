from google import genai
import os
from dotenv import load_dotenv

load_dotenv()  

def get_gemini_response(prompt: str) -> str:
   
    client = genai.Client()
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
    
#print(get_gemini_response("Hello, world!") ) # Example usage for testing