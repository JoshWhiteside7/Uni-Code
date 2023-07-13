from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def leaderboard():
    with open('leaderboard_results.txt', 'r') as f:
        results = f.read()
    return render_template('templates.html', results=results)

if __name__ == '__main__':
    app.run(host='localhost', port=8000)

# USE THE FOLLOWING LINE IN THE TERMINAL TO RUN THIS CODE!!
# python app.py