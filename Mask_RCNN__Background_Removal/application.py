from flask import Flask, request, send_file, Response, render_template, jsonify
import helper_methods as helper
import requests

MODEL, CLASS_NAMES = helper.get_default_model()
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('view.html')


@app.route('/image_url', methods=['GET','POST'])
def image_url():
    try:
        image_url = request.form['image_url']
        if ("http" in image_url) or ("https" in image_url):
            img_path = os.path.abspath("") + '/temp.jpg'
            f = open(img_path, 'wb')
            f.write(requests.get(image_url).content)
            f.close()
        else:
            img_path = image_url
        
        new_img_path = helper.display_segmented_image(MODEL,img_path)
        return render_template("index.html", user_image = new_img_path)

    except Exception as e:
        print(e)
        return 'error'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 5000)