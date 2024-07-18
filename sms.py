from twilio.rest import Client
from constants import (
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    FROM_NUMBER,
    TO_NUMBER,
    EMOJI_UP,
    EMOJI_DOWN,
)


def create_sms_message(stock_info_dict: dict):
    message_body = ""
    for symbol, details in stock_info_dict.items():
        change_percent = details["change_percent"]
        emoji = EMOJI_UP if change_percent > 0 else EMOJI_DOWN
        news_list = details["news"]
        news_bullet_points = "\n".join([f"• {news}" for news in news_list])
        message_body += (
            f"{symbol}: {emoji} {abs(change_percent):.2f}%\n{news_bullet_points}\n\n"
        )
    return message_body


def send_sms(message_body: str):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(from_=FROM_NUMBER, body=message_body, to=TO_NUMBER)
