from stock import get_stock_change_percent
from news import get_news
from sms import create_sms_message, send_sms
from constants import SYMBOL_COMPANY


def main():
    stock_info_dict = {
        stock_symbol: {
            "change_percent": get_stock_change_percent(stock_symbol),
            "news": get_news(company_name),
        }
        for stock_symbol, company_name in SYMBOL_COMPANY.items()
    }
    message_body = create_sms_message(stock_info_dict)
    send_sms(message_body)


if __name__ == "__main__":
    main()
