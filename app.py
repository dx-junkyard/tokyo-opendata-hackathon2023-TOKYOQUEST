from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/events')
def get_events():
    events = [
        {
            "date": "2023-08-25",
            "location": {"latitude": 35.6895, "longitude": 139.6917},
            "media": "Website",
            "detail": "This is event 1",
            "people": 200
        },
        {
            "date": "2023-08-26",
            "location": {"latitude": 34.6937, "longitude": 135.5023},
            "media": "TV",
            "detail": "This is event 2",
            "people": 150
        }
    ]
    return jsonify(events)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)