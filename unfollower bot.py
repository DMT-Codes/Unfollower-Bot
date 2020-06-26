from selenium import webdriver
from time import sleep
class InstaBot:
    def __init__(self,username,pw):
        self.username=username
        self.pw=pw
        self.driver=webdriver.Chrome("C:\\Users\\Deante\\Downloads\\chromedriver.exe")
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\'username\']")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]") \
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]") \
            .click()
        sleep(4)

    def list_of_names(self):
        sleep(4)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        last_height, current_height = 0, 1
        while last_height != current_height:
            last_height = current_height
            sleep(2)
            current_height = self.driver.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;""", scroll_box)
        name_links = scroll_box.find_elements_by_tag_name('a')
        name_array = [name.text for name in name_links if name.text != '']
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button") \
            .click()
        return name_array

    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username)).click()
        sleep(5)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]") \
            .click()
        following = self.list_of_names()
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]") \
            .click()
        followers = self.list_of_names()
        not_following_back = [names for names in following if names not in followers]
        print(f"\nNumber of people that are not following you back: {len(not_following_back)}")
        print("The users that are not following you back are: ")
        for users in not_following_back:
            print(users)

your_account=InstaBot("username","password")
your_account.get_unfollowers()