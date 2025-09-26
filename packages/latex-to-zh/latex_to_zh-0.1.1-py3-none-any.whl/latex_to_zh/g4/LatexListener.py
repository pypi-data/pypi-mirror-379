# Generated from g4/Latex.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LatexParser import LatexParser
else:
    from LatexParser import LatexParser

# This class defines a complete listener for a parse tree produced by LatexParser.
class LatexListener(ParseTreeListener):

    # Enter a parse tree produced by LatexParser#formula.
    def enterFormula(self, ctx:LatexParser.FormulaContext):
        pass

    # Exit a parse tree produced by LatexParser#formula.
    def exitFormula(self, ctx:LatexParser.FormulaContext):
        pass


    # Enter a parse tree produced by LatexParser#transpose.
    def enterTranspose(self, ctx:LatexParser.TransposeContext):
        pass

    # Exit a parse tree produced by LatexParser#transpose.
    def exitTranspose(self, ctx:LatexParser.TransposeContext):
        pass


    # Enter a parse tree produced by LatexParser#transform_atom.
    def enterTransform_atom(self, ctx:LatexParser.Transform_atomContext):
        pass

    # Exit a parse tree produced by LatexParser#transform_atom.
    def exitTransform_atom(self, ctx:LatexParser.Transform_atomContext):
        pass


    # Enter a parse tree produced by LatexParser#transform_scale.
    def enterTransform_scale(self, ctx:LatexParser.Transform_scaleContext):
        pass

    # Exit a parse tree produced by LatexParser#transform_scale.
    def exitTransform_scale(self, ctx:LatexParser.Transform_scaleContext):
        pass


    # Enter a parse tree produced by LatexParser#transform_swap.
    def enterTransform_swap(self, ctx:LatexParser.Transform_swapContext):
        pass

    # Exit a parse tree produced by LatexParser#transform_swap.
    def exitTransform_swap(self, ctx:LatexParser.Transform_swapContext):
        pass


    # Enter a parse tree produced by LatexParser#transform_assignment.
    def enterTransform_assignment(self, ctx:LatexParser.Transform_assignmentContext):
        pass

    # Exit a parse tree produced by LatexParser#transform_assignment.
    def exitTransform_assignment(self, ctx:LatexParser.Transform_assignmentContext):
        pass


    # Enter a parse tree produced by LatexParser#elementary_transform.
    def enterElementary_transform(self, ctx:LatexParser.Elementary_transformContext):
        pass

    # Exit a parse tree produced by LatexParser#elementary_transform.
    def exitElementary_transform(self, ctx:LatexParser.Elementary_transformContext):
        pass


    # Enter a parse tree produced by LatexParser#elementary_transforms.
    def enterElementary_transforms(self, ctx:LatexParser.Elementary_transformsContext):
        pass

    # Exit a parse tree produced by LatexParser#elementary_transforms.
    def exitElementary_transforms(self, ctx:LatexParser.Elementary_transformsContext):
        pass


    # Enter a parse tree produced by LatexParser#matrix.
    def enterMatrix(self, ctx:LatexParser.MatrixContext):
        pass

    # Exit a parse tree produced by LatexParser#matrix.
    def exitMatrix(self, ctx:LatexParser.MatrixContext):
        pass


    # Enter a parse tree produced by LatexParser#det.
    def enterDet(self, ctx:LatexParser.DetContext):
        pass

    # Exit a parse tree produced by LatexParser#det.
    def exitDet(self, ctx:LatexParser.DetContext):
        pass


    # Enter a parse tree produced by LatexParser#cases.
    def enterCases(self, ctx:LatexParser.CasesContext):
        pass

    # Exit a parse tree produced by LatexParser#cases.
    def exitCases(self, ctx:LatexParser.CasesContext):
        pass


    # Enter a parse tree produced by LatexParser#matrixRow.
    def enterMatrixRow(self, ctx:LatexParser.MatrixRowContext):
        pass

    # Exit a parse tree produced by LatexParser#matrixRow.
    def exitMatrixRow(self, ctx:LatexParser.MatrixRowContext):
        pass


    # Enter a parse tree produced by LatexParser#relation.
    def enterRelation(self, ctx:LatexParser.RelationContext):
        pass

    # Exit a parse tree produced by LatexParser#relation.
    def exitRelation(self, ctx:LatexParser.RelationContext):
        pass


    # Enter a parse tree produced by LatexParser#relation_list.
    def enterRelation_list(self, ctx:LatexParser.Relation_listContext):
        pass

    # Exit a parse tree produced by LatexParser#relation_list.
    def exitRelation_list(self, ctx:LatexParser.Relation_listContext):
        pass


    # Enter a parse tree produced by LatexParser#relationListContent.
    def enterRelationListContent(self, ctx:LatexParser.RelationListContentContext):
        pass

    # Exit a parse tree produced by LatexParser#relationListContent.
    def exitRelationListContent(self, ctx:LatexParser.RelationListContentContext):
        pass


    # Enter a parse tree produced by LatexParser#equality.
    def enterEquality(self, ctx:LatexParser.EqualityContext):
        pass

    # Exit a parse tree produced by LatexParser#equality.
    def exitEquality(self, ctx:LatexParser.EqualityContext):
        pass


    # Enter a parse tree produced by LatexParser#expr.
    def enterExpr(self, ctx:LatexParser.ExprContext):
        pass

    # Exit a parse tree produced by LatexParser#expr.
    def exitExpr(self, ctx:LatexParser.ExprContext):
        pass


    # Enter a parse tree produced by LatexParser#additive.
    def enterAdditive(self, ctx:LatexParser.AdditiveContext):
        pass

    # Exit a parse tree produced by LatexParser#additive.
    def exitAdditive(self, ctx:LatexParser.AdditiveContext):
        pass


    # Enter a parse tree produced by LatexParser#mp.
    def enterMp(self, ctx:LatexParser.MpContext):
        pass

    # Exit a parse tree produced by LatexParser#mp.
    def exitMp(self, ctx:LatexParser.MpContext):
        pass


    # Enter a parse tree produced by LatexParser#mp_nofunc.
    def enterMp_nofunc(self, ctx:LatexParser.Mp_nofuncContext):
        pass

    # Exit a parse tree produced by LatexParser#mp_nofunc.
    def exitMp_nofunc(self, ctx:LatexParser.Mp_nofuncContext):
        pass


    # Enter a parse tree produced by LatexParser#unary.
    def enterUnary(self, ctx:LatexParser.UnaryContext):
        pass

    # Exit a parse tree produced by LatexParser#unary.
    def exitUnary(self, ctx:LatexParser.UnaryContext):
        pass


    # Enter a parse tree produced by LatexParser#unary_nofunc.
    def enterUnary_nofunc(self, ctx:LatexParser.Unary_nofuncContext):
        pass

    # Exit a parse tree produced by LatexParser#unary_nofunc.
    def exitUnary_nofunc(self, ctx:LatexParser.Unary_nofuncContext):
        pass


    # Enter a parse tree produced by LatexParser#postfix.
    def enterPostfix(self, ctx:LatexParser.PostfixContext):
        pass

    # Exit a parse tree produced by LatexParser#postfix.
    def exitPostfix(self, ctx:LatexParser.PostfixContext):
        pass


    # Enter a parse tree produced by LatexParser#postfix_nofunc.
    def enterPostfix_nofunc(self, ctx:LatexParser.Postfix_nofuncContext):
        pass

    # Exit a parse tree produced by LatexParser#postfix_nofunc.
    def exitPostfix_nofunc(self, ctx:LatexParser.Postfix_nofuncContext):
        pass


    # Enter a parse tree produced by LatexParser#postfix_op.
    def enterPostfix_op(self, ctx:LatexParser.Postfix_opContext):
        pass

    # Exit a parse tree produced by LatexParser#postfix_op.
    def exitPostfix_op(self, ctx:LatexParser.Postfix_opContext):
        pass


    # Enter a parse tree produced by LatexParser#eval_at.
    def enterEval_at(self, ctx:LatexParser.Eval_atContext):
        pass

    # Exit a parse tree produced by LatexParser#eval_at.
    def exitEval_at(self, ctx:LatexParser.Eval_atContext):
        pass


    # Enter a parse tree produced by LatexParser#eval_at_sub.
    def enterEval_at_sub(self, ctx:LatexParser.Eval_at_subContext):
        pass

    # Exit a parse tree produced by LatexParser#eval_at_sub.
    def exitEval_at_sub(self, ctx:LatexParser.Eval_at_subContext):
        pass


    # Enter a parse tree produced by LatexParser#eval_at_sup.
    def enterEval_at_sup(self, ctx:LatexParser.Eval_at_supContext):
        pass

    # Exit a parse tree produced by LatexParser#eval_at_sup.
    def exitEval_at_sup(self, ctx:LatexParser.Eval_at_supContext):
        pass


    # Enter a parse tree produced by LatexParser#exp.
    def enterExp(self, ctx:LatexParser.ExpContext):
        pass

    # Exit a parse tree produced by LatexParser#exp.
    def exitExp(self, ctx:LatexParser.ExpContext):
        pass


    # Enter a parse tree produced by LatexParser#exp_nofunc.
    def enterExp_nofunc(self, ctx:LatexParser.Exp_nofuncContext):
        pass

    # Exit a parse tree produced by LatexParser#exp_nofunc.
    def exitExp_nofunc(self, ctx:LatexParser.Exp_nofuncContext):
        pass


    # Enter a parse tree produced by LatexParser#triangle.
    def enterTriangle(self, ctx:LatexParser.TriangleContext):
        pass

    # Exit a parse tree produced by LatexParser#triangle.
    def exitTriangle(self, ctx:LatexParser.TriangleContext):
        pass


    # Enter a parse tree produced by LatexParser#comp.
    def enterComp(self, ctx:LatexParser.CompContext):
        pass

    # Exit a parse tree produced by LatexParser#comp.
    def exitComp(self, ctx:LatexParser.CompContext):
        pass


    # Enter a parse tree produced by LatexParser#comp_nofunc.
    def enterComp_nofunc(self, ctx:LatexParser.Comp_nofuncContext):
        pass

    # Exit a parse tree produced by LatexParser#comp_nofunc.
    def exitComp_nofunc(self, ctx:LatexParser.Comp_nofuncContext):
        pass


    # Enter a parse tree produced by LatexParser#group.
    def enterGroup(self, ctx:LatexParser.GroupContext):
        pass

    # Exit a parse tree produced by LatexParser#group.
    def exitGroup(self, ctx:LatexParser.GroupContext):
        pass


    # Enter a parse tree produced by LatexParser#norm_group.
    def enterNorm_group(self, ctx:LatexParser.Norm_groupContext):
        pass

    # Exit a parse tree produced by LatexParser#norm_group.
    def exitNorm_group(self, ctx:LatexParser.Norm_groupContext):
        pass


    # Enter a parse tree produced by LatexParser#abs_group.
    def enterAbs_group(self, ctx:LatexParser.Abs_groupContext):
        pass

    # Exit a parse tree produced by LatexParser#abs_group.
    def exitAbs_group(self, ctx:LatexParser.Abs_groupContext):
        pass


    # Enter a parse tree produced by LatexParser#floor_group.
    def enterFloor_group(self, ctx:LatexParser.Floor_groupContext):
        pass

    # Exit a parse tree produced by LatexParser#floor_group.
    def exitFloor_group(self, ctx:LatexParser.Floor_groupContext):
        pass


    # Enter a parse tree produced by LatexParser#ceil_group.
    def enterCeil_group(self, ctx:LatexParser.Ceil_groupContext):
        pass

    # Exit a parse tree produced by LatexParser#ceil_group.
    def exitCeil_group(self, ctx:LatexParser.Ceil_groupContext):
        pass


    # Enter a parse tree produced by LatexParser#accent.
    def enterAccent(self, ctx:LatexParser.AccentContext):
        pass

    # Exit a parse tree produced by LatexParser#accent.
    def exitAccent(self, ctx:LatexParser.AccentContext):
        pass


    # Enter a parse tree produced by LatexParser#atom_expr_no_supexpr.
    def enterAtom_expr_no_supexpr(self, ctx:LatexParser.Atom_expr_no_supexprContext):
        pass

    # Exit a parse tree produced by LatexParser#atom_expr_no_supexpr.
    def exitAtom_expr_no_supexpr(self, ctx:LatexParser.Atom_expr_no_supexprContext):
        pass


    # Enter a parse tree produced by LatexParser#atomExpr.
    def enterAtomExpr(self, ctx:LatexParser.AtomExprContext):
        pass

    # Exit a parse tree produced by LatexParser#atomExpr.
    def exitAtomExpr(self, ctx:LatexParser.AtomExprContext):
        pass


    # Enter a parse tree produced by LatexParser#atom.
    def enterAtom(self, ctx:LatexParser.AtomContext):
        pass

    # Exit a parse tree produced by LatexParser#atom.
    def exitAtom(self, ctx:LatexParser.AtomContext):
        pass


    # Enter a parse tree produced by LatexParser#mathit.
    def enterMathit(self, ctx:LatexParser.MathitContext):
        pass

    # Exit a parse tree produced by LatexParser#mathit.
    def exitMathit(self, ctx:LatexParser.MathitContext):
        pass


    # Enter a parse tree produced by LatexParser#mathit_text.
    def enterMathit_text(self, ctx:LatexParser.Mathit_textContext):
        pass

    # Exit a parse tree produced by LatexParser#mathit_text.
    def exitMathit_text(self, ctx:LatexParser.Mathit_textContext):
        pass


    # Enter a parse tree produced by LatexParser#text.
    def enterText(self, ctx:LatexParser.TextContext):
        pass

    # Exit a parse tree produced by LatexParser#text.
    def exitText(self, ctx:LatexParser.TextContext):
        pass


    # Enter a parse tree produced by LatexParser#frac.
    def enterFrac(self, ctx:LatexParser.FracContext):
        pass

    # Exit a parse tree produced by LatexParser#frac.
    def exitFrac(self, ctx:LatexParser.FracContext):
        pass


    # Enter a parse tree produced by LatexParser#binom.
    def enterBinom(self, ctx:LatexParser.BinomContext):
        pass

    # Exit a parse tree produced by LatexParser#binom.
    def exitBinom(self, ctx:LatexParser.BinomContext):
        pass


    # Enter a parse tree produced by LatexParser#func_normal_functions_single_arg.
    def enterFunc_normal_functions_single_arg(self, ctx:LatexParser.Func_normal_functions_single_argContext):
        pass

    # Exit a parse tree produced by LatexParser#func_normal_functions_single_arg.
    def exitFunc_normal_functions_single_arg(self, ctx:LatexParser.Func_normal_functions_single_argContext):
        pass


    # Enter a parse tree produced by LatexParser#func_normal_functions_multi_arg.
    def enterFunc_normal_functions_multi_arg(self, ctx:LatexParser.Func_normal_functions_multi_argContext):
        pass

    # Exit a parse tree produced by LatexParser#func_normal_functions_multi_arg.
    def exitFunc_normal_functions_multi_arg(self, ctx:LatexParser.Func_normal_functions_multi_argContext):
        pass


    # Enter a parse tree produced by LatexParser#func_operator_names_single_arg.
    def enterFunc_operator_names_single_arg(self, ctx:LatexParser.Func_operator_names_single_argContext):
        pass

    # Exit a parse tree produced by LatexParser#func_operator_names_single_arg.
    def exitFunc_operator_names_single_arg(self, ctx:LatexParser.Func_operator_names_single_argContext):
        pass


    # Enter a parse tree produced by LatexParser#func_operator_names_multi_arg.
    def enterFunc_operator_names_multi_arg(self, ctx:LatexParser.Func_operator_names_multi_argContext):
        pass

    # Exit a parse tree produced by LatexParser#func_operator_names_multi_arg.
    def exitFunc_operator_names_multi_arg(self, ctx:LatexParser.Func_operator_names_multi_argContext):
        pass


    # Enter a parse tree produced by LatexParser#func_normal_single_arg.
    def enterFunc_normal_single_arg(self, ctx:LatexParser.Func_normal_single_argContext):
        pass

    # Exit a parse tree produced by LatexParser#func_normal_single_arg.
    def exitFunc_normal_single_arg(self, ctx:LatexParser.Func_normal_single_argContext):
        pass


    # Enter a parse tree produced by LatexParser#func_normal_multi_arg.
    def enterFunc_normal_multi_arg(self, ctx:LatexParser.Func_normal_multi_argContext):
        pass

    # Exit a parse tree produced by LatexParser#func_normal_multi_arg.
    def exitFunc_normal_multi_arg(self, ctx:LatexParser.Func_normal_multi_argContext):
        pass


    # Enter a parse tree produced by LatexParser#func.
    def enterFunc(self, ctx:LatexParser.FuncContext):
        pass

    # Exit a parse tree produced by LatexParser#func.
    def exitFunc(self, ctx:LatexParser.FuncContext):
        pass


    # Enter a parse tree produced by LatexParser#args.
    def enterArgs(self, ctx:LatexParser.ArgsContext):
        pass

    # Exit a parse tree produced by LatexParser#args.
    def exitArgs(self, ctx:LatexParser.ArgsContext):
        pass


    # Enter a parse tree produced by LatexParser#func_common_args.
    def enterFunc_common_args(self, ctx:LatexParser.Func_common_argsContext):
        pass

    # Exit a parse tree produced by LatexParser#func_common_args.
    def exitFunc_common_args(self, ctx:LatexParser.Func_common_argsContext):
        pass


    # Enter a parse tree produced by LatexParser#limit_sub.
    def enterLimit_sub(self, ctx:LatexParser.Limit_subContext):
        pass

    # Exit a parse tree produced by LatexParser#limit_sub.
    def exitLimit_sub(self, ctx:LatexParser.Limit_subContext):
        pass


    # Enter a parse tree produced by LatexParser#func_single_arg.
    def enterFunc_single_arg(self, ctx:LatexParser.Func_single_argContext):
        pass

    # Exit a parse tree produced by LatexParser#func_single_arg.
    def exitFunc_single_arg(self, ctx:LatexParser.Func_single_argContext):
        pass


    # Enter a parse tree produced by LatexParser#func_single_arg_noparens.
    def enterFunc_single_arg_noparens(self, ctx:LatexParser.Func_single_arg_noparensContext):
        pass

    # Exit a parse tree produced by LatexParser#func_single_arg_noparens.
    def exitFunc_single_arg_noparens(self, ctx:LatexParser.Func_single_arg_noparensContext):
        pass


    # Enter a parse tree produced by LatexParser#func_multi_arg.
    def enterFunc_multi_arg(self, ctx:LatexParser.Func_multi_argContext):
        pass

    # Exit a parse tree produced by LatexParser#func_multi_arg.
    def exitFunc_multi_arg(self, ctx:LatexParser.Func_multi_argContext):
        pass


    # Enter a parse tree produced by LatexParser#func_multi_arg_noparens.
    def enterFunc_multi_arg_noparens(self, ctx:LatexParser.Func_multi_arg_noparensContext):
        pass

    # Exit a parse tree produced by LatexParser#func_multi_arg_noparens.
    def exitFunc_multi_arg_noparens(self, ctx:LatexParser.Func_multi_arg_noparensContext):
        pass


    # Enter a parse tree produced by LatexParser#subexpr.
    def enterSubexpr(self, ctx:LatexParser.SubexprContext):
        pass

    # Exit a parse tree produced by LatexParser#subexpr.
    def exitSubexpr(self, ctx:LatexParser.SubexprContext):
        pass


    # Enter a parse tree produced by LatexParser#supexpr.
    def enterSupexpr(self, ctx:LatexParser.SupexprContext):
        pass

    # Exit a parse tree produced by LatexParser#supexpr.
    def exitSupexpr(self, ctx:LatexParser.SupexprContext):
        pass


    # Enter a parse tree produced by LatexParser#subeq.
    def enterSubeq(self, ctx:LatexParser.SubeqContext):
        pass

    # Exit a parse tree produced by LatexParser#subeq.
    def exitSubeq(self, ctx:LatexParser.SubeqContext):
        pass


    # Enter a parse tree produced by LatexParser#supeq.
    def enterSupeq(self, ctx:LatexParser.SupeqContext):
        pass

    # Exit a parse tree produced by LatexParser#supeq.
    def exitSupeq(self, ctx:LatexParser.SupeqContext):
        pass



del LatexParser