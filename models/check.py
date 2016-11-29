# from .node import NodeInfo
from .user import UserSqlOperation

from handlers.base import BaseHandler

class Check(BaseHandler):
    @staticmethod
    def md5(result):
        import hashlib
        m = hashlib.md5()
        # m.update(result.encode('utf-8'))也可以
        m.update(bytes(result,encoding='utf-8'))
        return m.hexdigest()

    @staticmethod
    def login_check(input_username,input_password):
        mysql_adm_password = UserSqlOperation.check_adm_login(input_username)
        if mysql_adm_password:
            #这里没有对md5加盐
            md5_input_password = Check.md5(input_password)
            if mysql_adm_password[0][1] == md5_input_password:
                return mysql_adm_password[0][2]
            else:
                return 'Incorrect password'
        else:
            return 'Invalid user'