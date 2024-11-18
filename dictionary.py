def process_files(source_file, check_file, output_file):
    # 读取源文件中的单词并去重
    with open(source_file, 'r', encoding='utf-8') as f:
        words = set(f.read().splitlines())  # 使用set去重

    # 读取检查文件中的单词
    with open(check_file, 'r', encoding='utf-8') as f:
        check_words = set(f.read().splitlines())

    # 找出不存在于检查文件中的单词
    missing_words = words - check_words

    # 将缺失的单词追加到检查文件
    with open(check_file, 'a', encoding='utf-8') as f:
        for word in missing_words:
            f.write(word + '\n')

    # 输出缺失单词的格式
    with open(output_file, 'w', encoding='utf-8') as f:
        formatted_output = ', '.join([f'"{word}"' for word in missing_words])  # 修改变量名
        f.write(formatted_output)



# 使用示例
source_file = 'D:/workspace/vocabulary-crawl-example-sentences/check/source.csv'  # 源文件名
check_file = 'D:/workspace/vocabulary-crawl-example-sentences/check/dictionary.csv'     # 检查文件名
output_file = 'D:/workspace/vocabulary-crawl-example-sentences/check/output.csv'   # 输出文件名

process_files(source_file, check_file, output_file)
