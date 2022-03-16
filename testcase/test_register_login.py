import pytest
import allure

from tools.DB import db3, db2
from tools.auth_post import Auth
from tools.log import log
from tools.parse_data import pd
import json
import os
from tools.update_data import update_data


@allure.epic("注册-登录模块")
class TestRegisterLogin(object):
    register_success = False

    def setup_class(self) -> None:
        del_sql1 = "DELETE from user WHERE `username`=\"autotest_register\""
        db2.delete(del_sql1)
        del_sql2 = "DELETE from valid_code WHERE  phone=\"1299639230@qq.com\""
        db2.delete(del_sql2)

    def teardown_class(self) -> None:
        print("全部用例运行完成")

    @allure.title("1.使用非正确格式的邮箱地址进行注册")
    @pytest.mark.register
    @pytest.mark.run(order=1)
    def test_register_001(self):
        """
        第一步
        第二步
        第三步
        :return:
        """
        sql = "SELECT * FROM aimarket_case_data where  id =1"
        result = db3.select(sql=sql)
        id, method, url, data, expect_return_data, username, password, status_code, *ig = pd.parse_data(result[0])
        dict_return_data, real_status_code = Auth().register_post(data=data, url=url)
        dict_expect_return_data = json.loads(expect_return_data)

        sql1 = "SELECT * FROM valid_code WHERE phone=\"123456@qq\" ORDER BY id LIMIT 1 "
        result1 = db2.select_real(sql1)
        if dict_expect_return_data == dict_return_data and status_code == real_status_code and not result1:
            log.debug(
                f" \n账号{username}\n url:{url}\n 密码：{password}\n 请求参数: {data}\n 返回状态码: {real_status_code}\n 返回值: {dict_return_data}")
        else:
            log.error(
                f" \n url:{url}\n  请求参数: {data} \n 预期状态码{status_code}\n 返回状态码: {real_status_code}\n 返回值: {dict_return_data} 预期返回值：{dict_expect_return_data}")

            assert dict_expect_return_data == dict_return_data, f"case1 {ig[0]}--{ig[1]}失败"

    @allure.title("2.使用正确格式的邮箱地址进行注册,可以获得验证码")
    @pytest.mark.register
    @pytest.mark.run(order=2)
    def test_register_002(self):
        sql = "SELECT * FROM aimarket_case_data where  id =2"
        result = db3.select(sql=sql)
        id, method, url, data, expect_return_data, username, password, status_code, *ig = pd.parse_data(result[0])
        dict_return_data, real_status_code = Auth().register_post(data=data, url=url)
        dict_expect_return_data = json.loads(expect_return_data)

        sql1 = "SELECT * FROM valid_code WHERE phone=\"1299639230@qq.com\" ORDER BY id LIMIT 1 "
        result1 = db2.select_real(sql1)
        if dict_expect_return_data == dict_return_data and status_code == real_status_code and result1:
            log.debug(
                f" \n账号{username}\n url:{url}\n 密码：{password}\n 请求参数: {data}\n 返回状态码: {real_status_code}\n 返回值: {dict_return_data}")
        else:
            log.error(
                f" \n url:{url}\n  请求参数: {data} \n 预期状态码{status_code}\n 返回状态码: {real_status_code}\n 返回值: {dict_return_data} 预期返回值：{dict_expect_return_data}")
            assert dict_expect_return_data == dict_return_data, f"case1 {ig[0]}--{ig[1]}失败"

    @allure.title("3.使用正确格式的邮箱地址进行注册,错误的验证码不能注册成功")
    @pytest.mark.register
    @pytest.mark.run(order=3)
    def test_register_003(self):
        sql = "SELECT * FROM aimarket_case_data where  id =3"
        result = db3.select(sql=sql)
        id, method, url, data, expect_return_data, username, password, status_code, *ig = pd.parse_data(result[0])
        dict_return_data, real_status_code = Auth().register_post(data=data, url=url)
        dict_expect_return_data = json.loads(expect_return_data)

        if dict_expect_return_data == dict_return_data and status_code == real_status_code:
            log.debug(
                f" \n账号{username}\n url:{url}\n 密码：{password}\n 请求参数: {data}\n 返回状态码: {real_status_code}\n 返回值: {dict_return_data}")
        else:
            log.error(
                f" \n url:{url}\n  请求参数: {data} \n 返回状态码: {real_status_code}\n 返回值: {dict_return_data} \n 预期返回值：{dict_expect_return_data}")
            assert dict_expect_return_data == dict_return_data, f"case1 {ig[0]}--{ig[1]}失败"

    @allure.title("4.使用正确格式的邮箱地址进行注册,过期验证码不能注册成功")
    @pytest.mark.register
    @pytest.mark.run(order=4)
    def test_register_004(self):

        sql4_2 = "SELECT * FROM valid_code WHERE phone=\"1299639230@qq.com\" ORDER BY id LIMIT 1"
        result = db2.select(sql4_2)
        id = result[0]["id"]
        code = result[0]["code"]
        expires_at = result[0]["created_at"]
        # 更新 验证码有效期
        update_data(database="aimarket", table_name="valid_code", id=id, field="expires_at", content=expires_at)
        # sql4_3 = f"update valid_code set expires_at={updated_at} where id={id}"
        # db2.update(sql4_3)

        # 更新 第四条用例请求参数
        update_data(database="testgroup", table_name="aimarket_case_data", id=4, key="code", value=code)

        sql4_1 = "SELECT * FROM aimarket_case_data where  id =4"
        result = db3.select(sql=sql4_1)
        id, method, url, data, expect_return_data, username, password, status_code, *ig = pd.parse_data(result[0])
        dict_return_data, real_status_code = Auth().register_post(data=data, url=url)
        dict_expect_return_data = json.loads(expect_return_data)

        if status_code == real_status_code and dict_expect_return_data == dict_return_data:
            log.debug(
                f" \n账号{username}\n 密码：{password}\n url:{url}\n  请求参数: {data}\n 返回状态码: {real_status_code}\n 返回值: {dict_return_data}")
        else:
            log.error(
                f" \n 预期状态码{status_code} \n 返回状态码: {real_status_code}\n url:{url}\n  请求参数: {data} \n  返回值: {dict_return_data}\n 预期返回值：{dict_expect_return_data}")
            assert status_code == real_status_code, f"case1 {ig[0]}--{ig[1]}失败"

    @allure.title("5.已注册账号再次注册，不能注册成功")
    @pytest.mark.register
    @pytest.mark.run(order=5)
    def test_register_005(self):
        sql = "SELECT * FROM aimarket_case_data where  id =5"
        result = db3.select(sql=sql)
        id, method, url, data, expect_return_data, username, password, status_code, *ig = pd.parse_data(result[0])
        dict_return_data, real_status_code = Auth().register_post(data=data, url=url)
        dict_expect_return_data = json.loads(expect_return_data)

        if status_code == real_status_code:
            log.debug(
                f" \n账号{username}\n url:{url}\n 密码：{password}\n 请求参数: {data}\n 返回状态码: {real_status_code}\n 返回值: {dict_return_data}")
        else:
            log.error(
                f" \n 预期状态码{status_code} \n 返回状态码: {real_status_code}\n url:{url}\n  请求参数: {data} \n  返回值: {dict_return_data}")
            assert status_code == real_status_code, f"case1 {ig[0]}--{ig[1]}失败"

    @allure.title("6.未注册账号使用已注册的邮箱注册,不能注册成功")
    @pytest.mark.register
    @pytest.mark.run(order=6)
    def test_register_006(self):
        sql = "SELECT * FROM aimarket_case_data where  id =6"
        result = db3.select(sql=sql)
        id, method, url, data, expect_return_data, username, password, status_code, *ig = pd.parse_data(result[0])
        dict_return_data, real_status_code = Auth().register_post(data=data, url=url)
        dict_expect_return_data = json.loads(expect_return_data)

        if status_code == real_status_code:
            log.debug(
                f" \n账号{username}\n url:{url}\n 密码：{password}\n 请求参数: {data}\n 返回状态码: {real_status_code}\n 返回值: {dict_return_data}")
        else:
            log.error(
                f" \n 预期状态码{status_code} \n 返回状态码: {real_status_code}\n url:{url}\n  请求参数: {data} \n  返回值: {dict_return_data}")

            assert status_code == real_status_code, f"case1 {ig[0]}--{ig[1]}失败"


@allure.epic("注册-登录主流程正向用例")
class TestRegisterLoginSmoke(object):
    @allure.title("1.未经")
    @pytest.mark.register
    @pytest.mark.run(order=1)
    def test_register_login_smoke_001(self):
        pass


if __name__ == '__main__':
    pytest.main(["-sv", "test_register_login.py", "-m", "register"])
    os.system(
        "allure generate  ../report/temp_jsonreport -o ../report/html --clean")
