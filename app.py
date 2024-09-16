from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [
  {
    'id':1,
    'title': 'Backend Developer',
    'salary' : 'Rs. 1,00,000',
    'location' : 'Bangalore, India'
  },
  {
    'id':2,
    'title': 'Software Engineer',
    'salary' : 'Rs. 15,00,000',
    'location' : 'Delhi, India'
  },
  {
    'id':3,
    'title': 'Data Scientist',
    'salary' : 'Rs. 20,00,000',
    'location' : 'Chennai, India'
  },
  {
    'id':4,
    'title': 'Frontend Engineer',
    'salary' : 'Rs. 12,00,000',
    'location' : 'Remote'
  },
  {
    'id':5,
    'title': 'Data Analyst',
    'salary' : 'Rs. 1,00,000',
    'location' : 'Delhi, India'
  }
]


@app.route('/')
def hello_world():
  return render_template('home.html',jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
