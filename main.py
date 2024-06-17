from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import random
import string
from fake_useragent import UserAgent


url = 'https://signup.ru.leagueoflegends.com/ru/signup/index'

ua = UserAgent()


def main():
    while True:
        try:
            options = webdriver.ChromeOptions()
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_argument(f"user-agent={ua.chrome}")
            options.add_argument("--headless")
            #    options.add_argument('--disable-application-cache')

            driver = webdriver.Chrome(
            executable_path=f'PATHDRIVER')
            driver.delete_all_cookies()

            random_name = [random.choice(string.ascii_lowercase + string.digits if i != 5 else string.ascii_uppercase)
                           for i
                           in
                           range(10)]
            random_name = ''.join(random_name)

            driver.get(url=url)
            driver.execute_script("window.scrollTo(70, document.body.scrollHeight);")
            time.sleep(1)
            email_input = driver.find_element(By.TYPE, 'text')
            email_input.send_keys(f'{random_name}@mail.ru')
            driver.execute_script("window.scrollTo(70, document.body.scrollHeight);")
            driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/form/div[2]').click()
            driver.execute_script("window.scrollTo(70, document.body.scrollHeight);")
            time.sleep(1)
            driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[1]/form/div[1]/div[2]/select/option[2]').click()
            driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[1]/form/div[1]/div[4]/select/option[37]').click()
            driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[1]/form/div[1]/div[3]/select/option[4]').click()
            driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/form/div[2]/button').click()
            driver.execute_script("window.scrollTo(70, document.body.scrollHeight);")
            time.sleep(2)
            driver.find_element(By.NAME, 'username').send_keys(f'{random_name}')
            driver.find_element(By.NAME, 'password').send_keys(f'{random_name}.123')
            driver.find_element(By.NAME, 'confirm_password').send_keys(f'{random_name}.123')
            driver.execute_script("window.scrollTo(70, document.body.scrollHeight);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/form/div[4]/label').click()
            driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/form/div[6]/button').click()
            driver.execute_script("window.scrollTo(70, document.body.scrollHeight);")
            time.sleep(30)
            info_url = driver.current_url
            if info_url == 'https://signup.ru.leagueoflegends.com/ru/signup/download':
                print('Аккаунт зарегестрирован!')
                with open('PATHGOODTXT', 'a') as f:
                    f.write(f'{random_name}:{random_name}.123\r')
            driver.close()
            driver.quit()

        except Exception as ex:
            print(ex)


if __name__ == '__main__':
    main()
