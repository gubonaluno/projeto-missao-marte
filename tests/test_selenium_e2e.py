import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1280,800")

    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    browser.quit()


def test_solicitacao_cota_oxigenio_painel_web(driver):
    caminho_html = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "web", "painel.html")
    )
    driver.get(f"file://{caminho_html}")

    try:
        campo_qtd = driver.find_element(By.ID, "qtd-oxigenio")
        btn_solicitar = driver.find_element(By.ID, "btn-solicitar")

        campo_qtd.clear()
        campo_qtd.send_keys("250")
        btn_solicitar.click()

        # Espera explícita (proibido usar time.sleep)
        wait = WebDriverWait(driver, 5)
        wait.until(
            EC.text_to_be_present_in_element(
                (By.ID, "mensagem-status"), "Solicitação aprovada!"
            )
        )

        nivel_atualizado = driver.find_element(By.ID, "nivel-oxigenio").text
        assert nivel_atualizado == "750"

    except Exception:
        driver.save_screenshot("evidencia_falha_painel.png")
        raise