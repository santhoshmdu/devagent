from flask import Blueprint, render_template, request
from .groq_client import call_groq_api, PROMPT_OPTIMIZER_PROMPT

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    user_input = ""
    optimized_prompt = ""
    code_output = ""

    if request.method == 'POST':
        user_input = request.form['prompt']
        optimized_prompt = call_groq_api(PROMPT_OPTIMIZER_PROMPT, user_input)
        code_output = call_groq_api("You are a helpful AI coding assistant.", optimized_prompt)

    return render_template('index.html',
                           user_input=user_input,
                           optimized_prompt=optimized_prompt,
                           code_output=code_output)
