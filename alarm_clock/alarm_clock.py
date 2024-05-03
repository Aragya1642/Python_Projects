from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    timeElapsed = 0

    print(CLEAR)
    while timeElapsed < seconds:
        time.sleep(1)
        timeElapsed += 1

        timeLeft = seconds - timeElapsed
        minutesLeft = timeLeft // 60
        secondsLeft = timeLeft % 60

        print(f"{CLEAR_AND_RETURN}Alarm will sound in:\n{minutesLeft:02d}:{secondsLeft:02d}")
    playsound("myAlarm.mp3")

# Main Program
myMinutes = int(input("How many minutes would you want on you alarm?\n"))
mySeconds = int(input("How many seconds would you want on you alarm?\n"))
mySeconds = mySeconds + (myMinutes * 60)
alarm(mySeconds)