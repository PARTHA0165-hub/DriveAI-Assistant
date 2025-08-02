import openai
import os

# You can either load from env or directly paste here (for demo)
openai.api_key = os.getenv("OPENAI_API_KEY", "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")

def summarize_text(text):
    try:
        if len(text.strip()) == 0:
            return "No text found in the file."

        response = openai.ChatCompletion.create(
            model="gpt-4o",  # or use "gpt-3.5-turbo" if needed
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Summarize the following text into bullet points."},
                {"role": "user", "content": text}
            ],
            temperature=0.3,
            max_tokens=300
        )

        summary = response['choices'][0]['message']['content'].strip()
        return summary

    except Exception as e:
        return f"Error generating summary: {str(e)}"
