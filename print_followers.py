import instaloader
from datetime import date
import sys

L = instaloader.Instaloader()

if len(sys.argv) == 1:
    print("username not given")
    sys.exit()
USER = sys.argv[1]
PROFILE = USER

# Load session previously saved with `instaloader -l USERNAME`:
L.load_session_from_file(USER)

profile = instaloader.Profile.from_username(L.context, PROFILE)
followers = set(profile.get_followers())

today = date.today()
file_name = "users/{}/{}_{}".format(USER, USER, today)

with open(file_name, 'w') as file:
    for f in followers:
        print(f.username, f.userid, file=file)


