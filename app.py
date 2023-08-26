from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/mock')
def mock_response():
    return jsonify({"message": "This is a mock response"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)