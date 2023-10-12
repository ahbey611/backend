import unittest

# import sys
# sys.path.append('/utils/')
from django.test import TestCase

from utils.register_params_check import register_params_check


class BasicTestCase(unittest.TestCase):
    """
    TODO: 在这里补充注册相关测试用例
    """

    def setUp(self):
        self.testCase1 = {
            "username": "ahaHfty611",
            "password": "2*By-Qs6rfDS*_",
            "nickname": "ahsdFef",
            "url": "https://e-34d.2sAD-w.32.2D-asE.com",
            "mobile": "+86.195687290936",
            "magic_number": 2301
        }

        self.testCase2 = {
            "username": "wAbc1223",
            "password": "Pa_w0rd-*",
            "nickname": "JohnDoe",
            "url": "https://231-test.software.school.202108078.beyzhexua.cm",
            "mobile": "+12.123456789012",
            "magic_number": 1123
        }

        self.testCase3 = {
            "username": "forRGahuq324",
            "password": "Pre_gDF0G^d-*",
            "nickname": "JeE83ASDhde_s",
            "url": "https://23.4.123.231.com",
            "mobile": "+86.197402137224",
            "magic_number": 0
        }

        self.testCase4 = {
            "username": "suDy2",
            "password": "-sdjk*jdfD1^",
            "nickname": "sdfkj#24sDS*!e_s",
            "url": "https://t.cn",
            "mobile": "+06.153424122324",
            "magic_number": 1782441239
        }

        self.testCase5 = {
            "username": "SwalaKUp2235",
            "password": "-sdjk*jd1^f*dhF",
            "nickname": "sdf#EF_s",
            "url": "https://www.y8.c2m",
            "mobile": "+94.153345714134",
            "magic_number": 15234798932412390
        }

        self.testCase6 = {
            "username": "e0000000",
            "password": "00000a^F",
            "nickname": "43gfdDF3^$2",
            "url": "http://www.github-test.7823DSs2-1.611.com",
            "mobile": "+53.153250114134",
            "magic_number": 8
        }

        self.testCase7 = {
            "username": "P21630000000",
            "password": "^^^^^^^^^^aK0",
            "nickname": "75hrfFiASD#%%",
            "url": "http://w.df.we53-1.12.21.d.my",
            "mobile": "+93.143608533134",
            "magic_number": 2437894247823247839472389243789423
        }

        self.testCase8 = {
            "username": "aaaa0",
            "password": "^*nksdf0Ehe____",
            "nickname": "7jggytu%%",
            "url": "http://1.R.3.1.c",
            "mobile": "+92.147519302134",
            "magic_number": 846536235
        }

        self.testCase9 = {
            "username": "aadfeku43270",
            "password": "fe*_dhjFR92***",
            "nickname": "46hfgFGsk(#hd",
            "url": "http://hwof.23.fd-jc1.232ok.3247891casd.ur",
            "mobile": "+18.242364580723",
            "magic_number": 3
        }

        self.testCase10 = {
            "username": "FFF888888888",
            "password": "rth*_****SF1",
            "nickname": "uiJRTjtytut(#t",
            "url": "https://www.runoob.com",
            "mobile": "+25.634685273541",
            "magic_number": 58524523
        }

        # username过短
        self.testCase11 = {
            "username": "FFF8",
            "password": "rth*_****SF1",
            "nickname": "uiJRTjtytut(#t",
            "url": "https://www.runoob.com",
            "mobile": "+25.634685273541",
            "magic_number": 58524523
        }

        # username字母必须在数字前面
        self.testCase12 = {
            "username": "dwd80a",
            "password": "rth*_****SF1",
            "nickname": "uiJRTjtytut(#t",
            "url": "https://www.runoob.com",
            "mobile": "+25.634685273541",
            "magic_number": 58524523
        }

        # username没有数字
        self.testCase13 = {
            "username": "aaaaaaaaa",
            "password": "rth*_****SF1",
            "nickname": "uiJRTjtytut(#t",
            "url": "https://www.runoob.com",
            "mobile": "+25.634685273541",
            "magic_number": 58524523
        }

        # username过长
        self.testCase14 = {
            "username": "atgrDFJDFSfsa134342",
            "password": "rth*_****SF1",
            "nickname": "uiJRTjtytut(#t",
            "url": "https://www.runoob.com",
            "mobile": "+25.634685273541",
            "magic_number": 58524523
        }
        # password少了符号_*-^之一
        self.testCase15 = {
            "username": "atgGa134342",
            "password": "rthsdfSF1",
            "nickname": "uiJRTjtytut(#t",
            "url": "https://www.runoob.com",
            "mobile": "+25.634685273541",
            "magic_number": 58524523
        }
        # password少了大写字母
        self.testCase16 = {
            "username": "atgGa134342",
            "password": "rthf*d0",
            "nickname": "uiJRTjtytut(#t",
            "url": "https://www.runoob.com",
            "mobile": "+25.634685273541",
            "magic_number": 58524523
        }

        # password少了数字
        self.testCase17 = {
            "username": "atgGa134342",
            "password": "rew_________DD",
            "nickname": "uiJRTjtytut(#t",
            "url": "https://www.runoob.com",
            "mobile": "+25.634685273541",
            "magic_number": 58524523
        }

        # password少了小写字母
        self.testCase18 = {
            "username": "atgGa134342",
            "password": "GITHUB***____DD",
            "nickname": "uiJRTjtytut(#t",
            "url": "https://www.runoob.com",
            "mobile": "+25.634685273541",
            "magic_number": 58524523
        }

        # url标签以-开头
        self.testCase19 = {
            "username": "atgGa134342",
            "password": "GIp***1____DD",
            "nickname": "uiJRTjtytut(#t",
            "url": "https://www.runoob.-df.com",
            "mobile": "+25.634685273541",
            "magic_number": 58524523
        }

        # url标签以-结尾
        self.testCase20 = {
            "username": "atgGa134342",
            "password": "GIwB***1____DD",
            "nickname": "uiJRTjtytut(#t",
            "url": "https://www.runoob.234-df-.com",
            "mobile": "+25.634685273541",
            "magic_number": 58524523
        }

        # url不满足域名部分包含 1 到多个点 .
        self.testCase21 = {
            "username": "atgGa134342",
            "password": "wB***1____DD",
            "nickname": "uiJRTjtytut(#t",
            "url": "https://github",
            "mobile": "+25.634685273541",
            "magic_number": 58524523
        }

        # url顶级域名纯数字
        self.testCase22 = {
            "username": "atgGa134342",
            "password": "dB***1____DD",
            "nickname": "uiJRTjtytut(#t",
            "url": "https://github.23478-278dfd.233.123",
            "mobile": "+25.634685273541",
            "magic_number": 58524523
        }

        # url过长
        self.testCase23 = {
            "username": "atgGa134342",
            "password": "dB***1____DD",
            "nickname": "uiJRTjtytut(#t",
            "url": "http://gERRTEb.23478-4sd.klewEFW-34.24DSD3.2dfd.23t3.com",#49
            "mobile": "+25.634685273541",
            "magic_number": 58524523
        }

        # url并非http开头（有空格）
        self.testCase24 = {
            "username": "atgGa134342",
            "password": "dB***1____DD",
            "nickname": "uiJRTjtytut(#t",
            "url": " http://grERRTEb.23478-4sd.klew3.2dfd.233.123.ci",
            "mobile": "+25.634685273541",
            "magic_number": 58524523
        }

        # url并非https开头
        self.testCase25 = {
            "username": "atgGa134342",
            "password": "dB***1____DD",
            "nickname": "uiJRTjtytut(#t",
            "url": "1https://grERRTEb.23478-4sd.klew3.2dfd.233.123.ci",
            "mobile": "+25.634685273541",
            "magic_number": 58524523
        }

        # mobile区号1位
        self.testCase26 = {
            "username": "atgGa134342",
            "password": "dB***1____DD",
            "nickname": "uiJRTjtytut(#t",
            "url": "http://g-ERRTEb.23478-4sd.kl33.123.com",
            "mobile": "+2.634685273541",
            "magic_number": 58524523
        }

        # mobile手机号不为12位
        self.testCase27 = {
            "username": "atgGa134342",
            "password": "dB***1____DD",
            "nickname": "uiJRTjtytut(#t",
            "url": "https://gfERRTEb.23l33.123.com",
            "mobile": "+25.63468527351",
            "magic_number": 58524523
        }

        # mobile手机号不为12位
        self.testCase28 = {
            "username": "atgGa134342",
            "password": "dB***1____DD",
            "nickname": "uiJRTjtytut(#t",
            "url": "https://gfERRTEb.23l33.123.com",
            "mobile": "+25.6346852766351",
            "magic_number": 58524523
        }

        # mobile手机号有字母
        self.testCase29 = {
            "username": "atgGa134342",
            "password": "dB***1____DD",
            "nickname": "uiJRTjtytut(#t",
            "url": "https://gfERRTEb.23l33.123.com",
            "mobile": "+25.6346852761A1",
            "magic_number": 58524523
        }

        # magic_number为负值
        self.testCase30 = {
            "username": "atgGa134342",
            "password": "dB***1____DD",
            "nickname": "uiJRTjtytut(#t",
            "url": "https://gfERRTEb.23l33.123.com",
            "mobile": "+25.634685276101",
            "magic_number": -1223
        }

        # magic_number为负值小数
        self.testCase31 = {
            "username": "atgGa134342",
            "password": "dB***1____DD",
            "nickname": "uiJRTjtytut(#t",
            "url": "https://gfERRTEb.23l33.123.com",
            "mobile": "+25.634685276101",
            "magic_number": -12.23
        }

        # magic_number有小数
        self.testCase32 = {
            "username": "atgGa134342",
            "password": "dB***1____DD",
            "nickname": "uiJRTjtytut(#t",
            "url": "https://gfERRTEb.23l33.123.com",
            "mobile": "+25.634685276101",
            "magic_number": 42243.1
        }

        # magic_number有小数
        self.testCase33 = {
            "username": "atgGa134342",
            "password": "dB***1____DD",
            "nickname": "uiJRTjtytut(#t",
            "url": "https://gfERRTEb.23l33.123.com",
            "mobile": "+25.634685276101",
            "magic_number": 42243.1223555
        }

        # magic_number有字母
        self.testCase34 = {
            "username": "atgGa134342",
            "password": "dB***1____DD",
            "nickname": "uiJRTjtytut(#t",
            "url": "https://gfERRTEb.23l33.123.com",
            "mobile": "+25.634685276101",
            "magic_number": "j2333"
        }

        # magic_number有其他符号
        self.testCase35 = {
            "username": "atgGa134342",
            "password": "dB***1____DD",
            "nickname": "uiJRTjtytut(#t",
            "url": "https://gfERRTEb.23l33.123.com",
            "mobile": "+25.634685276101",
            "magic_number": "@2333"
        }


    def test_register_params_check(self):

        self.assertEqual(register_params_check(self.testCase1), ("ok", True))
        self.assertEqual(register_params_check(self.testCase2), ("ok", True))
        self.assertEqual(register_params_check(self.testCase3), ("ok", True))
        self.assertEqual(register_params_check(self.testCase4), ("ok", True))
        self.assertEqual(register_params_check(self.testCase5), ("ok", True))
        self.assertEqual(register_params_check(self.testCase6), ("ok", True))
        self.assertEqual(register_params_check(self.testCase7), ("ok", True))
        self.assertEqual(register_params_check(self.testCase8), ("ok", True))
        self.assertEqual(register_params_check(self.testCase9), ("ok", True))
        self.assertEqual(register_params_check(self.testCase10), ("ok", True))
        self.assertEqual(register_params_check(self.testCase11), ("username", False))
        self.assertEqual(register_params_check(self.testCase12), ("username", False))
        self.assertEqual(register_params_check(self.testCase13), ("username", False))
        self.assertEqual(register_params_check(self.testCase14), ("username", False))
        self.assertEqual(register_params_check(self.testCase15), ("password", False))
        self.assertEqual(register_params_check(self.testCase16), ("password", False))
        self.assertEqual(register_params_check(self.testCase17), ("password", False))
        self.assertEqual(register_params_check(self.testCase18), ("password", False))
        self.assertEqual(register_params_check(self.testCase19), ("url", False))
        self.assertEqual(register_params_check(self.testCase20), ("url", False))
        self.assertEqual(register_params_check(self.testCase21), ("url", False))
        self.assertEqual(register_params_check(self.testCase22), ("url", False))
        self.assertEqual(register_params_check(self.testCase23), ("url", False))
        self.assertEqual(register_params_check(self.testCase24), ("url", False))
        self.assertEqual(register_params_check(self.testCase25), ("url", False))
        self.assertEqual(register_params_check(self.testCase26), ("mobile", False))
        self.assertEqual(register_params_check(self.testCase27), ("mobile", False))
        self.assertEqual(register_params_check(self.testCase28), ("mobile", False))
        self.assertEqual(register_params_check(self.testCase29), ("mobile", False))
        self.assertEqual(register_params_check(self.testCase30), ("magic_number", False))
        self.assertEqual(register_params_check(self.testCase31), ("magic_number", False))
        self.assertEqual(register_params_check(self.testCase32), ("magic_number", False))
        self.assertEqual(register_params_check(self.testCase33), ("magic_number", False))
        self.assertEqual(register_params_check(self.testCase34), ("magic_number", False))
        self.assertEqual(register_params_check(self.testCase35), ("magic_number", False))

if __name__ == "__main__":
    unittest.main()
