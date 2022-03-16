from tools.DB import db2, db3
from tools.auth_post import Auth
from tools.parse_data import pd
import json


#
# sql = "SELECT * FROM aimarket_case_data where  id =1"
# result = db3.select(sql=sql)
# id, method, url, data, expect_return_data, username, password, status_code, *ig = pd.parse_data(result[0])
# # real_return_data, real_status_code = Auth().register_post(data=data, url=url)
# print(repr(expect_return_data),type(expect_return_data))
# str_expect_return_data = json.loads(expect_return_data)
# print(repr(str_expect_return_data),type(str_expect_return_data))
# print(type(str_expect_return_data),type(real_return_data))
# print(str_expect_return_data)
# print(str_expect_return_data == real_return_data)

# sql4_2 = "SELECT * FROM valid_code WHERE phone=\"1299639230@qq.com\" ORDER BY id LIMIT 1"
# result = db2.select(sql4_2)
# id = result[0]["id"]
# code = result[0]["code"]
# updated_at = result[0]["created_at"]
# sql4_3 = f"update valid_code set updated_at={updated_at} where id={id}"
# db2.update(sql4_3)

def test():
    print(1)




