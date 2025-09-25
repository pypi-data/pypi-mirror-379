# jupyter_ai_debugger

AI-assisted error debugger for Jupyter notebooks using OpenRouter with automatic model fallback.

## Features
- Hooks into Jupyter/IPython exceptions
- Sends error + code to OpenRouter AI
- Returns explanation and corrected code
- Auto-suggests corrected code into next cell

## Installation
```bash
pip install jupyter-ai-debugger
```

## Usage
Set your API key as an environment variable:
```bash
export OPENROUTER_API_KEY="your_key_here"
```

Or pass it directly in Python:
```python
from jupyter_ai_debugger import AIDebugger
AIDebugger(api_key="your_key").activate()
```

Now any error in Jupyter will trigger AI debugging suggestions!

## License
MIT
