from distutils.command.upload import upload
from bettercomm import uploadGJComment
import time

print("Comment Sender by Sevenworks\n\n")
print("Use ^^ to bypass the word filter.\n")
print("Example: I love this level so fu^^cking much! lol\n\n\n\n")

un = input("Username: ")
pw = input("Password: ")
lvlid = input("Level ID: ")

def PostComment(commentText):
    uploadGJComment(un,pw,commentText,"69",lvlid)

while True:
    b = "‎"

    comInput = input("Comment: ")
    com = comInput.replace("^^", b)

    PostComment(com)
    time.sleep(1)
