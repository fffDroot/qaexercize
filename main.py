from selenium import webdriver
from selenium.webdriver.common.by import By


class Calc:
    def search(self):
        self.driver = webdriver.Chrome()
        s = "Калькулятор"
        self.driver.get("https://google.co.in/search?q=" + s)

    def use(self):
        element = self.driver.find_element(By.XPATH,
                                           '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[1]/div/div')
        self.driver.execute_script("arguments[0].click();", element)  # 1

        element = self.driver.find_element(By.XPATH,
                                           '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[3]/td[4]/div/div')
        self.driver.execute_script("arguments[0].click();", element)  # *

        element = self.driver.find_element(By.XPATH,
                                           '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[2]/div/div')
        self.driver.execute_script("arguments[0].click();", element)  # 2

        element = self.driver.find_element(By.XPATH,
                                           '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[4]/div/div')
        self.driver.execute_script("arguments[0].click();", element)  # -

        element = self.driver.find_element(By.XPATH,
                                           '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[3]/div/div')
        self.driver.execute_script("arguments[0].click();", element)  # 3

        element = self.driver.find_element(By.XPATH,
                                           '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[5]/td[4]/div/div')
        self.driver.execute_script("arguments[0].click();", element)  # +

        element = self.driver.find_element(By.XPATH,
                                           '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[1]/div/div')
        self.driver.execute_script("arguments[0].click();", element)  # 1

        element = self.driver.find_element(By.XPATH,
                                           '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[5]/td[3]/div/div')
        self.driver.execute_script("arguments[0].click();", element)  # =

    def close(self):
        self.driver.close()

    def getstor(self):
        element = self.driver.find_element(By.XPATH, '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div[1]/div/span')
        return element.text[0:-2]

    def getres(self):
        element = self.driver.find_element(By.XPATH, '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div/span')
        return element.text

def opencalc():
    test = Calc()
    test.search()
    test.use()
    gs = test.getstor()
    gr = test.getres()
    test.close()
    sp = [gs, gr]
    return sp
