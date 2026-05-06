import tkinter as tk

redTeamScore = 0
blueTeamScore = 0

scorecard = {
    "blue": blueTeamScore,
    "red": redTeamScore
}

root = tk.Tk()

root.title("Score Counter")
root.configure(background="white")
root.minsize(200, 200)
root.maxsize(500, 500)
root.geometry("400x420+300+100")

tk.Label(root, text="Welcome to the Basketball Score Counter!")

main = tk.Frame(root)
redTeam = tk.Label(main, text="00").grid(row=0, column=0)
blueTeam = tk.Label(main, text="00").grid(row=0, column=2)

gameTime = 0
gameTimeLabel = tk.Label(main, text=f"{gameTime % 60} mins {gameTime - (60 * (gameTime % 60))}").grid(row=0, column=1)
gameRunning = False

def tick(time, duration):
    global gameTimeLabel
    currentTime = 0
    while currentTime < duration:
        gameTimeLabel.config(text=f"{time % 60} mins {time - (60 * (time % 60))}")
        time.sleep(1)
        time += 1
        currentTime += 1


def score(team, value):
    global scorecard
    currentScore = scorecard[team]
    if gameRunning is True:
        currentScore += value
    scorecard[team] = currentScore

redScore2 = tk.Button(main, text="+2", command=score("red", 2))
redScore3 = tk.Button(main, text="+3", command=score("red", 3))
blueScore2 = tk.Button(main, text="+2", command=score("red", 2))
blueScore3 = tk.Button(main, text="+3", command=score("red", 3))

def mainF(status):
    global gameRunning
    global gameTime

    if status:
        gameRunning = True
        tick(gameTime, 720)
    if not status:
        global scorecard

        gameRunning = False
        for team in scorecard.keys():
            scorecard[team] = 0
        gameTime = 0
    

playBtn = tk.Button(main, "Start Timer", command=mainF(True))
ResetBtn = tk.Button(main, "Reset Game", command=mainF(False))

root.mainloop()
    
