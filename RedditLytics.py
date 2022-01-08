from flask import Flask, render_template, request

from app.sentiment_app import SentimentApp
from config import Config
from io import BytesIO
import base64
import matplotlib.pyplot as plt
import numpy as np


app = Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        url = request.form.get('url')
        
        try:
            sp = SentimentApp(url)
            result = sp.run()
            img = BytesIO()
            
            positive = result.positive
            negative = result.negative

            labels = ['Positive','Negative']
            values = np.array([positive,negative])
            myexplode = [0.1, 0]
            mycolors = ["blue", "red"]

            fig,ax = plt.subplots(figsize=(6,5))
            ax.pie(values, labels = labels, explode = myexplode, shadow = True, colors = mycolors)
            ax.legend()
            ax.set_title("Positive vs Negative Text(%)")

            plt.savefig(img, format='png')
            plt.close()
            img.seek(0)
            plot_url = base64.b64encode(img.getvalue()).decode('utf8')
            return render_template('result.html', result=result, plot_url=plot_url, error=None)
        
        except Exception as e:
            print(e)
            return render_template('main.html', error=e)
    return render_template('main.html', error=None)


if __name__ == '__main__':
    app.run()
