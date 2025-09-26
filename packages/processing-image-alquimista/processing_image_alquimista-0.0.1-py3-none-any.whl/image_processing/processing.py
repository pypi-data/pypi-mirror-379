# Importa a biblioteca de manipulação de imagens Pillow
from PIL import Image
import os.path

def blend_images(image_path1: str, image_path2: str, alpha: float = 0.5):
    """
    Mescla duas imagens usando um fator de alpha blending.

    Args:
        image_path1 (str): O caminho para a primeira imagem (base).
        image_path2 (str): O caminho para a segunda imagem (sobreposição).
        alpha (float): O fator de mistura. 0.0 resulta na primeira imagem,
                       1.0 resulta na segunda. O padrão é 0.5.
    """
    # Verifica se os caminhos dos arquivos existem
    if not os.path.exists(image_path1):
        print(f"Erro: O arquivo '{image_path1}' não foi encontrado.")
        return
    if not os.path.exists(image_path2):
        print(f"Erro: O arquivo '{image_path2}' não foi encontrado.")
        return

    try:
        # Abre as duas imagens
        img1 = Image.open(image_path1).convert("RGBA")
        img2 = Image.open(image_path2).convert("RGBA")

        # Garante que as imagens tenham o mesmo tamanho para a mesclagem
        # Redimensiona a segunda imagem para o tamanho da primeira, se necessário
        if img1.size != img2.size:
            print("Aviso: As imagens têm tamanhos diferentes. Redimensionando a segunda imagem para combinar com a primeira.")
            img2 = img2.resize(img1.size)

        # Mescla as imagens usando o alpha
        blended_image = Image.blend(img1, img2, alpha=alpha)

        # Cria um novo nome para o arquivo salvo
        path1, _ = os.path.splitext(image_path1)
        new_image_path = f"{path1}_blended.png"

        # Salva a nova imagem mesclada
        blended_image.save(new_image_path)

        print(f"Imagens mescladas com sucesso! Salva em: {new_image_path}")

    except Exception as e:
        print(f"Ocorreu um erro ao processar as imagens: {e}")