from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Open Mobile</title>
    <style>
        body { margin: 0; padding: 0; overflow: hidden; background: #fff; }
        iframe { width: 100vw; height: 100vh; border: none; }
    </style>
</head>
<body>
    <iframe src="https://possibly-delicious-anaconda.cloudpub.ru/inarch"></iframe>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
