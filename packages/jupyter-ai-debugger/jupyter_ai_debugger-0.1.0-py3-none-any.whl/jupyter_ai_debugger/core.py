import os
import re
import requests
import traceback
from IPython.display import display, Markdown
from IPython import get_ipython
from .config import DEFAULT_MODELS, OPENROUTER_ENDPOINT

class AIDebugger:
    """
    AI-assisted error debugger for Jupyter notebooks using OpenRouter models with fallback.

    This class hooks into IPython's exception handling system. When an exception occurs in a notebook cell,
    it sends the code and traceback to an AI model (via OpenRouter) to generate an explanation and suggest
    a fix. The suggested code can automatically populate the next cell in the notebook.

    Attributes:
        api_key (str): OpenRouter API key.
        models (list[str]): List of model names in priority order to try.
    """
    def __init__(self, api_key=None, models=None):
        """
        Initialize the AIDebugger.

        Args:
            api_key (str, optional): OpenRouter API key. Defaults to None, in which case
                                     it is read from the environment variable OPENROUTER_API_KEY.
            models (list[str], optional): List of OpenRouter model strings to try in order.
                                          Defaults to DEFAULT_MODELS from config.py.

        Raises:
            ValueError: If no API key is provided and the environment variable is not set.
        """
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY")
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY must be provided or set as environment variable.")
        self.models = models or DEFAULT_MODELS

    def ask_ai_for_fix(self, code, error_trace):
        """
        Send code and traceback to OpenRouter AI and return explanation and suggested fix.

        Args:
            code (str): Python code from the notebook cell that caused an exception.
            error_trace (str): Full traceback string from the exception.

        Returns:
            str: AI response containing explanation and suggested code block. If all models fail,
                 returns an error message with the last exception encountered.
        """
        prompt = f"""
You are a Python expert. The following code produced an error:

```python
{code}
```

Error traceback:

{error_trace}

Instructions:
1. Explain why the error happened.
2. Suggest a fix if possible.
3. ONLY provide corrected Python code in a single ```python``` block.
4. If the code is already correct, just say "No correction needed".
"""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        last_error = None
        for model in self.models:
            payload = {
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0,
            }
            try:
                response = requests.post(OPENROUTER_ENDPOINT, json=payload, headers=headers, timeout=30)
                response.raise_for_status()
                result = response.json()
                return result["choices"][0]["message"]["content"] + f"\n\n*(Model used: {model})*"
            except Exception as e:
                last_error = str(e)
                continue
        return f"AI request failed for all models. Last error: {last_error}"

    def ai_exception_handler(self, shell, etype, evalue, tb, tb_offset=None):
        """
        Custom IPython exception handler that calls AI for debugging suggestions.

        Args:
            shell (InteractiveShell): The current IPython shell instance.
            etype (type): Exception type.
            evalue (Exception): Exception instance.
            tb (traceback): Traceback object.
            tb_offset (int, optional): Traceback offset. Defaults to None.
        """
        tb_str = "".join(traceback.format_exception(etype, evalue, tb))
        try:
            code = shell.user_ns.get("_ih", [""])[-1]
        except Exception:
            code = ""
        ai_response = self.ask_ai_for_fix(code, tb_str)
        display(Markdown("### ⚡ AI Debugging Suggestion"))
        display(Markdown(ai_response))
        match = re.search(r"```python\n(.*?)```", ai_response, re.DOTALL)
        if match:
            corrected_code = match.group(1).strip()
            if corrected_code and corrected_code != code.strip():
                shell.set_next_input(corrected_code, replace=False)

    def activate(self):
        """
        Activate the AI-assisted error debugger in the current Jupyter notebook.

        Raises:
            RuntimeError: If not running inside an IPython/Jupyter environment.
        """
        ip = get_ipython()
        if not ip:
            raise RuntimeError("This debugger can only run inside IPython/Jupyter.")
        ip.set_custom_exc((Exception,), self.ai_exception_handler)
        display(Markdown("**AI-assisted error handling with model fallback is now active!**"))
