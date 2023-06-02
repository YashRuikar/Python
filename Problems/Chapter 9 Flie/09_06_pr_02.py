def game():
    return 84

score = game()
with open("highscore.txt") as f:
    highScoreStr = f.read()

if highScoreStr == '':
    with open("highscore.txt", "w") as f:
        f.write(str(score))

elif highScoreStr<score :
    with open("highscore.txt", 'w') as f:
        f.write(str(score))
