from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Chrome(executable_path="./chromedriver.exe")

# Iniciando:
try:
    # Entrar no site do Google
    driver.get("https://google.com.br")

    driver.implicitly_wait(1)
    sleep(1)

    driver.maximize_window()

    # Buscar Youtube
    busca_g = driver.find_element_by_name("q")

    busca_g.send_keys('youtube')
    busca_g.send_keys(Keys.ENTER)

    sleep(2)

    # Entrar no youtube
    div = driver.find_element_by_class_name('yuRUbf')

    tag = div.find_element_by_tag_name('a')

    link = tag.get_attribute('href')
    driver.get(link)

    sleep(3)

    # Buscar a música
    busca_y = driver.find_element_by_name('search_query')

    busca_y.click()
    busca_y.send_keys('living on a prayer - bon jovy')
    busca_y.send_keys(Keys.ENTER)

    sleep(3)

    # Entrar no vídeo
    xpath = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a')

    video = xpath.get_attribute('href')
    driver.get(video)

    # Pular o anúncio se tiver
    try:
        sleep(7)
        pular = driver.find_element_by_id('ad-text:6')
        pular.click()
    except:
        print('\033[1;31mdeu errado\033[m')
        print('\033[1;33mEsperando o anúncio passar...\033[m')
        sleep(20)

    sleep(3)
    
    # Apertar em Agora Não, caso a mensagem apareça
    try:
        botão = driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-mealbar-promo-renderer/div/div[2]/ytd-button-renderer[1]/a/tp-yt-paper-button/yt-formatted-string')
        botão.click()
    except:
        print("\033[1;32mA mensagem não foi exibida.\033[m")

    print("\033[1;32m\nApenas ouça 🎵 !!!\033[m")

    # Tirar a Legenda caso queira
    try:
        sleep(1)
        legenda = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[34]/div[2]/div[2]/button[3]')
        legenda.click()
    except:
        print('\033[1;31mNão foi possível tirar as legendas.\033[m')

    sleep(2)

    # Pegar o título do vídeo
    titulo = driver.find_element_by_xpath(
        '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/h1/yt-formatted-string').text

    print(f'\033[1;32m\nTitulo do Vídeo:\033[m \033[1;34m{titulo}\033[m')

    sleep(241)

    driver.minimize_window()

    print('\033[1;32m\nMuito melhor agora\033[m')
    print("\033[1;32m\nQue Deus te abençoe !!!\033[m")

    driver.close()
except:
    print('\033[1;33\nmO programa foi interrompido pelo usuário.\033[m')
