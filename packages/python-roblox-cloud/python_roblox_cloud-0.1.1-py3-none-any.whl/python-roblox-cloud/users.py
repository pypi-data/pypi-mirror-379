import requests

def rocloud_avatar_image(user_or_cookie, var_name="robloxavatarurl"):
    if user_or_cookie.startswith("n:"):
        username = user_or_cookie[2:]
        r = requests.get(f"https://api.roblox.com/users/get-by-username?username={username}")
        if r.status_code == 200:
            userid = r.json().get("Id")
        else:
            userid = None
    else:
        userid = user_or_cookie

    url = f"https://www.roblox.com/headshot-thumbnail/image?userId={userid}&width=420&height=420&format=png"
    globals()[var_name] = url
    return url

def rocloud_count_friends(user_or_cookie, var_name="robloxfriendscount"):
    r = requests.get(f"https://friends.roblox.com/v1/users/{user_or_cookie}/friends/count")
    globals()[var_name] = r.json().get("count", 0) if r.status_code == 200 else 0
    return globals()[var_name]

def rocloud_userid_from_name(nickname, var_name="robloxuserid"):
    nickname = nickname.replace("n:", "")
    r = requests.get(f"https://api.roblox.com/users/get-by-username?username={nickname}")
    globals()[var_name] = r.json().get("Id") if r.status_code == 200 else None
    return globals()[var_name]

def rocloud_name_from_userid(userid, var_name="robloxusername"):
    r = requests.get(f"https://users.roblox.com/v1/users/{userid}")
    globals()[var_name] = r.json().get("name") if r.status_code == 200 else None
    return globals()[var_name]

def rocloud_friends_list(userid, var_name="robloxfriendslist"):
    r = requests.get(f"https://friends.roblox.com/v1/users/{userid}/friends")
    globals()[var_name] = [u["name"] for u in r.json().get("data", [])] if r.status_code == 200 else []
    return globals()[var_name]
