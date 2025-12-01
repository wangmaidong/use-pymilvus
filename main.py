from pymilvus import CollectionSchema, FieldSchema,DataType,Collection,connections
connections.connect("default", host="49.235.139.52",port="19530",db_name="rensheng")
fields = [
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
    FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=1024)
]
schema = CollectionSchema(fields, description="example")
collection_name = "example"
try:
    collection = Collection(collection_name)
    print(f"集合{collection_name} 已存在")
except Exception:
    collection = Collection(collection_name, schema)
    print(f"集合{collection_name}创建成功")
