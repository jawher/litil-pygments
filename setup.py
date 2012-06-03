from setuptools import setup, find_packages

setup(
    name = "Litil Lexer",
    version = "0.1",
    packages = find_packages(),
    install_requires = ['Pygments>=1.4'],
    author = "Jawher",
    author_email = "me@example.com",
    description = "Pygments's lexer for the Litil Language",
    license = "MIT",
    keywords = "pygments lexer litil",
    url = "https://github.com/jawher/litil-pygments",
    entry_points="""
    [pygments.lexers]
    litil = litil:LitilLexer
    """
)
