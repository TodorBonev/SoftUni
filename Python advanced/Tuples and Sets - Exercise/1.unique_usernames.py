def unique_usernames():
    unique_names = {input().strip() for _ in range(int(input()))}
    print("\n".join(unique_names))

unique_usernames()
