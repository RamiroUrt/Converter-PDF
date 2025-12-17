import os
from docx2pdf import convert

try:
    print("\n *** Word to PDF Batch Converter *** \n")

    input_folder = input("Enter input folder path: ")
    output_folder = input("Enter output folder path: ")

    os.makedirs(output_folder, exist_ok=True)

    for file in os.listdir(input_folder):
        if file.endswith(".docx"):
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, file.replace(".docx", ".pdf"))

            convert(input_path, output_path)
            print(f"✔ Converted {file}")

    print("\nAll Word files converted successfully!\n")

except Exception as e:
    print(f"\nError: {e}\n")
