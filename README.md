# Readmify

**Turn Codebases Into Clear Documentation.**

Readmify is an AI-powered codebase understanding and documentation assistant. It analyzes repositories, summarizes source files, manages context efficiently, and generates professional README documentation from the command line.

## Problem

Large codebases are difficult to document consistently. Readmify automates repository discovery and converts source files into compact summaries before generating a final project README.

## Key Features

- Repository scanning with `.gitignore` awareness
- File-level source summarization
- Multi-stage context compression
- Persistent `.readmify/cache.json` summaries
- Selective file updates
- Groq model discovery and configuration
- README generation and backup
- CLI configuration through `readmify.yaml`

## Technology Stack

- Python 3.10+
- Click
- Rich
- PyYAML
- python-dotenv
- Groq API
- setuptools

## Architecture

1. `readmify init` scans the repository and writes `readmify.yaml`.
2. The scan identifies the files available for documentation.
3. `readmify generate` extracts file content and splits it into bounded chunks.
4. Each chunk is summarized through the Groq API.
5. Summaries are stored in `.readmify/cache.json`.
6. The final stage combines the summaries and generates `README.md`.

The summaries act as a compact context artefact, reducing repeated exposure to raw source code in later stages. `readmify update` can refresh summaries for one path or the complete configured file set.

## Installation

```powershell
python -m pip install -e .
```

For development:

```powershell
python -m pip install -e ".[dev]"
```

## API Configuration

Readmify uses Groq and reads the API key from `GROQ_API_KEY`.

PowerShell:

```powershell
$env:GROQ_API_KEY="your_groq_api_key"
```

Linux or macOS:

```bash
export GROQ_API_KEY="your_groq_api_key"
```

Alternatively, copy `.env.example` to `.env` and add the key:

```text
GROQ_API_KEY=your_groq_api_key
```

Never commit `.env` or place a real API key in source control.

## CLI Commands

```powershell
readmify --help
readmify init
readmify models
readmify generate
readmify update .
```

`readmify run` remains available as a backward-compatible alias for `readmify generate`.

### Generate documentation

```powershell
readmify generate
readmify generate --model openai/gpt-oss-20b
```

### Update documentation

```powershell
readmify update src/example.py
readmify update .
```

## Configuration

Run `readmify init` to create `readmify.yaml`.

```yaml
project: my-project
structure:
  - src/main.py
  - README.md
llm:
  model: openai/gpt-oss-20b
```

- `project`: project name used for final metadata
- `structure`: files included in documentation generation
- `llm.model`: Groq model ID

Runtime cache and logs are stored in `.readmify/`. This directory is ignored by Git.

## Project Structure

```text
readmify/
  components/       init, generation, update, and model commands
  config/           shared configuration constants
  pipelines/        Click CLI entry point
  prompts/          batch and final README prompts
  resources/        repository ignore resources
  schema/           configuration and response schemas
  utils/            scanning, extraction, caching, logging, and README generation
```

## Testing

Run the existing Python compilation check:

```powershell
python -m compileall -q readmify main.py
```

Install the development dependencies and run the test runner when tests are present:

```powershell
python -m pip install -e ".[dev]"
pytest
```

No API key is required for import or compilation checks. Generation and model discovery require a valid `GROQ_API_KEY`.

## Contributing

1. Fork the repository.
2. Create a focused feature branch.
3. Make and test your changes.
4. Submit a pull request with a clear description of the behavior and verification performed.

## License and Attribution

Readmify is distributed under the GNU Affero General Public License v3.0. The original license remains in [LICENSE](LICENSE).

Readmify is derived from and rebranded from the Doclify project. Legal copyright remains with the respective original and modification authors. The adaptation and rebranding are attributed in [NOTICE](NOTICE).

Repository: https://github.com/Mageshk100/Readmify
