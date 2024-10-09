from setuptools import setup, find_packages

setup(
    name="emoji-lang",
    version="0.1",
    packages=find_packages(),  # This will find emoji_lang as a package
    entry_points={
        'console_scripts': [
            'emoji-lang=emoji_lang.cli:run',  # This should use "emoji_lang"
        ],
    },
    install_requires=[],
    description="A funny emoji-based programming language.",
    author="Pranav Kulkarni",
    author_email="your_email@example.com",
    python_requires='>=3.6',
)
