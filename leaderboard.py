import random

def generate_random_time():
    hours = random.randint(0, 1)
    minutes = random.randint(0, 59)
    seconds = random.randint(0, 59)
    milliseconds = random.randint(0, 999)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}"

def get_random_word(filename):
    with open(filename, "r") as file:
        words = file.read().splitlines()
        return random.choice(words)

group_profiles = ["Corporate Event", "Date Night", "Over 21 (age)", "Under 21 (age)", "Intergenerational"]

leaderboard_times = []
group_names = []

for _ in range(100):
    time = generate_random_time()
    profile = random.choice(group_profiles)
    adjective = get_random_word("adjectives.txt")  # Get a random adjective
    noun = get_random_word("nouns.txt")  # Get a random noun
    group_name = f"{adjective} {noun}"
    group_names.append(group_name)
    leaderboard_times.append((group_name, profile, time))

leaderboard_sorted = sorted(leaderboard_times, key=lambda x: x[2])

with open("leaderboard_results.txt", "w") as file:
    file.write("Team\tProfile\tTime\n")
    for entry in leaderboard_sorted:
        group_name, profile, time = entry
        file.write(f"{group_name}\t{profile}\t{time}\n")