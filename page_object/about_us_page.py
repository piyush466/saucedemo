from selenium.webdriver.common.by import By

from page_object.base_file import Basepage


class About_Us(Basepage):
    HUMBERGER_MENU_ID = (By.ID, "react-burger-menu-btn")
    CLICK_ABOUT_US_MENU = (By.LINK_TEXT, "About")
    CLICK_ON_RESET_APP = (By.PARTIAL_LINK_TEXT, "Reset App State")


    def about_us_page(self):
        self.do_click(self.HUMBERGER_MENU_ID)
        self.do_click(self.CLICK_ABOUT_US_MENU)

    def reset_app_page(self):
        self.do_click(self.HUMBERGER_MENU_ID)
        self.do_click(self.CLICK_ON_RESET_APP)

    def social_media_app(self):
        social_media = self.driver.find_elements(By.XPATH, "//ul[@class='social']/li/a")
        self.lists_of_social_media = ["Twitter", "Facebook", "LinkedIn"]
        self.actual_list = []
        for self.social in social_media:
            # print(social.text)
            self.actual_list.append(self.social.text)
            if self.social.text in self.lists_of_social_media:
                if self.social.is_displayed():
                    print(f"{self.social.text} is visible")
