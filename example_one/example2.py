from flask import Flask, render_template
app = Flask(__name__)

#TODO: list의 값을 바꾸어주며 보여줄 것
@app.route('/')
def index() :
    list = ['이찬희', '배주웅', '김효준']
    return render_template("example2.html", list=list)

if __name__ == "__main__" :
    app.run(debug=True)
