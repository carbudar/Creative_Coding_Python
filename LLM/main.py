from flask import Flask, render_template, request  
import torch 
from transformers import pipeline  

app = Flask(__name__)


hf_name = 'google/flan-t5-small'
generator = pipeline(
    "text2text-generation",
    hf_name,
    device=0 if torch.cuda.is_available() else -1,
)

# Poem generation function
def generate_poem(word):
    prompt = f"Write a short 4-line poem about '{word}'."

    result = generator(
        prompt,
        max_length=60,
        num_return_sequences=1,
        temperature=0.5, 
        top_k=50,
        top_p=0.9,
        no_repeat_ngram_size=3,
    )

    return result[0]['generated_text']


@app.route('/', methods=['GET', 'POST'])
def index():
    poem_text = None

    if request.method == 'POST':
        user_word = request.form['word_input'].strip()

        if user_word:
            try:
                poem_text = generate_poem(user_word)
            except Exception as e:
                poem_text = f"Error generating poem: {str(e)}"

    return render_template('index.html', poem=poem_text)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
