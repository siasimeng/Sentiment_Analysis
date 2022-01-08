from flask import Flask, render_template, request

from app.sentiment_app import SentimentApp
from config import Config
from io import BytesIO
import base64
import matplotlib.pyplot as plt


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
            left = [1, 2, 3, 4, 5]
            # heights of bars
            height = [10, 24, 36, 40, 5]
            # labels for bars
            tick_label = ['one', 'two', 'three', 'four', 'five']
            # plotting a bar chart
            plt.bar(left, height, tick_label=tick_label, width=0.8, color=['red', 'green'])

            # naming the y-axis
            plt.ylabel('y - axis')
            # naming the x-axis
            plt.xlabel('x - axis')
            # plot title
            plt.title('My bar chart!')

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
