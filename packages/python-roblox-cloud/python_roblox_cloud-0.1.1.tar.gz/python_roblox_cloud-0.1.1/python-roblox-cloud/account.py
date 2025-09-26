import requests

BASE_URL = "https://www.roblox.com"

def rocloud_cookie_account_valid(cookie, var_name="robloxcookievalid0x09",
                                 invalid_text="Invalid cookie", valid_text="Valid cookie"):
    headers = {"Cookie": f".ROBLOSECURITY={cookie}"}
    r = requests.get(f"{BASE_URL}/my/settings/json", headers=headers)
    globals()[var_name] = valid_text if r.status_code == 200 else invalid_text
    return globals()[var_name]

def rocloud_robux_balance(cookie, var_name="robloxrobuxbalance"):
    headers = {"Cookie": f".ROBLOSECURITY={cookie}"}
    r = requests.get("https://economy.roblox.com/v1/user/currency", headers=headers)
    if r.status_code == 200:
        globals()[var_name] = r.json().get("robux", 0)
    else:
        globals()[var_name] = None
    return globals()[var_name]

def rocloud_premium_status(cookie, var_name="robloxpremiumstatus"):
    headers = {"Cookie": f".ROBLOSECURITY={cookie}"}
    r = requests.get("https://premiumfeatures.roblox.com/v1/users/authenticated", headers=headers)
    globals()[var_name] = (r.status_code == 200)
    return globals()[var_name]
