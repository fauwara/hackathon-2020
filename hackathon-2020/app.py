from flask import Flask, render_template
from web import data

app = Flask(__name__)

# dummy data

# data = [
#     {
#         "heading" : "heading 1",
#         "author" : "fawaz",
#         "content" : "blalaldjdld;k " 
#     },
#     {
#         "heading" : "heading 2",
#         "author" : "sdfsdfsz",
#         "content" : "blaladfefewffsz "
#     }
# ]

@app.route('/')
def hello_world():
    return render_template('home.html',data = data)

if __name__ == "__main__":
    app.run(debug = True)