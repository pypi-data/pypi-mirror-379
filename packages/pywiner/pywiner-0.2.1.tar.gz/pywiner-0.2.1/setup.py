from setuptools import setup, find_packages

setup(
    name="pywiner",
    version="0.2.1",
    author="GuestRoblox Studios",
    author_email="maria.gomes23.1949@gmail.com",
    description="A Python library for Windows automation and a native window framework.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/RoVerify/pywiner",
    packages=find_packages(),
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.6',
    install_requires=[
        'PyQt6',
        'Pillow'
    ],
)