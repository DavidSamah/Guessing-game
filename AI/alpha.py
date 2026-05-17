import tkinter as tk
import pandas as pd
import re
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="C:/Users/carin/Desktop/project/.env")
api_key = os.getenv("OPENAI_API_KEY")
print("API_KEY:", api_key)

client = OpenAI(api_key=api_key)

GPT_SYSTEM_PROMPT = (
    "You are a helpful and friendly assistant."
    "Respond clearly and naturally in simple language."
    "Do not show hidden reasoning or step by step internal thinking."
    "Respond in a conversational way."
)

# sample dataset
df = pd.DataFrame({
    "x": [1, 2, 3, 4],
    "y": [2, 4, 6, 8]
})

#memory
history = [{"role":"system", "content": GPT_SYSTEM_PROMPT}]

def ask_ai(user_text):
    try:

        history.append({"role":"user", "content":user_text})
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages= history,
            temperature=0.5,
            max_tokens=600
            
            
        )

        reply = response.choices[0].message.content.strip()

        history.append({"role": "assistant", "content": reply})
        return reply
        

    except Exception as e:
        return f"Error: {e}"
    


def local_response(text):
   
    text = re.sub(r"[^a-z0-9\s]", "", text.lower())

    if any(greeting in text for greeting in ["hi", "hello", "hey", "good morning", "good afternoon", "good evening", "good night", "yo"]):
        return "Hello! How can I help you today?"
    if "how are you" in text or "how r you" in text:
        return "I'm an assistant bot and I'm ready to help."
    if "your name" in text or "who are you" in text:
        return "I'm your AI assistant."
    return None


root = tk.Tk()
root.title("AI Assistant")

chat_box = tk.Text(root, height=20, width=60)
chat_box.pack()

entry = tk.Entry(root, width=50)
entry.pack()

def send():
    user_text = entry.get()
    entry.delete(0, tk.END)

    if not user_text.strip():
        return

    chat_box.insert(tk.END, "You:" + user_text + "\n")

    

    if user_text.lower().strip() == "data":
        summary = df.describe().to_string()
        reply = ask_ai("Explain this dataset:\n" + summary)
    else:
        reply = local_response(user_text)

        if reply is None:
            reply = ask_ai(user_text)
    
    chat_box.insert(tk.END, "AI: " + reply + "\n\n")
    chat_box.see(tk.END)

button = tk.Button(root, text="Send", command=send)
button.pack()

root.mainloop()

