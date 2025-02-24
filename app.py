from flask import Flask, jsonify, request
import subprocess
import json

app = Flask(__name__)

def is_valid_json(json_string):
    """
    Checks if a string is valid JSON before parsing it.

    Args:
        json_string: The string to check.

    Returns:
        True if the string is valid JSON, False otherwise.
    """
    try:
        json.loads(json_string)
        return True
    except json.JSONDecodeError:
        return False

@app.route('/api', methods=['GET'])
def api():
    return jsonify({"message": "API working"})

@app.route('/instagram_post/<shortcode>', methods=['GET'])
def getInstaPost(shortcode):
    try:
        # Run the external Python script with the given parameter
        result = subprocess.run(['python', 'custom-script.py',shortcode], capture_output=True, text=True)
        res=result.stdout.strip()
        if is_valid_json(res):
        # Check if the script ran successfully
            if result.returncode == 0:
                response = {
                    "status": "success",
                    "output": json.loads(res)
                 }
            else:
                response = {
                "status": "error",
                "message": res
                }
        else:
            response = {
            "status": "error",
            "message": res
        }
        
    except Exception as e:
        response = {
            "status": "error",
            "message": str(e)
        }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)