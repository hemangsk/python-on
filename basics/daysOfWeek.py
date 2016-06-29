"""
It is possible to name the days 0 through 6 where day 0 is Sunday and day 6 is Saturday. If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you return home after 10 nights. Write a general version of the program which asks for the starting day number, and the length of your stay, and it will tell you the number of day of the week you will return on.

"""

starting = input("Starting Day ?")
lengthOfStay = input("Length of stay ?")

returnDay = (int(starting) % 7 + int(lengthOfStay)%7 ) % 7

print("Day of return", returnDay)
