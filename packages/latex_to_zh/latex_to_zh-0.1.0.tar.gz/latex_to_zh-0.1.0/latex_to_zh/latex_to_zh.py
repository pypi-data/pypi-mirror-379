
from antlr4 import *

from .g4.LatexLexer import LatexLexer
from .g4.LatexParser import LatexParser
from .g4.LatexVisitor import LatexVisitor


class Visitor(LatexVisitor):

    def visit(self, tree):
        return tree.accept(self)

    def visitAtom(self, ctx:LatexParser.AtomContext):
        """原子数"""
        if ctx.atom_expr():
            return self.visit(ctx.atom_expr())
        elif ctx.triangle():
            return f'三角形{ctx.triangle().TRIANGLE_LETTER().getText()}'
        elif ctx.text():
            return ctx.text().TEXT_LETTER().getText()
        elif ctx.SYMBOL():
            if ctx.SYMBOL().getText() == '\pi':
                return 'π'
        else:
            return ctx.getText()

    def visitAtomExpr(self, ctx:LatexParser.AtomExprContext):
        """原子表达式, y^n, """
        base = ctx.children[0].getText()
        if ctx.getChildCount() == 2:
            return f'{base}的{self.visit(ctx.children[1])}'
        return base

    def visitAdditive(self, ctx: LatexParser.AdditiveContext):
        """加减"""
        if ctx.ADD():
            return f'{self.visit(ctx.additive(0))}加{self.visit(ctx.additive(1))}'
        elif ctx.SUB():
            return f'{self.visit(ctx.additive(0))}减{self.visit(ctx.additive(1))}'
        elif ctx.CMD_PM():
            return f'{self.visit(ctx.additive(0))}加减{self.visit(ctx.additive(1))}'
        elif ctx.mp():
            return self.visit(ctx.mp())
        else:
            return self.visitChildren(ctx)

    def visitMp(self, ctx: LatexParser.MpContext):
        """乘除"""
        if ctx.MUL() or ctx.CMD_CDOT() or ctx.CMD_TIMES():
            return f'{self.visit(ctx.mp(0))}乘{self.visit(ctx.mp(1))}'
        elif ctx.DIV() or ctx.CMD_DIV():
            return f'{self.visit(ctx.mp(0))}除以{self.visit(ctx.mp(1))}'
        elif ctx.COLON():
            return f'{self.visit(ctx.mp(0))}比{self.visit(ctx.mp(1))}'
        elif ctx.CMD_CDOTS():
            return f'{self.visit(ctx.mp(0))}余{self.visit(ctx.mp(1))}'
        else:
            return self.visitChildren(ctx)

    def visitFrac(self, ctx:LatexParser.FracContext):
        """分数"""
        return f'{self.visit(ctx.lower)}分之{self.visit(ctx.upper)}'

    def visitUnary(self, ctx: LatexParser.UnaryContext):
        """一元表达式"""
        if ctx.unary():
            if ctx.SUB():
                return f'负{self.visit(ctx.unary())}'
            elif ctx.ADD():
                return f'正{self.visit(ctx.unary())}'
            elif ctx.PM():
                return f'正负{self.visit(ctx.unary())}'
        elif ctx.postfix():
            ret = ''
            for i in ctx.children:
                if ret:
                    ret += '乘'
                c = self.visit(i)
                if c:
                    ret += c
            return ret
        else:
            return self.visitChildren(ctx)

    def visitSupexpr(self, ctx: LatexParser.SupexprContext):
        """上标"""
        if ctx.atom():
            base = ctx.atom().getText()
            if base == '2':
                return '平方'
            elif base == '3':
                return '立方'
            else:
                return f'{base}次方'
        elif ctx.expr():
            return f'{self.visit(ctx.expr())}次方'
        else:
            return self.visitChildren(ctx)

    def visitFunc(self, ctx:LatexParser.FuncContext):
        """表达式， 比如根号"""
        if ctx.FUNC_SQRT():
            base = self.visit(ctx.base)
            if ctx.root:
                root = self.visit(ctx.root)
                return f'{root}次根号{base}'
            return f'根号{base}'
        return self.visitChildren(ctx)

    def visitRelation(self, ctx:LatexParser.RelationContext):
        """关系式"""
        if ctx.ASSIGNMENT() or ctx.EQUAL():
            return f'{self.visit(ctx.relation(0))}等于{self.visit(ctx.relation(1))}'
        elif ctx.UNEQUAL():
            return f'{self.visit(ctx.relation(0))}不等于{self.visit(ctx.relation(1))}'
        elif ctx.AROUND():
            return f'{self.visit(ctx.relation(0))}等于{self.visit(ctx.relation(1))}'
        elif ctx.LT():
            return f'{self.visit(ctx.relation(0))}小于{self.visit(ctx.relation(1))}'
        elif ctx.LTE():
            return f'{self.visit(ctx.relation(0))}小于等于{self.visit(ctx.relation(1))}'
        elif ctx.GT():
            return f'{self.visit(ctx.relation(0))}大于{self.visit(ctx.relation(1))}'
        elif ctx.GTE():
            return f'{self.visit(ctx.relation(0))}大于等于{self.visit(ctx.relation(1))}'

        else:
            return self.visitChildren(ctx)

    def visitCases(self, ctx:LatexParser.CasesContext):
        """条件定义"""
        ret = ''
        for index,  matrix_row in enumerate(ctx.matrix_row(), start=1):
            ret += f'第{index}方程：{self.visit(matrix_row)};'
        return ret

    def visitGroup(self, ctx:LatexParser.GroupContext):
        return f' {self.visit(ctx.expr())} '

    def visitRelationListContent(self, ctx:LatexParser.RelationListContentContext):
        connect_symbol = ctx.connect.text
        ret = connect_symbol.join([self.visit(i) for i in ctx.relation()])
        return ret


def convert(text: str) -> str:
    """将latex转换成中文"""
    lexer = LatexLexer(InputStream(text))
    stream = CommonTokenStream(lexer)
    parser = LatexParser(stream)
    tree = parser.formula()
    visitor = Visitor()
    visitor_out = visitor.visit(tree)   # 使用visitor对block进行处理，获取语法树解析结果
    return visitor_out