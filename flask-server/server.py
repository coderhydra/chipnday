from flask import Flask

from db.from_db import db_select

app = Flask(__name__)

# member api route
@app.route("/members")
def members():
    return {"members": ["Member1","Member2","Member3"]}

@app.route("/ott")
def ott():
    df = db_select('movie_info')
    return {"DATA": df.to_dict('record')}

if __name__ == "__main__":
    app.run(debug=True)