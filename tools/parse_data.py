from tools.log import log


class ParseData(object):
    def parse_data(self, case):
        # try:
        url_prefix = 'http://106.75.154.221:8391'  # 测试环境前缀
        id = case["id"]
        method = case["method"]
        url = url_prefix + case["url"]
        data = case["data"]
        expect_return_data = case["expect_return_data"]
        username = case["username"]
        password = case["password"]
        status_code = case["status_code"]
        name = case["name"]
        case_step = case["case_step"]
        return id, method, url, data, expect_return_data, username, password, status_code, name, case_step
        # except Exception as e:
        #     log.error(e)


pd = ParseData()

if __name__ == '__main__':
    a = ParseData()
