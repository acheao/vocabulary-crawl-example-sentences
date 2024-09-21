def read_words_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.read().split()
    return words

def write_unique_words_to_file(words, output_file_path):
    unique_words = set(words)  # 去重
    formatted_words = ', '.join(f'"{word}"' for word in unique_words)  # 格式化单词
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(formatted_words + '\n')

# 示例用法
input_file_path = 'D:/workspace/vocabulary-crawl-example-sentences/sentences_semicolon.csv'  # 替换为你的输入文件路径
output_file_path = 'D:/workspace/vocabulary-crawl-example-sentences/anki-vocabulary-deck.csv'  # 输出文件路径

words = read_words_from_file(input_file_path)
write_unique_words_to_file(words, output_file_path)

print(f"Unique words written to {output_file_path}")
