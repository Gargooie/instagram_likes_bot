from time import sleep
class Login:
    def __init__(self,browse):
        self.browse = browse

    def login(self, username, password):
        user_input = self.browse.find_element_by_css_selector("input[name='username']").send_keys(username)
        pass_input = self.browse.find_element_by_css_selector("input[name='password']").send_keys(password)
        #user_input.send_keys(username)
        # pass_input.send_keys(password)
        log_button = self.browse.find_element_by_css_selector("button[type='submit']")
        log_button.click()


    def search_tags(self,tag):
        browse=self.browse
        browse.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        browse.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        browse.get('https://www.instagram.com/explore/tags/' + tag)

    def likey(self,count):
        browse=self.browse
        browse.find_element_by_class_name('v1Nh3').click()
        i=1
        while i <= count:
            sleep(1)
            # browse.find_element_by_class_name('fr66n').click()
            # sleep(1)
            browse.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            i+=1

        browse.get('https://www.instagram.com/')

class Home:
    def __init__(self, browse):
        self.browse = browse
        self.browse.get("https://www.instagram.com/")

    def go_to_login(self):
        return Login(self.browse)
