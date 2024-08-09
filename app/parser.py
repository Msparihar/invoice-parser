from unstructured.partition.auto import partition

def parse_pdf(pdf_file):
    print("working")
    elements = partition(pdf_file)
    print("working2")
    print(elements[0])
    pdf_content = ""
    pdf_content= "\n\n".join([str(el) for el in elements])
    return pdf_content