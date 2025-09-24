from setuptools import setup, find_packages

setup(
    name="brainforge-tokenizer",
    version="1.0.0", 
    author="Mayur Kalekar",
    description="BrainForge custom tokenizer with tiktoken",
    packages=find_packages(),
    install_requires=[
        "tiktoken>=0.5.0"
    ],
    python_requires=">=3.7",
)
