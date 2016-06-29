currentTime = input("What's the current time (24 Hours clock) ? ")
delayTime = input("Alarm must ring after how many hours ? ")
waitTime = (int(currentTime) + (int(delayTime) % 24))%24
print("Alarm time will be", waitTime, "hours.")
