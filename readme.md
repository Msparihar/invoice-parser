# Invoice Parsing Tool

## Overview

This project provides a tool for parsing invoices from PDF files and extracting structured data using OpenAI. The tool follows a two-step process: first, it parses the PDF content, and then it generates a prompt with additional instructions to extract specific data. The results are stored in a JSON file.

## Features

- **PDF Parsing**: Extracts all text content from the provided PDF invoice using [Unstructured](https://github.com/Unstructured-IO/unstructured).
- **Prompt Generation**: Creates a prompt based on parsed content and additional instructions.
- **Data Extraction**: Utilizes OpenAI's API to extract specific data fields.
- **JSON Output**: Saves the extracted data in a structured JSON format.

## Installation

1. Clone the repository:

```
   git clone https://github.com/Msparihar/invoice-parser.git
   cd invoice-parser
```

2. Install the required packages:

```
   pip install -r requirements.txt
```

## Usage

1. Place your PDF invoice in the project directory.
2. Run the main script:

```bash
   python main.py --pdf_file your_invoice.pdf --output_json output_data.json
```

3. The extracted data will be saved in the specified JSON file.

## Configuration

- **API Key**: Set your OpenAI API key in the environment file `.env`.
- **Additional Instructions**: Customize the instructions in the `generate_prompt` function to extract specific data fields.

## Contributing

We welcome contributions! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

For more information or support, please contact:

- **Manish Singh Parihar**
- **LinkedIn**: [LinkedIn](https://www.linkedin.com/in/manishsparihar/)
- **Email**: manishsparihar2020@gmail.com
- **Phone**: 6232748224

---

This README file serves as a template and placeholder for your project's documentation. Please replace placeholders with actual content as the project progresses.
