from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

# def get_group_number(profile):
#     if profile == "Date Night":
#         return 2
#     elif profile == "Corporate Event":
#         return random.randint(5, 10)
#     elif profile == "Over 21 (age)" or profile == "Under 21 (age)" or profile == "Intergenerational":
#         return random.randint(2, 10)
#     else:
#         return 0  # Default case if the profile doesn't match any specific group number logic

def assign_rank(leaderboard):
    ranked_leaderboard = []
    rank_names = ["1st", "2nd", "3rd"]
    for rank, entry in enumerate(leaderboard):
        if rank < 3:
            rank_name = rank_names[rank]
        else:
            rank_name = str(rank + 1) + "th"
        ranked_entry = (rank_name, *entry)
        ranked_leaderboard.append(ranked_entry)
    return ranked_leaderboard

@app.route('/leaderboard')
def leaderboard():
    leaderboard = []
    with open('leaderboard_results.txt', 'r') as f:
        next(f)  # Skip the header line
        for line in f:
            group_name, profile, group_number, time = line.strip().split('\t')
            # group_number = get_group_number(profile)
            leaderboard.append((group_name, profile, group_number, time))
    ranked_leaderboard = assign_rank(leaderboard)
    return render_template('leaderboard.html', leaderboard=ranked_leaderboard)

@app.route('/book')
def book():
    return render_template('book.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='localhost', port=8000)

# USE THE FOLLOWING LINE IN THE TERMINAL TO RUN THIS CODE!!
# python leaderboard.py ; python app.py