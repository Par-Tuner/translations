import re

# 一个读取外部markdown文件的函数，接受文件路径作为参数
# 读取文件内容，使用正则表达式判断每一行的内容，如果这一行包含了markdown链接格式的内容
# 则将它的链接存到一个列表，最终函数的返回值是这个列表
def read_markdown_file(filepath):
    links = []
    pattern = re.compile(r'\[.*?\]\((.*?)\)')
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            matches = pattern.findall(line)
            links.extend(matches)
    return links

# 这个函数接受一段html内容作为参数，转化为markdown格式并返回
def html_to_markdown(html_content):
    from markdownify import markdownify as md

    # 将HTML内容转换为Markdown格式
    markdown_content = md(html_content)
    return markdown_content



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

    title = tree.xpath('/html/body/main/div/h1/a/text()')[0]
    date = tree.xpath('/html/body/main/div/p/em/text()')[0]
    content = tree.xpath('/html/body/main/article')[0]

    html_str = html.tostring(content, encoding='unicode')

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
    filename = os.path.basename(url).replace('.html', '.md')
    filepath = os.path.join(base_path, filename)

    # 确保目录存在
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    # 写入内容到文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return filepath


def main():
    links = read_markdown_file(r"C:\code\translations\twobithistory\original\timeline.md")
    base_path = r"C:\code\translations\twobithistory\original\markdown"
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
