from setuptools import setup, find_packages

setup(
    name="JarvisSTT-ItsArsh",
    version="0.2",
    author="ItsArsh",
    author_email="noamarsh2010@gmail.com",
    description="This is a speech to text package",
    install_requires=["selenium", "webdriver-manager"],
    packages=find_packages(),
)