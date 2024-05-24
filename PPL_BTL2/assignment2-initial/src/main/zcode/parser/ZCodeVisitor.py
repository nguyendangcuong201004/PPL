# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#list_declared.
    def visitList_declared(self, ctx:ZCodeParser.List_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#declared.
    def visitDeclared(self, ctx:ZCodeParser.DeclaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#variables.
    def visitVariables(self, ctx:ZCodeParser.VariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#implicit_var.
    def visitImplicit_var(self, ctx:ZCodeParser.Implicit_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#keyword_var.
    def visitKeyword_var(self, ctx:ZCodeParser.Keyword_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#list_NUMBER_LIT.
    def visitList_NUMBER_LIT(self, ctx:ZCodeParser.List_NUMBER_LITContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#implicit_dynamic.
    def visitImplicit_dynamic(self, ctx:ZCodeParser.Implicit_dynamicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function.
    def visitFunction(self, ctx:ZCodeParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parameters_list.
    def visitParameters_list(self, ctx:ZCodeParser.Parameters_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parameter.
    def visitParameter(self, ctx:ZCodeParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#typ.
    def visitTyp(self, ctx:ZCodeParser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#list_expression.
    def visitList_expression(self, ctx:ZCodeParser.List_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression.
    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr1.
    def visitExpr1(self, ctx:ZCodeParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr2.
    def visitExpr2(self, ctx:ZCodeParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr3.
    def visitExpr3(self, ctx:ZCodeParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr4.
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr5.
    def visitExpr5(self, ctx:ZCodeParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr6.
    def visitExpr6(self, ctx:ZCodeParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr7.
    def visitExpr7(self, ctx:ZCodeParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr8.
    def visitExpr8(self, ctx:ZCodeParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#literal.
    def visitLiteral(self, ctx:ZCodeParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_literal.
    def visitArray_literal(self, ctx:ZCodeParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_call.
    def visitFunc_call(self, ctx:ZCodeParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ignore.
    def visitIgnore(self, ctx:ZCodeParser.IgnoreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statement.
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#declaration_statement.
    def visitDeclaration_statement(self, ctx:ZCodeParser.Declaration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assignment_statement.
    def visitAssignment_statement(self, ctx:ZCodeParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lhs.
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_statement.
    def visitIf_statement(self, ctx:ZCodeParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_list.
    def visitElif_list(self, ctx:ZCodeParser.Elif_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_stmt.
    def visitElif_stmt(self, ctx:ZCodeParser.Elif_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#for_statement.
    def visitFor_statement(self, ctx:ZCodeParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#break_statement.
    def visitBreak_statement(self, ctx:ZCodeParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continue_statement.
    def visitContinue_statement(self, ctx:ZCodeParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#return_statement.
    def visitReturn_statement(self, ctx:ZCodeParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#call_statement.
    def visitCall_statement(self, ctx:ZCodeParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block_statement.
    def visitBlock_statement(self, ctx:ZCodeParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_list.
    def visitStmt_list(self, ctx:ZCodeParser.Stmt_listContext):
        return self.visitChildren(ctx)



del ZCodeParser