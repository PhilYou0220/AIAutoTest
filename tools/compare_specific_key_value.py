# 针对{"k":[{"k1":v}]}
def compare(values, return_data, verify):
    if return_data["data"][0].get(verify):
        if values == return_data["data"][0].get(verify):
            return False
        else:
            return False


if __name__ == '__main__':
    a = {"data": [{"id": 226, "name": "游飞3测试砂石场", "sand_factory_type": None, "address": "1234", "lng": "93.4115987",
                   "lat": "31.3813058", "area": "0.00", "image": None, "open_status": 1, "deleted": 0, "area_id": 8,
                   "department_id": 584, "plan": "file\/10\/2022\/0107\/b843f996-9eaf-47a6-ada1-0d5c49924756.png",
                   "create_time": "2022-02-14 17:27:31", "pm_2_5": None, "pm_10": 0, "temperature": None,
                   "humidity": None,
                   "aqi": None, "b_pm_2_5": None, "b_pm_10": None, "b_temperature": None, "b_humidity": None,
                   "b_aqi": None,
                   "realname": None, "street_id": None, "manager_department_id": None, "constructor_manager": None,
                   "constructor_manager_telephone": None, "consum_type": 2, "forever": 1, "begin_time": None,
                   "end_time": None, "other_info": "", "videos": "", "images": "", "created_by": 89089,
                   "area_name": "高新区",
                   "report_method": 1, "gps_polygon": 1, "user_name": "测试--游飞--总部坐席"}],
         "page": {"page": 1, "limit": 10, "total": 1}}

    verify = "address"
    address = "1234"
    print(compare(address, a, verify))
    # c =a["data"][0]
    # print(c)
    # print(c.get("address"))
