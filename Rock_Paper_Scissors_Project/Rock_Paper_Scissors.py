import random
playing = True

user_score = 0
bot_score = 0
tie_score = 0

user = user_score
bot = bot_score
tie = tie_score

while playing:
    print("Rock-Paper-Scissors:")
    user = input().capitalize()



    lst = ["Rock", "Paper", "Scissors"]
    bot = random.choice(lst)
    print(bot)


    if user == bot:
        print("Tie")
        tie_score += 1
    elif user == "Rock" and bot == "Scissors":
        print("User Wins")
        user_score += 1
    elif user == 'Rock' and bot == 'Paper':
        print("Bot wins")
        bot_score += 1
    elif user == 'Paper' and bot == "Scissors":
        print("Bot wins")
        bot_score += 1
    elif user == 'Paper' and bot == "Rock":
        print("User wins")
        user_score += 1
    elif user == 'Scissors' and bot == "Paper":
        print("User wins")
        user_score += 1
    elif user == 'Scissors' and bot == "Rock":
        print("Bot wins")
        bot_score += 1



    print("User Score: ", user_score)
    print("Bot Score: ", bot_score)
    print("Tie: ", tie_score)

    print("Play Again? (Y/N) ")
    play_again = input().capitalize()
    if play_again != 'Y':
        break
if user_score > bot_score:
    print("USER WINS 🏆")
elif bot_score > user_score:
    print("Bot wins 🤖❌")
else:
    print("Tie Game (×_×)")

print("Scorecard 📊:","User:",user_score,"Bot Score:",bot_score, "Tie:",tie_score)














