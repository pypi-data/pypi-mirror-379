# Image Blender Utilities

![PyPI](https://img.shields.io/pypi/v/<NOME-DO-PACOTE-NO-PYPI>)

Um pacote Python simples, porém poderoso, para realizar operações de processamento de imagem, com foco inicial na mesclagem (blending) de imagens.

## ✨ Features

* Mescla duas imagens com um fator de transparência (alpha) customizável.
* Lida automaticamente com imagens de tamanhos diferentes antes da mesclagem.
* Simples e fácil de usar.

## ⚙️ Requisitos

* Python 3.6+
* Pillow

## 📦 Instalação

Quando o pacote estiver no PyPI, você poderá instalá-lo facilmente com `pip`:

```bash
pip install <NOME-DO-PACOTE-NO-PYPI>
```

## 🚀 Como Usar

Aqui está um exemplo rápido de como importar e usar a função `blend_images`:

```python
# Importe a função do pacote
from image_processing.processing import blend_images

# Defina os caminhos para as suas imagens
imagem_base = "caminho/para/sua/imagem1.jpg"
imagem_sobreposicao = "caminho/para/sua/imagem2.png"

# Chame a função para mesclar as imagens
# O resultado será salvo como "imagem1_blended.png"
blend_images(imagem_base, imagem_sobreposicao, alpha=0.6)
```
**Atenção:** Certifique-se de que os arquivos de imagem realmente existem nos caminhos especificados.

## 📄 Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.