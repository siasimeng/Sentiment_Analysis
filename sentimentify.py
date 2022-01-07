from flask import Flask, render_template, request

from app.sentiment_app import SentimentApp
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        url = request.form.get('url')
        
        try:
            sp = SentimentApp(url)
            result = sp.run()
            return render_template('result.html', result=result, error=None)
        except Exception as e:
            print(e)
            return render_template('main.html', error=e)
    return render_template('main.html', error=None)

if __name__ == '__main__':
    app.run()
