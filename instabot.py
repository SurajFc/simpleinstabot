from selenium import webdriver
from time import sleep
from webdriver_manager.firefox import GeckoDriverManager as fox
from webdriver_manager.chrome import ChromeDriverManager as chrome


class InstaBot:

    def __init__(self, username, password, pagename, d=None):
        if d == 1:
            self.driver = webdriver.Chrome(
                executable_path=chrome().install())
        else:
            self.driver = webdriver.Firefox(
                executable_path=fox().install())

        self.instalogin(username, password)
        print("Login Done")
        self.latestpostlike(pagename)
        print("latest post liked")

    def instalogin(self, username, password):
        self.driver.get("https://www.instagram.com/?hl=en")
        sleep(2)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").send_keys(username)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").send_keys(password)
        sleep(2)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]").click()
        sleep(5)

    def latestpostlike(self, pagename):
        self.driver.find_element_by_xpath(
            "//button[contains(text(), 'Not Now')]").click()
        sleep(2)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(pagename)
        sleep(2)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div").click()
        sleep(3)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]").click()
        sleep(2)
        self.driver.find_element_by_xpath(
            "/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button").click()


if __name__ == "__main__":
    print("Welcome To Simple Insta Bot")
    username = input("Enter the Instagram Username: ")
    password = input("Enter the Instagram Password: ")
    page = input("Enter the Page Name you want to like the latest post: ")
    s = int(input("Choose \n 1.Chrome \n 2. Firefox \n"))
    print("started")
    x = InstaBot(username, password, page, s)
    print("Done")
