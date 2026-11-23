import click
import shutil
from rich.console import Console
from dotenv import load_dotenv

from readmify.components.init import init_project
from readmify import __version__

console = Console()

# Load environment variables from a .env file if it exists in the current directory
load_dotenv()

@click.group()
@click.version_option(version=__version__)
def cli():
    """
    Readmify: AI-powered project documentation generator.
    
    Automatically generate, update, and manage your project's 
    README and codebase documentation using LLMs.
    """
    pass

@cli.command()
def init():
    """
    Initialize a new Readmify project and create readmify.yaml.
    
    This command scans your current directory (respecting your .gitignore), creates a local
    caching folder (.readmify/), and generates a readmify.yaml configuration file 
    which you can manually edit to include or exclude specific files.
    """
    init_project()

@cli.group(name="set")
def set_group():
    """
    Set configuration settings for Readmify.
    
    Use this command group to modify your readmify.yaml configuration 
    directly from the command line.
    """
    pass

@set_group.command("default")
@click.argument("model")
def set_default(model):
    """
    Set the default LLM model in readmify.yaml.
    
    MODEL: The exact Model ID from Groq you wish to use (e.g. 'openai/gpt-oss-20b').
    """
    from readmify.components.config import update_config
    update_config(model=model)

@cli.command()
@click.option('--model', help='Temporarily override the LLM model specified in readmify.yaml.')
@click.option('--provider', help='Temporarily override the LLM provider.')
def generate(model, provider):
    """
    Run the complete documentation generation pipeline.
    
    This command will read your readmify.yaml file, extract code from all 
    specified files, generate intelligent AI summaries for each of them, 
    and compile a massive and professional README.md. 
    
    If a README.md already exists, it will be safely backed up to README-prev.md.
    """
    from readmify.components.run import run_docs
    run_docs(model=model, provider=provider)

# Backward-compatible alias for existing users.
cli.add_command(generate, name="run")

@cli.command()
@click.argument('path', type=click.Path(exists=True), required=True)
@click.option('--model', help='Temporarily override the LLM model specified in readmify.yaml.')
@click.option('--provider', help='Temporarily override the LLM provider.')
def update(path, model, provider):
    """
    Update documentation for a specific file or all files.
    
    PATH: The specific file or directory to update (e.g. 'src/utils.py'). 
    Pass '.' to quickly regenerate the README.md from the existing cache without making new API calls.
    """
    from readmify.components.update import update_docs
    update_docs(path, model=model, provider=provider)

@cli.command()
def models():
    """
    List all available models from the Groq API.
    
    Displays a real-time, aesthetically formatted table of all currently 
    available AI models on the Groq network, sorted alphabetically by Developer.
    """
    from readmify.components.models import list_models
    list_models()