from flask import Flask, request, jsonify

app: Flask = Flask(__name__)

qa = {
    'question 1': 'answer 1',
    'question 2': 'answer 2',
}


@app.route('/')
def get():
    return "OK"


@app.route('/model/', methods=['POST'])
def post():
    request_data = request.get_json()
    question = request_data['question']

    return jsonify(reply(question))


def reply(q):
    return qa.get(q, 'not implemented')


if __name__ == '__main__':
    app.run(debug=True)
