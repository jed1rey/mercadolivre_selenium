from driver_setup import create_driver
from mercadolivre_bot import (
    abrir_home, aceitar_cookies, buscar_produto,
    ordenar_por_menor_preco, filtrar_novos,
    scroll_pagina, pegar_produtos
)

def main():
    driver, wait = create_driver(headless=False)
    try:
        abrir_home(driver, wait)
        aceitar_cookies(driver, wait)

        # Primeira busca
        buscar_produto(driver, wait, "processador AMD")
        ordenar_por_menor_preco(driver, wait)
        filtrar_novos(driver, wait)
        scroll_pagina(driver, 8)
        produtos = pegar_produtos(driver, wait, 5)

        print("\n✔ Produtos capturados:")
        for nome, preco in produtos:
            print("-", nome, "-> R$", preco)

        # Validação simples de ordenação
        precos = [p[1] for p in produtos]
        if len(precos) >= 2:
            for i in range(len(precos)-1):
                assert precos[i] <= precos[i+1], f"Preço fora de ordem: {precos[i]} > {precos[i+1]}"
            print("\n✔ Preços validados em ordem crescente!")

        print("\n✔ Teste concluído com sucesso!")

    finally:
        input("Pressione ENTER para fechar o navegador...")
        driver.quit()

if __name__ == "__main__":
    main()
