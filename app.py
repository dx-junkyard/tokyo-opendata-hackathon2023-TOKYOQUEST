from flask import Flask, jsonify

app = Flask(__name__)

def mock():
    events = [
        {
            "date": "2023-08-25",
            "address": "東京都新宿区西新宿二丁目8番1号",
            "media": "Website",
            "detail": "This is event 1",
            "people": 200
        },
        {
            "date": "2023-08-26",
            "address" : "東京都墨田区押上１丁目１−２",
            "media": "TV",
            "detail": "This is event 2",
            "people": 150
        }
    ]
    return events

@app.route('/api/events')
def get_events():
    res = mock()
    return jsonify(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)