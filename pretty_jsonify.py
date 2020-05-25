from flask import Flask, jsonify
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route("/")
def json_hello():
    return jsonify({x:x*x for x in range(5)}), 200

if __name__ == "__main__":
    app.run(debug=False)