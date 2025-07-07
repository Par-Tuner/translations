import re
import os

# 全局变量：读取 .env 文件，获取到一些路径变量，避免硬编码路径
IMAGE_PATH = os.getenv("IMAGE_PATH", r"translations/twobithistory/images")
TIMELINE_PATH = os.getenv("TIMELINE_PATH", r"translations/twobithistory/code/timeline.md")
ORIGINAL_PATH = os.getenv("ORIGINAL_PATH", r"translations/twobithistory/original")


# 一个读取外部markdown文件的函数，接受文件路径作为参数
# 读取文件内容，使用正则表达式判断每一行的内容，如果这一行包含了markdown链接格式的内容
# 则将它的链接存到一个列表，最终函数的返回值是这个列表
def read_markdown_file(filepath):
    links = []
    pattern = re.compile(r"\[.*?\]\((.*?)\)")
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            matches = pattern.findall(line)
            links.extend(matches)
    return links


# 这个函数接受一段html内容作为参数，转化为markdown格式并返回
def html_to_markdown(html_content):
    from html_to_markdown import convert_to_markdown

    # 将HTML内容转换为Markdown格式
    markdown_content = convert_to_markdown(
        html_content,
        heading_style="atx",
    )
    # 处理脚注内容
    # 将[8](#fn:8)转换为[^8]
    markdown_content = re.sub(r"\[(\d+)\]\(#fn:(\d+)\)", r"[^\1]", markdown_content)

    # 将8. Isaacson, 20. [↩](#fnref:8)转换为[^8]: Isaacson, 20.
    def footnote_repl(match):
        num = match.group(1)
        text = match.group(2).strip()
        return f"[^{num}]: {text}"

    markdown_content = re.sub(
        r"(\d+)\.\s*(.*?)\[↩\]\(#fnref:[\d]*\)",
        footnote_repl,
        markdown_content,
    )

    return markdown_content


# 处理 html 内容的钩子函数，主要目的：
# - 处理相对链接，转换为绝对链接
# - 下载相对链接内的内容，防止相对链接无法访问
def html_hook(html_tree, output_path):
    base_url = "https://twobithistory.org"
    from urllib.parse import urljoin
    # 处理相对链接
    # 对于内容是 #fn: 或 #fnref: 开头的不处理
    for a in html_tree.xpath("//a[@href]"):
        href = a.get("href")
        if href and not href.startswith("#") and not href.startswith("http"):
            absolute_url = urljoin(base_url, href)
            a.set("href", absolute_url)

    # 处理图片链接
    for img in html_tree.xpath("//img[@src]"):
        src = img.get("src")
        if src and not src.startswith("http"):
            absolute_url = urljoin(base_url, src)
            img.set("src", absolute_url)
    # 下载图片内容
    # 因为上面处理过，所以需要链接 prefix 是 https://twobithistory.org/images/
    # 而且没在黑名单内
    # 保存到 output_path 中
    import os
    import requests
    blacklist = [
        "https://twobithistory.org/images/feed.png",
        "https://twobithistory.org/images/twitter.svg",
    ]
    for img in html_tree.xpath("//img[@src]"):
        src = img.get("src")
        if src.startswith(base_url + "/images/") and src not in blacklist:
            img_name = os.path.basename(src)
            img_path = os.path.join(output_path, img_name)
            if not os.path.exists(img_path):
                response = requests.get(src)
                if response.status_code == 200:
                    with open(img_path, "wb") as f:
                        f.write(response.content)
                else:
                    print(f"Failed to download image: {src}")
    return html_tree



# 接受一个网页链接作为参数，下载内容，并讲内容转换为markdown格式
# 其中几个关键内容的xpath对应：
# - 标题：/html/body/main/div/h1/a
# - 时间：/html/body/main/div/p/em
# - 主体内容：/html/body/main/article
def download_and_convert_to_markdown(url):
    import requests
    from lxml import html

    response = requests.get(url)
    response.encoding = response.apparent_encoding  # 自动检测编码

    if response.status_code != 200:
        raise Exception(f"Failed to fetch {url}")

    tree = html.fromstring(response.text)  # 用正确编码的文本

    html_hook(tree, output_path=IMAGE_PATH)

    title = tree.xpath("/html/body/main/div/h1/a/text()")[0]
    date = tree.xpath("/html/body/main/div/p/em/text()")[0]
    content = tree.xpath("/html/body/main/article")[0]

    html_str = html.tostring(content, encoding="unicode")

    markdown_content = f"# {title.strip()}\n\n*{date.strip()}*\n\n"
    markdown_content += html_to_markdown(html_str)
    markdown_content = markdown_content.strip()

    return markdown_content


# 这个函数接受三个参数
# base_path: 一个文件夹路径
# - url: 一个网页链接
# - content: markdown格式的内容
# 函数需要将url进行处理，只保留链接的最后一部分（不包含.html）作为后续的文件名，content作为文件内容，保存在base_path中
def save_markdown_file(base_path, url, content):
    import os

    # 从URL中提取文件名
    filename = os.path.basename(url).replace(".html", ".md")
    filepath = os.path.join(base_path, filename)

    # 确保目录存在
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    # 写入内容到文件
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return filepath


def main():
    links = read_markdown_file(TIMELINE_PATH)
    # links = ["https://twobithistory.org/2018/10/14/lisp.html"]
    base_path = ORIGINAL_PATH
    for link in links:
        # 避免请求过于频繁
        import time
        time.sleep(1)
        try:
            markdown_content = download_and_convert_to_markdown(link)
            filepath = save_markdown_file(base_path, link, markdown_content)
            print(f"Saved: {filepath}")
        except Exception as e:
            print(f"Error processing {link}: {e}")


if __name__ == "__main__":
    main()
