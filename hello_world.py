import click


@click.group()
def cli():
    pass

@cli.command()
@click.option('--operacao', type =click.Choice(['soma','subtracao']), help='add numbers')
@click.argument('num1')
@click.argument('num2') 

def operacoes(operacao,num1,num2):
    if operacao=="soma":
        total = int(num1) + int(num2)
        click.echo('Soma= %s' % total)
    else:
        total = int(num1) - int(num2)
        click.echo('Subtracao = %s' %total)
        
if __name__ == '__main__':
    operacoes()


