import os
import json
from groq import Groq
from dotenv import load_dotenv

# Load environment variables securely
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize client only if key exists
client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None

def get_response(user_message, college_data):
    if not client:
        return "⚠️ AI service unavailable. Please check your API key configuration."

    try:
        college_info = json.dumps(college_data, indent=2)
        
        # System instructions separate from user input
        system_prompt = f"""You are FM Guider, a friendly AI companion for VVITU (Vasireddy Venkatadri International Technological University), Namburu, Guntur, Andhra Pradesh. Created by students Fayaz and Masthan in 2026.

College Information:
{college_info}

Instructions:
- Be friendly and helpful to new students.
- Always call the university VVITU.
- Use emojis to make responses fun.
- Answer ONLY based on the college data provided. Do not hallucinate external information.
- If you don't know the answer, say "Please contact the university office at 09100305336".
- Keep answers clear and short.
- End every reply with: "Is there anything else I can help you with? 😊"
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            max_tokens=800,
            temperature=0.7
        )
        
        return response.choices[0].message.content

    except Exception as e:
        print(f"Groq API Error: {str(e)}")
        return "⚠️ I'm having trouble connecting to my brain! Please try again later."
