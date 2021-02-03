from datetime import date, timedelta
from os import path
import sys

if len(sys.argv) == 1:
    print("username not given")
    sys.exit()

user = sys.argv[1]

followers_dict = dict()
today = date.today()
yesterday = today - timedelta(days=1)

todays_list = "users/{}/{}_{}".format(user, user, today)
yesterdays_list = "users/{}/{}_{}".format(user, user, yesterday)
while (path.exists(yesterdays_list) == False) or (yesterday + timedelta(days=30) < today):
    yesterday -= timedelta(days=1)
    yesterdays_list = "users/{}/{}_{}".format(user, user, yesterday)

with open(todays_list, 'r') as tl:
    while True:
        line = tl.readline().split()
        if line == []:
            break
        followers_dict[line[1]] = line[0] # add userID : userName to dict, userID is key

print("Report for {} from {}: ".format(user, today), end="")
unfollows = 0
with open(yesterdays_list, 'r') as yl:
    while True:
        line = yl.readline().split()
        if line == []:
            break
        if line[1] not in followers_dict:
            print(line[0] + " stopped following you")
            unfollows += 1

if unfollows == 0:
    print("All your followers are there, don't worry")

