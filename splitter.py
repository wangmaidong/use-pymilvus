class RecursiveCharacterTextSplitter:
    """
    递归字符分割器类
    """
    def __init__(
            self,
            chunk_size:int = 100, # 默认分块大小
            chunk_overlap:int = 0, # 默认块间重叠为0
            separators: list[str] | None = None # 分割符列表
    ):
        # 赋值分块大小
        self.chunk_size = chunk_size
        # 赋值分块重叠长度
        self.chunk_overlap = chunk_overlap
        # 如果未传入分隔符，则使用默认分隔符列表
        self.separators = separators or ["\n\n","\n"," ", ""]
    def _split_text(self,text:str, separators: list[str]) -> list[str]:
        # 最终结果：存放所有切好的文本块
        final_chunk = []
        # 初始化选择的分隔符为最后一个
        chosen_separator = separators[-1]
        # 记录还没使用过的分割符
        remaining_separators = []
        # 遍历所有分割符
        for i,sep in enumerate(separators):
            # 如果分隔符为空，直接选中并跳出
            if not sep:
                chosen_separator = sep
                break
            if sep in text:
                chosen_separator = sep
                # 记录剩余的分割符（如果切出来的块还是太大，就用这些更小的）
                remaining_separators = separators[i+1:]
                break
        if chosen_separator:
            text_pieces = text.split(chosen_separator)
        else:
            text_pieces = list(text)
        for piece in text_pieces:
            if len(piece) <= self.chunk_size:
                final_chunk.append(piece)
            else:
                if remaining_separators:
                    # 如果还有更小的分割符可以用，就递归分割这个大块的
                    sub_chunks = self._split_text(piece, remaining_separators)
                    final_chunk.extend(sub_chunks)
                else:
                    for i in range(0, len(piece), self.chunk_size):
                        final_chunk.append(piece[i: (i+self.chunk_size)])
        return final_chunk
    def split_text(self, text: str) -> list[str]:
        return self._split_text(text,self.separators)
