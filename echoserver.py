from flask import Flask, request, jsonify, redirect, url_for
from flask.ext.cors import CORS
import os
from werkzeug.utils import secure_filename
import sys
import json
import requests
import ast, time
import convert_uni2ascii
import convert_asci2uni
import subprocess

UPLOAD_FOLDER = '/home/dipsico/Desktop/Projects/ascii2uni/backend/downloads/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf','odt','doc','docx'])

app = Flask(__name__)
cors = CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/send_u2a', methods=['POST'])
def handle_u2a():
	if request.method == 'POST' and 'file' in request.files :
		file = request.files['file']
		# if user does not select file, browser also
		# submit a empty part without filename
		if file.filename == '':
			flash('No selected file')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			if '.pdf' in filename:
				os.system('pdftotext -layout %s %s -f 1 -l 30' %(os.path.join(app.config['UPLOAD_FOLDER'], filename),os.path.join(app.config['UPLOAD_FOLDER'], filename+'.txt')))
				os.system('rm %s' %(os.path.join(app.config['UPLOAD_FOLDER'], filename)))
				input_text = open(os.path.join(app.config['UPLOAD_FOLDER'], filename+'.txt'),'r').read()
				os.system('rm %s' %(os.path.join(app.config['UPLOAD_FOLDER'], filename+'.txt')))
			elif '.odt' in filename:
				os.system('odt2txt --output=%s %s' %(os.path.join(app.config['UPLOAD_FOLDER'], filename+'.txt'),os.path.join(app.config['UPLOAD_FOLDER'], filename)))
				os.system('rm %s' %(os.path.join(app.config['UPLOAD_FOLDER'], filename)))
				input_text = open(os.path.join(app.config['UPLOAD_FOLDER'], filename+'.txt'),'r').read()
				os.system('rm %s' %(os.path.join(app.config['UPLOAD_FOLDER'], filename+'.txt')))
			elif '.txt' in filename:
				input_text = open(os.path.join(app.config['UPLOAD_FOLDER'], filename),'r').read()
			elif '.doc' in filename:
				os.system('catdoc %s > %s' %(os.path.join(app.config['UPLOAD_FOLDER'], filename),os.path.join(app.config['UPLOAD_FOLDER'], filename+'.txt')))
				os.system('rm %s' %(os.path.join(app.config['UPLOAD_FOLDER'], filename)))
				input_text = open(os.path.join(app.config['UPLOAD_FOLDER'], filename+'.txt'),'r').read()
				os.system('rm %s' %(os.path.join(app.config['UPLOAD_FOLDER'], filename+'.txt')))
			elif '.docx' in filename:
				os.system('docx2txt %s' %(os.path.join(app.config['UPLOAD_FOLDER'], filename)))
				os.system('rm %s' %(os.path.join(app.config['UPLOAD_FOLDER'], filename)))
				input_text = open(os.path.join(app.config['UPLOAD_FOLDER'], filename.replace('.docx','.txt')),'r').read()
				os.system('rm %s' %(os.path.join(app.config['UPLOAD_FOLDER'], filename.replace('.docx','.txt'))))
			text,mapping = convert_uni2ascii.convert(input_text,request.form['font'])
			return  jsonify(response=text,font=mapping)
	else:
		payload = request.get_data()
		payload = payload.decode("utf-8")
		payload = ast.literal_eval(payload)
		text,mapping = convert_uni2ascii.convert(payload["text"],payload["font"])
		return jsonify(response=text,font=mapping)

@app.route('/send_a2u', methods=['POST'])
def handle_a2u():
	if request.method == 'POST' and 'file' in request.files :
		file = request.files['file']
		# if user does not select file, browser also
		# submit a empty part without filename
		if file.filename == '':
			flash('No selected file')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			if '.pdf' in filename:
				os.system('pdftotext -layout %s %s -f 1 -l 30' %(os.path.join(app.config['UPLOAD_FOLDER'], filename),os.path.join(app.config['UPLOAD_FOLDER'], filename+'.txt')))
				os.system('rm %s' %(os.path.join(app.config['UPLOAD_FOLDER'], filename)))
				input_text = open(os.path.join(app.config['UPLOAD_FOLDER'], filename+'.txt'),'r').read()
				os.system('rm %s' %(os.path.join(app.config['UPLOAD_FOLDER'], filename+'.txt')))
			elif '.odt' in filename:
				cmd = ["odt2txt",os.path.join(app.config['UPLOAD_FOLDER'], filename)]
				fh = open(os.path.join(app.config['UPLOAD_FOLDER'], filename+'.txt'), "w") 
				process = subprocess.Popen(cmd, shell=True, stdout=fh)
				fh.close()
				#with open(, 'w') as fout:
					#subprocess.Popen(cmd, stdout=fout,stderr=subprocess.PIPE,stdin=subprocess.PIPE, shell=True)
				#os.system('odt2txt --output=%s %s' %(,))
				#os.system('rm %s' %(os.path.join(app.config['UPLOAD_FOLDER'], filename)))
				input_text = open(os.path.join(app.config['UPLOAD_FOLDER'], filename+'.txt'),'r').read()
				#os.system('rm %s' %(os.path.join(app.config['UPLOAD_FOLDER'], filename+'.txt')))
			elif '.txt' in filename:
				input_text = open(os.path.join(app.config['UPLOAD_FOLDER'], filename),'r').read()
			elif '.doc' in filename:
				os.system('catdoc %s > %s' %(os.path.join(app.config['UPLOAD_FOLDER'], filename),os.path.join(app.config['UPLOAD_FOLDER'], filename+'.txt')))
				os.system('rm %s' %(os.path.join(app.config['UPLOAD_FOLDER'], filename)))
				input_text = open(os.path.join(app.config['UPLOAD_FOLDER'], filename+'.txt'),'r').read()
				os.system('rm %s' %(os.path.join(app.config['UPLOAD_FOLDER'], filename+'.txt')))
			elif '.docx' in filename:
				os.system('docx2txt %s' %(os.path.join(app.config['UPLOAD_FOLDER'], filename)))
				os.system('rm %s' %(os.path.join(app.config['UPLOAD_FOLDER'], filename)))
				input_text = open(os.path.join(app.config['UPLOAD_FOLDER'], filename.replace('.docx','.txt')),'r').read()
				os.system('rm %s' %(os.path.join(app.config['UPLOAD_FOLDER'], filename.replace('.docx','.txt'))))
			text,mapping = convert_asci2uni.convert(input_text,request.form['font'])
			return  jsonify(response=text,font=mapping)
	else:
		payload = request.get_data()
		payload = payload.decode("utf-8")
		payload = ast.literal_eval(payload)
		text,mapping = convert_asci2uni.convert(payload["text"],payload["font"])
		return jsonify(response=text,font="Anja")


if __name__ == '__main__':
  app.run()
