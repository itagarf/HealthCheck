from flask import Flask, render_template
import requests
import excepts
 

app = Flask(__name__)


@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/health")
def health():
    try:
        response = requests.get("http://127.0.0.1:5000/home")
        status = "The application is ok {}".format(response.status_code)
    except:
        status = "The application is not ok {}".format(response.status_code)
    
    return status

@app.route("/error")
def errors():
    raise excepts.FakeException("A fake error occured!")
    


if __name__ == "__main__":
    app.run(debug = "TRUE")
    app.run(host="0.0.0.0", port = 5000)

