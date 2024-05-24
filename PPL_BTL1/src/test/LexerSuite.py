import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test1(self):
        input = "true false number bool string return var dynamic func for until by break continue if else elif begin end not and or"
        expect = "true,false,number,bool,string,return,var,dynamic,func,for,until,by,break,continue,if,else,elif,begin,end,not,and,or,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 1))

    def test2(self):
        input = "1 2 3 4 5 6 7 8 9 0"
        expect = "1,2,3,4,5,6,7,8,9,0,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 2))

    def test3(self):
        input = "+-*/%= <- != < <= > >= ... =="
        expect = "+,-,*,/,%,=,<-,!=,<,<=,>,>=,...,==,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 3))

    def test4(self):
        input = "[(,,)]"
        expect = "[,(,,,,,),],<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 4))

    def test5(self):
        input = "&"
        expect = "Error Token &"
        self.assertTrue(TestLexer.test(input, expect, 5))

    def test6(self):
        input = "#"
        expect = "Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 6))

    def test7(self):
        input = "11abc"
        expect = "11,abc,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 7))

    def test8(self):
        input = "abc11"
        expect = "abc11,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 8))

    def test9(self):
        input = "0 -0 1 4 5 6 7 8 9 0 4.e3 0.e-30 31e+3 31e-3 0e+3 0e-3"
        expect = "0,-,0,1,4,5,6,7,8,9,0,4.e3,0.e-30,31e+3,31e-3,0e+3,0e-3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 9))

    def test10(self):
        input = ".1"
        expect = "Error Token ."
        self.assertTrue(TestLexer.test(input, expect, 10))

    def test11(self):
        input = "1."
        expect = "1.,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 11))

    def test12(self):
        input = "Hoang\nNam"
        expect = "Hoang,\n,Nam,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 12))

    def test13(self):
        input = """ " " """
        expect = " ,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 13))
    def test14(self):
        input = """ "Hoang Nam" """
        expect = "Hoang Nam,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 14))
    def test15(self):
        input = """ "' \\b \\f \\r \\n \\t \\\\ Vo \\b \\f \\r \\n \\t \\\\   \\b \\f \\r \\n \\t \\\\" """
        expect = "' \\b \\f \\r \\n \\t \\\\ Vo \\b \\f \\r \\n \\t \\\\   \\b \\f \\r \\n \\t \\\\,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 15))
    def test16(self):
        input=""" "Hoang\nNam" """
        expect = "Unclosed String: Hoang"
        self.assertTrue(TestLexer.test(input, expect, 16))
    def test17(self):
        input=""" "Hoang Nam """
        expect = "Unclosed String: Hoang Nam "
        self.assertTrue(TestLexer.test(input, expect, 17))
    def test18(self):
        input=""" "Hoang Nam \n" """
        expect = "Unclosed String: Hoang Nam "
        self.assertTrue(TestLexer.test(input, expect, 18))
    def test19(self):
        input=""" "Hoang \\o" """
        expect = "Illegal Escape In String: Hoang \\o"
        self.assertTrue(TestLexer.test(input, expect, 19))
    def test20(self):
        input=""" "Hoang \\\ " """
        expect = "Hoang \\\ ,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 20))
    def test21(self):
        input=""" "Hoang \\\n" """
        expect = "Illegal Escape In String: Hoang \\\n"
        self.assertTrue(TestLexer.test(input, expect, 21))
    def test22(self):
        input=""" "Hoang \\\t" """
        expect = "Illegal Escape In String: Hoang \\\t"
        self.assertTrue(TestLexer.test(input, expect, 22))
    def test23(self):
        input=" ###Happy newyear 2024"
        expect="<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 23))
    def test24(self):
        input="###"
        expect="<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 24))
    def test25(self):
        input="a##1"
        expect="a,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 25))
    def test26(self):
        input="a#"
        expect="a,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 26))
    def test27(self):
        input="~"
        expect="Error Token ~"
        self.assertTrue(TestLexer.test(input, expect, 27))
    def test28(self):
        input="~a"
        expect="Error Token ~"
        self.assertTrue(TestLexer.test(input, expect, 28))
    def test29(self):
        input="~1"
        expect="Error Token ~"
        self.assertTrue(TestLexer.test(input, expect, 29))
    def test30(self):
        input="~1.2"
        expect="Error Token ~"
        self.assertTrue(TestLexer.test(input, expect, 30))
    def test31(self):
        input="^"
        expect="Error Token ^"
        self.assertTrue(TestLexer.test(input, expect, 31))
    def test32(self):
        input="""
            xin chao "Hoang Nam"
            #loi chao cao hon mam co
        """
        expect = "\n,xin,chao,Hoang Nam,\n,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 32))
    def test33(self):
        input="""
            xin chao "Hoang Nam"
            ###loi chao cao hon mam co
        """
        expect="\n,xin,chao,Hoang Nam,\n,\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 33))
    def test34(self):
        input="""a<-b"""
        expect="a,<-,b,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 34))
    def test35(self):
        input="""a<-##b"""
        expect="a,<-,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 35))
    def test36(self):
        input="""a<-##b"""
        expect="a,<-,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 36))
    def test37(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 37))
    def test38(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 38))
    def test39(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 39))
    def test40(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 40))
    def test41(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 41))
    def test42(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 42))
    def test43(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 43))
    def test44(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 44))
    def test45(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 45))
    def test46(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 46))
    def test47(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 47))
    def test48(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 48))
    def test49(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 49))
    def test50(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 50))
    def test51(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 51))
    def test52(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 52))
    def test53(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 53))
    def test54(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 54))
    def test55(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 55))
    def test56(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 56))
    def test57(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 57))
    def test58(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 58))
    def test59(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 59))
    def test60(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 60))
    def test61(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 61))
    def test62(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 62))
    def test63(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 63))
    def test64(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 64))
    def test65(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 65))
    def test66(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 66))
    def test67(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 67))
    def test68(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 68))
    def test69(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 69))
    def test70(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 70))
    def test71(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 71))
        
    def test72(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 72))
    def test73(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 73))
    def test74(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 74))
    def test75(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 75))
    def test76(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 76))
    def test77(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 77))
    def test78(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 78))
    def test79(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 79))
    def test80(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 80))
    def test81(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 81))
    def test82(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 82))
    def test83(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 83))
    def test84(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 84))
    def test85(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 85))
    def test86(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 86))
    def test87(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 87))
    def test88(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 88))
    def test89(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 89))
    def test90(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 90))
    def test91(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 91))
    def test92(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 92))
    def test93(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 93))
    def test94(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 94))
    def test95(self):
        
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 95))
    def test96(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 96))
    def test97(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 97))
    def test98(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 98))
    def test99(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 99))
    def test100(self):
        input="""a<-#b"""
        expect="a,<-,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 100))
        
   

