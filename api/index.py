from flask import Flask
from flask_cors import CORS
from routes.insignias_routes import insignias_bp
from routes.educandos_routes import educandos_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(insignias_bp)
app.register_blueprint(educandos_bp)

@app.route("/")
def hello_world():
    return {"message": "Hello, World!"}, 200

if __name__ == "__main__":
    app.run(debug=True)