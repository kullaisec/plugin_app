from flask import Flask, request
from loader import load_plugin

app = Flask(__name__)

@app.route("/run")
def run():
    plugin = request.args.get("plugin")
    action = request.args.get("action")

    # user controls both plugin + action
    return load_plugin(plugin, action)

if __name__ == "__main__":
    app.run(debug=True)
