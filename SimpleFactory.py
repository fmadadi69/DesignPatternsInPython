# ###################### NOT USING SIMPLE FACTORY ########################
# class PDFDocument:
#     def __init__(self, file_path):
#         self.file_path = file_path
#
#     def extract_text(self):
#         return f"Extracting text from PDF: {self.file_path}"
#
#
# class WordDocument:
#     def __init__(self, file_path):
#         self.file_path = file_path
#
#     def extract_text(self):
#         return f"Extracting text from Word document: {self.file_path}"
#
#
# class ExcelDocument:
#     def __init__(self, file_path):
#         self.file_path = file_path
#
#     def extract_text(self):
#         return f"Extracting text from Excel file: {self.file_path}"
#
#
# pdf_doc = PDFDocument("Doc1.pdf")
# word_doc = WordDocument("Doc2.docx")
# excel_doc = ExcelDocument("Doc3.xls")
#
# print(pdf_doc.extract_text())
# print(word_doc.extract_text())
# print(excel_doc.extract_text())

# ###################### USING SIMPLE FACTORY ########################
class Document:
    def __init__(self, file_path):
        self.file_path = file_path

    def extract_text(self):
        return NotImplementedError("This method should be implemented in subclass")


class PDFDocument(Document):
    def extract_text(self):
        return f"Extracting text from PDF: {self.file_path}"


class WordDocument(Document):
    def extract_text(self):
        return f"Extracting text from Word document: {self.file_path}"


class ExcelDocument(Document):
    def extract_text(self):
        return f"Extracting text from Excel file: {self.file_path}"


class DocumentFactory:
    @staticmethod
    def create_document(file_path):
        if file_path.endswith(".pdf"):
            return PDFDocument(file_path)
        elif file_path.endswith(".docx"):
            return WordDocument(file_path)
        elif file_path.endswith(".xls"):
            return ExcelDocument(file_path)
        else:
            raise ValueError("Unsupported file format")


documents = [DocumentFactory.create_document("doc1.docx"),
             DocumentFactory.create_document("doc2.pdf"),
             # DocumentFactory.create_document("doc3.ppt"),
             DocumentFactory.create_document("doc4.xls")]

for doc in documents:
    print(doc.extract_text())





