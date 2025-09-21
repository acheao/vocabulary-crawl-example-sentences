import json

def generate_ordered_list_by_edges(canvas_path, output_path):
    """
    根据 Canvas edges 顺序生成 Markdown 有序列表。
    
    :param canvas_path: Canvas 文件路径 (.canvas)
    :param output_path: 输出 Markdown 文件路径 (.md)
    :return: Markdown 内容字符串
    """
    with open(canvas_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 构建 id -> 节点 映射
    node_dict = {node['id']: node for node in data['nodes'] if node.get('type') == 'file'}

    # 构建 fromNode -> toNode 映射，按 edges 顺序
    from_to_map = {}
    for edge in data.get('edges', []):
        from_id = edge['fromNode']
        to_id = edge['toNode']
        if from_id in node_dict and to_id in node_dict:
            if from_id not in from_to_map:
                from_to_map[from_id] = []
            from_to_map[from_id].append(to_id)

    # 找到起始节点（没有其他节点指向它的节点）
    to_nodes = {edge['toNode'] for edge in data.get('edges', [])}
    start_nodes = [nid for nid in node_dict if nid not in to_nodes]
    if not start_nodes:
        start_nodes = list(node_dict.keys())  # 防止没有明确起点

    visited = set()
    ordered_nodes = []

    def dfs(node_id):
        if node_id in visited:
            return
        visited.add(node_id)
        ordered_nodes.append(node_dict[node_id])
        for next_id in from_to_map.get(node_id, []):
            dfs(next_id)

    for start_id in start_nodes:
        dfs(start_id)

    # 生成 Markdown
    lines = []
    for i, node in enumerate(ordered_nodes, start=1):
        file_name = node['file'].split('/')[-1]  # 只取文件名
        md_file_name = file_name.replace(' ', '%20')
        lines.append(f"{i}. [{file_name}]({md_file_name})")

    markdown_text = '\n'.join(lines)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown_text)

    return markdown_text


if __name__ == "__main__":
    canvas_file = r"C:\Users\acheao\OneDrive\文档\language\English\material\TED\TED.canvas"
    output_file = r"C:\Users\acheao\OneDrive\文档\language\English\material\TED\Index.md"

    md_content = generate_ordered_list_by_edges(canvas_file, output_file)
    print(f"生成 Markdown 列表成功，共 {len(md_content.splitlines())} 行")
