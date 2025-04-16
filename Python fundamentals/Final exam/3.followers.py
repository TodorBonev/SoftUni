followers = {}
follower_order = []

while True:
    command = input().split(": ")
    action = command[0]

    if action == "Log out":
        break

    username = command[1]

    if action == "New follower":
        if username not in followers:
            followers[username] = {"likes": 0, "comments": 0}
            follower_order.append(username)
    elif action == "Like":
        count = int(command[2])
        if username not in followers:
            followers[username] = {"likes": count, "comments": 0}
            follower_order.append(username)
        else:
            followers[username]["likes"] += count
    elif action == "Comment":
        if username not in followers:
            followers[username] = {"likes": 0, "comments": 1}
            follower_order.append(username)
        else:
            followers[username]["comments"] += 1
    elif action == "Blocked":
        if username in followers:
            del followers[username]
            follower_order.remove(username)
        else:
            print(f"{username} doesn't exist.")

print(f"{len(followers)} followers")

for follower in follower_order:
    total_likes_comments = followers[follower]["likes"] + followers[follower]["comments"]
    print(f"{follower}: {total_likes_comments}")
