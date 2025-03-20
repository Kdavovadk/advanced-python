def generate_latex_table(table_list):
    """
    Генерирует LaTeX-код таблицы.
    
    :param data: Данные таблицы.
    :return: LaTeX-код таблицы.
    """

    count_columns = len(table_list[0])
    column_format = ' | '.join(['c'] * count_columns)

    rows = [' & '.join(map(str, row)) + r' \\' for row in table_list]
    latex_table = f"""
\\begin{{table}}[h]
\\centering
\\begin{{tabular}}{{| {column_format} |}}
\\hline
{f' \n\\hline\n'.join(rows)}
\\hline
\\end{{tabular}}
\\caption{{RPC}}
\\label{{tab:table_1}}
\\end{{table}}"""

    return latex_table