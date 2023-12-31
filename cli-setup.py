from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name = 'YT_Installer',
    version = '0.0.5',
    author = 'Hans Chaudry',
    author_email = 'hanschaudry@outlook.com',
    license = 'MIT License',
    description = 'CLI tool that allows yu to download a youtube video to a choosen directory',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/HansChaudry/YT_Downloader',
    py_modules = ['CLI', 'app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        yt=CLI:cli
    '''
)