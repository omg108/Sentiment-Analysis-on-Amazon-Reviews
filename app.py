import os
import pandas as pd
from flask import Flask, render_template, request, send_file, redirect, url_for, session
import joblib
import torch
from transformers import DistilBertForSequenceClassification, DistilBertTokenizerFast

# ----------------------------
# Flask setup
# ----------------------------
app = Flask(__name__)
app.secret_key = "supersecretkey"  # required for sessions
app.config["UPLOAD_FOLDER"] = "uploads"
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# ----------------------------
# Load models
# ----------------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

models = {
    "distilbert": {
        "model": DistilBertForSequenceClassification.from_pretrained("models").to(device).eval(),
        "tokenizer": DistilBertTokenizerFast.from_pretrained("models"),
        "type": "transformer"
    },
    "multinb": {
        "model": joblib.load("models/CountVectorizer_MultinomialNB_based.pkl"),
        "type": "sklearn"
    },
    "basic": {
        "model": joblib.load("models/basic_alexa_review_model.pkl"),
        "type": "sklearn"
    }
}

# ----------------------------
# Label map
# ----------------------------
label_map = {
    2: "Negative 😞",
    1: "Neutral 😐",
    0: "Positive 😄"
}

label_map2 = {
    2: "Negative",
    1: "Neutral",
    0: "Positive"
}

# ----------------------------
# Prediction function
# ----------------------------
def predict_sentiment(text, model_choice):
    model_info = models.get(model_choice)
    if not model_info:
        return "Invalid model"

    model_type = model_info["type"]

    if model_type == "transformer":
        tokenizer = model_info["tokenizer"]
        model = model_info["model"]

        encodings = tokenizer(
            text,
            truncation=True,
            padding=True,
            max_length=128,
            return_tensors="pt"
        )
        input_ids = encodings["input_ids"].to(device)
        attention_mask = encodings["attention_mask"].to(device)

        with torch.no_grad():
            outputs = model(input_ids, attention_mask=attention_mask)
            logits = outputs.logits
            predicted_class = torch.argmax(logits, dim=1).item()

        return predicted_class

    else:  # sklearn models
        model = model_info["model"]
        pred = model.predict([text])[0]
        return pred

# ----------------------------
# Routes
# ----------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    download_link = None

    if request.method == "POST":
        # get model choice from form
        model_choice = request.form.get("model")

        # if selected, save in session
        if model_choice:
            session["model_choice"] = model_choice
        else:
            # fallback to session model if already selected
            model_choice = session.get("model_choice")

        if not model_choice:
            result = "Error: Please select a model."
            return render_template("index.html", result=result)

        # -------- Single review prediction --------
        review_text = request.form.get("review")
        if review_text:
            pred = predict_sentiment(review_text, model_choice)
            result = label_map[pred]

        # -------- CSV upload prediction --------
        file = request.files.get("file")
        if file and file.filename.endswith(".csv"):
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            df = pd.read_csv(filepath)

            if "review" not in df.columns:
                result = "Error: CSV must contain a column named 'review'."
            else:
                preds = []
                for text in df["review"].astype(str):
                    preds.append(predict_sentiment(text, model_choice))

                df["Pred_sentiment"] = [label_map2[x] for x in preds]

                output_path = os.path.join(app.config["UPLOAD_FOLDER"], "predicted.csv")
                df.to_csv(output_path, index=False)
                result = "CSV processed successfully!"
                download_link = url_for("download_file")

    # pass currently selected model to template
    return render_template(
        "index.html",
        result=result,
        download_link=download_link,
        selected_model=session.get("model_choice")
    )

# -------- Download route for predicted CSV --------
@app.route("/download")
def download_file():
    output_path = os.path.join(app.config["UPLOAD_FOLDER"], "predicted.csv")
    if os.path.exists(output_path):
        return send_file(output_path, as_attachment=True)
    return redirect(url_for("index"))

# ----------------------------
# Run the server
# ----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
