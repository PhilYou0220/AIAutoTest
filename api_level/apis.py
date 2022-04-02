from tools.DB import db3
from tools.api_requests_duration import outer
from tools.auth_post import Auth
from tools.parse_data import pd
import json
import allure


class AllApis(object):
    """接口层 和 业务数据注入层 只接收sql语句 此项目所有接口都在这个类 不写死 在此完成接口数据的组装、请求 和返回值的处置
        本来想一个接口一个方法，
    """

    # @outer
    def case_normal_api(self, sql: str):
        result = db3.select(sql=sql)
        id, method, url, data, expect_return_data, username, password, status_code, *ig = pd.parse_data(result[0])
        with allure.step(f"{ig[1]}"):
            dict_expect_return_data = json.loads(expect_return_data)
            dict_return_data, real_status_code = Auth().register_post(data=data, url=url)
        return id, method, url, data, dict_expect_return_data, username, password, status_code, ig, real_status_code, dict_return_data

    def case_login_api(self, sql: str):
        result = db3.select(sql=sql)
        id, method, url, data, expect_return_data, username, password, status_code, *ig = pd.parse_data(result[0])
        with allure.step(f"{ig[1]}"):
            dict_expect_return_data = json.loads(expect_return_data)
            dict_return_data, real_status_code = Auth().base_post(username=username, password=password)
        return id, method, url, data, dict_expect_return_data, username, password, status_code, ig, real_status_code, dict_return_data

    def case_auth_api(self, sql: str):
        result = db3.select(sql=sql)
        id, method, url, data, expect_return_data, username, password, status_code, *ig = pd.parse_data(result[0])
        with allure.step(f"{ig[1]}"):
            dict_expect_return_data = json.loads(expect_return_data)
            dict_return_data, real_status_code = Auth().auth_post(username=username, password=password, data2=data,
                                                                  url=url)
        return id, method, url, data, dict_expect_return_data, username, password, status_code, ig, real_status_code, dict_return_data
