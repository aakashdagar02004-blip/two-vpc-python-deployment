from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>My Python Application</h1>
    <p>Successfully deployed using Docker, Ansible and AWS EC2!</p>
    <p>Status: Running - Auto Deployment Test</p>
    """

@app.route("/health")
def health():
    return jsonify(status="healthy")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
