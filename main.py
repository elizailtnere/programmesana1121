from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/teksts")
def teksts():
   return render_template("teksts.html")


if __name__ == '__main__':
    app.run(port = 5000 )

    
print("Sveiki!")