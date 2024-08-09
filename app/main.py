from parser import parse_pdf
from prompt_generator import generate_prompt
from data_extractor import extract_data
from utils import save_to_json
import time
import json

def main(pdf_file: str, output_json: str):
    start_time = time.perf_counter()
    parsed_content = parse_pdf(pdf_file)
    print(f"Time taken to parse the pdf: {time.perf_counter() - start_time:.2f} seconds")
    prompt = generate_prompt(parsed_content)

    extracted_data = extract_data(prompt)
    data_dict = json.loads(extracted_data)
    save_to_json(data_dict, output_json)
        
if __name__ == "__main__":
    pdf_file = "pdf_files/sample_file_1.pdf"
    output_json = "output_data.json"
    main(pdf_file, output_json)