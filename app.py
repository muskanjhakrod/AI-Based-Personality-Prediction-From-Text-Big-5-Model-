from flask import Flask, render_template, request
from model_utils import predict_personality

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    user_text = ""
    scores = None     # raw 0–100 scores
    levels = None     # Low / Medium / High
    summary = None    # text summary

    if request.method == "POST":
        user_text = request.form.get("user_text", "")
        scores, levels, summary = predict_personality(user_text)

    return render_template(
        "index.html",
        user_text=user_text,
        scores=scores,
        levels=levels,
        summary=summary
    )

if __name__ == "__main__":
    app.run(debug=True)
