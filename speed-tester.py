import time
import openai
import os
import json
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

def get_random_sentence() -> str:
    resp = openai.chat.completions.create(
        model="gpt-4o",
        temperature=0.2,
        messages=[
            {"role": "user", "content": "Give me a random sentence for typing practice. Should be simple and clear. Max 10 words."}
        ],
    )
    content = resp.choices[0].message.content.strip()
    return content

def calculate_wpm(start_time: float, end_time: float, text: str) -> float:
    elapsed_minutes = (end_time - start_time) / 60
    word_count = len(text.split())
    return word_count / elapsed_minutes

def calculate_accuracy(typed: str, original: str) -> float:
    total = len(original)
    correct = sum(1 for o, t in zip(typed, original) if o == t)
    return (correct / total) * 100

def main():
    sentence = get_random_sentence()
    print("Type the following sentence:")
    print(sentence)

    input("Press Enter when you are ready...")
    start = time.time()
    typed = input("Your input: ")
    end = time.time()

    wpm = calculate_wpm(start, end, typed)
    accuracy = calculate_accuracy(typed, sentence)

    print(f"Your typing speed: {wpm:.2f} WPM")
    print(f"Your accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    main()