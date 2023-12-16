from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class AdvSearch:

    # Constructor
    def __init__(self, web_url):
        self.url = web_url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 30)
        self.act = ActionChains(self.driver)

    # Search function with multiple selectors, each field and button names are mentioned
    def key_search(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        signin = self.wait.until(EC.presence_of_element_located((By.XPATH, '//button[@title="Close"]')))
        signin.click()
        # used for loop multiple place to move the screen accordingly
        for _ in range(9):
            self.act.send_keys(Keys.DOWN).perform()
        expand_all = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@data-testid="adv-search-expand-all"]')))
        expand_all.click()
        # Title name
        title_name = self.wait.until(EC.presence_of_element_located((By.ID, "text-input__7")))
        title_name.send_keys("Uttam Kumar")
        # Birth date from
        bd_from = self.wait.until(EC.presence_of_element_located((By.ID, "text-input__8")))
        bd_from.send_keys("01-01-1920")
        # Birth date to
        bd_to = self.wait.until(EC.presence_of_element_located((By.ID, "text-input__9")))
        bd_to.send_keys("31-12-1927")
        for _ in range(9):
            self.act.send_keys(Keys.DOWN).perform()
        # Birth month and date
        b_m_d = self.wait.until(EC.presence_of_element_located((By.NAME, "birthday-input")))
        b_m_d.send_keys("09-03")
        # Awards and recognition
        actor_nominee = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid*="oscar_best_actor_nominees"]')))
        actor_nominee.click()
        sup_actor_nominee = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid*="oscar_best_supporting_actor_nominees"]')))
        sup_actor_nominee.click()
        oscar_winner = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid*="oscar_winner"]')))
        oscar_winner.click()
        for _ in range(9):
            self.act.send_keys(Keys.DOWN).perform()
        # Page topics
        award_nomination = self.wait.until(EC.presence_of_element_located((By.XPATH, '//button[contains(@data-testid,"AWARD_NOMINATIONS")]')))
        award_nomination.click()
        trivia = self.wait.until(EC.presence_of_element_located((By.XPATH, '//button[contains(@data-testid,"TRIVIA")]')))
        trivia.click()
        for _ in range(9):
            self.act.send_keys(Keys.DOWN).perform()
        # Topic dropdown
        t_dd = self.wait.until(EC.presence_of_element_located((By.XPATH, '//select[contains(@id,"topic-dropdown-id")]/option[6]')))
        t_dd.click()
        # example input box
        eg = self.wait.until(EC.presence_of_element_located((By.XPATH, '//input[contains(@id,"input__11")]')))
        eg.send_keys("Greatest Actor")
        # death date from
        dd_from = self.wait.until(EC.presence_of_element_located((By.NAME, "death-date-start-input")))
        dd_from.send_keys("01-01-1980")
        dd_to = self.wait.until(EC.presence_of_element_located((By.NAME, "death-date-end-input")))
        dd_to.send_keys("31-12-1980")
        for _ in range(5):
            self.act.send_keys(Keys.DOWN).perform()
        # gender
        male = self.wait.until(EC.presence_of_element_located((By.XPATH, '//button[contains(@data-testid,"-MALE")]')))
        male.click()
        # credits
        credit = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid*="filmography"]')))
        credit.send_keys("awesome")
        for _ in range(5):
            self.act.send_keys(Keys.DOWN).perform()
        # Adult name
        include = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="include-adult-names"]')))
        include.click()
        # result
        see_res = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="adv-search-get-results"]')))
        see_res.click()


url = "https://www.imdb.com/search/name/"
# object for the class is created
s = AdvSearch(url)
# called the method via object
s.key_search()


