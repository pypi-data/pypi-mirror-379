from setuptools import setup, find_packages

setup(
    name="jupyter-ai-debugger",
    version="0.1.0",
    description="AI-assisted error debugger with OpenRouter model fallback for Jupyter.",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["requests", "ipython"],
)




