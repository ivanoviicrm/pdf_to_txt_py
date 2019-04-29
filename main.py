import PyPDF2
from os import listdir


def ask_path():
    path = input("Introduce CARPETA para pasar TODOS los documentos PDF a TXT:\n")
    return path


def get_files_in_path(path):
    pdf_files = []
    for file in listdir(path):
        if file.endswith("pdf"):
            pdf_files.append(file)
    return pdf_files


def create_text_files(path, files):
    print("Creando los archivos txt...")
    for file in files:
        stream = open(path + file, "rb")

        reader = PyPDF2.PdfFileReader(stream)
        file_pages = reader.getNumPages()

        text_file_name = path + file[:-4] + ".txt"    # Con [:-4] quito .pdf y le agrego .txt
        print("Creando archivo ", text_file_name)
        txt_file = open(text_file_name, "w")

        for page in range(0, file_pages):
            page_content = reader.getPage(page).extractText()
            txt_file.write(page_content + "\n --end page--\n\n")


if __name__ == "__main__":
    path = ask_path()
    files = get_files_in_path(path)
    if len(files) > 0:
        print("Los documentos PDF encontrados en %s son:" %(path))
        for file in files:
            print(file)
        answer = input("¿Desea pasarlos a TXT? [s / n]: \n")
        if answer == "s":
            create_text_files(path, files)
