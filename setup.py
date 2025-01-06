import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

__version__ = "0.0.0"

REPO_NAME = "text-summaries"
AUTHOR_USER_NAME = "Venkatesh Munaga"
SRC_REPO = "text_summarizer"
AUTHOR_EMAIL = ""

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A package to summarize text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/venkatesh171/{REPO_NAME}",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)