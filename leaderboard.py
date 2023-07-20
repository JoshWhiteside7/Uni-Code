import random

def generate_random_time():
    if random.random() < 0.05:  # 5% chance for "Did Not Finish"
        return "Did Not Finish"
    minutes = random.randint(45, 89)
    seconds = random.randint(0, 59)
    hours = minutes // 60
    minutes %= 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def get_random_word(filename):
    with open(filename, "r") as file:
        words = file.read().splitlines()
        return random.choice(words)

def get_group_number(profile):
    if profile == "Date Night":
        return 2
    elif profile == "Corporate Event":
        return random.randint(5, 10)
    elif profile == "Over 21 (age)" or profile == "Under 21 (age)" or profile == "Intergenerational":
        return random.randint(2, 10)
    else:
        return 0  # Default case if the profile doesn't match any specific group number logic

group_profiles = ["Corporate Event", "Date Night", "Over 21 (age)", "Under 21 (age)", "Intergenerational"]

leaderboard_times = []
group_names = []

for _ in range(100):
    time = generate_random_time()
    profile = random.choice(group_profiles)
    group_number = get_group_number(profile)
    adjective = get_random_word("adjectives.txt")  # Get a random adjective
    noun = get_random_word("nouns.txt")  # Get a random noun
    group_name = f"{adjective} {noun}"
    group_names.append(group_name)
    leaderboard_times.append((group_name, profile, group_number, time))

leaderboard_sorted = sorted(leaderboard_times, key=lambda x: x[3])

with open("leaderboard_results.txt", "w") as file:
    file.write("Team\tProfile\tTime\n")
    for entry in leaderboard_sorted:
        group_name, profile, group_number, time = entry
        file.write(f"{group_name}\t{profile}\t{group_number}\t{time}\n")