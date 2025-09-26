from setuptools import setup, find_packages

# Lê o conteúdo do requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="processing_image_alquimista",  # <-- IMPORTANTE: Troque por um nome único!
    version="0.0.1",
    author="Michael Costa",
    author_email="sambapunkboto@gmai.com",
    description="Um pacote simples para mesclar duas imagens.",
    long_description="Uma descrição mais longa pode ser adicionada aqui, ou lida de um arquivo README.",
    packages=find_packages(),
    install_requires=requirements,
    keywords=["python", "image processing", "blend", "PIL", "Pillow"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)