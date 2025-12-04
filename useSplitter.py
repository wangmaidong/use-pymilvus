# 导入RecursiveCharacterTextSplitter类用于文本分割
from langchain_text_splitters import RecursiveCharacterTextSplitter
# from splitter import RecursiveCharacterTextSplitter  # 可以选用自定义的splitters模块

# 创建一个文本分割器对象，设置分块大小为4，分块重叠为0
text_splitter = RecursiveCharacterTextSplitter(chunk_size=4,chunk_overlap=0)

# 定义一个包含三个段落的文档字符串
document = f"""段落1\n段落2\n\n段落3\n段落4"""

# 使用分割器对文档内容进行分割，返回分块列表
texts = text_splitter.split_text(document)

# 遍历每个分块，输出分块编号、长度和内容
for i, text in enumerate(texts):
    print(f"分块 {i+1}: 长度={len(text)} 内容: {repr(text)}")