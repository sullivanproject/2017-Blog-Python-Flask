from flask import Flask, render_template
app = Flask(__name__)

#TODO: list의 값을 바꾸어주며 보여줄 것
@app.route('/<id>')
def index(id) :
    return render_template("example3.html", id=id)

if __name__ == "__main__" :
    app.run(debug=True)
