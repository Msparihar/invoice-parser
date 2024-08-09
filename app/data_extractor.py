from openai import OpenAI
import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv(override=True)

class InvoiceData(BaseModel):
    customer_details: str
    products: list[str]
    total_amount: str

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_data(prompt: str) -> dict:
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "Extract the data in json format from the given text"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        response_format={"type": "json_object"}
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    test_prompt = """
    Invoice Number: INV-12345
    Date: 2024-08-09
    Customer: John Doe
    Items: 
    1x Widget A - $100
    2x Widget B - $200
    Total: $300
    """

    extracted_data = extract_data(test_prompt)
    print(extracted_data)
