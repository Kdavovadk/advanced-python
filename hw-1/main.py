import click


@click.group()
def cli():
    pass


@click.command()
@click.argument('filename', type=click.Path(exists=True), required=False)
def nl(filename):
    lines = []
    if filename:
        with open(filename, 'r') as f:
            line = f.readline()
            while line:
                lines.append(line.rstrip('\n'))
                line = f.readline()
    else:
        while True:
            try:
                lines.append(input())
            except:
                break

    for number, line in enumerate(lines, 1):
        click.echo(f'{str(number).rjust(6)}\t{line}')


@click.command()
@click.argument('filenames', type=click.Path(exists=True), required=False, nargs=-1)
def tail(filenames):
    contents = {}
    if filenames:
        for filename in filenames:
            lines = []
            with open(filename, 'r') as f:
                line = f.readline()
                while line:
                    lines.append(line.rstrip('\n'))
                    line = f.readline()
            contents[filename] = lines
    else:
        lines = []
        while True:
            try:
                lines.append(input())
            except:
                break
        contents['stdin'] = lines

    is_out_filename = False if len(contents) in (0, 1) else True 
    for filename, line in contents.items():
        if filename == 'stdin':
            click.echo('\n'.join(line[-17:]))
            break

        if is_out_filename:
            click.echo(f'==> {filename} <==')
        click.echo('\n'.join(line[-10:]))


@click.command()
@click.argument('filenames', type=click.Path(exists=True), required=False, nargs=-1)
def wc(filenames):
    stats = {}
    if filenames:
        for filename in filenames:
            stats[filename] = {
                'lines': 0,
                'words': 0,
                'bytes': 0
            }
            with open(filename, 'rb') as f:
                line = f.readline()
                while line:
                    stats[filename]['lines'] += 1 if line.decode().find('\n') != -1 else 0
                    stats[filename]['words'] += len(list(filter(None, line.decode().rstrip('\n').split(' '))))
                    stats[filename]['bytes'] += len(line)
                    line = f.readline()
    else:
        stats['stdin'] = {
            'lines': 0,
            'words': 0,
            'bytes': 0
        }
        while True:
            try:
                line = input()
                stats['stdin']['lines'] += 1
                stats['stdin']['words'] += len(list(filter(None, line.split(' '))))
                stats['stdin']['bytes'] += len((line + '\n').encode())
            except:
                break

    total_stats = {
        'lines': 0,
        'words': 0,
        'bytes': 0
    }
    for filename, stat in stats.items():
        if filename == 'stdin':
            click.echo(f'{stat['lines']} {stat['words']} {stat['bytes']}')
            break

        click.echo(f'{stat['lines']} {stat['words']} {stat['bytes']} {filename}')
        total_stats['lines'] += stats[filename]['lines']
        total_stats['words'] += stats[filename]['words']
        total_stats['bytes'] += stats[filename]['bytes']
    
    if len(stats) > 1:
        click.echo(f'{total_stats['lines']} {total_stats['words']} {total_stats['bytes']} total')


cli.add_command(nl)
cli.add_command(tail)
cli.add_command(wc)


if __name__ == "__main__":
    cli()
