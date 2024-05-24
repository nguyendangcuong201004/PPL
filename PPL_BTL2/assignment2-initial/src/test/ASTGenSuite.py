import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    
    def test1(self):
        input = """var a <- 1 + -1 / 2 % -3 * 1
"""
        expect = "Program([VarDecl(Id(a), None, var, BinaryOp(+, NumLit(1.0), BinaryOp(*, BinaryOp(%, BinaryOp(/, UnaryOp(-, NumLit(1.0)), NumLit(2.0)), UnaryOp(-, NumLit(3.0))), NumLit(1.0))))])"
        self.assertTrue(TestAST.test(input, expect, 300))
        
    def test2(self):
        input = """number a
bool b
string c
number a1[1, 2]
bool _[0]
string s[1, 2]
"""
        expect = "Program([VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), BoolType, None, None), VarDecl(Id(c), StringType, None, None), VarDecl(Id(a1), ArrayType([1.0, 2.0], NumberType), None, None), VarDecl(Id(_), ArrayType([0.0], BoolType), None, None), VarDecl(Id(s), ArrayType([1.0, 2.0], StringType), None, None)])"
        self.assertTrue(TestAST.test(input, expect, 301))
        
    def test3(self):
        input = """number a <- 3
bool b <- true
string c <- "test string"
number a1[1, 2] <- [3, 4]
bool _[0] <- funcall()
string s[1, 2] <- a1
"""
        expect = "Program([VarDecl(Id(a), NumberType, None, NumLit(3.0)), VarDecl(Id(b), BoolType, None, BooleanLit(True)), VarDecl(Id(c), StringType, None, StringLit(test string)), VarDecl(Id(a1), ArrayType([1.0, 2.0], NumberType), None, ArrayLit(NumLit(3.0), NumLit(4.0))), VarDecl(Id(_), ArrayType([0.0], BoolType), None, CallExpr(Id(funcall), [])), VarDecl(Id(s), ArrayType([1.0, 2.0], StringType), None, Id(a1))])"
        self.assertTrue(TestAST.test(input, expect, 302))
        
    def test4(self):
        input = """number a <- 3
bool b <- true
string c <- "test string"
number a1[1, 2] <- [3, 4]
bool _[0] <- funcall()
string s[1, 2] <- funcall(1, true, [1, 2], [funcall(), 3])
"""
        expect = "Program([VarDecl(Id(a), NumberType, None, NumLit(3.0)), VarDecl(Id(b), BoolType, None, BooleanLit(True)), VarDecl(Id(c), StringType, None, StringLit(test string)), VarDecl(Id(a1), ArrayType([1.0, 2.0], NumberType), None, ArrayLit(NumLit(3.0), NumLit(4.0))), VarDecl(Id(_), ArrayType([0.0], BoolType), None, CallExpr(Id(funcall), [])), VarDecl(Id(s), ArrayType([1.0, 2.0], StringType), None, CallExpr(Id(funcall), [NumLit(1.0), BooleanLit(True), ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(CallExpr(Id(funcall), []), NumLit(3.0))]))])"
        self.assertTrue(TestAST.test(input, expect, 303))
        
    def test5(self):
        input = """dynamic c
var d <- [1, 2, 3]
"""
        expect = "Program([VarDecl(Id(c), None, dynamic, None), VarDecl(Id(d), None, var, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))])"
        self.assertTrue(TestAST.test(input, expect, 304))
        
    def test6(self):
        input = """dynamic c
var d <- "[1, 2, 3]"
func fun()
func fun2(number a)
func fun3(bool b[1, 2])

func fun4(string c) return
func fun5()
begin
    return null
end
"""
        expect = "Program([VarDecl(Id(c), None, dynamic, None), VarDecl(Id(d), None, var, StringLit([1, 2, 3])), FuncDecl(Id(fun), [], None), FuncDecl(Id(fun2), [VarDecl(Id(a), NumberType, None, None)], None), FuncDecl(Id(fun3), [VarDecl(Id(b), ArrayType([1.0, 2.0], BoolType), None, None)], None), FuncDecl(Id(fun4), [VarDecl(Id(c), StringType, None, None)], Return()), FuncDecl(Id(fun5), [], Block([Return(Id(null))]))])"
        self.assertTrue(TestAST.test(input, expect, 305))
        
    def test7(self):
        input = """func main()
begin
    a <- 1
    b <- true
    c <- "bruh"
    d <- [1, 2, 3]
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(a), NumLit(1.0)), AssignStmt(Id(b), BooleanLit(True)), AssignStmt(Id(c), StringLit(bruh)), AssignStmt(Id(d), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))]))])"
        self.assertTrue(TestAST.test(input, expect, 306))
        
    def test8(self):
        input = """func main()
begin
    a <- [[1,2,3], funcall("wrong")]
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(a), ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), CallExpr(Id(funcall), [StringLit(wrong)])))]))])"
        self.assertTrue(TestAST.test(input, expect, 307))
        
    def test9(self):
        input = """func main()
begin
    a <- [[1,2,3], funcall("wrong")]
    a[2] <- "cell"
    a[2, cellfun()] <- [funcell(), ["str", true]]
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(a), ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), CallExpr(Id(funcall), [StringLit(wrong)]))), AssignStmt(ArrayCell(Id(a), [NumLit(2.0)]), StringLit(cell)), AssignStmt(ArrayCell(Id(a), [NumLit(2.0), CallExpr(Id(cellfun), [])]), ArrayLit(CallExpr(Id(funcell), []), ArrayLit(StringLit(str), BooleanLit(True))))]))])"
        self.assertTrue(TestAST.test(input, expect, 308))
        
    def test10(self):
        input = """func main()
begin
    a[2] <- a[0]
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(Id(a), [NumLit(2.0)]), ArrayCell(Id(a), [NumLit(0.0)]))]))])"
        self.assertTrue(TestAST.test(input, expect, 309))
        
    def test11(self):
        input = """func main()
begin
    a[2] <- a[0 + 1, 1 - 2]
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(Id(a), [NumLit(2.0)]), ArrayCell(Id(a), [BinaryOp(+, NumLit(0.0), NumLit(1.0)), BinaryOp(-, NumLit(1.0), NumLit(2.0))]))]))])"
        self.assertTrue(TestAST.test(input, expect, 310))
        
    def test12(self):
        input = """func main()
begin
    a[2] <- [a[0 + 1, b], funcall(1)]
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(Id(a), [NumLit(2.0)]), ArrayLit(ArrayCell(Id(a), [BinaryOp(+, NumLit(0.0), NumLit(1.0)), Id(b)]), CallExpr(Id(funcall), [NumLit(1.0)])))]))])"
        self.assertTrue(TestAST.test(input, expect, 311))
        
    def test13(self):
        input = """func main()
begin
    a[2] <- [a[0 + 1, b], funcall(not 12)]
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(Id(a), [NumLit(2.0)]), ArrayLit(ArrayCell(Id(a), [BinaryOp(+, NumLit(0.0), NumLit(1.0)), Id(b)]), CallExpr(Id(funcall), [UnaryOp(not, NumLit(12.0))])))]))])"
        self.assertTrue(TestAST.test(input, expect, 312))
        
    def test14(self):
        input = """func main()
begin
    a[2] <- [a[0 + 1, b], funcall("1"...(not 12))]
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(Id(a), [NumLit(2.0)]), ArrayLit(ArrayCell(Id(a), [BinaryOp(+, NumLit(0.0), NumLit(1.0)), Id(b)]), CallExpr(Id(funcall), [BinaryOp(..., StringLit(1), UnaryOp(not, NumLit(12.0)))])))]))])"
        self.assertTrue(TestAST.test(input, expect, 313))
        
    def test15(self):
        input = """func main()
begin
    break
    continue
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([Break, Continue]))])"
        self.assertTrue(TestAST.test(input, expect, 314))
        
    def test16(self):
        input = """func main()
begin
    call()
    call2(call())
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([CallStmt(Id(call), []), CallStmt(Id(call2), [CallExpr(Id(call), [])])]))])"
        self.assertTrue(TestAST.test(input, expect, 315))
        
    def test17(self):
        input = """func main()
begin
    begin
    begin
    end
    end
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([Block([Block([])])]))])"
        self.assertTrue(TestAST.test(input, expect, 316))
        
    def test18(self):
        input = """func main()
begin
    begin
    begin
        a <- 3
        call()
        return
    end
    end
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([Block([Block([AssignStmt(Id(a), NumLit(3.0)), CallStmt(Id(call), []), Return()])])]))])"
        self.assertTrue(TestAST.test(input, expect, 317))
        
    def test19(self):
        input = """func main()
begin
    if (expr(a) == "exprstr") return false
    if (a) begin
    end
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([If((BinaryOp(==, CallExpr(Id(expr), [Id(a)]), StringLit(exprstr)), Return(BooleanLit(False))), [], None), If((Id(a), Block([])), [], None)]))])"
        self.assertTrue(TestAST.test(input, expect, 318))
        
    def test20(self):
        input = """func main()
begin
    if (Qdeptrai() == true)
    begin
        if (above() == true) return true
        elif (c) begin
            break
        end
        else
            continue
    end
    elif (d) return false
    else 
        return d
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([If((BinaryOp(==, CallExpr(Id(Qdeptrai), []), BooleanLit(True)), Block([If((BinaryOp(==, CallExpr(Id(above), []), BooleanLit(True)), Return(BooleanLit(True))), [(Id(c), Block([Break]))], Continue)])), [(Id(d), Return(BooleanLit(False)))], Return(Id(d)))]))])"
        self.assertTrue(TestAST.test(input, expect, 319))
        
    def test21(self):
        input = """func main()
begin
    if (Qdeptrai() == true)
    begin
        if (above() == true) return true
        elif (c) begin
            break
        end
        else
            continue
    end
    else 
        return d
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([If((BinaryOp(==, CallExpr(Id(Qdeptrai), []), BooleanLit(True)), Block([If((BinaryOp(==, CallExpr(Id(above), []), BooleanLit(True)), Return(BooleanLit(True))), [(Id(c), Block([Break]))], Continue)])), [], Return(Id(d)))]))])"
        self.assertTrue(TestAST.test(input, expect, 320))
        
    def test22(self):
        input = """func main()
begin
    if (Qdeptrai() == true)
    begin
        if (above() == true) return true
        elif (c) begin
            break
        end
        else
            continue
    end
    elif (d) return false
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([If((BinaryOp(==, CallExpr(Id(Qdeptrai), []), BooleanLit(True)), Block([If((BinaryOp(==, CallExpr(Id(above), []), BooleanLit(True)), Return(BooleanLit(True))), [(Id(c), Block([Break]))], Continue)])), [(Id(d), Return(BooleanLit(False)))], None)]))])"
        self.assertTrue(TestAST.test(input, expect, 321))
        
    def test23(self):
        input = """func main()
begin
    if (Qdeptrai() == true)
        if (above() == true) return true
        elif (c) begin
            break
        end
    elif (d) return false
    else break
    else continue
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([If((BinaryOp(==, CallExpr(Id(Qdeptrai), []), BooleanLit(True)), If((BinaryOp(==, CallExpr(Id(above), []), BooleanLit(True)), Return(BooleanLit(True))), [(Id(c), Block([Break])), (Id(d), Return(BooleanLit(False)))], Break)), [], Continue)]))])"
        self.assertTrue(TestAST.test(input, expect, 322))
        
    def test24(self):
        input = """func main()
begin
    if (Qdeptrai() == true)
        if (above() == true) return true
        elif (c) begin
            break
        end
    elif (d) return false
    else break
    elif (e) return main(quan)
    else continue
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([If((BinaryOp(==, CallExpr(Id(Qdeptrai), []), BooleanLit(True)), If((BinaryOp(==, CallExpr(Id(above), []), BooleanLit(True)), Return(BooleanLit(True))), [(Id(c), Block([Break])), (Id(d), Return(BooleanLit(False)))], Break)), [(Id(e), Return(CallExpr(Id(main), [Id(quan)])))], Continue)]))])"
        self.assertTrue(TestAST.test(input, expect, 323))
        
    def test25(self):
        input = """func main()
begin
    for i until i > Q() by Q() - i simple()
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(>, Id(i), CallExpr(Id(Q), [])), BinaryOp(-, CallExpr(Id(Q), []), Id(i)), CallStmt(Id(simple), []))]))])"
        self.assertTrue(TestAST.test(input, expect, 324))
        
    def test26(self):
        input = """func main()
begin
    for i until i > Q() by Q() - i begin
        j <- i
        if (j > 10) break
        else 
        continue
        wee()
    end
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(>, Id(i), CallExpr(Id(Q), [])), BinaryOp(-, CallExpr(Id(Q), []), Id(i)), Block([AssignStmt(Id(j), Id(i)), If((BinaryOp(>, Id(j), NumLit(10.0)), Break), [], Continue), CallStmt(Id(wee), [])]))]))])"
        self.assertTrue(TestAST.test(input, expect, 325))
        
    def test27(self):
        input = """func main()
begin
    var a <- 1 + 2/3 - not (a..."a") * 12 and (30 or true)
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, var, BinaryOp(and, BinaryOp(-, BinaryOp(+, NumLit(1.0), BinaryOp(/, NumLit(2.0), NumLit(3.0))), BinaryOp(*, UnaryOp(not, BinaryOp(..., Id(a), StringLit(a))), NumLit(12.0))), BinaryOp(or, NumLit(30.0), BooleanLit(True))))]))])"
        self.assertTrue(TestAST.test(input, expect, 326))
        
    def test28(self):
        input = """func main()
begin
    var a <- foo() + sys[1, 2] == -50e-12
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, var, BinaryOp(==, BinaryOp(+, CallExpr(Id(foo), []), ArrayCell(Id(sys), [NumLit(1.0), NumLit(2.0)])), UnaryOp(-, NumLit(5e-11))))]))])"
        self.assertTrue(TestAST.test(input, expect, 327))

    def test29(self):
        input = """func main()
begin
    for i until i + (sheesh / siuu) by siuu
        for j until (a[1, siuuu()] != true) by i if (i == j) if (j != 0) break
        elif (j == 1) continue
        else break
        else begin
        end
        
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(+, Id(i), BinaryOp(/, Id(sheesh), Id(siuu))), Id(siuu), For(Id(j), BinaryOp(!=, ArrayCell(Id(a), [NumLit(1.0), CallExpr(Id(siuuu), [])]), BooleanLit(True)), Id(i), If((BinaryOp(==, Id(i), Id(j)), If((BinaryOp(!=, Id(j), NumLit(0.0)), Break), [(BinaryOp(==, Id(j), NumLit(1.0)), Continue)], Break)), [], Block([]))))]))])"
        self.assertTrue(TestAST.test(input, expect, 328))
        
    def test30(self):
        input = """func main()
begin
    for i until i + (sheesh / siuu) by siuu
        if (siuu != i) 
        for j until (a[1, siuuu()] != true) by i if (i == j) if (j != 0) break
        elif (j == 1) continue
        else break
        else begin
        end

end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(+, Id(i), BinaryOp(/, Id(sheesh), Id(siuu))), Id(siuu), If((BinaryOp(!=, Id(siuu), Id(i)), For(Id(j), BinaryOp(!=, ArrayCell(Id(a), [NumLit(1.0), CallExpr(Id(siuuu), [])]), BooleanLit(True)), Id(i), If((BinaryOp(==, Id(i), Id(j)), If((BinaryOp(!=, Id(j), NumLit(0.0)), Break), [(BinaryOp(==, Id(j), NumLit(1.0)), Continue)], Break)), [], Block([])))), [], None))]))])"
        self.assertTrue(TestAST.test(input, expect, 329))
        