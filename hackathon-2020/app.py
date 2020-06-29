from flask import Flask, render_template
from web import data_news, data_tech, topics

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
def home():
    return render_template('home.html',topic = topics)

@app.route('/news')
def news():
    return render_template('news.html',data_news = data_news, data_tech = data_tech)

if __name__ == "__main__":
    app.run(debug=True)