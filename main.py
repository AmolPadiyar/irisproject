from flask import Flask,render_template,request

from project_file.utils import IrisClass

app = Flask(__name__)

@app.route("/")
def home_api():
    print("we are in home api")

    return render_template("index.html")

@app.route("/get_pred",methods = ["GET","POST"])
def prediction():
    if request.method == "GET":

        SepalLength = eval(request.args.get("SepalLength"))
        SepalWidth  = eval(request.args.get("SepalWidth"))
        PetalLength = eval(request.args.get("PetalLength"))
        PetalWidth  = eval(request.args.get("PetalWidth"))

        obj = IrisClass(SepalLength,SepalWidth,PetalLength,PetalWidth)

        result = obj.get_prediction()
        isris_versicolor= "https://www.fs.usda.gov/wildflowers/beauty/iris/Blue_Flag/images/iris_versicolor/iris_versicolor_10_lg.jpg"
        iris_verginica = "https://www.fnps.org/assets/images/plants/iris_virginica_2017.JPG"
        iris_setosa = "https://live.staticflickr.com/65535/51376589362_b92e27ae7a_b.jpg"

        if result == "Iris-virginica":
            return render_template("index.html",flower = result,iris=iris_verginica)
        
        elif result == "Iris-versicolor":
            return render_template("index.html",flower = result,iris=isris_versicolor)
        
        elif result == "Iris-setosa":
            return render_template("index.html",flower = result,iris=iris_setosa)
if __name__ == "__main__":
    app.run()