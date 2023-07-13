from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def leaderboard():
    leaderboard = []
    with open('leaderboard_results.txt', 'r') as f:
        next(f)  # Skip the header line
        for line in f:
            group_name, profile, time = line.strip().split('\t')
            leaderboard.append((group_name, profile, time))
    return render_template('leaderboard.html', leaderboard=leaderboard)

if __name__ == '__main__':
    app.run(host='localhost', port=8000)

# USE THE FOLLOWING LINE IN THE TERMINAL TO RUN THIS CODE!!
# python app.py