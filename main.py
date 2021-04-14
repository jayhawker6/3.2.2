from Post import Post

all_posts_archive = []

Post("R2D2", "Bleep Bloop, Bloop Beep?")

# your code here
def printPost():
    for post in all_posts_archive:
        print(post)
while True:
    try:
        option = int(
            input("""
    What would you like to do?
    
    1 - View posts
    2 - Create posts
    
    9 - Quit
    """))
    except ValueError:
        print("")
        continue
    if option == 1:
        printPost()
    elif option == 2:
        continue
    elif option == 9:
        quit('User initiated Quit')
        break
    else:
        print('Not an option!')
        continue