
from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    "id": 2,
    "title": "Data Analyst",
    "location": "Bengaluru, India",
    "salary": "Rs. 10,00,000"
  }
  {
        "id": 1,
        "title": "Data Analyst",
        "location": "Delhi, India",
        "salary": "Rs. 15,00,000"
} 
    {
        "id": 3,
        "title": "Backend Engineer",
        "location": "San Francisco, USA",
        "salary": "$120,000"
    }
    {
    "id": 4,
    "title": "Frontend",
    "location": "remote",
    "salary": "Rs. 12,00,000"
    }
]

@app.route("/")
def hello_apoorva():
    return render_template("home.html", jobs=JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
