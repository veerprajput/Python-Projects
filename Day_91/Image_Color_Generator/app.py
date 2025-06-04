from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
from PIL import Image
from statistics import mode
from collections import Counter
import os
import numpy as np
import requests

app = Flask(__name__)
app.config['IMAGE_UPLOADS'] = 'static\images'
Bootstrap(app)

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'. format(r, g, b)

@app.route('/', methods =["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            print(request.files)
            src = request.files['file']
            filename = secure_filename(src.filename)
            directory = os.path.abspath(os.path.dirname(__file__))
            src.save(os.path.join(directory, app.config['IMAGE_UPLOADS'], filename))
            img = Image.open(f'static/images/{filename}')
            img_array = np.array(img)
            ### reshape the array to a 2D numpy array of RGB tuples
            rgb_tuples = img_array.reshape(-1, 3)
            rgb_tuples = [tuple(rgb) for rgb in rgb_tuples]
            ### count the occurrences of each RGB tuple using Counter
            count_dict = Counter(rgb_tuples)
            # f = open('random_text.txt', mode='w')
            #     print(len(set(list(count_dict))))
            # for element in sorted(set(count_dict)):
            #     f.write(str(element) + '\n')
            # f.close()
            ### get the top 10 most common RGB tuples
            top10 = count_dict.most_common(10)
            rgb_colors = []
            for rgb, count in top10:
                rgb_colors.append(rgb_to_hex(rgb[0], rgb[1], rgb[2]))
            return render_template('index.html', src=filename, href='', numOfOccurrences=len(sorted(set(count_dict))), rgb_colors=rgb_colors)
        except:
            url = str(request.form.get("file"))
            response = requests.get(url)
            try:
                filename = 'static/images/' + url.split('/')[-1].split('?')[0]
            except:
                filename = 'static/images/' + url.split('/')[-1]
            with open(filename, "wb") as f:
                f.write(response.content)
            img = Image.open(filename)
            img_array = np.array(img)
            rgb_tuples = img_array.reshape(-1, 3)
            rgb_tuples = [tuple(rgb) for rgb in rgb_tuples]
            count_dict = Counter(rgb_tuples)
            top10 = count_dict.most_common(10)
            rgb_colors = []
            for rgb, count in top10:
                rgb_colors.append(rgb_to_hex(rgb[0], rgb[1], rgb[2]))
            return render_template('index.html', src='', href=request.form.get("file"), numOfOccurrences=len(sorted(set(count_dict))), rgb_colors=rgb_colors)
    return render_template('index.html', src='', href='')

if __name__ == '__main__':
    app.run(debug=True)