from flask import Flask, render_template, request

from app.sentiment_app import SentimentApp
from config import Config
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

            plt.savefig('/var/www/uploads/plot.png')
            return render_template('result.html', result=result, url='/var/www/uploads/plot.png', error=None)
        except Exception as e:
            print(e)
            return render_template('main.html', error=e)
    return render_template('main.html', error=None)


if __name__ == '__main__':
    app.run()
