# Generated from g4/Latex.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LatexParser import LatexParser
else:
    from LatexParser import LatexParser

# This class defines a complete generic visitor for a parse tree produced by LatexParser.

class LatexVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LatexParser#formula.
    def visitFormula(self, ctx:LatexParser.FormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#transpose.
    def visitTranspose(self, ctx:LatexParser.TransposeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#transform_atom.
    def visitTransform_atom(self, ctx:LatexParser.Transform_atomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#transform_scale.
    def visitTransform_scale(self, ctx:LatexParser.Transform_scaleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#transform_swap.
    def visitTransform_swap(self, ctx:LatexParser.Transform_swapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#transform_assignment.
    def visitTransform_assignment(self, ctx:LatexParser.Transform_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#elementary_transform.
    def visitElementary_transform(self, ctx:LatexParser.Elementary_transformContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#elementary_transforms.
    def visitElementary_transforms(self, ctx:LatexParser.Elementary_transformsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#matrix.
    def visitMatrix(self, ctx:LatexParser.MatrixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#det.
    def visitDet(self, ctx:LatexParser.DetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#cases.
    def visitCases(self, ctx:LatexParser.CasesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#matrixRow.
    def visitMatrixRow(self, ctx:LatexParser.MatrixRowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#relation.
    def visitRelation(self, ctx:LatexParser.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#relation_list.
    def visitRelation_list(self, ctx:LatexParser.Relation_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#relationListContent.
    def visitRelationListContent(self, ctx:LatexParser.RelationListContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#equality.
    def visitEquality(self, ctx:LatexParser.EqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#expr.
    def visitExpr(self, ctx:LatexParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#additive.
    def visitAdditive(self, ctx:LatexParser.AdditiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#mp.
    def visitMp(self, ctx:LatexParser.MpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#mp_nofunc.
    def visitMp_nofunc(self, ctx:LatexParser.Mp_nofuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#unary.
    def visitUnary(self, ctx:LatexParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#unary_nofunc.
    def visitUnary_nofunc(self, ctx:LatexParser.Unary_nofuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#postfix.
    def visitPostfix(self, ctx:LatexParser.PostfixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#postfix_nofunc.
    def visitPostfix_nofunc(self, ctx:LatexParser.Postfix_nofuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#postfix_op.
    def visitPostfix_op(self, ctx:LatexParser.Postfix_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#eval_at.
    def visitEval_at(self, ctx:LatexParser.Eval_atContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#eval_at_sub.
    def visitEval_at_sub(self, ctx:LatexParser.Eval_at_subContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#eval_at_sup.
    def visitEval_at_sup(self, ctx:LatexParser.Eval_at_supContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#exp.
    def visitExp(self, ctx:LatexParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#exp_nofunc.
    def visitExp_nofunc(self, ctx:LatexParser.Exp_nofuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#triangle.
    def visitTriangle(self, ctx:LatexParser.TriangleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#comp.
    def visitComp(self, ctx:LatexParser.CompContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#comp_nofunc.
    def visitComp_nofunc(self, ctx:LatexParser.Comp_nofuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#group.
    def visitGroup(self, ctx:LatexParser.GroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#norm_group.
    def visitNorm_group(self, ctx:LatexParser.Norm_groupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#abs_group.
    def visitAbs_group(self, ctx:LatexParser.Abs_groupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#floor_group.
    def visitFloor_group(self, ctx:LatexParser.Floor_groupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#ceil_group.
    def visitCeil_group(self, ctx:LatexParser.Ceil_groupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#accent.
    def visitAccent(self, ctx:LatexParser.AccentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#atom_expr_no_supexpr.
    def visitAtom_expr_no_supexpr(self, ctx:LatexParser.Atom_expr_no_supexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#atomExpr.
    def visitAtomExpr(self, ctx:LatexParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#atom.
    def visitAtom(self, ctx:LatexParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#mathit.
    def visitMathit(self, ctx:LatexParser.MathitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#mathit_text.
    def visitMathit_text(self, ctx:LatexParser.Mathit_textContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#text.
    def visitText(self, ctx:LatexParser.TextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#frac.
    def visitFrac(self, ctx:LatexParser.FracContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#binom.
    def visitBinom(self, ctx:LatexParser.BinomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#func_normal_functions_single_arg.
    def visitFunc_normal_functions_single_arg(self, ctx:LatexParser.Func_normal_functions_single_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#func_normal_functions_multi_arg.
    def visitFunc_normal_functions_multi_arg(self, ctx:LatexParser.Func_normal_functions_multi_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#func_operator_names_single_arg.
    def visitFunc_operator_names_single_arg(self, ctx:LatexParser.Func_operator_names_single_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#func_operator_names_multi_arg.
    def visitFunc_operator_names_multi_arg(self, ctx:LatexParser.Func_operator_names_multi_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#func_normal_single_arg.
    def visitFunc_normal_single_arg(self, ctx:LatexParser.Func_normal_single_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#func_normal_multi_arg.
    def visitFunc_normal_multi_arg(self, ctx:LatexParser.Func_normal_multi_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#func.
    def visitFunc(self, ctx:LatexParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#args.
    def visitArgs(self, ctx:LatexParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#func_common_args.
    def visitFunc_common_args(self, ctx:LatexParser.Func_common_argsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#limit_sub.
    def visitLimit_sub(self, ctx:LatexParser.Limit_subContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#func_single_arg.
    def visitFunc_single_arg(self, ctx:LatexParser.Func_single_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#func_single_arg_noparens.
    def visitFunc_single_arg_noparens(self, ctx:LatexParser.Func_single_arg_noparensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#func_multi_arg.
    def visitFunc_multi_arg(self, ctx:LatexParser.Func_multi_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#func_multi_arg_noparens.
    def visitFunc_multi_arg_noparens(self, ctx:LatexParser.Func_multi_arg_noparensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#subexpr.
    def visitSubexpr(self, ctx:LatexParser.SubexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#supexpr.
    def visitSupexpr(self, ctx:LatexParser.SupexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#subeq.
    def visitSubeq(self, ctx:LatexParser.SubeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#supeq.
    def visitSupeq(self, ctx:LatexParser.SupeqContext):
        return self.visitChildren(ctx)



del LatexParser