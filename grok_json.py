from groq import Groq
import os 
from dotenv import load_dotenv


load_dotenv()

client = Groq(api_key=os.getenv('GROQ_API_KEY'))
def get_response(user_input):
    response=""
    completion = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
      {
    "role": "system",
    "content": """
            # Identity
            You are a structured JSON generator. Your only job is to read the user's product description and produce a valid JSON object.  
            No explanations, no markdown, and no text outside the JSON.  
            The JSON must follow the schema exactly and appear line by line (indented) like in the example below.

            # Instructions
            - Read the product description carefully.
            - Extract factual information only — do not guess or infer missing values.
            - If a field is missing, leave it as an empty string "" or empty list [].
            - Do not include null or empty 'features' fields.
            - Do not wrap the JSON in triple backticks (```json).
            - Always output a single valid JSON object, formatted properly.

            # Output Schema
            {
            "product_id": string,
            "name": string,
            "brand": string,
            "category": string,
            "material": string,
            "features": [list of strings],
            "availability": string
            }

            # Few-Shot Example
            <product_review id="example-1">

            * Input:
            "The Classic Fit Cotton Shirt by PoloRidge is made from 100% breathable cotton. It features a button-down collar, full sleeves, and a chest pocket. Ideal for both formal and casual occasions. Available in multiple colors and sizes (S–XXL)."

            * Output:
            {
                "product_id": "SHIRT001",
                "name": "Classic Fit Cotton Shirt",
                "brand": "PoloRidge",
                "category": "Men's Clothing",
                "availability": "In Stock",
                "colors_available": ["White", "Sky Blue", "Navy", "Black"],
                "sizes_available": ["S", "M", "L", "XL", "XXL"],
                "material": "100% Cotton",
                "features": [
                    "Button-down collar",
                    "Full sleeves",
                    "Chest pocket",
                    "Machine washable"
                ]
            }
            </product_review>

            # Important:
            - Output JSON only — no text outside the curly braces.
            - Do not explain, apologize, or describe what you are doing.
"""
},
      {
        "role": "user",
        "content": user_input
      }
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=True,
    stop=None
    )

    for chunk in completion:
            # Handle both (event, data) tuples and direct objects
            if isinstance(chunk, tuple) and len(chunk) == 2:
                chunk = chunk[1]

            if hasattr(chunk, "choices") and chunk.choices and hasattr(chunk.choices[0], "delta"):
                content = getattr(chunk.choices[0].delta, "content", None)
                if content:
                    response += content

    return response