from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="visionclick",
    version="0.1.0",
    author="Kakuzu",
    author_email="kakuzu.aon@gmail.com",
    description="A Python library for GUI automation with visual feedback",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kakuzu-aon/visionclick",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'opencv-python>=4.0.0',
        'pyautogui>=0.9.0',
        'pynput>=1.7.0',
        'Pillow>=8.0.0',
        'numpy>=1.19.0',
        'colorama>=0.4.0',
    ],
    entry_points={
        'console_scripts': [
            'visionclick=visionclick.cli:main',
        ],
    },
)
