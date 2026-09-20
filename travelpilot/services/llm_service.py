import os
from dotenv import load_dotenv

load_dotenv()

def call_llm(prompt: str) -> str:
    provider = os.getenv("LLM_PROVIDER", "mock")
    
    if provider == "mock":
        return f"[Mock LLM Response]: Processed successfully for query: {prompt[:30]}..."
        
    elif provider == "openai":
        try:
            import openai
            openai.api_key = os.getenv("OPENAI_API_KEY")
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"[OpenAI Error]: {str(e)}"
            
    elif provider == "gemini":
        try:
            import google.generativeai as genai
            genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
            model = genai.GenerativeModel('gemini-1.5-pro')
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"[Gemini Error]: {str(e)}"
            
    return f"[LLM Generated Content]: {prompt}"