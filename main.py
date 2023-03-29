import openai
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Set up your OpenAI API key
openai.api_key = "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"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = get_gpt_response(prompt)
        return render_template("index.html", response=response)
    return render_template("index.html")
# Add this new route below the existing home() function
@app.route("/about")
def about():
    return render_template("about.html")
# Add this new route below the existing about() function
@app.route("/contact")
def contact():
    return render_template("contact.html")

def get_gpt_response(prompt):
    model_engine = "text-davinci-002" # Replace this with the desired GPT engine ID
    prompt = f"{prompt}\nAnswer:"

    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
