from flask import Flask, jsonify
import datetime, socket

app = Flask(__name__)

@app.route('/api/v1/info')
def info():
    return jsonify({
        'time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'hostname': socket.gethostname(),
    })

@app.route('/api/v1/health')
def health():
    return jsonify({'status': 'up', 'version': 'v3'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)