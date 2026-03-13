from groq import Groq
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Try environment variable first, then hardcoded fallback
GROQ_API_KEY = os.getenv("GROQ_API_KEY") or "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"

try:
    client = Groq(api_key=GROQ_API_KEY)
except Exception as e:
    print(f"Groq init error: {e}")
    client = None

def get_response(user_message, college_data):
    try:
        if not client:
            return "⚠️ AI service unavailable. Please contact Fayaz & Masthan."

        college_info = json.dumps(college_data, indent=2)
        prompt = f"""You are FM Guider, a friendly AI companion for VVITU (Vasireddy Venkatadri International Technological University), Namburu, Guntur, Andhra Pradesh. Created by students Fayaz and Masthan in 2026.

College Information:
{college_info}

Instructions:
- Be friendly and helpful to new students
- Always call the university VVITU
- Use emojis to make responses fun
- Answer only based on college data above
- If you don't know, say "Please contact the university office at 09100305336"
- Keep answers clear and short
- End every reply with: "Is there anything else I can help you with? 😊"

Student question: {user_message}"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=800,
            temperature=0.7
        )
        return response.choices[0].message.content

    except Exception as e:
        error_msg = str(e)
        print(f"Groq Error: {error_msg}")
        if "decommissioned" in error_msg or "model" in error_msg.lower():
            return "⚠️ Model error! Please contact Fayaz to update the AI model."
        return "⚠️ Something went wrong. Please try again in a moment! 😊"
