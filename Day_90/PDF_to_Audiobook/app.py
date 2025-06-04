from flask import Flask, render_template, request
from pdfreader import PDFDocument, SimplePDFViewer
from werkzeug.utils import secure_filename
from io import BytesIO
import pyttsx3
import os

app = Flask(__name__)
app.config['PDF_LOCATION'] = "static\PDF's"

# @app.route('/', methods =["GET", "POST"])
# def home():
#     return render_template('index.html')

# @app.route('/pdf', methods =["GET", "POST"])
# def pdf():
#     if request.method == "POST":
#         start_page = int(request.form.get('startPage'))
#         src = request.files['file']
#         filename = secure_filename(src.filename)
#         directory = os.path.abspath(os.path.dirname(__file__))
#         src.save(os.path.join(directory, app.config['PDF_LOCATION'], filename))
#         fd = open(f"static/PDF's/{filename}", "rb")
#         doc = PDFDocument(fd)
#         viewer = SimplePDFViewer(fd)
#         all_pages = [p for p in doc.pages()]
#         all_text = []
#         engine = pyttsx3.init()
#         rate = engine.getProperty('rate')
#         engine.setProperty('rate', 125)
#         for i in range(start_page, len(all_pages) + 1):
#             viewer.navigate(i)
#             viewer.render()
#             # engine.say('text')
#             # engine.runAndWait()
#             all_text.append(viewer.canvas.strings)
#         return render_template('pdf_reader.html', text=all_text)

# if __name__ == '__main__':
#     app.run(debug=True)

start_page = int(request.form.get('startPage'))
src = request.files['file']
filename = secure_filename(src.filename)
directory = os.path.abspath(os.path.dirname(__file__))
src.save(os.path.join(directory, app.config['PDF_LOCATION'], filename))
fd = open(f"static/PDF's/{filename}", "rb")
doc = PDFDocument(fd)
viewer = SimplePDFViewer(fd)
all_pages = [p for p in doc.pages()]
all_text = []
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)
for i in range(start_page, len(all_pages) + 1):
    viewer.navigate(i)
    viewer.render()
    engine.say('text')
    engine.runAndWait()
    all_text.append(viewer.canvas.strings)