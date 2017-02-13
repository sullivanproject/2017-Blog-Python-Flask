from flask import Flask, render_template
app = Flask(__name__)

#TODO: logged를 True, False로 바꾸어가며 보여 줄 것
@app.route('/')
def index() :
    return render_template("example1.html", logged = True)

if __name__ == "__main__" :
    app.run(debug=True)
