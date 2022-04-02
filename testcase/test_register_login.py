import pytest
import allure
from tools.DB import db3, db2
from tools.log import log
import os
from tools.update_data import update_data
from api_level.apis import AllApis
import pytest_check as check
import time


@allure.epic("注册-登录主流程正向用例")
class TestRegisterLoginSmoke(object):

    def setup_class(self) -> None:
        del_sql1 = "DELETE from user WHERE `username`=\"autotest_register\""
        db2.delete(del_sql1)
        del_sql2 = "DELETE from valid_code WHERE  phone=\"1299639230@qq.com\""
        db2.delete(del_sql2)

    def teardown_class(self) -> None:
        print("全部用例运行完成")

    @allure.title("1.登录注册流程--注册--输入账号邮箱")
    @pytest.mark.smoke
    @pytest.mark.run(order=1)
    def test_register_login_smoke_001(self):
        sql = "SELECT * FROM aimarket_case_data where  id =7  AND url=\"/api/valid-code/send\" "
        id, method, url, data, dict_expect_return_data, username, password, status_code, ig, real_status_code, dict_return_data = AllApis().case_normal_api(
            sql=sql)
        check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")
        check.equal(dict_expect_return_data, dict_return_data,
                    f"预期和实际不一致 预期返回值{dict_expect_return_data}和实际返回值{dict_return_data}不一致")
        log.debug(
            f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码{status_code}\n 实际返回状态码: {real_status_code}\n 预期返回值：{dict_expect_return_data}\n 实际返回值: {dict_return_data} ")

    @allure.title("2.登录注册流程--注册--输入验证码")
    @pytest.mark.smoke
    @pytest.mark.run(order=2)
    def test_register_login_smoke_002(self):
        # 更新用例请求参数
        sql2_1 = "SELECT * FROM valid_code WHERE phone=\"1299639230@qq.com\" ORDER BY id LIMIT 1"
        result = db2.select(sql2_1)
        code = result[0]["code"]
        now_time = int(str(time.time()).split(".")[0])
        update_data(database="testgroup", table_name="aimarket_case_data", id=8, key="code", value=code)
        update_data(database="testgroup", table_name="aimarket_case_data", id=9, key="code", value=code)
        update_data(database="testgroup", table_name="aimarket_case_data", id=9, key="timestamp", value=now_time)
        # update_data(database="testgroup", table_name="aimarket_case_data", id=10, key="timestamp", value=now_time)

        sql = "SELECT * FROM aimarket_case_data where  id =8  AND url=\"/api/valid-code/check\" "
        id, method, url, data, dict_expect_return_data, username, password, status_code, ig, real_status_code, dict_return_data = AllApis().case_normal_api(
            sql=sql)
        check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")
        check.equal(dict_expect_return_data, dict_return_data,
                    f"预期和实际不一致 预期返回值{dict_expect_return_data}和实际返回值{dict_return_data}不一致")
        log.debug(
            f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码{status_code}\n 实际返回状态码: {real_status_code}\n 预期返回值：{dict_expect_return_data}\n 实际返回值: {dict_return_data} ")

    @allure.title("3.登录注册流程--注册-设置密码")
    @pytest.mark.smoke
    @pytest.mark.run(order=3)
    def test_register_login_smoke_003(self):
        sql = "SELECT * FROM aimarket_case_data where  id =9  AND url=\"/api/user/register\" "
        id, method, url, data, dict_expect_return_data, username, password, status_code, ig, real_status_code, dict_return_data = AllApis().case_normal_api(
            sql=sql)
        check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")
        check.equal(dict_expect_return_data, dict_return_data,
                    f"预期和实际不一致 预期返回值{dict_expect_return_data}和实际返回值{dict_return_data}不一致")
        log.debug(
            f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码{status_code}\n 实际返回状态码: {real_status_code}\n 预期返回值：{dict_expect_return_data}\n 实际返回值: {dict_return_data} ")

    @allure.title("4.登录注册流程--登录--登录")
    @pytest.mark.smoke
    @pytest.mark.run(order=4)
    def test_register_login_smoke_004(self):
        with allure.step("此条用例不比较返回值 断言token存在"):
            sql = "SELECT * FROM aimarket_case_data where  id =10  AND url=\"/api/user/login\" "
            id, method, url, data, dict_expect_return_data, username, password, status_code, ig, real_status_code, dict_return_data = AllApis().case_normal_api(
                sql=sql)
            check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")
            __token = dict_return_data.get("token")
            check.is_not_none(dict_return_data.get("token"), f"token为{__token}")

            # 由于token的多变性 不能直接断言返回值 看是否存在返回值是否存在token
            log.debug(
                f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码{status_code}\n 实际返回状态码: {real_status_code}\n 预期返回值：{dict_expect_return_data}\n 实际返回值: {dict_return_data} ")


@allure.epic("注册-登录模块")
class TestRegisterLogin(object):
    # register_success = False

    def setup_class(self) -> None:
        del_sql1 = "DELETE from user WHERE `username`=\"autotest_register\""
        db2.delete(del_sql1)
        del_sql2 = "DELETE from valid_code WHERE  phone=\"1299639230@qq.com\""
        db2.delete(del_sql2)
        del_sql3 = "DELETE from valid_code WHERE  phone=\"123456@qq\""
        db2.delete(del_sql3)

    def teardown_class(self) -> None:
        print("全部用例运行完成")

    @allure.title("1.使用非正确格式的邮箱地址进行注册")
    @pytest.mark.register
    @pytest.mark.run(order=5)
    def test_register_001(self):
        # with allure.step("请点击查看步骤"):  # 将一个测试用例分成几个步骤，将步骤打印到测试报告中 with后面接代码
        # with allure.attach(name="标题",body="写入",attachment_type=allure.attachment_type.TEXT)
        # 通过sql 再次确定请求的接口
        sql = "SELECT * FROM aimarket_case_data where  id =1  AND url=\"/api/valid-code/send\" "
        id, method, url, data, dict_expect_return_data, username, password, status_code, ig, real_status_code, dict_return_data = AllApis().case_normal_api(
            sql=sql)
        check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")
        check.equal(dict_expect_return_data, dict_return_data,
                    f"预期和实际不一致 预期返回值{dict_expect_return_data}和实际返回值{dict_return_data}不一致")
        # 数据库验证 应没有此条数据
        sql1 = "SELECT * FROM valid_code WHERE phone=\"123456@qq\" ORDER BY id LIMIT 1 "
        result1 = db2.select_real(sql1)
        check.is_none(result1, "数据库有此条数据")
        log.debug(
            f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码{status_code}\n 实际返回状态码: {real_status_code}\n 预期返回值：{dict_expect_return_data}\n 实际返回值: {dict_return_data} ")

    # @allure.title("2.使用正确格式的邮箱地址进行注册,可以获得验证码")
    # @pytest.mark.register
    # @pytest.mark.run(order=2)
    # def test_register_002(self):
    #     # with allure.step("请点击查看步骤"):
    #     sql = "SELECT * FROM aimarket_case_data where  id =2"
    #     id, method, url, data, dict_expect_return_data, username, password, status_code, ig, real_status_code, dict_return_data = AllApis().case_normal_api(
    #         sql=sql)
    #     check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")
    #     check.equal(dict_expect_return_data, dict_return_data,
    #                 f"预期和实际不一致 预期返回值{dict_expect_return_data}和实际返回值{dict_return_data}不一致")
    #
    #     sql1 = "SELECT * FROM valid_code WHERE phone=\"1299639230@qq.com\" ORDER BY id LIMIT 1 "
    #     result1 = db2.select_real(sql1)
    #     check.is_not_none(result1, "数据库没有此条数据")
    #     log.debug(
    #         f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码{status_code}\n 实际返回状态码: {real_status_code}\n 预期返回值：{dict_expect_return_data}\n 实际返回值: {dict_return_data} ")
    #


#
#     @allure.title("3.使用正确格式的邮箱地址进行注册,错误的验证码不能注册成功")
#     @pytest.mark.register
#     @pytest.mark.run(order=3)
#     def test_register_003(self):
#         sql = "SELECT * FROM aimarket_case_data where  id =3"
#         result = db3.select(sql=sql)
#         id, method, url, data, expect_return_data, username, password, status_code, *ig = pd.parse_data(result[0])
#         dict_return_data, real_status_code = Auth().register_post(data=data, url=url)
#         dict_expect_return_data = json.loads(expect_return_data)
#
#         if dict_expect_return_data == dict_return_data and status_code == real_status_code:
#             log.debug(
#                 f" \n账号{username}\n url:{url}\n 密码：{password}\n 请求参数: {data}\n 返回状态码: {real_status_code}\n 返回值: {dict_return_data}")
#         else:
#             log.error(
#                 f" \n url:{url}\n  请求参数: {data} \n 返回状态码: {real_status_code}\n 返回值: {dict_return_data} \n 预期返回值：{dict_expect_return_data}")
#             assert dict_expect_return_data == dict_return_data, f"case1 {ig[0]}--{ig[1]}失败"
#
#     @allure.title("4.使用正确格式的邮箱地址进行注册,过期验证码不能注册成功")
#     @pytest.mark.register
#     @pytest.mark.run(order=4)
#     def test_register_004(self):
#
#         sql4_2 = "SELECT * FROM valid_code WHERE phone=\"1299639230@qq.com\" ORDER BY id LIMIT 1"
#         result = db2.select(sql4_2)
#         id = result[0]["id"]
#         code = result[0]["code"]
#         expires_at = result[0]["created_at"]
#         # 更新 验证码有效期
#         update_data(database="aimarket", table_name="valid_code", id=id, field="expires_at", content=expires_at)
#         # sql4_3 = f"update valid_code set expires_at={updated_at} where id={id}"
#         # db2.update(sql4_3)
#
#         # 更新 第四条用例请求参数
#         update_data(database="testgroup", table_name="aimarket_case_data", id=4, key="code", value=code)
#
#         sql4_1 = "SELECT * FROM aimarket_case_data where  id =4"
#         result = db3.select(sql=sql4_1)
#         id, method, url, data, expect_return_data, username, password, status_code, *ig = pd.parse_data(result[0])
#         dict_return_data, real_status_code = Auth().register_post(data=data, url=url)
#         dict_expect_return_data = json.loads(expect_return_data)
#
#         if status_code == real_status_code and dict_expect_return_data == dict_return_data:
#             log.debug(
#                 f" \n账号{username}\n 密码：{password}\n url:{url}\n  请求参数: {data}\n 返回状态码: {real_status_code}\n 返回值: {dict_return_data}")
#         else:
#             log.error(
#                 f" \n 预期状态码{status_code} \n 返回状态码: {real_status_code}\n url:{url}\n  请求参数: {data} \n  返回值: {dict_return_data}\n 预期返回值：{dict_expect_return_data}")
#             assert status_code == real_status_code, f"case1 {ig[0]}--{ig[1]}失败"
#
#     @allure.title("5.已注册账号再次注册，不能注册成功")
#     @pytest.mark.register
#     @pytest.mark.run(order=5)
#     def test_register_005(self):
#         sql = "SELECT * FROM aimarket_case_data where  id =5"
#         result = db3.select(sql=sql)
#         id, method, url, data, expect_return_data, username, password, status_code, *ig = pd.parse_data(result[0])
#         dict_return_data, real_status_code = Auth().register_post(data=data, url=url)
#         dict_expect_return_data = json.loads(expect_return_data)
#
#         if status_code == real_status_code:
#             log.debug(
#                 f" \n账号{username}\n url:{url}\n 密码：{password}\n 请求参数: {data}\n 返回状态码: {real_status_code}\n 返回值: {dict_return_data}")
#         else:
#             log.error(
#                 f" \n 预期状态码{status_code} \n 返回状态码: {real_status_code}\n url:{url}\n  请求参数: {data} \n  返回值: {dict_return_data}")
#             assert status_code == real_status_code, f"case1 {ig[0]}--{ig[1]}失败"
#
#     @allure.title("6.未注册账号使用已注册的邮箱注册,不能注册成功")
#     @pytest.mark.register
#     @pytest.mark.run(order=6)
#     def test_register_006(self):
#         sql = "SELECT * FROM aimarket_case_data where  id =6"
#         result = db3.select(sql=sql)
#         id, method, url, data, expect_return_data, username, password, status_code, *ig = pd.parse_data(result[0])
#         dict_return_data, real_status_code = Auth().register_post(data=data, url=url)
#         dict_expect_return_data = json.loads(expect_return_data)
#
#         if status_code == real_status_code:
#             log.debug(
#                 f" \n账号{username}\n url:{url}\n 密码：{password}\n 请求参数: {data}\n 返回状态码: {real_status_code}\n 返回值: {dict_return_data}")
#         else:
#             log.error(
#                 f" \n 预期状态码{status_code} \n 返回状态码: {real_status_code}\n url:{url}\n  请求参数: {data} \n  返回值: {dict_return_data}")
#
#             assert status_code == real_status_code, f"case1 {ig[0]}--{ig[1]}失败"
#
# @pytest.mark.run(order=1)


if __name__ == '__main__':
    pytest.main(["-sv", "test_register_login.py"])
    # os.system("pytest -vs ./test_register_login.py --alluredir ../report/temp_jsonreport")

    # 若想使用pycharm的pytest框架 还能生成报告 在对应目录下 命令行执行 allure generate  ../report/temp_jsonreport -o ../report/html --clean
    os.system(
        "allure generate  ../report/temp_jsonreport -o ../report/html --clean")
