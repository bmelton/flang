from flask import Flask, jsonify, request, send_from_directory
app = Flask(__name__, static_url_path='')


@app.route('/')
def send_index():
    return send_from_directory('./static/', 'index.html')


@app.route('/api/resource1')
def hello_world():
    # Replace this with whatever data you parse from the DB or whatever
    output = {}
    output["key1"] = "value 1"
    output["key2"] = "value 2"
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)
