from tools.DB import db3, db2
import json


def update_data(database, table_name, id, key=None, value=None, field=None, content=None):
    """
    :param database: 数据库类型  "testgroup"测试用例数据库，其他的根据业务来
    :param table_name: 表名
    :param id: 主键id
    :param key: 针对testgroup 请求参数中的key 请求参数中 键不存在多层嵌套
    :param value: 针对testgroup 请求参数中的key
    :param field 针对业务数据表 字段名称
    :param content 针对业务数据表 字段值
    :return: 无返回值
    """
    if database == "aimarket":
        content = content
        up_case_data = f"""update {table_name} set {field}={content} where id={id}"""
        db2.update(up_case_data)
    if database == "testgroup":
        sql = f"""SELECT data FROM {table_name} WHERE id={id}"""
        res = db3.select_real(sql)[0][0]
        re = json.loads(res)
        re[f"{key}"] = value
        r = json.dumps(re, ensure_ascii=False, separators=(',', ':'))  # 处理json串中 中文的显示及多余空格
        my_r = r.replace("\"", "\\\"")
        up_case_data = f"""update {table_name} set data=\"{my_r}\" where id={id}"""
        db3.update(up_case_data)


if __name__ == '__main__':
    # update_data(database="testgroup", table_name="aimarket_case_data", id=4, key="code", value="226")
    update_data(database="aimarket", table_name="valid_code", id=1, field="expires_at", content=1646821712)
