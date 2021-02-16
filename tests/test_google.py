from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage


def test_google(chrome_browser):
    main_page = MainPage(driver=chrome_browser)

    # Open page url
    main_page.go()

    #
    main_page.search_input.input_text("aws")

    #
    main_page.search_button.click()

    # TEST -> That logo button is visible
    assert EC.invisibility_of_element(main_page.logo_button)
