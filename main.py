from flask import Flask, render_template,request
import os 


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('video_upload.html')


@app.route("/getvideo", methods=['POST','GET'])
def predict():
    if request.method=='POST':
        vidfile = request.files['vid']
    
        if vidfile:
            filename = vidfile.filename
            path = os.path.join('static/uploads',filename)
            vidfile.save(path)
            return render_template('video_upload.html', msg="Here, is your video",filename=filename)
        else:
            return render_template('video_upload.html', msg="No file")

    elif request.method=='GET':
        return render_template('video_upload.html', prediction_text="Get Method")



if __name__ == "__main__":
    app.run(debug=True)