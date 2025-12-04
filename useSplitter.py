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
        # 初始化选择的分隔符为最后一个
        chosen_separator = separators[-1]
        for i,sep in enumerate(separators):
            # 如果分隔符为空，直接选中并跳出
            if not sep:
                chosen_separator = sep
                break
            if sep in text:
                chosen_separator = sep
                break
        if chosen_separator:
            text_pieces = text.split(chosen_separator)
        else:
            text_pieces = list(text)
        return text_pieces

    def split_txt(self, text: str) -> list[str]:
        return self._split_text(text,self.separators)
