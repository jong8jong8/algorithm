import random

def generate_string(str_len):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    alph_len = len(alphabet)
    str_gen = ""
    for i in range(str_len):
        str_gen = str_gen + alphabet[random.randrange(alph_len)]
    return str_gen

def score(str_goal, str_test):
    score_num = 0
    goal_len = len(str_goal)
    for i in range(goal_len):
        if str_goal[i] == str_test[i]:
            score_num = score_num + 1  # score_num += 1
    return score_num / goal_len

def main():
    str_goal = "hi yo"
    goal_len = len(str_goal)
    str_test = generate_string(goal_len)
    best_score = 0
    new_score = score(str_goal, str_test)
    while new_score < 1:
        if new_score > best_score:
            best_score = new_score
            print(f"{best_score:5.3f} {str_test}")
        str_test = generate_string(goal_len)
        new_score = score(str_goal, str_test)
    print(f"The final result: {str_test}")


main()
