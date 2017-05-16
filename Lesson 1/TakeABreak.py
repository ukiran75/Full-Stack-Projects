import webbrowser
import time
breaks_count = 0
total_breaks = 3
while(breaks_count < total_breaks):
    time.sleep(10)
    print("Break Started at " + time.ctime())
    webbrowser.open("https://www.youtube.com/watch?v=papuvlVeZg8")
    breaks_count+=1
