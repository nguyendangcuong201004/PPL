import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    # Me (TIN)
    def test2(self):
        input="""
            dynamic x
            number a<-[x]
            func main() return
        """
        expect=""
        self.assertTrue(TestChecker.test(input,expect,402))
#     def test1(self):
#         input = """number a
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 400))

#     def test2(self):
#         input = """
#         func foo()
#         func main() begin
#             foo()
#         end
#         """
#         expect = "No Function Definition: foo"
#         self.assertTrue(TestChecker.test(input, expect, 401))

#     def test3(self):
#         input = """
#         func foo() begin
#             return 1
#         end
#         func main() begin
#             foo()
#         end
#         """
#         expect = "Type Mismatch In Statement: CallStmt(Id(foo), [])"
#         self.assertTrue(TestChecker.test(input, expect, 402))

#     def test4(self):
#         input = """
#         func main() begin
            
#             dynamic b
#             dynamic a 
#             number x[1, 2] <- [[1,b]]
#         end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 403))

#     def test5(self):
#         input = """
#         func main() begin
            
#             dynamic b
#             dynamic a <- [b]
#             number x[1, 2] <- [[1,b]]
#         end
#         """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, dynamic, ArrayLit(Id(b)))"
#         self.assertTrue(TestChecker.test(input, expect, 404))

#     def test6(self):
#         input = """
#         func main() begin
#             number x[1, 2] <- [[1,2]]
#         end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 405))

#     def test7(self):
#         input = """
#         func main() begin
#         dynamic b
#             number x[2, 2] <- [[1,2], [b, b]]
#         end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 406))

#     def test8(self):
#         input = """
#         func main() begin
#         end
#         func foo(number x)
#         func foo(number x, number y) begin
#         end
#         """
#         expect = "Redeclared Function: foo"
#         self.assertTrue(TestChecker.test(input, expect, 407))

#     def test9(self):
#         input = """
#         func main() begin
#         number a <- a
#         end
#         func foo(number x, number y)
#         func foo(number z, number x) begin
#         end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 408))

#     def test10(self):
#         input = """
#         func main() begin
#         end
#         func foo(number x, number x) begin
#         end
#         """
#         expect = "Redeclared Parameter: x"
#         self.assertTrue(TestChecker.test(input, expect, 409))

#     def test11(self):
#         input = """
# func main()
# begin
#     var x <- [[[[1, 2]], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]]

# end
# """
#         myret_ = "Type Mismatch In Expression: ArrayLit(ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))), ArrayLit(NumLit(3.0), NumLit(4.0), NumLit(5.0)))"
#         self.assertTrue(TestChecker.test(input, myret_, 410))

#     def test12(self):
#         input = """
# func main()
# begin
#     number a[2, 2] <- [[1, 2], [3, 4]]
#     number b[2] <- a[0]
#     writeNumber(b[0])
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 411))

#     def test13(self):
#         input = """
#         func main()
# begin 
#     dynamic a
#     dynamic b
#     dynamic c
#     number x[3,3] <- [a,b]
#     a <- [1,2,3]
#     b <- [4,5,6]
#     c <- [7,8,9]
#     writeNumber(a[0] + b[0] + c[0])
# end
# """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(x), ArrayType([3.0, 3.0], NumberType), None, ArrayLit(Id(a), Id(b)))"
#         self.assertTrue(TestChecker.test(input, expect, 412))

#     def test14(self):
#         input = """
#         func main()
# begin 
#     dynamic a
#     dynamic b
#     dynamic c
#     number x[3,3] <- [a,b, c]
#     a <- [1,2,3]
#     b <- [4,5,6]
#     c <- [7,8,9]
#     writeNumber(a[0] + b[0] + c[0])
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 413))

#     def test15(self):
#         input = """
#         func main()
# begin 
#     dynamic a
#     dynamic b
#     dynamic c
#     dynamic d <- [a,b,c]
# end
# """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(d), None, dynamic, ArrayLit(Id(a), Id(b), Id(c)))"
#         self.assertTrue(TestChecker.test(input, expect, 414))

#     def test16(self):
#         input = """
#             dynamic a
#             dynamic x
#             dynamic y
#             func foo(number a,string b) return
#             func main() begin
#                 number a <- foo(x,y)
#                 number x
#             end
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(foo), [Id(x), Id(y)])"
#         self.assertTrue(TestChecker.test(input, expect, 415))
# # ################ QUAN #################

#     def test1(self):
#         input = """func test()
#                 func test() begin
#                 end
#                 func main() begin
#                 end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 400))

#     def test2(self):
#         input = """func test() begin
#     end
#     func test()
#     func main() begin
#     end
#         """
#         expect = "Redeclared Function: test"
#         self.assertTrue(TestChecker.test(input, expect, 401))

#     def test3(self):
#         input = """func test()
#     func main() begin
#     end
#     func test() begin
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 402))

#     def test4(self):
#         input = """func test()
#     func main() begin
#     end
#     func test()
#         """
#         expect = "Redeclared Function: test"
#         self.assertTrue(TestChecker.test(input, expect, 403))

#     def test5(self):
#         input = """
#         func test()
#         func test() begin
#         end
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 404))

#     def test6(self):
#         input = """func test()
#     func test() begin
#     end
#     func main(number a) begin
#     end
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 405))

#     def test7(self):
#         input = """func test(number a, string b)
#     func test(number a, string b) begin
#     end
#     func main() begin
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 406))

#     def test8(self):
#         input = """func test(number a, string b)
#     func test(number c, string d) begin
#     end
#     func main() begin
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 407))

#     def test9(self):
#         input = """func test(number a, string a)
#     func test(number c, string d) begin
#     end
#     func main() begin
#     end
#         """
#         expect = "Redeclared Parameter: a"
#         self.assertTrue(TestChecker.test(input, expect, 408))

#     def test10(self):
#         input = """
#     func main() begin
#         number a <- 1
#         a <- "bruh"
#     end
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(a), StringLit(bruh))"
#         self.assertTrue(TestChecker.test(input, expect, 409))

#     def test11(self):
#         input = """
#     func main() begin
#         number a <- 1
#         number a <- 1
#     end
#         """
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input, expect, 410))

#     def test12(self):
#         input = """
#     func main() begin
#         var a <- 1
#         a <- 10.99
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 411))

#     def test13(self):
#         input = """
#     func main() begin
#         var a <- 1
#         a <- true
#     end
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(a), BooleanLit(True))"
#         self.assertTrue(TestChecker.test(input, expect, 412))

#     def test14(self):
#         input = """
#     func main() begin
#         dynamic a
#         a <- 1000
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 413))

#     def test15(self):
#         input = """
#     func main() begin
#         dynamic a
#         a <- 1000
#         a <- "hello"
#     end
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(a), StringLit(hello))"
#         self.assertTrue(TestChecker.test(input, expect, 414))

#     def test16(self):
#         input = """
#     dynamic a
#     func main() begin
#         a <- 1000
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 415))

#     def test17(self):
#         input = """
#     func main() begin
#         dynamic a
#         var b <- a
#     end
#         """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(b), None, var, Id(a))"
#         self.assertTrue(TestChecker.test(input, expect, 416))

#     def test18(self):
#         input = """
#     func main() begin
#         dynamic a
#         dynamic b
#         b <- a
#     end
#         """
#         expect = "Type Cannot Be Inferred: AssignStmt(Id(b), Id(a))"
#         self.assertTrue(TestChecker.test(input, expect, 417))

#     def test19(self):
#         input = """
#     func main() begin
#         dynamic a
#         dynamic b <- a
#     end
#         """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(b), None, dynamic, Id(a))"
#         self.assertTrue(TestChecker.test(input, expect, 418))

#     def test20(self):
#         input = """
#     func main() begin
#         number a <- a
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 419))

#     def test21(self):
#         input = """
#     number a
#     string b
#     bool c
#     func main() begin
#         a <- 123
#         b <- "hello"
#         c <- true
#         string a <- "another a"
#         dynamic b <- a
#         var c <- a
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 420))

#     def test22(self):
#         input = """
#     number a
#     string b
#     bool c
#     func main() begin
#         a <- 123
#         b <- "hello"
#         c <- true
#         string a <- "another a"
#         dynamic b <- a
#         var c <- a
#         a <- 456
#     end
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(a), NumLit(456.0))"
#         self.assertTrue(TestChecker.test(input, expect, 421))

#     def test23(self):
#         input = """
#     number a
#     string b
#     bool c
#     func main() begin
#         a <- 123
#         b <- "hello"
#         c <- true
#         string a <- "another a"
#         var c <- a
#         b <- c
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 422))

#     def test24(self):
#         input = """
#     func test() begin
#     end
#     func main() begin
#         test()
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 423))

#     def test25(self):
#         input = """
#     func test(number a, bool b) begin
#     end
#     func main() begin
#         test(1, true)
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 424))

#     def test26(self):
#         input = """
#     func test(number a, bool b) begin
#     end
#     func main() begin
#         test("wrong", true)
#     end
#         """
#         expect = "Type Mismatch In Statement: CallStmt(Id(test), [StringLit(wrong), BooleanLit(True)])"
#         self.assertTrue(TestChecker.test(input, expect, 425))

#     def test27(self):
#         input = """
#     func test(number a, bool b) return true
#     func main() begin
#         bool b <- test(1, true)
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 426))

#     def test28(self):
#         input = """
#     func test(number a, bool b) return true
#     func main() begin
#         number b <- test(1, true)
#     end
#         """
#         expect = "Type Mismatch In Statement: VarDecl(Id(b), NumberType, None, CallExpr(Id(test), [NumLit(1.0), BooleanLit(True)]))"
#         self.assertTrue(TestChecker.test(input, expect, 427))

#     def test29(self):
#         input = """
#     func test(number a, bool b) return true
#     func main() begin
#         test(1, true)
#     end
#         """
#         expect = "Type Mismatch In Statement: CallStmt(Id(test), [NumLit(1.0), BooleanLit(True)])"
#         self.assertTrue(TestChecker.test(input, expect, 428))

#     def test30(self):
#         input = """
#     func test(number a, bool b) return true
#     func main() begin
#         dynamic a
#         bool b <- test(1, a)
#         a <- true
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 429))

#     def test31(self):
#         input = """
#     func test(number a, bool b) return true
#     func main() begin
#         dynamic a
#         bool b <- test(1, a)
#         a <- 123
#     end
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(a), NumLit(123.0))"
#         self.assertTrue(TestChecker.test(input, expect, 430))

#     def test32(self):
#         input = """
#     func test(number a, bool b) return true
#     func main() begin
#         bool b <- test(1, test(2, false))
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 431))

#     def test33(self):
#         input = """
#     func test(number a, bool b)
#     func main() begin
#         bool b <- test(1, test(2, false))
#     end
#         """
#         expect = "No Function Definition: test"
#         self.assertTrue(TestChecker.test(input, expect, 432))

#     def test34(self):
#         input = """
#     func test(number a, bool b)
#     func main() begin
#         string b <- test(1, test(2, false))
#     end
#         """
#         expect = "Type Mismatch In Statement: VarDecl(Id(b), StringType, None, CallExpr(Id(test), [NumLit(1.0), CallExpr(Id(test), [NumLit(2.0), BooleanLit(False)])]))"
#         self.assertTrue(TestChecker.test(input, expect, 433))

#     def test35(self):
#         input = """
#     func test(number a, bool b)
#     func main() begin
#         bool b <- test(1, test(2, false))
#     end
#     func test(number c, bool d) return 1.23
#         """
#         expect = "Type Mismatch In Statement: Return(NumLit(1.23))"
#         self.assertTrue(TestChecker.test(input, expect, 434))

#     def test36(self):
#         input = """
#     func test(number a, bool b)
#     func main() begin
#         bool b <- test(1, test(2, false))
#     end
#     func test(number c, bool d) return true
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 435))
# # Nam

#     def test_1(self):
#         input = """
#             number a
#             number a
#         """
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input, expect, 1))


#     def test_3(self):
#         input = """
#             func foo()
#             func foo()
#         """
#         expect = "Redeclared Function: foo"
#         self.assertTrue(TestChecker.test(input, expect, 3))

#     def test_4(self):
#         input = """
#             func foo() return
#             func foo() return
#         """
#         expect = "Redeclared Function: foo"
#         self.assertTrue(TestChecker.test(input, expect, 4))

#     def test_5(self):
#         input = """
#             func foo() return
#             func foo() 
#         """
#         expect = "Redeclared Function: foo"
#         self.assertTrue(TestChecker.test(input, expect, 5))

#     def test_6(self):
#         input = """
#             func foo(number a,string b) 
#             func foo(string a,number b) 
#         """
#         expect = "Redeclared Function: foo"
#         self.assertTrue(TestChecker.test(input, expect, 6))

#     def test_7(self):
#         input = """
#             func foo(number a,string b) 
#             func foo(number a,string b) 
#         """
#         expect = "Redeclared Function: foo"
#         self.assertTrue(TestChecker.test(input, expect, 7))

#     def test_8(self):
#         input = """
#             func foo(number a,string b) 
#             func foo(number a,string b) begin
#             end
#             func main() return
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 8))

#     def test_9(self):
#         input = """
#             number a
#             func foo(number a,string a)
#                 begin
#                     number a
#                 end
#         """
#         expect = "Redeclared Parameter: a"
#         self.assertTrue(TestChecker.test(input, expect, 9))

#     def test_10(self):
#         input = """
#             number a
#             func foo(number a,string b)
#                 begin
#                     c <- a
#                 end
#         """
#         expect = "Undeclared Identifier: c"
#         self.assertTrue(TestChecker.test(input, expect, 10))

#     def test_11(self):
#         input = """
#             number a
#             number b
#             var c <- d
#         """
#         expect = "Undeclared Identifier: d"
#         self.assertTrue(TestChecker.test(input, expect, 11))

#     def test_12(self):
#         input = """
#             number a
#             number b
#             func main() begin
#                 c <- d
#             end
#         """
#         expect = "Undeclared Identifier: c"
#         self.assertTrue(TestChecker.test(input, expect, 12))

#     def test_13(self):
#         input = """
#             number a
#             number b
#             func foo(number a,string b) begin
#             end
#             func main() begin
#                 foo1()
#             end
#         """
#         expect = "Undeclared Function: foo1"
#         self.assertTrue(TestChecker.test(input, expect, 13))

#     def test_14(self):
#         input = """
#             number a[2,3]
#             number c
#             func foo() begin
#                 c[1,2]<-5
#             end
#             func main() return
#         """
#         expect = "Type Mismatch In Expression: ArrayCell(Id(c), [NumLit(1.0), NumLit(2.0)])"
#         self.assertTrue(TestChecker.test(input, expect, 14))

#     def test_15(self):
#         input = """
#             number a[2,3]
#             number c
#             func foo() begin
#                 c["1","2"]<-5
#             end
#             func main() return
#         """
#         expect = "Type Mismatch In Expression: ArrayCell(Id(c), [StringLit(1), StringLit(2)])"
#         self.assertTrue(TestChecker.test(input, expect, 15))

#     def test_16(self):
#         input = """
#             number a[2,3]
#             number c
#             func foo() begin
#                 a["1","2"]<-5
#             end
#             func main() return
#         """
#         expect = "Type Mismatch In Expression: ArrayCell(Id(a), [StringLit(1), StringLit(2)])"
#         self.assertTrue(TestChecker.test(input, expect, 16))

#     def test_17(self):
#         input = """
#             number a[2,3]
#             number c
#             func foo() begin
#                 a[2,3]<-5
#             end
#             func main() return
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 17))

#     def test_18(self):
#         input = """
#             number a[2,3]
#             number c
#             func foo() begin
#                 a[2,3]<-"5"
#             end
#             func main() return
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a), [NumLit(2.0), NumLit(3.0)]), StringLit(5))"
#         self.assertTrue(TestChecker.test(input, expect, 18))

#     def test_19(self):
#         input = """
#             number a
#             string b
#             func foo() begin
#                 number c <- a + b
#             end
#             func main() return
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(+, Id(a), Id(b))"
#         self.assertTrue(TestChecker.test(input, expect, 19))

#     def test_20(self):
#         input = """
#             bool a
#             bool b
#             func foo() begin
#                 number c <- a + b
#             end
#             func main() return
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(+, Id(a), Id(b))"
#         self.assertTrue(TestChecker.test(input, expect, 20))

#     def test_21(self):
#         input = """
#             bool a
#             bool b
#             func foo() begin
#                 number c <- -a
#             end
#             func main() return
#         """
#         expect = "Type Mismatch In Expression: UnaryOp(-, Id(a))"
#         self.assertTrue(TestChecker.test(input, expect, 21))

#     def test_22(self):
#         input = """
#             number a
#             bool b
#             func foo() begin
#                 number c <- -a
#             end
#             func main() return
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 22))

#     def test_23(self):
#         input = """
#             number a
#             bool b
#             func foo() begin
#                 number c <- -a
#             end
#             func foo1() begin
#                 b <- foo()
#             end
#             func main() return
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(foo), [])"
#         self.assertTrue(TestChecker.test(input, expect, 23))

#     def test_24(self):
#         input = """
#             number a
#             bool b
#             func foo() begin
#                 number c <- -a
#                 return true
#             end
#             func foo1() begin
#                 b <- foo()
#             end
#             func main() return
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 24))

#     def test_25(self):
#         input = """
#             number a
#             func foo() return
#             func main() begin
#                 number b <- a
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 25))

#     def test_26(self):
#         input = """
#             dynamic a
#             func foo() return
#             func main() begin
#                 var b <- a
#             end
#         """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(b), None, var, Id(a))"
#         self.assertTrue(TestChecker.test(input, expect, 26))

#     def test_27(self):
#         input = """
#             var a<-5
#             func foo() return
#             func main() begin
#                 var b <- a
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 27))

#     def test_28(self):
#         input = """
#             dynamic a
#             func foo() return
#             func main() begin
#                 var b <- a and (a>b)
#             end
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(>, Id(a), Id(b))"
#         self.assertTrue(TestChecker.test(input, expect, 28))

#     def test_29(self):
#         input = """
#             dynamic a
#             func foo() return
#             func main() begin
#                 var b <- a and true
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 29))

    

#     def test_31(self):
#         input = """
#             dynamic a
#             func foo(number a) return
#             func main() begin
#                 var y <- a+foo(x)
#             end
#         """
#         expect = "Undeclared Identifier: x"
#         self.assertTrue(TestChecker.test(input, expect, 31))

#     def test_32(self):
#         input = """
#             dynamic a
#             dynamic x
#             func foo(number a) return
#             func main() begin
#                 var y <- a+foo(x)
#             end
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(foo), [Id(x)])"
#         self.assertTrue(TestChecker.test(input, expect, 32))

#     def test_33(self):
#         input = """
#             dynamic a
#             dynamic x
#             func foo(number a) return a
#             func main() begin
#                 var y <- a+foo(x)
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 33))

   

#     def test_35(self):
#         input = """
#             dynamic a
#             dynamic x
#             dynamic y
#             func foo(number a,string b) return 
#             func main() begin
#                 foo(x,y)
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 35))

#     def test_36(self):
#         input = """
#             dynamic a
#             dynamic x
#             dynamic y
#             func foo(number a,string b) return
#             func main() begin
#                 number a <- foo(x,y)
#             end
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(foo), [Id(x), Id(y)])"
#         self.assertTrue(TestChecker.test(input, expect, 36))

#     def test_37(self):
#         input = """
#             dynamic a
#             dynamic b
#             func main() begin
#                 a<-b
#             end
#         """
#         expect = "Type Cannot Be Inferred: AssignStmt(Id(a), Id(b))"
#         self.assertTrue(TestChecker.test(input, expect, 37))

#     def test_38(self):
#         input = """
#             dynamic a
#             dynamic b
#             number c
#             func main() begin
#                 b <- c
#                 a <- b
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 38))

#     def test_39(self):
#         input = """
#             dynamic a
#             dynamic b
#             number c[2,3]
#             func main() begin
#                 b <- c
#                 a <- b
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 39))

#     def test_40(self):
#         input = """
#             dynamic a
#             var b <- [2,3,4,5]
#             number c[2,3]
#             func main() begin
#                 b <- [2,3,4,5]
#                 a <- b
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 40))

#     def test_41(self):
#         input = """
#             dynamic a
#             dynamic b
#             number c[2,3]
#             func main() begin
#                 b <- [2,3,4,a]
#                 a <- b
#             end
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(a), Id(b))"
#         self.assertTrue(TestChecker.test(input, expect, 41))

#     def test_42(self):
#         input = """
#             dynamic a
#             dynamic b
#             number c[2,3]
#             func main() begin
#                 b <- [2,3,4,a]
#                 c <- b
#             end
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(c), Id(b))"
#         self.assertTrue(TestChecker.test(input, expect, 42))

#     def test_43(self):
#         input = """
#             dynamic a
#             dynamic b
#             number c[2,3]
#             dynamic d
#             func main() begin
#                 b <- [2,3,4,a]
#                 d <- b
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 43))

#     def test_44(self):
#         input = """
#             dynamic a
#             dynamic b
#             number c[2,3]
#             dynamic d
#             func main() begin
#                 b <- [2,3,4,a]
#                 d <- b
#                 if(a) begin
#                     a <- b
#                 end
#             end
#         """
#         expect = "Type Mismatch In Statement: If((Id(a), Block([AssignStmt(Id(a), Id(b))])), [], None)"
#         self.assertTrue(TestChecker.test(input, expect, 44))

#     def test_45(self):
#         input = """
#             dynamic a
#             dynamic b
#             number c[2,3]
#             dynamic d
#             func main() begin
#                 b <- [2,3,4,a]
#                 d <- b
#                 if(1) begin
#                     a <- b
#                 end
#             end
#         """
#         expect = "Type Mismatch In Statement: If((NumLit(1.0), Block([AssignStmt(Id(a), Id(b))])), [], None)"
#         self.assertTrue(TestChecker.test(input, expect, 45))

#     def test_46(self):
#         input = """
#             dynamic a
#             dynamic b
#             number c[2,3]
#             dynamic d
#             func main() begin
#                 b <- [2,3,4,a]
#                 d <- b
#                 if(true) begin
#                     writeString("hehe")
#                 end
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 46))

#     def test_47(self):
#         input = """
#             func foo() return
#             func foo1() begin
#                 foo <- 2
#             end
#             func main() return
#         """
#         expect = "Undeclared Identifier: foo"
#         self.assertTrue(TestChecker.test(input, expect, 47))

#     def test_48(self):
#         input = """
#             func foo() return
#             func foo1() begin
#                 number a[2,3]
#                 number b[2,3,4]
#                 a <- b
#             end
#             func main() return
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(a), Id(b))"
#         self.assertTrue(TestChecker.test(input, expect, 48))

#     def test_49(self):
#         input = """
#             func foo() return 1
#             func foo1() begin
#                 foo()
#             end
#             func main() return
#         """
#         expect = "Type Mismatch In Statement: CallStmt(Id(foo), [])"
#         self.assertTrue(TestChecker.test(input, expect, 49))

   

#     def test_51(self):
#         input = """
#             func foo(number x,string y) return 
#             func foo1() begin
#                 number y
#                 string x
#                 foo(x,y)
#             end
#             func main() return
#         """
#         expect = "Type Mismatch In Statement: CallStmt(Id(foo), [Id(x), Id(y)])"
#         self.assertTrue(TestChecker.test(input, expect, 51))

#     def test_52(self):
#         input = """
#             func foo() begin
#                 return 
#                 return "hehe"
#             end
#             func main() return
#         """
#         expect = "Type Mismatch In Statement: Return(StringLit(hehe))"
#         self.assertTrue(TestChecker.test(input, expect, 52))

#     def test_53(self):
#         input = """
#             func foo() begin
#                 return "hehe"
#                 return 
#             end
#             func main() return
#         """
#         expect = "Type Mismatch In Statement: Return()"
#         self.assertTrue(TestChecker.test(input, expect, 53))

#     def test_54(self):
#         input = """
#             func a()
#             func foo() begin
#                 return "hehe"
#             end
#             func main() return
#         """
#         expect = "No Function Definition: a"
#         self.assertTrue(TestChecker.test(input, expect, 54))

#     def test_55(self):
#         input = """
#             func main() begin
#                 break
#             end
#         """
#         expect = "Break Not In Loop"
#         self.assertTrue(TestChecker.test(input, expect, 55))

#     def test_56(self):
#         input = """
#             func main() begin
#                 continue
#                 break
#             end
#         """
#         expect = "Continue Not In Loop"
#         self.assertTrue(TestChecker.test(input, expect, 56))

#     def test_57(self):
#         input = """
#             func foo() begin
#                 ## continue
#                 ## break
#             end
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 57))

#     def test_58(self):
#         input = """
#             func a()
#             func main() begin 
#                 a()
#             end
#             func a() return 1
#         """
#         expect = "Type Mismatch In Statement: Return(NumLit(1.0))"
#         self.assertTrue(TestChecker.test(input, expect, 410))
# # KHANG

#     def test_1_1_No_entry_point(self):
#         input = """
#             func main() return
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 401))

#     def test_1_2_No_entry_point(self):
#         input = """
#             func main()
#             func main() begin
#                 number main
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 402))

#     def test_1_3_No_entry_point(self):
#         input = """
#             func main(number a) begin
#             end
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 403))

#     def test_1_4_No_entry_point(self):
#         input = """
#             func main() return 1   
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 404))

#     def test_1_5_No_entry_point(self):
#         input = """
#             number VoTien
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 405))

#     def test_2_1_NoDefinition(self):
#         input = """
#             func foo(number a)
#             func foo(number a) return     

#             func main() return
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 406))

#     def test_2_2_NoDefinition(self):
#         input = """
#             func foo(number a) return   

#             func main() return
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 407))

#     def test_2_3_NoDefinition(self):
#         input = """
#             func foo(number a) 

#             func main() return
#         """
#         expect = "No Function Definition: foo"
#         self.assertTrue(TestChecker.test(input, expect, 408))
#     # Redeclare and Undeclare

#     def test1(self):
#         input = """
#             number a
#             string a 
            
#             func main() return
#         """
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input, expect, 410))

#     def test2(self):
#         input = """
#             func a()
#             number a
            
#             func main() return
#         """
#         expect = "No Function Definition: a"
#         self.assertTrue(TestChecker.test(input, expect, 411))

#     def test3(self):
#         input = """
#             func foo() return
#             func foo()
            
#             func main() return
#         """
#         expect = "Redeclared Function: foo"
#         self.assertTrue(TestChecker.test(input, expect, 412))

#     def test4(self):
#         input = """
#             func foo()
#             func foo()
            
#             func main() return
#         """
#         expect = "Redeclared Function: foo"
#         self.assertTrue(TestChecker.test(input, expect, 413))

#     def test5(self):
#         input = """
#             func foo() return
#             func foo() return
            
#             func main() return
#         """
#         expect = "Redeclared Function: foo"
#         self.assertTrue(TestChecker.test(input, expect, 414))

#     def test6(self):
#         input = """
#             number foo
#             func foo() return
            
#             func main() return
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 415))

#     def test7(self):
#         input = """
#             number a
#             func VoTien() return
#             func main()begin
#                 number a
#                 number c
#                 string VoTien
#                 begin
#                     number c
#                     string VoTien
#                 end
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 416))

#     def test8(self):
#         input = """
#             number a
#             func VoTien() return
#             func main()begin
#                 number a
#                 string a
#             end
#         """
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input, expect, 417))

#     def test9(self):
#         input = """
#             number a
#             func VoTien() return
#             func main()begin
#                 number a
#                 begin
#                     number a
#                 end
#                 string a
#             end
#         """
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input, expect, 418))

#     def test10(self):
#         input = """
#             number a
#             func VoTien() return
#             func main()begin
#                 number a
#                 begin
#                     number a
#                     string a
#                 end
                
#             end
#         """
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input, expect, 419))

#     def test11(self):
#         input = """
#             number a
#             func VoTien(number a, number VoTien, number c)
#             begin
#                 string c
#             end
            
#             func main() return
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 420))

#     def test12(self):
#         input = """
#             number a
#             func VoTien(number a, number VoTien, number c, string c)
#             begin
#             end
            
#             func main() return
#         """
#         expect = "Redeclared Parameter: c"
#         self.assertTrue(TestChecker.test(input, expect, 421))

#     def test13(self):
#         input = """
#             number a
#             func foo(number a, number VoTien, number c)
#             begin
#                 begin
#                     number a
#                 end
#                 number a
#             end
            
#             func main() return
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 422))

#     def test14(self):
#         input = """
#             func foo(number a) 
#             func foo(number b) return
            
#             func main() return
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 423))

#     def test15(self):
#         input = """
#             func foo(number a) 
#             func foo(string a) return
            
#             func main() return
#         """
#         expect = "Redeclared Function: foo"
#         self.assertTrue(TestChecker.test(input, expect, 423))

#     def test16(self):
#         input = """
#             func foo(number a) 
#             func foo(number a, string c) return
            
#             func main() return
#         """
#         expect = "Redeclared Function: foo"
#         self.assertTrue(TestChecker.test(input, expect, 424))

#     def test17(self):
#         input = """
#             func foo(number a, string c) 
#             func foo(number a) return
            
#             func main() return
#         """
#         expect = "Redeclared Function: foo"
#         self.assertTrue(TestChecker.test(input, expect, 425))

#     def test18(self):
#         input = """
#             number a <- a
#             func main() begin
#                 number b <- a
#                 number c <- e
#             end
#         """
#         expect = "Undeclared Identifier: e"
#         self.assertTrue(TestChecker.test(input, expect, 426))

#     def test19(self):
#         input = """
#             func a() return 1
#             func main() begin
#                 number b <- a
#             end
#         """
#         expect = "Undeclared Identifier: a"
#         self.assertTrue(TestChecker.test(input, expect, 427))

#     def test20(self):
#         input = """
#             func a() return 1
#             func main() begin
#                 number a
#                 begin 
#                     number d
#                 end
#                 number b <- a
#                 number c <- d
#             end
#         """
#         expect = "Undeclared Identifier: d"
#         self.assertTrue(TestChecker.test(input, expect, 428))

#     def test21(self):
#         input = """
#             func a() begin
#                 a()
#             end
#             func main() begin
#                 a()
#                 b()
#             end
#         """
#         expect = "Undeclared Function: b"
#         self.assertTrue(TestChecker.test(input, expect, 429))

#     def test22(self):
#         input = """
#             func a() return
#             func main() begin
#                 number a
#                 a()
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 430))

#     def test23(self):
#         input = """
#             func a()
#             func main() begin
#                 a()
#             end
#             func a() return
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 431))

#     def test_4_MustInLoop(self):
#         input = """
#             func main() begin
#                 var i <- 2
#                 for i until true by 1
#                 begin
#                     break
#                     continue
#                     begin
#                         break
#                         continue
#                     end
                    
#                     for i until true by 1
#                     begin
#                         break
#                         continue
#                     end
#                     break
#                     continue
#                 end
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 432))

#         input = """
#             func main() begin
#                 break
#             end
#         """
#         expect = "Break Not In Loop"
#         self.assertTrue(TestChecker.test(input, expect, 433))

#         input = """
#             func main() begin
#                 continue
#             end
#         """
#         expect = "Continue Not In Loop"
#         self.assertTrue(TestChecker.test(input, expect, 434))

#     def test_5_1_TypeCannotBeInferred(self):
#         input = """
#             dynamic VoTien
#             var a <- VoTien

#             func main() return
#         """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, Id(VoTien))"
#         self.assertTrue(TestChecker.test(input, expect, 435))

#     def test_5_2_TypeCannotBeInferred(self):
#         input = """
#             number VoTien
#             var a <- VoTien
#             number b <- a

#             func main() return
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 436))

#     def test_5_3_TypeCannotBeInferred(self):
#         input = """
#             dynamic VoTien
#             number a <- VoTien
#             number b <- VoTien

#             func main() return
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 437))

#     def test_5_4_TypeCannotBeInferred(self):
#         input = """
#             func foo() begin
#                 dynamic a
#                 return a
#             end

#             func main() return
#         """
#         expect = "Type Cannot Be Inferred: Return(Id(a))"
#         self.assertTrue(TestChecker.test(input, expect, 438))

#     def test_5_5_TypeCannotBeInferred(self):
#         input = """
#             func foo() begin
#                 return 1
#                 dynamic a
#                 return a
#             end

#             func main() return
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 439))

#     def test_5_6_TypeCannotBeInferred(self):
#         input = """
#             func foo() begin
#                 number a
#                 return a
#                 return 1
#             end

#             func main() return
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 440))

#     def test_5_7_TypeCannotBeInferred(self):
#         input = """
#             func foo() begin
#                 dynamic a
#                 dynamic b
#                 a <- b
#             end

#             func main() return
#         """
#         expect = "Type Cannot Be Inferred: AssignStmt(Id(a), Id(b))"
#         self.assertTrue(TestChecker.test(input, expect, 441))

#     def test_5_8_TypeCannotBeInferred(self):
#         input = """
#             func foo() begin
#                 number a
#                 dynamic b
#                 a <- b
#                 b <- 1
#             end

#             func main() return
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 442))

#     def test_5_9_TypeCannotBeInferred(self):
#         input = """
#             func foo() begin
#                 number a
#                 dynamic b
#                 b <- a
#                 b <- 1
#             end

#             func main() return
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 443))

#     def test_6_1_TypeMismatchInStatement(self):
#         input = """
#             number a <- "1"

#             func main() return
#         """
#         expect = "Type Mismatch In Statement: VarDecl(Id(a), NumberType, None, StringLit(1))"
#         self.assertTrue(TestChecker.test(input, expect, 444))

#     def test_6_2_TypeMismatchInStatement(self):
#         input = """
#             number a[1,2] <- [[1,2]]

#             func main() return
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 445))

#     def test_6_3_TypeMismatchInStatement(self):
#         input = """
#             number a[1,2,3] <- [[1,2]]

#             func main() return
#         """
#         expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([1.0, 2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))))"
#         self.assertTrue(TestChecker.test(input, expect, 446))

#     def test_6_4_TypeMismatchInStatement(self):
#         input = """
#             number a[1] <- [[1,2]]

#             func main() return
#         """
#         expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([1.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))))"
#         self.assertTrue(TestChecker.test(input, expect, 447))

#     def test_6_5_TypeMismatchInStatement(self):
#         input = """
#             func foo() return

#             func main()begin
#                 foo()
#                 foo(1)
#             end
#         """
#         expect = "Type Mismatch In Statement: CallStmt(Id(foo), [NumLit(1.0)])"
#         self.assertTrue(TestChecker.test(input, expect, 448))

#     def test_6_6_TypeMismatchInStatement(self):
#         input = """
#             func foo(number a) return

#             func main()begin
#                 foo()
#             end
#         """
#         expect = "Type Mismatch In Statement: CallStmt(Id(foo), [])"
#         self.assertTrue(TestChecker.test(input, expect, 449))

#     def test_6_7_TypeMismatchInStatement(self):
#         input = """
#             func foo(number a) return

#             func main()begin
#                 foo("1")
#             end
#         """
#         expect = "Type Mismatch In Statement: CallStmt(Id(foo), [StringLit(1)])"
#         self.assertTrue(TestChecker.test(input, expect, 450))

#     def test_6_8_TypeMismatchInStatement(self):
#         input = """
#             func foo(number a) return

#             func main()begin
#                 dynamic a
#                 foo(a)
#                 number c <- a
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 451))

#     def test_6_9_TypeMismatchInStatement(self):
#         input = """
#             func main()begin
#                 dynamic a
#                 if (a) return
#                 a <- true
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 452))

#     def test_6_10_TypeMismatchInStatement(self):
#         input = """
#             func main()begin
#                 dynamic a <- 1
#                 if (a) return
#             end
#         """
#         expect = "Type Mismatch In Statement: If((Id(a), Return()), [], None)"
#         self.assertTrue(TestChecker.test(input, expect, 453))

#     def test_6_11_TypeMismatchInStatement(self):
#         input = """
#             func main()begin
#                 dynamic a
#                 if (a) number a
#                 elif (a)  return
#                 else number a
                
#                 if(true) number a
#                 elif (1) number a
#             end
#         """
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input, expect, 454))

#     def test_6_12_TypeMismatchInStatement(self):
#         input = """
#             func foo() begin
#                 dynamic a
#                 dynamic b
#                 dynamic c
#                 for a until b by c return
#                 a <- 1
#                 b <- true
#                 c <- 1
#             end
#             func main() return
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 455))

#     def test_6_13_TypeMismatchInStatement(self):
#         input = """
#             func foo() begin
#                 dynamic a <- true
#                 dynamic b
#                 dynamic c
#                 for a until b by c return
#             end
#             func main() return
#         """
#         expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
#         self.assertTrue(TestChecker.test(input, expect, 456))

#     def test_6_14_TypeMismatchInStatement(self):
#         input = """
#             func foo() begin
#                 dynamic a 
#                 dynamic b <- 2
#                 dynamic c
#                 for a until b by c return
#             end
#             func main() return
#         """
#         expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
#         self.assertTrue(TestChecker.test(input, expect, 457))

#     def test_6_15_TypeMismatchInStatement(self):
#         input = """
#             func foo() begin
#                 dynamic a 
#                 dynamic b
#                 dynamic c <- "1"
#                 for a until b by c return
#             end
#             func main() return
#         """
#         expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
#         self.assertTrue(TestChecker.test(input, expect, 458))

#     def test_6_16_TypeMismatchInStatement(self):
#         input = """
#             func foo() begin
#                 number a
#                 return 1
#                 return a
#                 return "!"
#             end
#             func main() return
#         """
#         expect = "Type Mismatch In Statement: Return(StringLit(!))"
#         self.assertTrue(TestChecker.test(input, expect, 459))

#     def test_6_17_TypeMismatchInStatement(self):
#         input = """
#             func foo() begin
#                 number a
#                 a <- 1
#                 a <- true
#             end
#             func main() return
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(a), BooleanLit(True))"
#         self.assertTrue(TestChecker.test(input, expect, 460))

#     def test_6_1_TypeMismatchInExpression(self):
#         input = """
#             func foo() return 1

#             func main() begin
#                 var a <- foo()
#                 var b <- foo(1)
#             end
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(foo), [NumLit(1.0)])"
#         self.assertTrue(TestChecker.test(input, expect, 461))

#     def test_6_2_TypeMismatchInExpression(self):
#         input = """
#             func foo(number a) return 1

#             func main() begin
#                 var a <- foo()
#             end
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(foo), [])"
#         self.assertTrue(TestChecker.test(input, expect, 462))

#     def test_6_3_TypeMismatchInExpression(self):
#         input = """
#             func foo(number a) return 1

#             func main() begin
#                 var a <- foo("1")
#             end
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(1)])"
#         self.assertTrue(TestChecker.test(input, expect, 463))

#     def test_6_4_TypeMismatchInExpression(self):
#         input = """
#             func foo(number a) return
            
#             func main() begin
#                 var a <- foo("1")
#             end
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(1)])"
#         self.assertTrue(TestChecker.test(input, expect, 464))

#     def test_6_5_TypeMismatchInExpression(self):
#         input = """
#             func foo(number a) return
            
#             func main() begin
#                 var a <- foo("1")
#             end
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(1)])"
#         self.assertTrue(TestChecker.test(input, expect, 465))

#     def test_6_6_TypeMismatchInExpression(self):
#         input = """
#             func main() begin
#                 dynamic left
#                 dynamic right
                
#                 var c <- left + right
#                 left <- 1
#                 right <- 1
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 466))

#     def test_6_7_TypeMismatchInExpression(self):
#         input = """
#             func main() begin
#                 dynamic left
#                 dynamic right
                
#                 var c <- left + 1
#                 left <- 1
#                 right <- 1
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 467))

#     def test_6_8_TypeMismatchInExpression(self):
#         input = """
#             func main() begin
#                 dynamic left
#                 dynamic right
                
#                 var c <- 1 + right
#                 left <- 1
#                 right <- 1
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 468))

#     def test_6_9_TypeMismatchInExpression(self):
#         input = """
#             func main() begin
#                 dynamic left
#                 dynamic right
                
#                 var c <- - left
#                 left <- 1
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 469))

#     def test_6_10_TypeMismatchInExpression(self):
#         input = """
#             func main() begin
#                 number a[1,2]
#                 number b
#                 var c <- b[1]
#             end
#         """
#         expect = "Type Mismatch In Expression: ArrayCell(Id(b), [NumLit(1.0)])"
#         self.assertTrue(TestChecker.test(input, expect, 470))

#     def test_6_11_TypeMismatchInExpression(self):
#         input = """
#             func main() begin
#                 number a[1,2]
#                 dynamic b
#                 var c <- b[1]
#             end
#         """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(c), None, var, ArrayCell(Id(b), [NumLit(1.0)]))"
#         self.assertTrue(TestChecker.test(input, expect, 471))

#     def test_6_12_TypeMismatchInExpression(self):
#         input = """
#             func main() begin
#                 number a[1,2]
#                 dynamic b
#                 var c <- a[b, 1]
#                 b <- 1
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 472))

#     def test_6_13_TypeMismatchInExpression(self):
#         input = """
#             func main() begin
#                 number a[1,2]
#                 dynamic b
#                 var c <- a["1"]
#             end
#         """
#         expect = "Type Mismatch In Expression: ArrayCell(Id(a), [StringLit(1)])"
#         self.assertTrue(TestChecker.test(input, expect, 473))

#     def test_6_14_TypeMismatchInExpression(self):
#         input = """
#             func main() begin
#                 number a[1,2]
#                 dynamic b
#                 var c <- a[1,2,3]
#             end
#         """
#         expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(1.0), NumLit(2.0), NumLit(3.0)])"
#         self.assertTrue(TestChecker.test(input, expect, 474))

#     def test_6_15_TypeMismatchInExpression(self):
#         input = """
#             func main() begin
#                 number a[1,2]
#                 dynamic b
#                 var c <- a[1,3]
#                 c <- 1
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 475))

#     def test_6_16_TypeMismatchInExpression(self):
#         input = """
#             func main() begin
#                 number a[1,2]
#                 dynamic b
#                 var c <- a[1]
#                 c <- [1,2]
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 476))

#     def test_6_17_TypeMismatchInExpression(self):
#         input = """
#             func a()
#             func main() begin
#                 number VoTien_ <- a()
#             end
#             func a() begin
                
#             end
#         """
#         # spec dpn't have and as forum said no testcase like this
#         # expect = "Type Mismatch In Statement: Return()"
#         # self.assertTrue(TestChecker.test(input, expect, 477))

#     def test_6_18_TypeMismatchInExpression(self):
#         input = """
#             func main() return
#             dynamic VoTien
#             var x <- VoTien or (VoTien > VoTien)
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(>, Id(VoTien), Id(VoTien))"
#         self.assertTrue(TestChecker.test(input, expect, 478))

#     def test_6_19_TypeMismatchInExpression(self):
#         input = """
#             dynamic VoTien
#             var x <- VoTien + VoTien * VoTien
#             number y <- VoTien
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 479))

#     def test_6_20_TypeMismatchInExpression(self):
#         input = """
#             dynamic VoTien
#             var x <- VoTien > VoTien ... VoTien < VoTien
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(..., BinaryOp(>, Id(VoTien), Id(VoTien)), BinaryOp(<, Id(VoTien), Id(VoTien)))"
#         self.assertTrue(TestChecker.test(input, expect, 480))

#     def test_7_1(self):
#         input = """
#             func areDivisors(number num1, number num2)
#             return ((num1 % num2 = 0) or (num2 % num1 = 0))
#             func main()
#             begin
#             var num1 <- readNumber()
#             var num2 <- readNumber()
#             if (areDivisors(num1, num2)) writeString("Yes")
#             else writeString("No")
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 499))

#     def test_7_2(self):
#         input = """
# func isPrime(number x)
# func main()
# begin
# number x <- readNumber()
# if (isPrime(x)) writeString("Yes")
# else writeString("No")
# end
# func isPrime(number x)
# begin
# if (x <= 1) return false
# var i <- 2
# for i until i > x / 2 by 1
# begin
# if (x % i = 0) return false
# end
# return true
# end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 499))

#     def test_7_3(self):
#         input = """
#             var VoTien <- VoTien
#             func main() return
#         """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(VoTien), None, var, Id(VoTien))"
#         self.assertTrue(TestChecker.test(input, expect, 499))

#     def test_7_4(self):
#         input = """
#             func main() return main()
#         """
#         expect = "Type Cannot Be Inferred: Return(CallExpr(Id(main), []))"
#         self.assertTrue(TestChecker.test(input, expect, 499))

#     def test_arraylit_1(self):
#         input = """
#             func main() return
#             dynamic x
#             number a <- [x]
#         """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(a), NumberType, None, ArrayLit(Id(x)))"
#         self.assertTrue(TestChecker.test(input, expect, 501))

#     def test_arraylit_2(self):
#         input = """
#             dynamic x
#             number a[3] <- [x]
#             func f()
#             begin
#                 x <- [1,2,3]
#             end
#         """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(a), ArrayType([3.0], NumberType), None, ArrayLit(Id(x)))"
#         self.assertTrue(TestChecker.test(input, expect, 502))

#     def test_arraylit_3(self):
#         input = """
#             dynamic x
#             number a[3] <- [x, 1, 2]
#             func  main()
#             begin
#                 x <- 1
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 503))

#     def test_arraylit_4(self):
#         input = """
#             dynamic x
#             number a[3] <- [x, x, x]
#             func  main()
#             begin
#                 x <- 1
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 504))

#     def test_arraylit_5(self):
#         input = """
#             dynamic x
#             number a[3] <- [x, x, "1"]
#             func  main()
#             begin
#                 x <- 1
#             end
#         """
#         expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([3.0], NumberType), None, ArrayLit(Id(x), Id(x), StringLit(1)))"
#         self.assertTrue(TestChecker.test(input, expect, 505))

#     def test_arraylit_6(self):
#         input = """
#             dynamic x
#             number a[3] <- [x, 1, "1"]
#             func  main()
#             begin
#                 x <- 1
#             end
#         """
#         expect = "Type Mismatch In Expression: ArrayLit(Id(x), NumLit(1.0), StringLit(1))"
#         self.assertTrue(TestChecker.test(input, expect, 506))

#     def test_arraylit_7(self):
#         input = """
#             dynamic x
#             number a[3] <- [x, [x,x], 1]
#             func  main()
#             begin
#                 x <- 1
#             end
#         """
#         expect = "Type Mismatch In Expression: ArrayLit(Id(x), ArrayLit(Id(x), Id(x)), NumLit(1.0))"
#         self.assertTrue(TestChecker.test(input, expect, 507))

#     def test_arraylit_8(self):
#         input = """
#             dynamic x
#             number a[3] <- [1, [x,x]]
#             func  main()
#             begin
#                 x <- 1
#             end
#         """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(a), ArrayType([3.0], NumberType), None, ArrayLit(NumLit(1.0), ArrayLit(Id(x), Id(x))))"
#         self.assertTrue(TestChecker.test(input, expect, 508))

#     # def test_arraylit_9(self):
#     #     input = """
#     #         dynamic x
#     #         number a[3] <- [[1,2,3], [x,x]]
#     #         func  main()
#     #         begin
#     #             x <- 1
#     #         end
#     #     """
#     #     expect = "Type Cannot Be Inferred: VarDecl(Id(a), ArrayType([3.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(Id(x), Id(x))))"
#     #     self.assertTrue(TestChecker.test(input, expect, 509))

#     def test_arraylit_10(self):
#         input = """
#             dynamic x
#             number a[3,3] <- [[1,2,3], x, x]
#             func  main()
#             begin
#                 x <- [1,2,3]
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 510))

#     def test_arraylit_11(self):
#         input = """
#             dynamic x
#             number a[2,3] <- [[1,2,3], [x,x,x]]
#             func  main()
#             begin
#                 x <- 1
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 511))

#     def test_arraylit_12(self):
#         input = """
#             dynamic x
#             number a[2,3] <- [[1,2,3], 1]
#             func  main()
#             begin
#                 x <- 1
#             end
#         """
#         expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), NumLit(1.0))"
#         self.assertTrue(TestChecker.test(input, expect, 512))

#     # def test_arraylit_13(self):
#     #     input = """
#     #         dynamic x
#     #         number a[2,3] <- [[1,2,3], [x,x]]
#     #         func  main()
#     #         begin
#     #             x <- 1
#     #         end
#     #     """
#     #     expect = "Type Cannot Be Inferred: VarDecl(Id(a), ArrayType([2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(Id(x), Id(x))))"
#     #     self.assertTrue(TestChecker.test(input, expect, 513))

#     def test_arraylit_14(self):
#         input = """
#             dynamic x
#             number a[1,1,1,1] <- [[[x]]]
#             func  main()
#             begin
#                 x <- [1]
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 514))

#     def test_arraylit_15(self):
#         input = """
#             dynamic x
#             number a[1,1,2,2] <- [[[[1,2], x]]]
#             func  main()
#             begin
#                 x <- [1,2]
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 515))

#     def test_arraylit_16(self):
#         input = """
#             dynamic x
#             number a[1,1,2,2] <- [[[x, x]]]
#             func  main()
#             begin
#                 x <- [1,2]
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 516))

#     def test_arraylit_17(self):
#         input = """
#             dynamic x
#             var a <- [x]
#         """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, ArrayLit(Id(x)))"
#         self.assertTrue(TestChecker.test(input, expect, 1024))

#     def test_arraylit_18(self):
#         input = """
#             func foo() begin
#                 dynamic x
#                 return [x]                
#             end
#             func main() return 
#         """
#         expect = "Type Cannot Be Inferred: Return(ArrayLit(Id(x)))"
#         self.assertTrue(TestChecker.test(input, expect, 1025))

#     def test_arraylit_19(self):
#         input = """
#             func foo() begin
#                 dynamic x
#                 return [x, [1,2]]                
#             end
#             func main() return 
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 1026))

#     def test_arraylit_20(self):
#         input = """
#             func foo() begin
#                 dynamic x
#                 dynamic y
#                 return [[y], [y]]
#                 return x
#                 return [[1], [2]]
#             end
#             func main() return 
#         """
#         expect = "Type Cannot Be Inferred: Return(ArrayLit(ArrayLit(Id(y)), ArrayLit(Id(y))))"
#         self.assertTrue(TestChecker.test(input, expect, 517))

#     def test_arraylit_21(self):
#         input = """
#             func foo() begin
#                 dynamic x
#                 dynamic y
#                 return [[1], [2]]
#                 return [x, y]
#                 x <- [1]
#                 y <- x
#             end
#             func main() return 
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 518))

#     def test_arraylit_22(self):
#         input = """
#             func foo() begin
#                 dynamic x
#                 dynamic y
#                 return [[1], [2]]
#                 return [x, [y]]
#                 x <- [1]
#                 y <- x
#             end
#             func main() return 
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(y), Id(x))"
#         self.assertTrue(TestChecker.test(input, expect, 519))

#     def test_arraylit_23(self):
#         input = """
#             func foo(number a[2,2]) return
#             func main() begin
#                 dynamic x
#                 foo(x)
#                 x <- [[2,2], [2,3]]
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 920))

#     def test_arraylit_24(self):
#         input = """
#             func foo(number a[2,2]) return
#             func main() begin
#                 dynamic x
#                 foo([x])
#                 x <- [1]
#             end
#         """
#         expect = "Type Cannot Be Inferred: CallStmt(Id(foo), [ArrayLit(Id(x))])"
#         self.assertTrue(TestChecker.test(input, expect, 921))

#     def test_arraylit_25(self):
#         input = """
#             func foo(number a[2,2]) return
#             func main() begin
#                 dynamic x
#                 foo([x, x])
#                 x <- [1,2]
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 922))

#     def test_arraylit_26(self):
#         input = """
#             func foo(number a[2,2]) return 1
#             func main() begin
#                 dynamic x
#                 var a <- foo([x, x])
#                 x <- [1,2]
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 923))

#     def test_arraylit_27(self):
#         input = """
#             func foo(number a[2,2]) return 1
#             func main() begin
#                 dynamic x
#                 var a <- foo(x)
#                 x <- [1,2]
#             end
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(x), ArrayLit(NumLit(1.0), NumLit(2.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 924))

#     def test_return(self):
#         input = """
#             func main() begin 
#                 return
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 606))

#         input = """
#             func main() begin 
#                 return 1
#             end
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 607))

#         input = """
#             func main() begin 
#                 return 1
#                 begin
#                     return "string"
#                 end
#             end
#         """
#         expect = "Type Mismatch In Statement: Return(StringLit(string))"
#         self.assertTrue(TestChecker.test(input, expect, 608))

#         input = """
#             func main() begin 
#                 dynamic i
#                 return 1
#                 return i
#             end
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 609))

#         input = """
#             func fun() begin
#                 return 
#                 return
#                 return 1
#             end
#             func main() begin 
               
#             end
#         """
#         expect = "Type Mismatch In Statement: Return(NumLit(1.0))"
#         self.assertTrue(TestChecker.test(input, expect, 610))

#         input = """
#             func fun() begin
#                 return 1
#                 return "string"
#             end
#             func main() begin 
               
#             end
#         """
#         expect = "Type Mismatch In Statement: Return(StringLit(string))"
#         self.assertTrue(TestChecker.test(input, expect, 611))

#         input = """
#             func fun() begin
#                 number a[3]
#                 return [1, 4, 3]
#                 return a
#             end
#             func main() begin 
               
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 999))

#         input = """
#             func fun() begin
#                 number a[2,2]
#                 return [[1,2], [3,4]]
#                 return a
#             end
#             func main() begin 
               
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 998))

#         input = """
#             func fun() begin
#                 number a[3,2]
#                 return [[1,2], [3,4]]
#                 return a
#             end
#             func main() begin 
               
#             end
#         """
#         expect = "Type Mismatch In Statement: Return(Id(a))"
#         self.assertTrue(TestChecker.test(input, expect, 997))

#         input = """
#             func fun() begin
#                 number a[2,2]
#                 return a
#                 return [["1","2"], ["3","4"]]
#             end
#             func main() begin 
               
#             end
#         """
#         expect = "Type Mismatch In Statement: Return(ArrayLit(ArrayLit(StringLit(1), StringLit(2)), ArrayLit(StringLit(3), StringLit(4))))"
#         self.assertTrue(TestChecker.test(input, expect, 996))

#         input = """
#             func fun() begin
#                 string a[2,2, 3]
#                 return a
#                 return [["1","2"], ["3","4"]]
#             end
#             func main() begin 
               
#             end
#         """
#         expect = "Type Mismatch In Statement: Return(ArrayLit(ArrayLit(StringLit(1), StringLit(2)), ArrayLit(StringLit(3), StringLit(4))))"
#         self.assertTrue(TestChecker.test(input, expect, 995))

#         input = """
#             func fun() begin
#                 string a[2]
#                 return a
#                 return [["1","2"], ["3","4"]]
#             end
#             func main() begin 
               
#             end
#         """
#         expect = "Type Mismatch In Statement: Return(ArrayLit(ArrayLit(StringLit(1), StringLit(2)), ArrayLit(StringLit(3), StringLit(4))))"
#         self.assertTrue(TestChecker.test(input, expect, 994))

#         input = """
#             func fun() begin
#                 string a[1,1,1,1,1]
#                 return a
#                 return [[[[["1"]]]]]
#             end
#             func main() begin 
               
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 993))

#         input = """
#             func fun() begin
#                 return [1,2]
#                 return [3,4]
#             end
            
#             func fun1() begin
#                 return [[1,2], [3,4]]
#                 return [[1,5], [3,4]]
#             end
            
#             func main() begin 
               
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 992))

#         input = """
#             func fun1() return 1
#             func fun2() return
#             func fun3()
            
#             func main() begin 
#                return fun3()
#             end
#         """
#         expect = "Type Cannot Be Inferred: Return(CallExpr(Id(fun3), []))"
#         self.assertTrue(TestChecker.test(input, expect, 612))

#         input = """
#             func fun1() return 1
#             func fun2() return
#             func fun3()
            
#             func main() begin 
#                return fun1()
#             end
#             func fun3() return 1   
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 613))

#         input = """
#             func fun1() return 1
#             func fun2() return "k"
#             func fun3() 
            
#             func main() begin 
#                number a <- fun3()
#             end
#             func fun3() return "1" 
#         """
#         expect = "Type Mismatch In Statement: Return(StringLit(1))"
#         self.assertTrue(TestChecker.test(input, expect, 614))

#         input = """
#             func fun1() return [1,2]
#             func fun2() return [3,4]
#             func fun3()
            
#             func main() begin 
#                return fun1()
#                return fun2()
#                return fun3()
#             end 
#         """
#         expect = "No Function Definition: fun3"
#         self.assertTrue(TestChecker.test(input, expect, 406))

#     def test_Assign(self):
#         input = """
#             func main() begin 
#                 number a
#                 dynamic b
#                 dynamic c
#                 b <- c
#             end
#         """
#         expect = "Type Cannot Be Inferred: AssignStmt(Id(b), Id(c))"
#         self.assertTrue(TestChecker.test(input, expect, 707))

#         input = """
#             func main() begin 
#                 number a
#                 dynamic b
#                 dynamic c
#                 a <- c
#                 b <- c
#                 return a
#                 return b
#                 return c
#             end
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 708))

#         input = """
#             func main() begin 
#                 number a
#                 string b
#                 dynamic c
#                 a <- c
#                 c <- b

#             end
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(c), Id(b))"
#         self.assertTrue(TestChecker.test(input, expect, 709))

#         input = """
#             func main() begin 
#                 number a
#                 string b
#                 dynamic c
#                 c <- a
#                 b <- c

#             end
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(b), Id(c))"
#         self.assertTrue(TestChecker.test(input, expect, 407))

#         input = """
#             func main() begin 
#                 number a[1,3]
#                 dynamic c
#                 c <- [[1,2,3]]
#                 c <- a
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 407))

#         input = """
#             func foo()
#             func main() begin 
#                 number a[1,3]
#                 dynamic c
#                 c <- foo()
#             end
#         """
#         expect = "Type Cannot Be Inferred: AssignStmt(Id(c), CallExpr(Id(foo), []))"
#         self.assertTrue(TestChecker.test(input, expect, 407))

#         input = """
#             func foo()
#             func main() begin 
#                 number a[1,3]
#                 dynamic c
#                 a <- foo()
#             end
#             func foo()
#                 return [[1,2,3]]
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 407))

#         input = """
#             func foo()
#             func main() begin 
#                 number a[1,3]
#                 dynamic c
#                 a <- foo()
#             end
#             func foo()
#                 return [1,2,3]
#         """
#         expect = "Type Mismatch In Statement: Return(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 407))

#     def test_random(self):
#         input = """
#             func foo()
#             func main() begin 
#                 number a <- a
#             end
#             func foo()
#                 return 2
#             """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 1903))
#         input = """
#             func foo(number a) 
#             begin
#                 number a
#             end
#             func main() begin 
               
#             end
#             """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 1905))

#     def testx(self):
#         input = """
#         func main() begin
#             dynamic x
#             number a[2,2] <- [[x,x], [4,4]]
#         end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 1906))

#     def testy(self):
#         input = """
#             func foo()
#             func main() begin
#                 dynamic x
#                 number a[2,2] <- [[foo(),x], [4,4]]
#             end
            
#             func foo() return "abc"
#         """
#         expect = "Type Mismatch In Statement: Return(StringLit(abc))"
#         self.assertTrue(TestChecker.test(input, expect, 1907))

#     def testz(self):
#         input = """
#         dynamic x
#         func main() begin
#             x <- (x = 1) or ("abc" == "abc")
#         end
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(x), BinaryOp(or, BinaryOp(=, Id(x), NumLit(1.0)), BinaryOp(==, StringLit(abc), StringLit(abc))))"
#         self.assertTrue(TestChecker.test(input, expect, 1908))

#     def testt(self):
#         input = """
#             dynamic a
#             func foo() return a
#             func main()
#             begin
#                 number num <- foo()
#             end
#         """
#         expect = "Type Cannot Be Inferred: Return(Id(a))"
#         self.assertTrue(TestChecker.test(input, expect, 1909))
# # Quan (Moi update)

#     def test1(self):
#         input = """func test()
#     func test() begin
#     end
#     func main() begin
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 400))

#     def test2(self):
#         input = """func test() begin
#     end
#     func test()
#     func main() begin
#     end
#         """
#         expect = "Redeclared Function: test"
#         self.assertTrue(TestChecker.test(input, expect, 401))

#     def test3(self):
#         input = """func test()
#     func main() begin
#     end
#     func test() begin
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 402))

#     def test4(self):
#         input = """func test()
#     func main() begin
#     end
#     func test()
#         """
#         expect = "Redeclared Function: test"
#         self.assertTrue(TestChecker.test(input, expect, 403))

#     def test5(self):
#         input = """func test()
#     func test() begin
#     end
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 404))

#     def test6(self):
#         input = """func test()
#     func test() begin
#     end
#     func main(number a) begin
#     end
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 405))

#     def test7(self):
#         input = """func test(number a, string b)
#     func test(number a, string b) begin
#     end
#     func main() begin
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 406))

#     def test8(self):
#         input = """func test(number a, string b)
#     func test(number c, string d) begin
#     end
#     func main() begin
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 407))


#     def test10(self):
#         input = """
#     func main() begin
#         number a <- 1
#         a <- "bruh"
#     end
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(a), StringLit(bruh))"
#         self.assertTrue(TestChecker.test(input, expect, 409))

#     def test11(self):
#         input = """
#     func main() begin
#         number a <- 1
#         number a <- 1
#     end
#         """
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input, expect, 410))

#     def test12(self):
#         input = """
#     func main() begin
#         var a <- 1
#         a <- 10.99
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 411))

#     def test13(self):
#         input = """
#     func main() begin
#         var a <- 1
#         a <- true
#     end
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(a), BooleanLit(True))"
#         self.assertTrue(TestChecker.test(input, expect, 412))

#     def test14(self):
#         input = """
#     func main() begin
#         dynamic a
#         a <- 1000
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 413))

#     def test15(self):
#         input = """
#     func main() begin
#         dynamic a
#         a <- 1000
#         a <- "hello"
#     end
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(a), StringLit(hello))"
#         self.assertTrue(TestChecker.test(input, expect, 414))

#     def test16(self):
#         input = """
#     dynamic a
#     func main() begin
#         a <- 1000
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 415))

#     def test17(self):
#         input = """
#     func main() begin
#         dynamic a
#         var b <- a
#     end
#         """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(b), None, var, Id(a))"
#         self.assertTrue(TestChecker.test(input, expect, 416))

#     def test18(self):
#         input = """
#     func main() begin
#         dynamic a
#         dynamic b
#         b <- a
#     end
#         """
#         expect = "Type Cannot Be Inferred: AssignStmt(Id(b), Id(a))"
#         self.assertTrue(TestChecker.test(input, expect, 417))

#     def test19(self):
#         input = """
#     func main() begin
#         dynamic a
#         dynamic b <- a
#     end
#         """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(b), None, dynamic, Id(a))"
#         self.assertTrue(TestChecker.test(input, expect, 418))

#     def test20(self):
#         input = """
#     func main() begin
#         number a <- a
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 419))

#     def test21(self):
#         input = """
#     number a
#     string b
#     bool c
#     func main() begin
#         a <- 123
#         b <- "hello"
#         c <- true
#         string a <- "another a"
#         dynamic b <- a
#         var c <- a
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 420))

#     def test22(self):
#         input = """
#     number a
#     string b
#     bool c
#     func main() begin
#         a <- 123
#         b <- "hello"
#         c <- true
#         string a <- "another a"
#         dynamic b <- a
#         var c <- a
#         a <- 456
#     end
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(a), NumLit(456.0))"
#         self.assertTrue(TestChecker.test(input, expect, 421))

#     def test23(self):
#         input = """
#     number a
#     string b
#     bool c
#     func main() begin
#         a <- 123
#         b <- "hello"
#         c <- true
#         string a <- "another a"
#         var c <- a
#         b <- c
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 422))

#     def test24(self):
#         input = """
#     func test() begin
#     end
#     func main() begin
#         test()
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 423))

#     def test25(self):
#         input = """
#     func test(number a, bool b) begin
#     end
#     func main() begin
#         test(1, true)
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 424))

#     def test26(self):
#         input = """
#     func test(number a, bool b) begin
#     end
#     func main() begin
#         test("wrong", true)
#     end
#         """
#         expect = "Type Mismatch In Statement: CallStmt(Id(test), [StringLit(wrong), BooleanLit(True)])"
#         self.assertTrue(TestChecker.test(input, expect, 425))

#     def test27(self):
#         input = """
#     func test(number a, bool b) return true
#     func main() begin
#         bool b <- test(1, true)
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 426))

#     def test28(self):
#         input = """
#     func test(number a, bool b) return true
#     func main() begin
#         number b <- test(1, true)
#     end
#         """
#         expect = "Type Mismatch In Statement: VarDecl(Id(b), NumberType, None, CallExpr(Id(test), [NumLit(1.0), BooleanLit(True)]))"
#         self.assertTrue(TestChecker.test(input, expect, 427))

#     def test29(self):
#         input = """
#     func test(number a, bool b) return true
#     func main() begin
#         test(1, true)
#     end
#         """
#         expect = "Type Mismatch In Statement: CallStmt(Id(test), [NumLit(1.0), BooleanLit(True)])"
#         self.assertTrue(TestChecker.test(input, expect, 428))

#     def test30(self):
#         input = """
#     func test(number a, bool b) return true
#     func main() begin
#         dynamic a
#         bool b <- test(1, a)
#         a <- true
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 429))

#     def test31(self):
#         input = """
#     func test(number a, bool b) return true
#     func main() begin
#         dynamic a
#         bool b <- test(1, a)
#         a <- 123
#     end
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(a), NumLit(123.0))"
#         self.assertTrue(TestChecker.test(input, expect, 430))

#     def test32(self):
#         input = """
#     func test(number a, bool b) return true
#     func main() begin
#         bool b <- test(1, test(2, false))
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 431))

#     def test33(self):
#         input = """
#     func test(number a, bool b)
#     func main() begin
#         bool b <- test(1, test(2, false))
#     end
#         """
#         expect = "No Function Definition: test"
#         self.assertTrue(TestChecker.test(input, expect, 432))

#     def test34(self):
#         input = """
#     func test(number a, bool b)
#     func main() begin
#         string b <- test(1, test(2, false))
#     end
#         """
#         expect = "Type Mismatch In Statement: VarDecl(Id(b), StringType, None, CallExpr(Id(test), [NumLit(1.0), CallExpr(Id(test), [NumLit(2.0), BooleanLit(False)])]))"
#         self.assertTrue(TestChecker.test(input, expect, 433))

#     def test35(self):
#         input = """
#     func test(number a, bool b)
#     func main() begin
#         bool b <- test(1, test(2, false))
#     end
#     func test(number c, bool d) return 1.23
#         """
#         expect = "Type Mismatch In Statement: Return(NumLit(1.23))"
#         self.assertTrue(TestChecker.test(input, expect, 434))

#     def test36(self):
#         input = """
#     func test(number a, bool b)
#     func main() begin
#         bool b <- test(1, test(2, false))
#     end
#     func test(number c, bool d) return true
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 435))

#     def test37(self):
#         input = """
#     func test(number a, bool b)
#     func main() begin
#         test(1, true)
#     end
#     func test(number a, bool b) begin
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 436))

#     def test38(self):
#         input = """
#     func test(number a, bool b)
#     func main() begin
#         test(1, true)
#     end
#     func test(number a, bool b) return 1
#         """
#         expect = "Type Mismatch In Statement: Return(NumLit(1.0))"
#         self.assertTrue(TestChecker.test(input, expect, 437))

#     def test39(self):
#         input = """
#     func main() begin
#         var a <- a
#     end
#         """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, Id(a))"
#         self.assertTrue(TestChecker.test(input, expect, 438))

#     def test40(self):
#         input = """
#     number a <- 1
#     func main() begin
#         var a <- a
#     end
#         """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, Id(a))"
#         self.assertTrue(TestChecker.test(input, expect, 439))

#     def test41(self):
#         input = """
#     number a <- 1
#     func main() begin
#         number a <- a
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 440))

#     def test42(self):
#         input = """
#     func main() begin
#         writeNumber(1)
#         writeString("hello")
#         writeBool(true)
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 441))

#     def test43(self):
#         input = """
#     func main() begin
#         writeNumber()
#     end
#         """
#         expect = "Type Mismatch In Statement: CallStmt(Id(writeNumber), [])"
#         self.assertTrue(TestChecker.test(input, expect, 442))

#     def test44(self):
#         input = """
#     func writeNumber(number a)
#     func main() begin
#         writeNumber(1)
#     end
#         """
#         expect = "Redeclared Function: writeNumber"
#         self.assertTrue(TestChecker.test(input, expect, 443))

#     def test45(self):
#         input = """
#     func main() begin
#         string s <- readString()
#         number n <- readNumber()
#         bool b <- readBool()
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 444))

#     def test46(self):
#         input = """
#     func main() begin
#         string s <- readString()
#         number n <- readNumber()
#         readBool()
#     end
#         """
#         expect = "Type Mismatch In Statement: CallStmt(Id(readBool), [])"
#         self.assertTrue(TestChecker.test(input, expect, 445))

#     def test47(self):
#         input = """
#     func readString() return "hello"
#     func main() begin
#         string s <- readString()
#         number n <- readNumber()
#         bool b <- readBool()
#     end
#         """
#         expect = "Redeclared Function: readString"
#         self.assertTrue(TestChecker.test(input, expect, 446))

#     def test48(self):
#         input = """
#     func main() begin
#         number a <- writeNumber(1)
#     end
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(writeNumber), [NumLit(1.0)])"
#         self.assertTrue(TestChecker.test(input, expect, 447))

#     def test49(self):
#         input = """
#     func main() begin
#         string s <- readString(1)
#         number n <- readNumber()
#         bool b <- readBool()
#     end
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(readString), [NumLit(1.0)])"
#         self.assertTrue(TestChecker.test(input, expect, 448))

#     def test50(self):
#         input = """
#     number a
#     func main() begin
#         string a <- readString()
#     end
#     func test() begin
#         a <- 1
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 449))

#     def test51(self):
#         input = """
#     number a
#     func main() begin
#         string a <- readString()
#     end
#     func test() begin
#         a <- "Hello, World!"
#     end
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(a), StringLit(Hello, World!))"
#         self.assertTrue(TestChecker.test(input, expect, 450))

#     def test52(self):
#         input = """
#     func test() begin
#         return 1
#         return "true"
#     end
#     func main() begin
#         number a <- test()
#     end
#         """
#         expect = "Type Mismatch In Statement: Return(StringLit(true))"
#         self.assertTrue(TestChecker.test(input, expect, 451))

#     def test53(self):
#         input = """
#     func test() begin
#         return 1
#         return 3.14
#     end
#     func main() begin
#         number a <- test()
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 452))

#     def test54(self):
#         input = """
#     number a
#     func test() return false
#     func test2(number c)
#     func main() begin
#         a <- test2(2)
#     end
#     func test2(number c) begin
#         bool b <- test()
#         return c
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 453))

#     def test55(self):
#         input = """
#     number a
#     func test() return false
#     func test2(number c)
#     func main() begin
#         a <- test2(2)
#     end
#     func test2(number c) begin
#         bool b <- test()
#         return b
#     end
#         """
#         expect = "Type Mismatch In Statement: Return(Id(b))"
#         self.assertTrue(TestChecker.test(input, expect, 454))

#     def test56(self):
#         input = """
#     number a
#     func test() return false
#     func test2(number c)
#     func main() begin
#         a <- test2(2)
#         c <- a
#     end
#     func test2(number c) begin
#         bool b <- test()
#         return c
#     end
#         """
#         expect = "Undeclared Identifier: c"
#         self.assertTrue(TestChecker.test(input, expect, 455))

#     def test57(self):
#         input = """
#     number a
#     func test() return false
#     func test2(number c)
#     func main() begin
#         a <- test2(2)
#         a()
#     end
#     func test2(number c) begin
#         bool b <- test()
#         return c
#     end
#         """
#         expect = "Undeclared Function: a"
#         self.assertTrue(TestChecker.test(input, expect, 456))

#     def test58(self):
#         input = """
#     number a
#     func test(number b) return false
#     func test2(number c)
#     func main() begin
#         a <- test2(2)
#         a <- b
#     end
#     func test2(number c) begin
#         bool b <- test()
#         return c
#     end
#         """
#         expect = "Undeclared Identifier: b"
#         self.assertTrue(TestChecker.test(input, expect, 457))

#     def test59(self):
#         input = """
#     dynamic a
#     func getA(number x)
#     func test2(number c)
#     func main() begin
#         dynamic x
#         test2(getA(x))
#     end
#     func getA(number x) return a
#     func test2(number c) begin
#         writeNumber(c)
#         return
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 458))

#     def test60(self):
#         input = """
#     dynamic a
#     func getA(number x)
#     func test2(number c)
#     func test3()
#     func main() begin
#         dynamic x
#         test2(getA(x))
#     end
#     func getA(number x) return test3()
#     func test2(number c) begin
#         writeNumber(c)
#         return
#     end
#     func test3() return 3.14
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 459))

#     def test61(self):
#         input = """
#     dynamic a
#     func getA(number x)
#     func test2(number c)
#     func test3()
#     func main() begin
#         dynamic x
#         test2(getA(x))
#     end
#     func getA(number x) return test3()
#     func test2(number c) begin
#         writeNumber(c)
#         return
#     end
#     func test3() return false
#         """
#         expect = "Type Mismatch In Statement: Return(BooleanLit(False))"
#         self.assertTrue(TestChecker.test(input, expect, 460))

#     def test62(self):
#         input = """
#     func main() begin
#         number a
#         bool b <- true
#         if (b)
#             a <- 1
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 461))

#     def test63(self):
#         input = """
#     func main() begin
#         number a
#         bool b <- true
#         if (a)
#             a <- 1
#         else
#             a <- 2
#     end
#         """
#         expect = "Type Mismatch In Statement: If((Id(a), AssignStmt(Id(a), NumLit(1.0))), [], AssignStmt(Id(a), NumLit(2.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 462))

#     def test64(self):
#         input = """
#     func main() begin
#         number a
#         bool b <- true
#         bool c <- false
#         if (b) begin
#             string a <- "hello"
#         end
#         elif (b) begin
#             a <- 1
#         end
#         else
#             a <- 2
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 463))

#     def test65(self):
#         input = """
#     func main() begin
#         number a
#         bool b <- true
#         if (b) begin
#             string a <- "hello"
#         end
#         else begin
#             a <- "error"
#         end
#     end
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(a), StringLit(error))"
#         self.assertTrue(TestChecker.test(input, expect, 464))

#     def test66(self):
#         input = """
#     func main() begin
#         number a
#         bool b <- true
#         dynamic c
#         dynamic d
#         if (c) begin
#             string a <- "hello"
#             c <- false
#         end
#         elif (d) d <- false
#         c <- d
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 465))

#     def test67(self):
#         input = """
#     func main() begin
#         bool a <- true
#         bool b <- false
#         if (a and b) begin
#             a <- false
#         end
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 466))

#     def test68(self):
#         input = """
#     func main() begin
#         bool a <- true
#         bool b <- false
#         number c
#         if (a or b) begin
#             c <- 1 + 2 / 3
#         end
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 467))

#     def test69(self):
#         input = """
#     func main() begin
#         bool a <- true
#         bool b <- false
#         number c
#         dynamic d
#         if (c = d) begin
#             d <- 1
#         end
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 468))

#     def test70(self):
#         input = """
#     func main() begin
#         dynamic a
#         dynamic b
#         dynamic c
#         dynamic d
#         dynamic e
#         dynamic f
#         if ((a = b) and (a < b) or (a > b) or (a <=b) or (a >= b) or (a != b)) begin
#             b <- a
#             a <- b
#         end
#         elif ((c and d) or (c or d)) c <- d
#         elif ((e..."zcode") == f) f <- "sucks"
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 469))

#     def test71(self):
#         input = """
#     number a <- 10
#     bool b <- true
#     func test(number e) begin
#         return e + 1
#     end
#     func main() begin
#         number c <- test(a)
#         if ((c > a) and b) return
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 470))

#     def test72(self):
#         input = """
#     number a <- 10
#     dynamic b
#     func main() begin
#         number i
#         for i until b by 1 begin
#             writeNumber(i)
#             if (i > 5) break
#         end
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 471))

#     def test73(self):
#         input = """
#     bool a <- true
#     var b <- a or b
#     func main() begin
#         number i
#         for i until b by 1 begin
#             writeNumber(i)
#             if (i > 5) continue
#         end
#         break
#     end
#         """
#         expect = "Break Not In Loop"
#         self.assertTrue(TestChecker.test(input, expect, 472))

#     def test74(self):
#         input = """
#     bool a <- true
#     var b <- a or b
#     func main() begin
#         number i
#         for i until b by 1 begin
#             var j <- i
#             for j until a by j + 1
#             begin
#                 if (j > 5) continue
#             end
#             if (i > 5) break
#         end
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 473))

#     def test75(self):
#         input = """
#     number a[1, 2]
#     func main() begin
#         a[1, 1] <- 1
#         a[2, 1] <- 2
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 474))

#     def test76(self):
#         input = """
#     number a[1, 2]
#     func main() begin
#         number a
#         a[1] <- 1
#     end
#         """
#         expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(1.0)])"
#         self.assertTrue(TestChecker.test(input, expect, 475))

#     def test77(self):
#         input = """
#     number a[1, 2]
#     func main() begin
#         a[1 + 1, 0] <- 1
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 476))

#     def test78(self):
#         input = """
#     number a[1, 2]
#     func main() begin
#         dynamic b
#         a[1 + 1, b] <- 1
#         b <- false
#     end
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(b), BooleanLit(False))"
#         self.assertTrue(TestChecker.test(input, expect, 477))

#     def test79(self):
#         input = """
#     func main() begin
#         bool a[2, 3] <- [[true, true, true], [false, false, false]]
#         a[1] <- [true, true, false]
#         a[1] <- true
#     end
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a), [NumLit(1.0)]), BooleanLit(True))"
#         self.assertTrue(TestChecker.test(input, expect, 478))

#     def test80(self):
#         input = """
#     func main() begin
#         number a[5] <- [1,2,3,4,5,6]
#     end
#         """
#         expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([5.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0), NumLit(6.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 479))

#     def test81(self):
#         input = """
#     func main() begin
#         number a[5] <- [1,true,3,4,5]
#     end
#         """
#         expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), BooleanLit(True), NumLit(3.0), NumLit(4.0), NumLit(5.0))"
#         self.assertTrue(TestChecker.test(input, expect, 480))

#     def test82(self):
#         input = """
#     func main() begin
#         dynamic a
#         number b[5] <- [1, 2, 3, a, 5]
#         a <- false
        
#     end
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(a), BooleanLit(False))"
#         self.assertTrue(TestChecker.test(input, expect, 481))

#     def test83(self):
#         input = """
#     func main() begin
#         dynamic a
#         number b[2, 5] <- [[1, 2, 3, 4, 5], a]
#         a <- [1, 2, 3, 4, 5]
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 482))

#     def test84(self):
#         input = """
#     func main() begin
#         dynamic a
#         number b[2, 5] <- [[1, 2, 3, 4, 5], a]
#         a <- [1, 2, 3, 4]
#     end
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(a), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 483))

#     def test85(self):
#         input = """
#     func main() begin
#         dynamic a
#         number b[2, 4] <- [[1, 2, 3, 4]]
#     end
#         """
#         expect = "Type Mismatch In Statement: VarDecl(Id(b), ArrayType([2.0, 4.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0))))"
#         self.assertTrue(TestChecker.test(input, expect, 484))

#     def test86(self):
#         input = """
#     func main() begin
#         dynamic a
#         number b[2, 4] <- [[1, 2, 3, 4, 5], [1, 2, 3, 4]]
#     end
#         """
#         expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 485))

#     def test87(self):
#         input = """
#     func main() begin
#         number a
#         if (true) number a
#     end
#         """
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input, expect, 486))

#     def test88(self):
#         input = """
#     func main() begin
#         dynamic a
#         number b[2, 5] <- [[1, 2, 3, 4, 5], a]
#         a <- [1, 2, 3, 4, 5]
#         b[1] <- [1, 2, 3, 4, 5, 6]
#     end
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(b), [NumLit(1.0)]), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0), NumLit(6.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 487))

#     def test89(self):
#         input = """
#     func main() begin
#         dynamic a
#         number b[3, 3, 3] <- [[[1,2,3],[4,5,6],[7,8,9]] , [[1,2,3],[4,5,6],[7,8,9]] , [[1,2,3],[4,5,6],[7,8,9]]]
        
#         var c <- b[1]
#         c <- [[1,2,3],[4,5,6],[7,8,9]]
        
#         var d <- b[1, 2]
#         d <- [41, 51, 61]
        
#         number e <- b[1,2,3]
#         e <- 3.14
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 488))

#     def test90(self):
#         input = """
#     func main() begin
#         dynamic a
#         number b[3, 3, 3] <- [[[1,2,3],[4,5,6],[7,8,9]] , [[1,2,3],[4,5,6],[7,8,9]] , [[1,2,3],[4,5,6],[7,8,9]]]
        
#         var c <- b[1]
#         c <- [[1,2,3],[4,5,6],[7,8,9]]
        
#         number d <- b[1, 2]
#     end
#         """
#         expect = "Type Mismatch In Statement: VarDecl(Id(d), NumberType, None, ArrayCell(Id(b), [NumLit(1.0), NumLit(2.0)]))"
#         self.assertTrue(TestChecker.test(input, expect, 489))

#     def test91(self):
#         input = """
#     func main() begin
#         dynamic a
#         dynamic b
#         a <- [b, 2, 3]
#         b <- 3.14
#         a <- [6,7,8]
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 490))

#     def test92(self):
#         input = """
#     func main() begin
#         dynamic a <- [a, 2, 3]
#     end
#         """
#         expect = "Type Mismatch In Statement: VarDecl(Id(a), None, dynamic, ArrayLit(Id(a), NumLit(2.0), NumLit(3.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 491))

#     def test93(self):
#         input = """
#     func main() begin
#         dynamic x
#         x[1, 2] <- [1,2,3]
#     end
#         """
#         expect = "Type Cannot Be Inferred: AssignStmt(ArrayCell(Id(x), [NumLit(1.0), NumLit(2.0)]), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 492))

#     def test94(self):
#         input = """
#     func main() begin
#         dynamic x
#         number a[2,2] <- [[x,1], [4,4]]
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 493))

#     def test95(self):
#         input = """
#     func main() begin
#         dynamic x
#         dynamic y
#         number a[2,2] <- [[x,x], [4,4]]
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 494))

#     def test96(self):
#         input = """
#     func main() begin
#         dynamic x
#         dynamic y
#         number a[2,2] <- [[x,x], [y,4]]
#         y <- 3.14
#         x <- 10
#         x <- true
#     end
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(x), BooleanLit(True))"
#         self.assertTrue(TestChecker.test(input, expect, 495))

#     def test97(self):
#         input = """
#     func main() begin
#         dynamic x
#         dynamic y
#         number a[2,2] <- [[x,x], [y,4]]
#         y <- 3.14
#         x <- 10
#         x <- true
#     end
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(x), BooleanLit(True))"
#         self.assertTrue(TestChecker.test(input, expect, 496))

#     def test97(self):
#         input = """
#     func main() begin
#         dynamic x
#         dynamic y
#         var a <- [[x,x], [y,4]]
#         y <- 3.14
#         x <- 10
#         x <- true
#     end
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(x), BooleanLit(True))"
#         self.assertTrue(TestChecker.test(input, expect, 496))

#     def test98(self):
#         input = """
#     func main() begin
#         dynamic x
#         dynamic y
#         var a <- [[x,x], [y,y]]
#     end
#         """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, ArrayLit(ArrayLit(Id(x), Id(x)), ArrayLit(Id(y), Id(y))))"
#         self.assertTrue(TestChecker.test(input, expect, 497))

#     def test99(self):
#         input = """
#     func foo()
#     func main() begin
#         dynamic x
#         number a[2,2] <- [[foo(),x], [4,4]]
#         x <- 1000
#         number c <- x + foo()
#     end
            
#     func foo() return 123
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 498))

#     def test100(self):
#         input = """
#     string a <- "final"
#     func supercomplextest123(number a, bool b, string c)
#     func main() begin
#         var a <- 1
#         dynamic b <- a
#         number m
#         dynamic n
#         var c <- [[123, 456], [m, n]]
#         dynamic q <- c[1,1]
#         n <- 101112
#         dynamic s
#         for a until b < c[0, 1] by m begin
#             if (a >= b / 20 + 1) begin
#                 number c <- b
#                 for c until a * 20 < q by c * supercomplextest123(c, s == "uper", s) begin
#                     writeNumber(c)
#                     continue
#                 end
#             end
#             elif (b != a) continue
#             else begin
#                 c[1] <- [a, b]
#                 return
#             end
#         end
#     end
#     func supercomplextest123(number e, bool f, string g)
#     begin
#         writeString(a)
#         if (((a..."test") == "finaltest") and not f) return 1
#         return e
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 499))

#     def test101(self):
#         input = """
#     func foo(number a[3, 4])
#     func main() begin
#         dynamic a
#         number b <- foo(a)
#         a <- [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
#     end
            
#     func foo(number a[3, 4]) return 123
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 500))

#     def test102(self):
#         input = """
#     func foo(number a[3, 4])
#     func main() begin
#         dynamic a
#         foo(a)
#         a <- [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
#     end
            
#     func foo(number a[3, 4]) return
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 501))

#     def test103(self):
#         input = """
#     func foo(number a[3, 4]) begin
#         dynamic gg
#         if (a[1,1] > 0) return a[1]
#         elif (a[1, 1] = 0) return gg
#         else begin
#             gg <- [1, 2, 3, 4]
#             return gg
#         end
#     end
#     func main() begin
#         dynamic a
#         var b <- foo(a)
#         b <- a[3]
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 502))

#     def test104(self):
#         input = """
#     func foo(number a[3, 4])
#     func main() begin
#         dynamic a
#         foo(a)
#         a <- [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
#     end
            
#     func foo(number a[3, 5]) return
#         """
#         expect = "Redeclared Function: foo"
#         self.assertTrue(TestChecker.test(input, expect, 503))

#     def test_424(self):
#         input = """
# dynamic b
# dynamic c
# dynamic d
# func main()
# begin
#     number a[3] <- [b,c,d]
#     number f <- d
# end
#         """
#         expect = ""
#         # infer b c d to number
#         self.assertTrue(TestChecker.test(input, expect, 424))

   

#     def test_uninfer_or_mismatch_13(self):
#         input = """
#             func main()
#             begin
#                 number a[2,3] <- [[1,2,3],[4,5,6]]
#                 a <- [[1,2,3,4],[4,5,6]]
#             end

#         """
#         expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0)), ArrayLit(NumLit(4.0), NumLit(5.0), NumLit(6.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 523))

#     def testsomething(self):
#         input = """
#         func trong(number a[1])
#                         return a[1]
#                     var abc <- false > "1" + 2
#                     """
#         expect = "Type Mismatch In Expression: BinaryOp(>, BooleanLit(False), BinaryOp(+, StringLit(1), NumLit(2.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 1910))
