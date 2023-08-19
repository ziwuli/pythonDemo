"""Modules and packages: Use external libraries, such as requests, to write a program to crawl the content of a web
page and extract some of the information. """

import requests
from bs4 import BeautifulSoup


def fetch_comments(url):
    # 发送请求，获取HTML内容
    # response = requests.get(url)
    # response.raise_for_status()
    # 使用BeautifulSoup解析HTML内容
    # soup = BeautifulSoup(response.content, 'html.parser')
    html = """
    <div class="comments">
        <span class="comment">Text 1</span>
        <p><span class="comment">Text 2</span></p>
        <p><span class="comment">Text 3</span></p>
    </div>
    """
    soup = BeautifulSoup(html, 'html.parser')
    span_contents = soup.select('div.comments span.comment')
    comments = []
    for comment_div in span_contents:
        comment_text = comment_div.text.strip()
        if comment_text:
            comments.append(comment_text)
    return comments


if __name__ == '__main__':
    URL = 'demo'
    cts = fetch_comments(URL)
    for comment in cts:
        print(f"comment is : {comment}")
