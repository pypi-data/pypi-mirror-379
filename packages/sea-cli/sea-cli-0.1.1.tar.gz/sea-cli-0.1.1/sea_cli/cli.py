import click
import yaml
from .pipeline import run_pipeline


@click.group()
def main():
    """SEA - Structured Entropy Analysis CLI"""
    pass


@main.command()
@click.option(
    '--config',
    '-c',
    type=click.Path(),
    required=True,
    help='''YAML config file of the format:
input:
  rmsd: rmsd.txt
  rg: rg.txt 
  rmsf: rmsf.txt
bits: 8
export_folder: Exported_Data'''
)
def run(config):
    with open(config) as f:
        cfg = yaml.safe_load(f)
    out = run_pipeline(cfg)
    click.echo("SEA run complete. Results keys: {}".format(
        ", ".join(out['results'].keys())))


if __name__ == "__main__":
    main()
