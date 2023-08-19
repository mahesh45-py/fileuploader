from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)
directory_path = os.getcwd()+'/api/tmp'
app.config['UPLOAD_FOLDER'] = directory_path

def getFiles():

    

    # List all files and directories in the specified directory
    files_and_directories = os.listdir(directory_path)

    # Filter only files from the list
    files = [file for file in files_and_directories if os.path.isfile(os.path.join(directory_path, file))]
    return files


@app.route('/')
def home():
    print("home page loaded")
    return render_template("index.html",files=getFiles())

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the 'file' field is in the request
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    # If the user does not select a file, the browser submits an empty part without a filename
    if file.filename == '':
        return redirect(request.url)

    if file:
        try:
            # Use secure_filename to avoid filename conflicts and potential security issues
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'File uploaded successfully'
        except Exception as err:
            return str(err)
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)