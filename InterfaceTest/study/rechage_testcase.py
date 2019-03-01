import openpyxl
from InterfaceTest.common import do_excel
from InterfaceTest.common import http_requests
from InterfaceTest.common import contants

if __name__ == '__main__':
    do_excel = do_excel.Do_Excel(contants.case_file, sheet_name="recharge")
    case_read = do_excel.get_cases()
    http_request = http_requests.HTTPRequest2()
    params = {"mobilephone": "15810447878", "pwd": "123456"}
    resp2 = http_request.request('POST', 'http://test.lemonban.com/futureloan/mvc/api/member/login',params)
    print(resp2.text)
    print(resp2.status_code)
    print(resp2)
    # print(resp2.json()['msg'])
    for case in case_read:
        print(case.__dict__)
        ##写入的话，要先调用httprequest执行，执行成功写入
        resp = http_request.request(case.method, case.url, eval(case.data))
        actual = resp.text
        if case.expected == actual:  ##判断执行厚的实际结果是否与预期结果一致
            do_excel.Write_excel(case.case_id + 1, actual, 'PASS')
        else:
            do_excel.Write_excel(case.case_id + 1, actual, 'FAIL')
