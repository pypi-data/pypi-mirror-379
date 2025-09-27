from setuptools import setup, find_packages

setup(
    name="infosecmachines",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,  
    author='Flick',
    long_description=open(file='README.md', encoding='utf-8', mode='r').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/SelfDreamer/Infosecmachines',
    install_requires=[
                      "typeguard",
                      "yt_dlp",
                      "aiohttp",
                      "screeninfo",
                      "requests",
                      ],
)
