def show_messages(names):
    for name in names:
        msg = f"Hi, {name.title()}."
        print(msg)

usernames = ['luka', 'ajax', 'martha']
show_messages(usernames)