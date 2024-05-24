from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce


class InferType(Type):  # InferType: Type that can be inferred
    pass


class FuncType(InferType):
    def __init__(self, param=[], typ=None, body=False):
        self.param = param  # List[Type]
        self.typ = typ  # Type: number, bool, string, arrayType or None
        self.body = body  # True if this function has body


class VarType(InferType):
    def __init__(self, typ=None):
        self.typ = typ  # Type: number, bool, string, arrayType or None


class ArrayLitType(Type):
    def __init__(self, eleType):
        # * eleType: List[Type]: kiểu của từng phần tử trong mảng
        # Type: InferType, ArrayLitType, StringType, BoolType, NumberType, ArrayType
        # * Ví dụ: [1, 2, 3] -> eleType = [NumberType(), NumberType(), NumberType()]
        # * Ví dụ: [[1, 2], [3, 4]] -> eleType = [ArrayType([2], NumberType()), ArrayType([2], NumberType())]
        # Các kiểu dữ liệu có thể là InferType, ArrayLitType, StringType, BoolType, NumberType, ArrayType
        self.eleType = eleType


class StaticChecker(BaseVisitor, Utils):
    def __init__(self, ast):
        self.ast = ast  # ast: AST from parser
        self.BlockFor = 0  # int:Check if we are in for loop
        self.function = None  # FuncZCode: Current function
        self.hasReturn = False  # bool: Check if we have return in function
        self.listFunction = {
            "readNumber": FuncType([], NumberType(), True),
            "readBool": FuncType([], BoolType(), True),
            "readString": FuncType([], StringType(), True),
            "writeNumber": FuncType([NumberType()], VoidType(), True),
            "writeBool": FuncType([BoolType()], VoidType(), True),
            "writeString": FuncType([StringType()], VoidType(), True)
        }
        self.innermost_stmt = None

    def check(self):
        self.visit(self.ast, [{}])
        return None

    def compareType(self, LHS, RHS):
        # LHS: Type:VoidType, NumberType, StringType, BoolType, ArrayType
        # RHS: Type:VoidType, NumberType, StringType, BoolType, ArrayType
        if type(LHS) is ArrayType and type(RHS) is ArrayType:
            if len(LHS.size) != len(RHS.size) or not self.compareType(LHS.eleType, RHS.eleType):
                return False
            return all([True if LHS.size[i] == RHS.size[i] else False for i in range(len(LHS.size))])
        return type(LHS) == type(RHS)

    def compareListType(self, LHS, RHS):
        # LHS: List[Type], Type: VoidType, NumberType, StringType, BoolType, ArrayType
        # RHS: List[Type], Type: VoidType, NumberType, StringType, BoolType, ArrayType
        if len(LHS) != len(RHS):
            return False
        return all([self.compareType(LHS[i], RHS[i]) for i in range(len(LHS))])

    def setTypeArray(self, typeArray, typeArrayZcode):
        # typeArray: ArrayType
        # typeArrayZcode: ArrayLitType

        # If first dimension of array is not equal, Ex: ArrayType([2, 3], NumberType) and ArrayLitType([NumberType, NumberType, NumberType])
        # 2 rows 3 columns but 3 elements
        if typeArray.size[0] != len(typeArrayZcode.eleType):
            return False

        # 1 dimension array
        # Ex: ArrayType([2], NumberType) and ArrayLitType([NumberType, NumberType])
        # If it is ZCode or ArrayLitType, we infer it, if it is ArrayType or PrimitiveType nothing to do
        if len(typeArray.size) == 1:
            for i in range(int(typeArray.size[0])):
                if isinstance(typeArrayZcode.eleType[i], InferType):
                    typeArrayZcode.eleType[i].typ = typeArray.eleType
                # If it is ArrayLitType, then it be like [[]] but the array is just 1 dimension so it return false
                if type(typeArrayZcode.eleType[i]) is ArrayLitType:
                    return False
        else:
            # > 1 dimension array
            # Ex: ArrayType([2,3],NumberType) ArrayLitType([VarType(None),ArrayLitType([VarType(None)])])
            # ArrayType([2,3],NumberType) [x,[y,y,y]]=> x is ArrayType([3],NumberType) and y is NumberType
            for i in range(int(typeArray.size[0])):
                if isinstance(typeArrayZcode.eleType[i], InferType):
                    typeArrayZcode.eleType[i].typ = ArrayType(
                        typeArray.size[1:], typeArray.eleType)
                if type(typeArrayZcode.eleType[i]) is ArrayLitType:
                    if not self.setTypeArray(ArrayType(typeArray.size[1:], typeArray.eleType), typeArrayZcode.eleType[i]):
                        return False
        return True

    def noDefinition(self):  # raise NoDefinition if there is a function that has no body
        for func in self.listFunction:
            if self.listFunction[func].body == False:
                raise NoDefinition(func)

    def noEntryPoint(self):  # raise NoEntryPoint if there is no entry point
        main = self.listFunction.get("main")
        if main is None or main.param != [] or not self.compareType(main.typ, VoidType()) or main.body == False:
            raise NoEntryPoint()

    def isPrimitiveType(self, typ):
        return isinstance(typ, NumberType) or isinstance(typ, StringType) or isinstance(typ, BoolType)

    def isArrayType(self, typ):
        return isinstance(typ, ArrayType)

    def isPriOrArrayType(self, typ):
        return self.isPrimitiveType(typ) or self.isArrayType(typ)

    def inferTypeExpr(self, LHS, RHS, ctx):
        if isinstance(LHS, InferType) and isinstance(RHS, InferType):  # VarType or FuncType
            raise TypeCannotBeInferred(self.innermost_stmt)
        if isinstance(LHS, InferType) and isinstance(RHS, ArrayLitType):
            raise TypeCannotBeInferred(self.innermost_stmt)
        if not isinstance(LHS, InferType) and isinstance(RHS, ArrayLitType):
            if self.isPrimitiveType(LHS):
                raise TypeCannotBeInferred(self.innermost_stmt)
            if self.isArrayType(LHS):
                if not self.setTypeArray(LHS, RHS):
                    raise TypeCannotBeInferred(self.innermost_stmt)
        if isinstance(LHS, InferType) and self.isPriOrArrayType(RHS):
            LHS.typ = RHS
        if self.isPriOrArrayType(LHS) and isinstance(RHS, InferType):
            RHS.typ = LHS
        if self.isPriOrArrayType(LHS) and self.isPriOrArrayType(RHS):
            if not self.compareType(LHS, RHS):
                raise TypeMismatchInExpression(ctx)

    def inferTypeStmt(self, LHS, RHS, ctx):
        if isinstance(LHS, InferType) and isinstance(RHS, InferType):  # VarType or FuncType
            raise TypeCannotBeInferred(ctx)
        if isinstance(LHS, InferType) and isinstance(RHS, ArrayLitType):
            raise TypeCannotBeInferred(ctx)
        if not isinstance(LHS, InferType) and isinstance(RHS, ArrayLitType):
            if self.isPrimitiveType(LHS):
                raise TypeCannotBeInferred(ctx)
            if self.isArrayType(LHS):
                if not self.setTypeArray(LHS, RHS):
                    raise TypeCannotBeInferred(ctx)
        if isinstance(LHS, InferType) and self.isPriOrArrayType(RHS):
            LHS.typ = RHS
        if self.isPriOrArrayType(LHS) and isinstance(RHS, InferType):
            RHS.typ = LHS
        if self.isPriOrArrayType(LHS) and self.isPriOrArrayType(RHS):
            if not self.compareType(LHS, RHS):
                raise TypeMismatchInStatement(ctx)

    def visitProgram(self, ast, param):
        for i in ast.decl:
            self.visit(i, param)
        # no definition function error
        self.noDefinition()
        # no entry point error
        self.noEntryPoint()

    def visitVarDecl(self, ast, param):
        self.innermost_stmt = ast
        # class VarDecl(Decl, Stmt):
        #     # name: Id
        #     # varType: Type = None  # None if there is no type
        #     # modifier: str = None  # None if there is no modifier
        #     # varInit: Expr = None  # None if there is no initial
        if ast.name.name in param[0]:
            raise Redeclared(Variable(), ast.name.name)
        param[0][ast.name.name] = VarType(ast.varType)
        if ast.varInit:
            LHS = self.visit(ast.name, param)
            RHS = self.visit(ast.varInit, param)
            LHS = self.visit(ast.name, param)
            RHS = self.visit(ast.varInit, param)
            self.inferTypeStmt(LHS, RHS, ast)

    def visitFuncDecl(self, ast, param):
        # class FuncDecl(Decl):
        # # name: Id
        # # param: List[VarDecl]  # empty list if there is no parameter
        # # body: Stmt = None  # None if this is just a declaration-part
        method = self.listFunction.get(ast.name.name)
        if method is not None and method.body is True:
            raise Redeclared(Function(), ast.name.name)
        if method is not None and ast.body is None:
            raise Redeclared(Function(), ast.name.name)
        listParam = {}
        typeParam = []
        self.hasReturn = False
        if ast.body is None:
            for i in ast.param:
                typeParam.append(i.varType)
            self.listFunction[ast.name.name] = FuncType(
                typeParam, None, False)
            return
        for i in ast.param:
            if i.name.name in listParam:
                raise Redeclared(Parameter(), i.name.name)
            listParam[i.name.name] = VarType(i.varType)
            typeParam.append(i.varType)
        if method:
            if not self.compareListType(method.param, typeParam):
                raise Redeclared(Function(), ast.name.name)
            method.body = True
            self.function = method
            self.visit(ast.body, [listParam] + param)
            if not self.hasReturn:
                if self.function.typ is None:
                    self.function.typ = VoidType()
                if not self.compareType(method.typ, VoidType()):
                    raise TypeMismatchInStatement(Return(None))
            self.listFunction[ast.name.name] = method
        else:
            self.listFunction[ast.name.name] = FuncType(typeParam, None, True)
            self.function = self.listFunction[ast.name.name]
            self.visit(ast.body,  [listParam] + param)
            if not self.hasReturn:
                if self.function.typ is None:
                    self.function.typ = VoidType()
                if not self.compareType(self.function.typ, VoidType()):
                    raise TypeMismatchInStatement(Return(None))

    def visitId(self, ast, param):
        # for scope in param:
        #     if ast.name in scope:
        #         return scope[ast.name].typ if scope[ast.name].typ else scope[ast.name]
        # raise Undeclared(Identifier(), ast.name)
        for i in range(len(param)):
            if ast.name in param[i]:
                return param[i][ast.name].typ if param[i][ast.name].typ else param[i][ast.name]
        raise Undeclared(Identifier(), ast.name)

    def visitCallExpr(self, ast, param):
        # name: Id
        # args: List[Expr]
        method = self.listFunction.get(ast.name.name)
        if method is None:
            raise Undeclared(Function(), ast.name.name)
        listLHS = method.param
        listRHS = [self.visit(i, param) for i in ast.args]
        if len(listLHS) != len(listRHS):
            raise TypeMismatchInExpression(ast)

        for i in range(len(listRHS)):
            self.inferTypeExpr(listLHS[i], listRHS[i], ast)
        listRHS = [self.visit(i, param) for i in ast.args]
        listLHS = method.param
        if method.typ is None:
            return method
        if self.compareType(method.typ, VoidType()):
            raise TypeMismatchInExpression(ast)
        return method.typ

    def visitCallStmt(self, ast, param):
        self.innermost_stmt = ast
        # name: Id
        # args: List[Expr]
        method = self.listFunction.get(ast.name.name)
        # print(method.typ)
        if method is None:
            raise Undeclared(Function(), ast.name.name)
        listLHS = method.param
        listRHS = [self.visit(i, param) for i in ast.args]
        if len(listLHS) != len(listRHS):
            raise TypeMismatchInStatement(ast)
        for i in range(len(listRHS)):
            self.inferTypeStmt(listLHS[i], listRHS[i], ast)
        if method.typ is None:
            method.typ = VoidType()
        if not self.compareType(method.typ, VoidType()):
            raise TypeMismatchInStatement(ast)
        return method.typ

    def visitIf(self, ast, param):
        self.innermost_stmt = ast
        # expr: Expr
        # thenStmt: Stmt
        # elifStmt: List[Tuple[Expr, Stmt]] # empty list if there is no elif statement
        # elseStmt: Stmt = None  # None if there is no else branch
        LHS = BoolType()
        RHS = self.visit(ast.expr, param)
        self.inferTypeStmt(LHS, RHS, ast)
        self.visit(ast.thenStmt,  param)
        for i in ast.elifStmt:
            LHS = BoolType()
            RHS = self.visit(i[0], param)
            self.inferTypeStmt(LHS, RHS, ast)
            self.visit(i[1], param)
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt,  param)

    def visitFor(self, ast, param):
        self.innermost_stmt = ast
        # name: Id
        # condExpr: Expr
        # updExpr: Expr
        # body: Stmt
        LHS = NumberType()
        RHS = self.visit(ast.name, param)
        self.inferTypeStmt(LHS, RHS, ast)

        LHS = BoolType()
        RHS = self.visit(ast.condExpr, param)
        self.inferTypeStmt(LHS, RHS, ast)

        LHS = NumberType()
        RHS = self.visit(ast.updExpr, param)
        self.inferTypeStmt(LHS, RHS, ast)

        self.BlockFor += 1
        self.visit(ast.body, param)
        self.BlockFor -= 1

    def visitReturn(self, ast, param):
        self.innermost_stmt = ast
        # print(ast)
        # expr: Expr = None  # None if there is no expression after return
        self.hasReturn = True
        LHS = self.function.typ if self.function.typ else self.function
        RHS = self.visit(ast.expr, param) if ast.expr else VoidType()
        if isinstance(LHS, InferType) and type(RHS) is VoidType:
            LHS.typ = VoidType()
            LHS = VoidType()
        if type(LHS) is not VoidType and type(RHS) is not VoidType:
            self.inferTypeStmt(LHS, RHS, ast)
            LHS = self.function.typ if self.function.typ else self.function
            RHS = self.visit(ast.expr, param) if ast.expr else VoidType()
        if type(LHS) != type(RHS):
            raise TypeMismatchInStatement(Return(ast.expr))

    def visitAssign(self, ast, param):
        self.innermost_stmt = ast
        # lhs: Expr
        # exp: Expr
        LHS = self.visit(ast.lhs, param)
        RHS = self.visit(ast.rhs, param)
        LHS = self.visit(ast.lhs, param)
        RHS = self.visit(ast.rhs, param)
        # print(LHS, RHS)
        self.inferTypeStmt(LHS, RHS, ast)

    def visitBinaryOp(self, ast, param):
        # op: str
        # left: Expr
        # right: Expr
        op = ast.op
        if op in ['+', '-', '*', '/', '%']:
            LHS = NumberType()
            left = self.visit(ast.left, param)
            if isinstance(left, InferType):
                left.typ = LHS
                left = LHS
            if not self.isPriOrArrayType(left):
                raise TypeCannotBeInferred(self.innermost_stmt)
            if type(left) is not NumberType:
                raise TypeMismatchInExpression(ast)
            right = self.visit(ast.right, param)
            # print(left,right)
            if isinstance(right, InferType):
                right.typ = LHS
                right = LHS
            if not self.isPriOrArrayType(right):
                raise TypeCannotBeInferred(self.innermost_stmt)
            if type(right) is not NumberType:
                raise TypeMismatchInExpression(ast)
            return NumberType()
        if op in ["=", "!=", "<", ">", ">=", "<="]:
            LHS = NumberType()
            left = self.visit(ast.left, param)
            if isinstance(left, InferType):
                left.typ = LHS
                left = LHS
            if not self.isPriOrArrayType(left):
                raise TypeCannotBeInferred(self.innermost_stmt)
            if type(left) is not NumberType:
                raise TypeMismatchInExpression(ast)
            right = self.visit(ast.right, param)
            if isinstance(right, InferType):
                right.typ = LHS
                right = LHS
            if not self.isPriOrArrayType(right):
                raise TypeCannotBeInferred(self.innermost_stmt)
            if type(right) is not NumberType:
                raise TypeMismatchInExpression(ast)
            return BoolType()
        if op in ['and', 'or']:
            LHS = BoolType()
            left = self.visit(ast.left, param)
            if isinstance(left, InferType):
                left.typ = LHS
                left = LHS
            if not self.isPriOrArrayType(left):
                raise TypeCannotBeInferred(self.innermost_stmt)
            if type(left) is not BoolType:
                raise TypeMismatchInExpression(ast)
            right = self.visit(ast.right, param)
            if isinstance(right, InferType):
                right.typ = LHS
                right = LHS
            if not self.isPriOrArrayType(right):
                raise TypeCannotBeInferred(self.innermost_stmt)
            if type(right) is not BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType()
        if op == "==":
            LHS = StringType()
            left = self.visit(ast.left, param)
            if isinstance(left, InferType):
                left.typ = LHS
                left = LHS
            if not self.isPriOrArrayType(left):
                raise TypeCannotBeInferred(self.innermost_stmt)
            if type(left) is not StringType:
                raise TypeMismatchInExpression(ast)
            right = self.visit(ast.right, param)
            if isinstance(right, InferType):
                right.typ = LHS
                right = LHS
            if not self.isPriOrArrayType(right):
                raise TypeCannotBeInferred(self.innermost_stmt)
            if type(right) is not StringType:
                raise TypeMismatchInExpression(ast)
            return BoolType()
        if op == "...":
            LHS = StringType()
            left = self.visit(ast.left, param)
            if isinstance(left, InferType):
                left.typ = LHS
                left = LHS
            if not self.isPriOrArrayType(left):
                raise TypeCannotBeInferred(self.innermost_stmt)
            if type(left) is not StringType:
                raise TypeMismatchInExpression(ast)
            right = self.visit(ast.right, param)
            if isinstance(right, InferType):
                right.typ = LHS
                right = LHS
            # print(left, right)
            if not self.isPriOrArrayType(right):
                raise TypeCannotBeInferred(self.innermost_stmt)
            if type(right) is not StringType:
                raise TypeMismatchInExpression(ast)
            return StringType()

    def visitUnaryOp(self, ast, param):
        right = self.visit(ast.operand, param)
        op = ast.op
        if op in ['+', '-']:
            LHS = NumberType()
            if isinstance(right, InferType):
                right.typ = LHS
                right = LHS
            if not self.isPriOrArrayType(right):
                raise TypeCannotBeInferred(self.innermost_stmt)
            if type(right) is not NumberType:
                raise TypeMismatchInExpression(ast)
            return NumberType()
        if op in ['not']:
            LHS = BoolType()
            if isinstance(right, InferType):
                right.typ = LHS
                right = LHS
            if not self.isPriOrArrayType(right):
                raise TypeCannotBeInferred(self.innermost_stmt)
            if type(right) is not BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType()

    def visitArrayCell(self, ast, param):
        # arr: Expr
        # idx: List[Expr]
        left = self.visit(ast.arr, param)
        # print("heh",left)
        if isinstance(left, InferType):
            raise TypeCannotBeInferred(self.innermost_stmt)
        if type(left) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        LHS = NumberType()
        for i in ast.idx:
            right = self.visit(i, param)
            if isinstance(right, InferType):
                right.typ = LHS
                right = LHS
            if type(right) is not NumberType:
                raise TypeMismatchInExpression(ast)
        if len(left.size) < len(ast.idx):
            raise TypeMismatchInExpression(ast)
        if len(left.size) == len(ast.idx):
            return left.eleType
        if len(left.size) > len(ast.idx):
            return ArrayType(left.size[len(ast.idx):], left.eleType)

    def visitArrayLiteral(self, ast, param):
        # value: List[Expr]
        typ = None
        for item in ast.value:
            checkTyp = self.visit(item, param)
            if not (isinstance(checkTyp, InferType) or isinstance(checkTyp, ArrayLitType)):
                typ = checkTyp
                break
        if typ is None:
            return ArrayLitType([self.visit(i, param) for i in ast.value])
        elif type(typ) in [NumberType, BoolType, StringType]:
            for item in ast.value:
                itemType = self.visit(item, param)
                if isinstance(itemType, InferType):
                    itemType.typ = typ
                    itemType = typ
                if isinstance(itemType, ArrayLitType):
                    raise TypeCannotBeInferred(self.innermost_stmt)
                if not self.compareType(itemType, typ):
                    raise TypeMismatchInExpression(ast)
            return ArrayType([float(len(ast.value))], typ)
        else:  # ArrayType
            for item in ast.value:
                itemType = self.visit(item, param)

                if isinstance(itemType, InferType):
                    itemType.typ = ArrayType(typ.size, typ.eleType)
                    itemType = itemType.typ
                if type(itemType) is ArrayLitType:
                    if not self.setTypeArray(typ, itemType):
                        raise TypeMismatchInExpression(ast)
                    itemType = typ
                if not self.compareType(itemType, typ):
                    raise TypeMismatchInExpression(ast)
            return ArrayType([float(len(ast.value))]+typ.size, typ.eleType)

    def visitBlock(self, ast, param):
        self.innermost_stmt = ast
        paramNew = [{}] + param  # ! tăng tầm vực
        for item in ast.stmt:
            self.visit(item, paramNew)

    def visitContinue(self, ast, param):
        self.innermost_stmt = ast
        #! kiểm tra đang ở vòng for hay không
        if self.BlockFor == 0:
            raise MustInLoop(ast)

    def visitBreak(self, ast, param):
        self.innermost_stmt = ast
        #! kiểm tra đang ở vòng for hay không
        if self.BlockFor == 0:
            raise MustInLoop(ast)

    def visitNumberType(self, ast, param): return ast
    def visitBoolType(self, ast, param): return ast
    def visitStringType(self, ast, param): return ast
    def visitArrayType(self, ast, param): return ast
    def visitNumberLiteral(self, ast, param): return NumberType()
    def visitBooleanLiteral(self, ast, param): return BoolType()
    def visitStringLiteral(self, ast, param): return StringType()
