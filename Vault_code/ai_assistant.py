from flask import Flask, render_template_string, request
from openai import OpenAI
import os
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()

# Get API key from environment for security
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

template = '''
<!doctype html>
<html>
<head>
    <title>AI Assistant</title>
    <style>
        body {
            background: linear-gradient(120deg, #b2fefa 0%, #efeffd 100%);
            color: #4B3869;
            font-family: 'Segoe UI', Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 520px;
            margin: 50px auto;
            background: #fff;
            border-radius: 20px;
            box-shadow: 0 8px 24px rgba(80,80,80,.09);
            padding: 32px 40px 20px 40px;
        }
        h2 {
            text-align: center;
            margin-bottom: 18px;
            font-weight: 700;
            color: #6533b4;
        }
        label {
            font-size: 1rem;
            font-weight: 500;
            margin-bottom: 4px;
            display: block;
            color: #374151;
        }
        select, textarea, input[type="submit"], input[type="radio"] {
            margin-top: 5px;
        }
        select, textarea {
            width: 100%;
            font-size: 1rem;
            padding: 8px;
            margin-bottom: 14px;
            border: 1px solid #bcccdc;
            border-radius: 8px;
            background: #f3f3fd;
            transition: border-color 0.2s;
        }
        select:focus, textarea:focus {
            border-color: #b16dfa;
            outline: none;
        }
        textarea {
            resize: vertical;
        }
        input[type="submit"], input[type="button"] {
            background: linear-gradient(90deg, #8457fe 0%, #6b7dfa 100%);
            color: white;
            font-weight: bold;
            border: none;
            border-radius: 8px;
            padding: 10px 0;
            width: 100%;
            cursor: pointer;
            margin-top: 10px;
            font-size: 1rem;
            box-shadow: 0 2px 10px rgba(140,140,220,.11);
        }
        input[type="submit"]:hover,
        input[type="button"]:hover {
            background: linear-gradient(90deg, #6b7dfa 0%, #8457fe 100%);
        }
        .response, .feedback-msg {
            background-color: #F1F5FA;
            border-radius: 10px;
            padding: 15px;
            margin: 20px 0;
            color: #3d2d6a;
            box-shadow: 0 0 6px #eee;
            font-size: 1.1rem;
        }
        hr {
            border: none;
            border-top: 2px solid #d6ddfd;
            margin: 32px 0 10px 0;
        }
        .feedback {
            margin: 10px 0;
            display: flex;
            align-items: center;
            gap: 15px;
        }
        .feedback label {
            font-weight: 500;
            color: #4B3869;
        }
        .feedback input[type="radio"] {
            accent-color: #6b7dfa;
            margin-left: 8px;
        }
        .thanks {
            background: #e6e6fa;
            padding: 8px 17px;
            border-radius: 7px;
            text-align: center;
            color: #461c6a;
            font-weight: 600;
            margin-bottom: 12px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>AI Assistant</h2>
        <form method="post">
            <label>Select function:</label>
            <select name="function">
                <option value="question">Answer a Question</option>
                <option value="summarize">Summarize Text</option>
                <option value="creative">Generate Creative Content</option>
            </select>

            <label>Your input/prompt:</label>
            <textarea name="user_input" rows="6" placeholder="Type your question, text to summarize, or creative idea..." required></textarea>

            <input type="submit" value="Get Response">
        </form>

        {% if response %}
            <hr>
            <h4 style="color:#6b7dfa;">AI Response:</h4>
            <div class="response">{{ response }}</div>
            <form method="post" class="feedback">
                <input type="hidden" name="function" value="{{ function }}">
                <input type="hidden" name="user_input" value="{{ user_input }}">
                <input type="hidden" name="response" value="{{ response }}">
                <label>Was this response helpful?</label>
                <input type="radio" name="feedback" value="yes" required> Yes
                <input type="radio" name="feedback" value="no" required> No
                <input type="submit" name="submit_feedback" value="Submit Feedback">
            </form>
        {% endif %}

        {% if feedback %}
            <div class="thanks">Thanks for your feedback!</div>
        {% endif %}
    </div>
</body>
</html>
'''

# Prompt templates for each mode
PROMPT_TEMPLATES = {
    "question": [
        "Answer the following question: {}",
        "Please provide a detailed answer: {}",
        "Respond briefly: {}"
    ],
    "summarize": [
        "Summarize this text: {}",
        "List key points of the following: {}",
        "Give a brief overview: {}"
    ],
    "creative": [
        "Write a story about: {}",
        "Compose a poem about: {}",
        "Generate an idea for a novel based on: {}"
    ]
}

def get_prompt(function, user_input):
    # Currently just uses the first template. You may randomize this if you like.
    template = PROMPT_TEMPLATES[function][0]
    return template.format(user_input)

def ai_response(function, user_input):
    prompt = get_prompt(function, user_input)
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    return completion.choices[0].message.content

@app.route('/', methods=['GET', 'POST'])
def index():
    response = None
    feedback = None
    function = ''
    user_input = ''

    if request.method == 'POST':
        if 'submit_feedback' in request.form:
            with open("feedback_log.txt", "a", encoding="utf-8") as f:
                f.write(
                    f"FUNCTION: {request.form['function']}\n"
                    f"USER_INPUT: {request.form['user_input']}\n"
                    f"RESPONSE: {request.form['response']}\n"
                    f"FEEDBACK: {request.form['feedback']}\n\n"
                )
            feedback = "Thank you for your feedback."
            response = request.form['response']
            function = request.form['function']
            user_input = request.form['user_input']
        else:
            function = request.form['function']
            user_input = request.form['user_input']
            response = ai_response(function, user_input)

    return render_template_string(
        template,
        response=response,
        feedback=feedback,
        function=function,
        user_input=user_input
    )

if __name__ == "__main__":
    app.run(debug=True)
