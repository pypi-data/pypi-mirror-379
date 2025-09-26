import requests

def rocloud_send_message(cookie, recipient_userid, subject, message, var_name="robloxmessagesent"):
    headers = {"Cookie": f".ROBLOSECURITY={cookie}"}
    payload = {
        "recipientId": recipient_userid,
        "subject": subject,
        "body": message
    }
    r = requests.post("https://privatemessages.roblox.com/v1/messages/send", headers=headers, json=payload)
    globals()[var_name] = (r.status_code == 200)
    return globals()[var_name]
