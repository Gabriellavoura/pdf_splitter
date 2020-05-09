import os
from PyPDF2 import PdfFileReader, PdfFileWriter

# Default Path for the upload folder:
#open_path = "\\input"
#save_path = "\\splitter_output"

# Function to get a PDF Document
def pdf_input(open_path = ".\\input"):

  # open only the .pdf files
  for root, dirs, files in os.walk(open_path):
    for name in files:
      if name.endswith(".pdf"):

        pdf = PdfFileReader(open_path + "\\" + name,"rb")

        # Save as an list the File and his name
        fileinfo = [pdf,name]

        # if there is an pdf file return the list:
        if fileinfo:
          return fileinfo

  return print("ERROR: Pdf not Found.")

# Function that returns number of pages of the pdf document
def get_numPages(pdf):
  return pdf.getNumPages()

# Function that divides PDF documents into single page PDF
def pdf_splitter(pdf, pdf_name, num_pages=3,
                save_path = ".\\splitter_output"):

    # Split filename to get only the first name, not the extension
    output_fname = pdf_name.split(".")[0]

    # Creates the folder that will hold the pdf units
    folder = os.path.join(save_path, output_fname)
    os.makedirs(folder)

    for page in range(0, num_pages):
      pdf_writer = PdfFileWriter()
      pdf_writer.addPage(pdf.getPage(page))

      with open(save_path + "\\" + output_fname +"\\" + output_fname+ "_pg_" + str(page+1) + ".pdf", 'wb') as out:
        pdf_writer.write(out)

    return print ("PDF file has been splitted!")