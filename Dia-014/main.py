import art
import game_data
import random

data = game_data.data


def get_random_index(database):
    random_index = random.randint(0, len(database) - 1)
    return random_index

def winner(database, index1, index2, user_guess):
    f1 = database[index1]['follower_count']
    f2 = database[index2]['follower_count']
    if f1 > f2:
        return 'a'
    elif f1 < f2:
        return 'b'
    else:
        return user_guess

def start_info(database):
    index_a = get_random_index(database)
    index_b = index_a
    while index_a == index_b:
        index_b = get_random_index(database)

    return index_a, index_b



def game_loop(data, index_a, index_b, score):
    game_over = False
    while not game_over:
        print(art.logo)

        print(f"Compare A: {data[index_a]['name']}, a {data[index_a]['description']}, from {data[index_a]['country']}.")

        print(art.versus)

        print(f"Compare B: {data[index_b]['name']}, a {data[index_b]['description']}, from {data[index_b]['country']}.")

        print("Score: ", score)
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        most_followers = winner(data, index_a, index_b, answer)
        if answer == most_followers:
            score += 1
            if most_followers == 'b':
                index_a = index_b
            index_b = get_random_index(data)
            while index_a == index_b:
                index_b = get_random_index(data)
        else:
            print("Wrong Answer!")
            print("Final score: ", score)
            game_over = True

score = 0
index_a, index_b = start_info(data)
game_loop(data, index_a, index_b, score)