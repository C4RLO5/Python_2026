from rich import print
from rich.table import Table

table_exemplo = Table(title='Tabela de Preços')

table_exemplo.add_column('Nome', justify='right', style='red')
table_exemplo.add_column('Preço', justify='center', style='yellow')



table_exemplo.add_row('Lapis', 'R$ 1.50')
table_exemplo.add_row('Borracha', '[green]R$ 5.00[/]')









print(table_exemplo)