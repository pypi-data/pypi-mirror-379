from setuptools import setup, find_packages

setup(
    name="brainforge-tokenizer",
    version="1.0.1",  # 🔥 NEW VERSION
    author="Mayur Kalekar",
    description="BrainForge custom tokenizer with tiktoken",
    packages=find_packages(),
    package_data={
        'brainforge_tokenizer': ['vocab.json'],  # 🔥 INCLUDE VOCAB FILE
    },
    include_package_data=True,
    install_requires=[
        "tiktoken>=0.5.0"
    ],
    python_requires=">=3.7",
)
