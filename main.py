from Post import Post

all_posts_archive = []

Post("R2D2", "Bleep Bloop, Bloop Beep?")


# your code here
def changeName():
    global username
    userNameTest = input("Name : ")
    if len(userNameTest) > 20:
        print("Name must not be longer than 20 characters!")
    elif len(userNameTest) < 1:
        print("Name must have at least 1 character!")
    else:
        username = userNameTest


def printPosts():
    global all_posts_archive
    for post in all_posts_archive:
        print(post)


def prompt():
    global username
    global all_posts_archive
    while True:
        try:
            option = int(
                input("""
        What would you like to do?

        1 - New Post
        2 - Clear Posts
        3 - Change Username
        4 - Read Posts

        9 - Quit
        """))
        except ValueError:
            print("")
            continue
        if option == 1:
            printPosts()
            postInfo = input(str("%s : " % (username)))
            all_posts_archive.append(Post(username, postInfo))
        elif option == 2:
            isSure = input("Are you sure? (y/n) : ")
            if isSure == "y":
                all_posts_archive = []
            else:
                print("Aborted")
                continue
        elif option == 3:
            changeName()
        elif option == 4:
            printPosts()
        elif option == 9:
            quit('User initiated Quit')
            break
        else:
            print('Not an option!')
            continue


username = "anon"
prompt()
