from src.generate_latex import generate_latex_table


def main():
    table_list = [
        ['Company', 'Revenue', 'Profit', 'Costs'],
        ['One', '1000', '500', '500'],
        ['Two', '2000', '250', '1750'],
        ['Three', '5000', '100', '4900'],
        ['Four', '10000', '10000', '0'],
        ['Five', '500', '100', '400']
    ]

    latex_code = generate_latex_table(table_list)
    with open('artifacts/table.tex', 'w', encoding='utf-8') as f:
        f.write('\\documentclass{article}\n\\begin{document}\n')
        f.write(latex_code)
        f.write('\n\\end{document}')

if __name__ == '__main__':
    main()
