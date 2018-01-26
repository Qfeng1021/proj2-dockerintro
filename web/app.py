from flask import Flask
from flask import render_template
from flask import abort


app = Flask(__name__)
symbols = ["..", "~", "//"]
@app.route("/<path:path>")
@app.route("/", defaults = {"path": ""})
@app.route("/error")


def hello(path=None):
    if path is None:
        return("UOCIS docker demo")
    elif path[-5:] == ".html" or path[-4:] == ".css":
        if any(m in path for m in symbols):
            abort(403)
        elif path == "trivia.html" or path == "trivia.css":
            return render_template(path), 200
        else:
            abort(404)
    else:
        abort(403)
            

    
@app.errorhandler(404)
def error_404(error):
    return render_template("404.html"), 404

@app.errorhandler(403)
def error_403(error):
    return render_template("403.html"), 403

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
