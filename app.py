from flask import Flask, render_template
import random
app = Flask(__name__)

def get_group_number(profile):
    if profile == "Date Night":
        return 2
    elif profile == "Corporate Event":
        return random.randint(5, 10)
    elif profile == "Over 21 (age)" or profile == "Under 21 (age)" or profile == "Intergenerational":
        return random.randint(2, 10)
    else:
        return 0  # Default case if the profile doesn't match any specific group number logic

@app.route('/')
def leaderboard():
    leaderboard = []
    with open('leaderboard_results.txt', 'r') as f:
        next(f)  # Skip the header line
        for line in f:
            group_name, profile, time = line.strip().split('\t')
            group_number = get_group_number(profile)
            leaderboard.append((group_name, profile, group_number, time))
    return render_template('leaderboard.html', leaderboard=leaderboard)

if __name__ == '__main__':
    app.run(host='localhost', port=8000)

# USE THE FOLLOWING LINE IN THE TERMINAL TO RUN THIS CODE!!
# python leaderboard.py ; python app.py