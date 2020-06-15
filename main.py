from naver import Naver
from taobao import Taobao

naver_login = {
    "id": "",
    "pw": ""
}
n = Naver()
n.login(naver_login.get("id"), naver_login.get("pw"))
products = n.get_products()

for p in products:
    print(p.text)


# taobao_login = {
#     "id": "",
#     "pw": ""
# }
# t = Taobao()
# t.login(taobao_login.get("id"), taobao_login.get("pw"))