usernames = ['luka', 'ajax', 'martha']
sent_messages = []


def show_messages(names):
    for name in names:
        msg = f"Hi, {name.title()}."
        print(msg)


show_messages(usernames)

def sending_messages(names):
    for name in names:
        msg = f"Hi, {name.title()}."
        print(msg)
        sent_messages.append(msg)



sending_messages(usernames)
print(usernames)
print(sent_messages)
