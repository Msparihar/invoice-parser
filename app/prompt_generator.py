def generate_prompt(parsed_content: str) -> str:
    
    instruction = (
        "Given the following liners extracted from an invoice, extract the Customer details, "
        "Products, and Total Amount. Format the extracted information in a JSON structure as shown "
        "in the examples below.\n"
    )

    # Example 1
    example_1 = (
        "Example 1:\n"
        "Lines: ['ABC TRADING CO. Invoice #: inv123', 'Customer Name: John Doe', 'Product: Widget A', 'Total: $100']\n"
        "Expected JSON: {\n"
        "    'Customer Details': {\n"
        "        'Name': 'John Doe'\n"
        "    },\n"
        "    'Products': [\n"
        "        {'Name': 'Widget A', 'Quantity': 1, 'Rate': '$100', 'Total Amount': '$100'}\n"
        "    ],\n"
        "    'Total Amount': '$100'\n"
        "}\n\n"
    )

    # Example 2
    example_2 = (
        "Example 2:\n"
        "Lines: ['XYZ SUPPLIES Invoice #: inv456', 'Bill To: Jane Smith', 'Items: Gadget B', 'Total: $200']\n"
        "Expected JSON: {\n"
        "    'Customer Details': {\n"
        "        'Name': 'Jane Smith'\n"
        "    },\n"
        "    'Products': [\n"
        "        {'Name': 'Gadget B', 'Quantity': 1, 'Rate': '$200', 'Total Amount': '$200'}\n"
        "    ],\n"
        "    'Total Amount': '$200'\n"
        "}\n\n"
    )
    
    # Complete prompt with parsed content and instructions
    prompt = (
        f"{instruction}"
        f"{example_1}"
        f"{example_2}"
        f"Lines: {parsed_content}"
        "Expected JSON:"
    )

    return prompt