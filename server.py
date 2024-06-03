# server.py

from app import create_app

app = create_app()

@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('app/static/assets', path)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('app/static/js', path)

@app.route('/interactive-video/<path:path>')
def send_interactive_video(path):
    return send_from_directory('app/static/interactive-video', path)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
