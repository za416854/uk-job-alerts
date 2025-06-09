import requests

def send_telegram_message(bot_token, chat_id, jobs):
    message = "📢 今日 UK 軟體職缺更新：\n\n"
    for job in jobs[:10]:  # 最多顯示 5 筆
    # for job in jobs:
        message += f"🔹 {job['title']}\n{job['url']}\n\n"

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("✅ 成功發送通知！")
    else:
        print("❌ 發送失敗", response.text)
        

