import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def abrir_home(driver, wait):
    driver.get("https://www.mercadolivre.com.br/")

def aceitar_cookies(driver, wait):
    try:
        cookie_btn = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.cookie-consent-banner-opt-out__action")
        ))
        cookie_btn.click()
        time.sleep(1)
    except:
        pass  # banner não apareceu

def buscar_produto(driver, wait, produto: str):
    campo_busca = wait.until(EC.visibility_of_element_located((By.ID, "cb1-edit")))
    campo_busca.clear()
    campo_busca.send_keys(produto)
    campo_busca.send_keys(Keys.ENTER)
    time.sleep(2)

def ordenar_por_menor_preco(driver, wait):
    botao_ordenar = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.andes-dropdown__trigger"))
    )
    botao_ordenar.click()
    menor_preco = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Menor preço']"))
    )
    menor_preco.click()
    time.sleep(2)

def filtrar_novos(driver, wait):
    filtro = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Novo']"))
    )
    driver.execute_script("arguments[0].click();", filtro)
    time.sleep(2)

def scroll_pagina(driver, vezes=5):
    for i in range(1, vezes+1):
        driver.execute_script(f"window.scrollTo(0, {i*600});")
        time.sleep(0.3)

def pegar_produtos(driver, wait, quantidade=5):
    produtos = []
    titulos = wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "h2.ui-search-item_title, a.poly-component_title")
    ))
    precos = driver.find_elements(By.CSS_SELECTOR, "span.andes-money-amount__fraction")

    for i in range(min(quantidade, len(titulos), len(precos))):
        nome = titulos[i].text.strip()
        try:
            preco = int(precos[i].text.replace(".", "").strip())
        except:
            preco = 0
        produtos.append((nome, preco))
    return produtos
