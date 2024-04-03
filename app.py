from flask import Flask, request, render_template
import os
from llama_index import SimpleDirectoryReader

app = Flask(__name__)

@app.route('/file_upload', methods=['GET','POST'])
def upload_pdf():
    if request.method == 'POST':
        pdf_files = request.files.getlist('pdf_file')
        first_docs = None
        print("Hi")

        for pdf_file in pdf_files:
            if pdf_file:
                save_path = "./first_company_files"
                if not os.path.exists(save_path):
                    os.makedirs(save_path)
                filename = pdf_file.filename.lower().replace("-", "_")    
                file_path = os.path.join(save_path, filename)
                pdf_file.save(file_path)
                first_filename = pdf_file.name.lower().replace(".pdf", "").replace("-", "_")
                first_docs = SimpleDirectoryReader(input_dir="./first_company_files", required_exts=[".pdf"]).load_data()

                if first_docs:
                    print("Hello")
        try:
           return first_docs
        except TypeError:
            print("You got the First docs here")
        
    return render_template('upload_form.html')

if __name__ == '__main__':
    app.run(debug=True)
