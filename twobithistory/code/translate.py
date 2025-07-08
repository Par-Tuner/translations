from llama_index.llms.google_genai import GoogleGenAI
from llama_index.core.llms import ChatMessage

import os

PROMPT_PATH = os.getenv("PROMPT_PATH", "translations/twobithistory/code/prompt.md")


def read_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
    return content


# 使用 llama_index 库，新建一个 google gemini 的实例
def create_translate_agent() -> GoogleGenAI:
    # 从环境变量中获取 API 密钥
    import os

    api_key = os.getenv("GOOGLE_GEMINI_API_KEY")
    # 创建 GoogleGemini 实例
    gemini = GoogleGenAI(
        api_key=api_key,
        model="gemini-2.5-flash",  # 使用 Gemini 2.5 Flash 模型
    )
    return gemini


# 使用 GoogleGemini 实例进行翻译
# 对 gemini 实例输入 text 作为输入，输出就是翻译后的文本
def translate_text(gemini: GoogleGenAI, text: str) -> str:
    prompt = read_file(PROMPT_PATH)

    messages = [
        ChatMessage(role="system", content=prompt),
        ChatMessage(role="user", content=text),
    ]
    response = gemini.chat(messages)
    return response.message.content


def translate_file(filepath):
    text = read_file(filepath)
    gemini = create_translate_agent()
    return translate_text(gemini, text)


# 主要流程：
# 1. 定义一个文件夹路径作为英文输入路径，input_folder
# 2. 定义一个文件夹路径作为中文输出路径，output_folder
# 3. 遍历 input_folder 中的所有文件，逐个进行翻译，并将翻译结果保存到 output_folder 中
def process_folder(input_folder, output_folder):
    import os

    # input_folder = r"C:\code\translations\twobithistory\original"  # 输入文件夹路径
    # output_folder = r"C:\code\translations\twobithistory"  # 输出文件夹路径

    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.endswith(".md"):  # 只处理 Markdown 文件
            filepath = os.path.join(input_folder, filename)
            print(f"Processing {filepath}...")

            # 翻译文件内容
            translated_text = translate_file(filepath)

            # 保存翻译结果到输出文件夹
            output_filepath = os.path.join(output_folder, filename)
            with open(output_filepath, "w", encoding="utf-8") as f:
                f.write(translated_text)

            print(f"Saved translated file to {output_filepath}")


def process_single_file(input_file, output_file):
    translated_text = translate_file(input_file)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(translated_text)
    print(f"Saved translated file to {output_file}")


def test_gemini():
    gemini = create_translate_agent()
    text = "Hello, world!"
    resp = gemini.complete(text)
    print(resp)


if __name__ == "__main__":
    process_single_file(
        r"C:\code\translations\twobithistory\original\the-ruby-story.md",
        r"C:\code\translations\twobithistory\the-ruby-story.md",
    )
