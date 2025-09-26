import requests

def rocloud_groups_list(userid, var_name="robloxgroupslist"):
    r = requests.get(f"https://groups.roblox.com/v2/users/{userid}/groups/roles")
    globals()[var_name] = r.json().get("data", []) if r.status_code == 200 else []
    return globals()[var_name]

def rocloud_group_roles(groupid, userid, var_name="robloxgrouprole"):
    r = requests.get(f"https://groups.roblox.com/v1/groups/{groupid}/users/{userid}")
    globals()[var_name] = r.json().get("role", {}).get("name") if r.status_code == 200 else None
    return globals()[var_name]

def rocloud_join_requests(groupid, cookie, var_name="robloxjoinrequests"):
    headers = {"Cookie": f".ROBLOSECURITY={cookie}"}
    r = requests.get(f"https://groups.roblox.com/v1/groups/{groupid}/join-requests", headers=headers)
    globals()[var_name] = r.json().get("data", []) if r.status_code == 200 else []
    return globals()[var_name]

def rocloud_accept_request(groupid, userid, cookie, var_name="robloxrequestaccepted"):
    headers = {"Cookie": f".ROBLOSECURITY={cookie}"}
    r = requests.post(f"https://groups.roblox.com/v1/groups/{groupid}/join-requests/users/{userid}", headers=headers, data={})
    globals()[var_name] = (r.status_code == 200)
    return globals()[var_name]
