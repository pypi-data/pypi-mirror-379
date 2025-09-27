from setuptools import setup, find_packages

setup(
    name='tarz',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4"
    ],
    author='Tahagaga',
    description='TArz is a Python package designed for tracking real-time cryptocurrency prices and gold prices from trusted sources. Whether you are a crypto enthusiast or just need the latest price of gold, TArz offers an easy-to-use interface for fetching live prices. With TArz, you can access a wide range of cryptocurrencies and gold prices directly within your Python applications.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    keywords="crypto, bitcoin, gold, finance, python"
)
