import re

def format_md(input_path, output_path):
    # 读取文件
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # 暂存 URL，避免处理
    url_pattern = r'(https?://[^\s]+)'
    urls = re.findall(url_pattern, text)
    text_no_url = re.sub(url_pattern, '<<URL>>', text)

    # 去掉非句子结尾的换行（换行后不是大写字母、引号、数字等）
    # 假设句子结尾是 . ! ? 或引号结尾
    text_no_url = re.sub(r'(?<![.!?])\n+', ' ', text_no_url)

    # 按句子分隔
    sentence_endings = re.compile(r'([.!?]["\']?\s)')
    parts = sentence_endings.split(text_no_url)
    
    # 合并句子和标点
    sentences = []
    for i in range(0, len(parts)-1, 2):
        sentence = parts[i] + parts[i+1].strip()
        sentences.append(sentence.strip())
    # 处理最后一部分（如果不是句子结尾）
    if len(parts) % 2 != 0:
        sentences.append(parts[-1].strip())
    
    # 生成新文本，每个句子之间空一行
    formatted_text = '\n\n'.join(sentences)
    
    # 恢复 URL
    for url in urls:
        formatted_text = formatted_text.replace('<<URL>>', url, 1)
    
    # 输出到新文件
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(formatted_text)


if __name__ == '__main__':
    input_md = r"C:\Users\acheao\OneDrive\文档\language\English\material\TED\The Surprising Power of Your Nature Photos.md"   # 输入文件路径
    output_md = "The Surprising Power of Your Nature Photos.md" # 输出 md 文件路径
    format_md(input_md, output_md)
    print("处理完成！")
