from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):
    # Visit a parse tree produced by ZCodeParser#program.
    #   program: NEWLINE* list_declared EOF;
    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.list_declared()))

    # Visit a parse tree produced by ZCodeParser#list_declared.
    # list_declared: declared list_declared | declared;
    def visitList_declared(self, ctx: ZCodeParser.List_declaredContext):
        if ctx.list_declared():
            return [self.visit(ctx.declared())]+self.visit(ctx.list_declared())
        return [self.visit(ctx.declared())]

    # Visit a parse tree produced by ZCodeParser#declared.
    # declared: function | variables ignore;
    def visitDeclared(self, ctx: ZCodeParser.DeclaredContext):
        if ctx.function():
            return self.visit(ctx.function())
        return self.visit(ctx.variables())

    # Visit a parse tree produced by ZCodeParser#variables.
    # variables: implicit_var | keyword_var | implicit_dynamic;
    def visitVariables(self, ctx: ZCodeParser.VariablesContext):
        if ctx.implicit_var():
            return self.visit(ctx.implicit_var())
        elif ctx.keyword_var():
            return self.visit(ctx.keyword_var())
        return self.visit(ctx.implicit_dynamic())

    # Visit a parse tree produced by ZCodeParser#implicit_var.
    # implicit_var: VAR ID ASSIGNINIT expression;
    def visitImplicit_var(self, ctx: ZCodeParser.Implicit_varContext):
        name = Id(ctx.ID().getText())
        varType = None
        modifier = "var"
        varInit = self.visit(ctx.expression())
        return VarDecl(name, varType, modifier, varInit)

    # Visit a parse tree produced by ZCodeParser#keyword_var.
        # keyword_var:
        #     typ ID (LBRACKET list_NUMBER_LIT RBRACKET)? (
        #         ASSIGNINIT expression
        # )?;
    def visitKeyword_var(self, ctx: ZCodeParser.Keyword_varContext):
        name = Id(ctx.ID().getText())
        varType = self.visit(ctx.typ())
        modifier = None
        varInit = None
        if ctx.list_NUMBER_LIT():
            size = self.visit(ctx.list_NUMBER_LIT())
            eleType = varType
            varType = ArrayType(size, eleType)
        if ctx.expression():
            varInit = self.visit(ctx.expression())
        return VarDecl(name, varType, modifier, varInit)
    # Visit a parse tree produced by ZCodeParser#list_NUMBER_LIT.
    # list_NUMBER_LIT: NUMBER_LIT COMMA list_NUMBER_LIT | NUMBER_LIT;

    def visitList_NUMBER_LIT(self, ctx: ZCodeParser.List_NUMBER_LITContext):
        if ctx.list_NUMBER_LIT():
            return [float(ctx.NUMBER_LIT().getText())]+self.visit(ctx.list_NUMBER_LIT())
        return [float(ctx.NUMBER_LIT().getText())]

    # Visit a parse tree produced by ZCodeParser#implicit_dynamic.
    # implicit_dynamic: DYNAMIC ID (ASSIGNINIT expression)?;
    def visitImplicit_dynamic(self, ctx: ZCodeParser.Implicit_dynamicContext):
        name = Id(ctx.ID().getText())
        varType = None
        modifier = "dynamic"
        varInit = None
        if ctx.expression():
            varInit = self.visit(ctx.expression())
        return VarDecl(name, varType, modifier, varInit)
    # Visit a parse tree produced by ZCodeParser#function.
    # function:
    #     FUNC ID LPAREN parameters_list? RPAREN (
    #         ignore? return_statement
    #         | ignore? block_statement
    #         | ignore
        # );

    def visitFunction(self, ctx: ZCodeParser.FunctionContext):
        name = Id(ctx.ID().getText())
        param = []
        body = None
        if ctx.parameters_list():
            param = self.visit(ctx.parameters_list())
        if ctx.return_statement():
            body = self.visit(ctx.return_statement())
        elif ctx.block_statement():
            body = self.visit(ctx.block_statement())
        return FuncDecl(name, param, body)
    # Visit a parse tree produced by ZCodeParser#parameters_list.
    # parameters_list: parameter COMMA parameters_list | parameter;

    def visitParameters_list(self, ctx: ZCodeParser.Parameters_listContext):
        if ctx.parameters_list():
            return [self.visit(ctx.parameter())]+self.visit(ctx.parameters_list())
        return [self.visit(ctx.parameter())]

    # Visit a parse tree produced by ZCodeParser#parameter.
    # parameter: typ ID (LBRACKET list_NUMBER_LIT RBRACKET)?;
    def visitParameter(self, ctx: ZCodeParser.ParameterContext):
        name = Id(ctx.ID().getText())
        varType = self.visit(ctx.typ())
        modifier = None
        varInit = None
        if ctx.list_NUMBER_LIT():
            size = self.visit(ctx.list_NUMBER_LIT())
            eleType = varType
            varType = ArrayType(size, eleType)
        return VarDecl(name, varType, modifier, varInit)
    # Visit a parse tree produced by ZCodeParser#typ.
    # typ: BOOL | NUMBER | STRING

    def visitTyp(self, ctx: ZCodeParser.TypContext):
        if ctx.BOOL():
            return BoolType()
        elif ctx.NUMBER():
            return NumberType()
        return StringType()

    # Visit a parse tree produced by ZCodeParser#list_expression.
    # list_expression: expression COMMA list_expression | expression;
    def visitList_expression(self, ctx: ZCodeParser.List_expressionContext):
        if ctx.list_expression():
            return [self.visit(ctx.expression())]+self.visit(ctx.list_expression())
        return [self.visit(ctx.expression())]

    # Visit a parse tree produced by ZCodeParser#expression.
    # expression: expr1 STRING_CONCAT expr1 | expr1;
    def visitExpression(self, ctx: ZCodeParser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr1()[0])
        op = ctx.STRING_CONCAT().getText()
        left = self.visit(ctx.expr1()[0])
        right = self.visit(ctx.expr1()[1])
        return BinaryOp(op, left, right)

    # Visit a parse tree produced by ZCodeParser#expr1.
    # expr1: expr2 (EQUAL| STRING_EQUAL| NOT_EQUAL| LESS_THAN| GREATER_THAN| LESS_THAN_EQUAL| GREATER_THAN_EQUAL) expr2| expr2;
    def visitExpr1(self, ctx: ZCodeParser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr2()[0])
        left = self.visit(ctx.expr2()[0])
        right = self.visit(ctx.expr2()[1])
        op = ctx.getChild(1).getText()
        return BinaryOp(op, left, right)

    # Visit a parse tree produced by ZCodeParser#expr2.
    # expr2: expr2 (AND | OR) expr3 | expr3;
    def visitExpr2(self, ctx: ZCodeParser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr3())
        left = self.visit(ctx.expr2())
        right = self.visit(ctx.expr3())
        op = ctx.getChild(1).getText()
        return BinaryOp(op, left, right)

    # Visit a parse tree produced by ZCodeParser#expr3.
    # expr3: expr3 (ADD | SUB) expr4 | expr4;
    def visitExpr3(self, ctx: ZCodeParser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr4())
        left = self.visit(ctx.expr3())
        right = self.visit(ctx.expr4())
        op = ctx.getChild(1).getText()
        return BinaryOp(op, left, right)

    # Visit a parse tree produced by ZCodeParser#expr4.
    # expr4: expr4 (MUL | DIV | MOD) expr5 | expr5;
    def visitExpr4(self, ctx: ZCodeParser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr5())
        left = self.visit(ctx.expr4())
        right = self.visit(ctx.expr5())
        op = ctx.getChild(1).getText()
        return BinaryOp(op, left, right)

    # Visit a parse tree produced by ZCodeParser#expr5.
    # expr5: NOT expr5 | expr6;
    def visitExpr5(self, ctx: ZCodeParser.Expr5Context):
        if ctx.expr6():
            return self.visit(ctx.expr6())
        op = ctx.NOT().getText()
        operand = self.visit(ctx.expr5())
        return UnaryOp(op, operand)

    # Visit a parse tree produced by ZCodeParser#expr6.
    # expr6: (SUB | ADD) expr6 | expr7;
    def visitExpr6(self, ctx: ZCodeParser.Expr6Context):
        if ctx.expr7():
            return self.visit(ctx.expr7())
        op = ctx.getChild(0).getText()
        operand = self.visit(ctx.expr6())
        return UnaryOp(op, operand)

    # Visit a parse tree produced by ZCodeParser#expr7.
    # expr7: (ID | func_call) LBRACKET (list_expression) RBRACKET| expr8;
    def visitExpr7(self, ctx: ZCodeParser.Expr7Context):
        if ctx.expr8():
            return self.visit(ctx.expr8())
        elif ctx.ID():
            return ArrayCell(Id(ctx.ID().getText()), self.visit(ctx.list_expression()))
        return ArrayCell(self.visit(ctx.func_call()), self.visit(ctx.list_expression()))

    # Visit a parse tree produced by ZCodeParser#expr8.
    # expr8: ID | literal | LPAREN expression RPAREN | func_call;
    def visitExpr8(self, ctx: ZCodeParser.Expr8Context):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.func_call():
            return self.visit(ctx.func_call())
        return self.visit(ctx.expression())

    # Visit a parse tree produced by ZCodeParser#literal.
    # literal: NUMBER_LIT | STRING_LIT | TRUE | FALSE | array_literal
    def visitLiteral(self, ctx: ZCodeParser.LiteralContext):
        if ctx.NUMBER_LIT():
            return NumberLiteral(float(ctx.NUMBER_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        return self.visit(ctx.array_literal())

    # Visit a parse tree produced by ZCodeParser#array_literal.
    # array_literal: LBRACKET list_expression RBRACKET;
    def visitArray_literal(self, ctx: ZCodeParser.Array_literalContext):
        return ArrayLiteral(self.visit(ctx.list_expression()))

    # Visit a parse tree produced by ZCodeParser#func_call.
    # func_call: ID LPAREN list_expression? RPAREN;
    def visitFunc_call(self, ctx: ZCodeParser.Func_callContext):
        name = Id(ctx.ID().getText())
        args = []
        if ctx.list_expression():
            args = self.visit(ctx.list_expression())
        return CallExpr(name, args)
    # Visit a parse tree produced by ZCodeParser#ignore.

    def visitIgnore(self, ctx: ZCodeParser.IgnoreContext):
        return None
    # Visit a parse tree produced by ZCodeParser#statement.
    # statement:
        # declaration_statement
        # | assignment_statement
        # | if_statement
        # | for_statement
        # | break_statement
        # | continue_statement
        # | return_statement
        # | call_statement
        # | block_statement;

    def visitStatement(self, ctx: ZCodeParser.StatementContext):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by ZCodeParser#declaration_statement.
    # declaration_statement: (implicit_var| keyword_var| implicit_dynamic) ignore;
    def visitDeclaration_statement(self, ctx: ZCodeParser.Declaration_statementContext):
        return self.visit(ctx.getChild(0))
        # return ctx.getChild(0).accept(self)

    # Visit a parse tree produced by ZCodeParser#assignment_statement.
    # assignment_statement: lhs ASSIGNINIT expression ignore;
    def visitAssignment_statement(self, ctx: ZCodeParser.Assignment_statementContext):
        lhs = self.visit(ctx.lhs())
        exp = self.visit(ctx.expression())
        return Assign(lhs, exp)

    # Visit a parse tree produced by ZCodeParser#lhs.
    # lhs: ID LBRACKET list_expression RBRACKET | ID;
    def visitLhs(self, ctx: ZCodeParser.LhsContext):
        if ctx.list_expression():
            return ArrayCell(Id(ctx.ID().getText()), self.visit(ctx.list_expression()))
        return Id(ctx.ID().getText())

    # Visit a parse tree produced by ZCodeParser#if_statement.
    # if_statement:
        # IF LPAREN expression RPAREN ignore? statement elif_list (
        # 	ELSE ignore? statement
        # )?;
    def visitIf_statement(self, ctx: ZCodeParser.If_statementContext):
        expr = self.visit(ctx.expression())
        thenStmt = self.visit(ctx.statement()[0])
        elifStmt = self.visit(ctx.elif_list())
        elseStmt = None
        if ctx.ELSE():
            elseStmt = self.visit(ctx.statement()[1])
        return If(expr, thenStmt, elifStmt, elseStmt)
    # Visit a parse tree produced by ZCodeParser#elif_list.
    # elif_list: elif_stmt elif_list | ;

    def visitElif_list(self, ctx: ZCodeParser.Elif_listContext):
        if ctx.elif_list():
            return [self.visit(ctx.elif_stmt())]+self.visit(ctx.elif_list())
        return []

    # Visit a parse tree produced by ZCodeParser#elif_stmt.
    # elif_stmt: ELIF LPAREN expression RPAREN ignore? statement;
    def visitElif_stmt(self, ctx: ZCodeParser.Elif_stmtContext):
        return (self.visit(ctx.expression()), self.visit(ctx.statement()))

    # Visit a parse tree produced by ZCodeParser#for_statement.
    # for_statement:FOR ID UNTIL expression BY expression ignore? statement;
    def visitFor_statement(self, ctx: ZCodeParser.For_statementContext):
        name = Id(ctx.ID().getText())
        condExpr = self.visit(ctx.expression()[0])
        updExpr = self.visit(ctx.expression()[1])
        body = self.visit(ctx.statement())
        return For(name, condExpr, updExpr, body)

    # Visit a parse tree produced by ZCodeParser#break_statement.
    # break_statement: BREAK ignore;
    def visitBreak_statement(self, ctx: ZCodeParser.Break_statementContext):
        return Break()

    # Visit a parse tree produced by ZCodeParser#continue_statement.
    # continue_statement: CONTINUE ignore;
    def visitContinue_statement(self, ctx: ZCodeParser.Continue_statementContext):
        return Continue()

    # Visit a parse tree produced by ZCodeParser#return_statement.
    # return_statement: RETURN expression? ignore;
    def visitReturn_statement(self, ctx: ZCodeParser.Return_statementContext):
        if ctx.expression():
            return Return(self.visit(ctx.expression()))
        return Return()

    # Visit a parse tree produced by ZCodeParser#call_statement.
    #    call_statement: ID LPAREN list_expression? RPAREN ignore;
    def visitCall_statement(self, ctx: ZCodeParser.Call_statementContext):
        name = Id(ctx.ID().getText())
        args = []
        if ctx.list_expression():
            args = self.visit(ctx.list_expression())
        return CallStmt(name, args)

    # Visit a parse tree produced by ZCodeParser#block_statement.
    # block_statement: BEGIN ignore stmt_list END ignore;
    def visitBlock_statement(self, ctx: ZCodeParser.Block_statementContext):
        return Block(self.visit(ctx.stmt_list()))

    # Visit a parse tree produced by ZCodeParser#stmt_list.
    # stmt_list: statement stmt_list |;
    def visitStmt_list(self, ctx: ZCodeParser.Stmt_listContext):
        if ctx.stmt_list():
            return [self.visit(ctx.statement())]+self.visit(ctx.stmt_list())
        return []
