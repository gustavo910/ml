from flask import Flask, render_template, request
import marks as m
import pymsgbox

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def marks():
    if request.method =="POST":
        hrs = request.form["hrs"]
        marks_pred = m.marks_prediction(hrs)
        #mk = marks_pred
        print(marks_pred)
        pymsgbox.alert(marks_pred, 'A previa de sua nota é:')

    return render_template("index.html")





if __name__ == "__main__":
    app.run(debug=True)
