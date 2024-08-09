import json

def save_to_json(data: dict, output_file: str):
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
