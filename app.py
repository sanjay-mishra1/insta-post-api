from flask import Flask, jsonify, request
import subprocess
import json

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def api():
    return jsonify({"message": "Hello, World!"})

@app.route('/instagram_post/<shortcode>', methods=['GET'])
def getInstaPost(shortcode):
    try:
        # Run the external Python script with the given parameter
        result = subprocess.run(['python', 'custom-script.py',shortcode], capture_output=True, text=True)
        
        # Check if the script ran successfully
        if result.returncode == 0:
            response = {
                "status": "success",
                "output": json.loads(result.stdout.strip())
            }
        else:
            response = {
               result.stderr.strip()
            }
    except Exception as e:
        response = {
            "status": "error",
            "message": str(e)
        }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)