# 导入 pymilvus的相关模块：集合模式 字段模式 数据类型 集合 连接
from pymilvus import CollectionSchema, FieldSchema,DataType,Collection,connections
# 连接到milvus 服务器 使用默认链接别名 连接到本地主机的19530端口，数据库名为rensheng
connections.connect("default", host="49.235.139.52",port="19530",db_name="rensheng")
# 定义集合的字段结构，包含主键ID字段和向量字段
fields = [
# 定义主键字段：64位整数类型，自动生成ID
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
# 定义向量字段：128维浮点向量
    FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=1024)
]
# 创建集合模式对象，包含字段定义和描述信息
schema = CollectionSchema(fields, description="example")
# 检查集合是否存在，不存在才创建
collection_name = "example"
try:
    # 尝试获取已存在的集合
    collection = Collection(collection_name)
    print(f"集合{collection_name} 已存在")
    # 定义索引参数配置
    index_params = {
        "metric_type": "L2",
        "index_type": "IVF_FLAT",
        "params": {"nlist": 128}
    }
    collection.create_index("embedding", index_params)
    print(f"创建索引成功")
except Exception:
    # 集合不存在，创建新集合
    collection = Collection(collection_name, schema)
    print(f"集合{collection_name}创建成功")
