import PyPDF2
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def compress_pdf(input_path, output_path):
    # Open the PDF file in read-binary mode
    with open(input_path, 'rb') as file:
        pdf = PyPDF2.PdfFileReader(file)

        # Create a new PDF writer object
        pdf_writer = PyPDF2.PdfFileWriter()

        # Iterate through each page of the PDF
        for page_num in range(pdf.getNumPages()):
            page = pdf.getPage(page_num)

            # Compress the content of the page
            page.compressContentStreams()

            # Add the compressed page to the PDF writer
            pdf_writer.addPage(page)

        # Write the compressed PDF to the output file
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

    print(f'Compressed PDF saved to: {output_path}')

# Create a Tkinter file picker dialog
root = Tk()
root.withdraw()

# Prompt the user to select a PDF file
input_file_path = askopenfilename(filetypes=[('PDF Files', '*.pdf')])

if input_file_path:
    # Generate the output file path by adding "_compressed" to the input file name
    output_file_path = input_file_path.replace('.pdf', '_compressed.pdf')

    # Call the function to compress the PDF
    compress_pdf(input_file_path, output_file_path)
