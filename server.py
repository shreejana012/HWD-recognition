from flask import Flask, url_for, send_from_directory, request
import logging, os
from werkzeug import secure_filename
from PIL import Image, ImageFilter
import glob

app = Flask(__name__)
file_handler = logging.FileHandler('server.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}/uploads/'.format(PROJECT_HOME)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def resize(img_path, max_px_size, output_folder):
  images= glob.glob(img_path)
  for image in images:
    with Image.open(image) as img:
      width_0, height_0 = img.size
      out_f_name = os.path.split(image)[-1]
      out_f_path = os.path.join(output_folder, out_f_name)

      if max((width_0, height_0)) == max_px_size:
        print('writing {} to disk (no change from original)'.format(out_f_path))
        img.save(out_f_path)
      else:
        img = img.resize((28, 28), Image.ANTIALIAS)
        print('writing {} to disk'.format(out_f_path))
        img.save(out_f_path)

def create_new_folder(local_dir):
  newpath = local_dir
  if not os.path.exists(newpath):
      os.makedirs(newpath)
  return newpath

@app.route('/', methods = ['POST', 'GET'])
def api_root():
  app.logger.info(PROJECT_HOME)
  if request.method == 'POST' and request.files['image']:
    app.logger.info(app.config['UPLOAD_FOLDER'])
    img = request.files['image']
    img_name = secure_filename(img.filename)
    create_new_folder(app.config['UPLOAD_FOLDER'])
    saved_path = os.path.join(app.config['UPLOAD_FOLDER'], img_name)
    app.logger.info("saving {}".format(saved_path))
    img.save(saved_path)
    resize("uploads/*",28,"output")
    return send_from_directory(app.config['UPLOAD_FOLDER'],img_name, as_attachment=True)
  else:
    return "Where is the image?"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)