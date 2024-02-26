from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'event night',
    'eventtime': '2023-01-01',
    'message': 'Welcome To The Best Model  Winner Contest ',
}, {
    'id': 2,
    'title': 'event day',
    'eventtime': '2023-01-02',
    'message': 'Welcome To The Best Model  Winner Contest 12',
}, {
    'id': 3,
    'title': 'event morning',
    'eventtime': '2023-01-03',
    'message': 'Welcome To The Best Model  Winner Contest 122',
}, {
    'id': 4,
    'title': 'event mid',
    'eventtime': '2023-01-04',
    'message': 'Welcome To The Best Model  Winner Contest 1256',
}, {
    'id': 5,
    'title': 'event new',
    'eventtime': '2024-02-06',
    'message': ' Contest 1256',
    'categori': "sport"
}]


@app.route("/")
def home_page():
  return render_template('index.html', jobs=JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)
