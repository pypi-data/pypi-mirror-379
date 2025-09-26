import requests

def rocloud_game_info(universe_id, var_name="robloxgameinfo"):
    r = requests.get(f"https://games.roblox.com/v1/games?universeIds={universe_id}")
    globals()[var_name] = r.json()["data"][0] if r.status_code == 200 else {}
    return globals()[var_name]

def rocloud_thumbnail_game(universe_id, var_name="robloxgamethumbnail"):
    url = f"https://www.roblox.com/asset-thumbnail/image?assetId={universe_id}&width=420&height=420&format=png"
    globals()[var_name] = url
    return url
