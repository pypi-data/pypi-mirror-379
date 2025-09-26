import click
import yaml
from pathlib import Path
from .pipeline import run_pipeline


@click.group()
def main():
    """SEA - Structured Entropy Analysis CLI"""
    pass


@main.command()
@click.option('--rmsd', type=click.Path(exists=True, path_type=Path), help='Path to RMSD file')
@click.option('--rg', type=click.Path(exists=True, path_type=Path), help='Path to RG file')
@click.option('--rmsf', type=click.Path(exists=True, path_type=Path), help='Path to RMSF file')
@click.option('--bits', type=click.IntRange(1, 32), default=8, help='Number of bits for analysis (1-32)')
@click.option('--plot', is_flag=True, default=False, help='Generate and display visualization plots')
@click.option('--export-folder', type=Path, default='Exported_Data', help='Folder for exported data')
@click.option(
    '--config',
    '-c',
    type=click.Path(exists=True, path_type=Path),
    help='YAML config file. Cannot be used with other parameters.'
)
def run(rmsd, rg, rmsf, bits, plot, export_folder, config):
    """Run SEA analysis pipeline"""
    if config and any([rmsd, rg, rmsf, bits != 8, export_folder != Path('Exported_Data')]):
        raise click.UsageError("Cannot use --config with other parameters")

    try:
        if config:
            with open(config) as f:
                cfg = yaml.safe_load(f)
        else:
            cfg = {
                'input': {
                    'rmsd': str(rmsd) if rmsd else None,
                    'rg': str(rg) if rg else None,
                    'rmsf': str(rmsf) if rmsf else None
                },
                'bits': bits,
                'export_folder': str(export_folder)
            }

        if plot:
            cfg['plot'] = True

        # Create export folder if it doesn't exist
        Path(cfg['export_folder']).mkdir(parents=True, exist_ok=True)

        out = run_pipeline(cfg)
        if not out or 'results' not in out:
            raise click.ClickException("Pipeline returned no results")

        click.echo(
            f"SEA run complete. Results keys: {', '.join(out['results'].keys())}")

    except Exception as e:
        raise click.ClickException(str(e))


if __name__ == "__main__":
    main()
