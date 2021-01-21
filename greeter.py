"""Functions"""


def greet_user(username):
    """Display simple greeting"""
    print("Hello, " + username + "!")


greet_user("jon")


def display_message(chapter_num):
    chapter_title = ""
    if chapter_num == 1:
        chapter_title = "variables"
    elif chapter_num == 2:
        chapter_title = "string"
    elif chapter_num == 3:
        chapter_title = "dictionary"

    if chapter_title == "":
        print("There's no such chapter number!")
    else:
        message = "This chapter talks about " + chapter_title
        print(message)


display_message(2)
display_message(0)
display_message("oo")
