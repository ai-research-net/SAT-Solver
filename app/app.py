from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
from pathlib import Path
import os
import uuid
from src.sat_functions import sat_solver, modify_subset, check_satisfiability_cached, write_clauses_to_cnf, read_cnf

app = Flask(__name__)
#app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'uploads')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        filename = secure_filename(file.filename)
        # Append a unique identifier to the filename
        filename_without_extension, extension = os.path.splitext(filename)
        unique_id = uuid.uuid4()
        filename = f'{filename_without_extension}_{unique_id}{extension}'

        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        
        
        clauses = read_cnf(filepath)
        
        # number of subsets
        particles = 50
        iterations = 100
        
        satisfied_clauses = sat_solver (clauses,num_particles=50, num_iterations=100)
        
        
        OUTPUT_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'outputs')
        output_filename = os.path.join(OUTPUT_DIR, 'output.cnf')
        write_clauses_to_cnf(satisfied_clauses, output_filename)
        


        return send_file(output_filename,  as_attachment=True)

if __name__ == '__main__':
    print("Starting app.py...")
    app.run(host='0.0.0.0', port=5000)#,debug=True)
