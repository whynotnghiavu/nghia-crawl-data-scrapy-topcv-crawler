import json
from parsel import Selector
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def remove_query_url(text):
    text = text.split('?ta_source=')[0]
    return text


def remove_newline(text):
    text = "".join(text)
    text = text.split("\n")
    text = [i.strip() for i in text if i.strip()]
    text = ", ".join(text)
    return text

 


def remove_text(text_to_remove):
    def remove_func(text):
        return text.replace(text_to_remove, '')
    return remove_func


def convert_html_to_list_string(text):
    selector = Selector(text)

    paragraphs = selector.xpath(".//p/text()").getall()
    list_items = selector.xpath(".//ul/li/text()").getall()
    links = selector.xpath(".//a/text()").getall()

    all_texts = paragraphs + list_items + links
    all_texts = ", ".join(all_texts)
    all_texts = all_texts.split("\n")
    all_texts = [i.strip() for i in all_texts if i.strip()]

    if (all_texts==""):
        all_texts = text

    return json.dumps(all_texts, ensure_ascii=False)
