from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['PDF_LOCATION'] = "static\PDF's"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pdf', methods =["GET", "POST"])
def pdf():
    if request.method == "POST":
        start_page = int(request.form.get('startPage'))
        src = request.files['file']
        filename = secure_filename(src.filename)
        directory = os.path.abspath(os.path.dirname(__file__))
        src.save(os.path.join(directory, app.config['PDF_LOCATION'], filename))
        return render_template('pdf.html', filename=filename)

if __name__ == '__main__':
    app.run(debug=True)