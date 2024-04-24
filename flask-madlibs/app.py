from flask import Flask, render_template, request
from stories import Story


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

@app.route("/")
def ask_questions():
    prompt = story.prompts
    return render_template("questions.html", prompt=prompt)



@app.route('/story', methods=['POST'])
def show_story():
    answers = {}
    for prompt in story.prompts:
        answers[prompt] = request.form[prompt]
    result = story.generate(answers)
    return render_template('story.html', result=result)







