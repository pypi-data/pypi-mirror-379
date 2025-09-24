from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="sensorylab-smeller",  #  **ИЗМЕНИТЕ НА УНИКАЛЬНОЕ ИМЯ ВАШЕГО ПАКЕТА (например, sensorylab-neuroair-control)**
    version="0.1.81",
    packages=find_packages(exclude=['tests*', 'docs*', 'examples*']),
    install_requires=[
        "future>=1.0.0",
        "iso8601>=2.1.0",
        "pybluez2>=0.46",
        "pyserial>=3.5",
        "PyYAML>=6.0.2",
        
    ],
    extras_require={ # <- Добавляем секцию extras_require для опциональных зависимостей
        'gui':  ["PyQt6", "PyQtGraph"], #  Группа зависимостей 'gui', устанавливается как: pip install smeller[gui]
    },
    python_requires='>=3.10',
    author="SensoryLAB",
    author_email="fox@sensorylab.ru",
    description="Python library for Neuroair device control", # <- Описание остаётся, но README обновим ниже
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://10.10.0.20:3000/SensoryLAB/smeller",  # <- **ОБЯЗАТЕЛЬНО ИЗМЕНИТЕ НА ПУБЛИЧНЫЙ URL ВАШЕГО РЕПОЗИТОРИЯ**
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)