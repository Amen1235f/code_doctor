from flask import Flask, jsonify
from routes import routes

app = Flask(__name__)
app.register_blueprint(routes)

@app.route('/')
def home():
    return jsonify({'message': 'Flask backend is running!'})

if __name__ == '__main__':
    app.run(debug=True)
