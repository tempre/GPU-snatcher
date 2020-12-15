from config import botCfg
import random
from selenium import webdriver
from time import sleep
import selenium

um = botCfg['USERNAME'];
pw = botCfg['PASSWORD'];
desired_cards = botCfg['desired_cards'];

class NewEggBot():

    def __init__(self):
        self.browser = webdriver.Chrome();

    def startNewEgg(self, um, pw):

        print("Bot Started");

        sleep(random.uniform(1.1, 5.35));
        self.browser.get('https://secure.newegg.com/NewMyAccount/AccountLogin.aspx?nextpage=https%3A%2F%2Fwww.newegg.com%2F');
        sleep(random.uniform(1, 4));

        if(len(self.browser.find_elements_by_xpath("//div[@class='page-content page-404']")) > 0):
            print("Please run a vpn and relauch..");
            self.browser.close();
            return;

        print("Checking for popups...");
        sleep(4);
        if(len(self.browser.find_elements_by_xpath('//div[@id=\"popup\"]')) > 0):
            self.browser.find_element_by_xpath('//a[@id=\"popup-close\"]').click();
            sleep(3);

        sleep(5);
        if(len(self.browser.find_elements_by_xpath('//div[@class=\"centerPopup-420-content\"]')) > 0):
            self.browser.find_element_by_xpath('//div[@class=\"centerPopup-420-content\"]').click();
            sleep(2);

        self.browser.find_element_by_xpath('//a[@class=\"nav-complex-inner\"]').click();

        self.browser.find_element_by_xpath('//input[@name=\"signEmail\"]').send_keys(um);
        sleep(2);
        self.browser.find_element_by_name("signIn").click();
        sleep(random.uniform(1, 4));
        self.browser.find_element_by_xpath('//input[@name=\"password\"]').send_keys(pw);
        sleep(2);
        self.browser.find_element_by_name("signIn").click();
        sleep(2);

        print("Succefully signed in!\n");

        self.browser.find_element_by_xpath('//div[@class="nav-complex"]').click();

        count = 0;
        while(count <= len(desired_cards)):
            if(count == len(desired_cards)):
                count = 0;

            if(len(self.browser.find_elements_by_xpath("//div[@class='page-content page-404']")) > 0):
                raise Exception("Automation Detected");
            else:
                self.browser.get("https://www.newegg.com/p/pl?d=RTX%20" + desired_cards[count] + "&N=8000%20100006662%204814");
                print("Checking for " + desired_cards[count]);

                total_height = int(self.browser.execute_script("return document.body.scrollHeight"));
                for i in range(1, total_height, 15):
                    self.browser.execute_script("window.scrollTo(0, {});".format(i));
                    if(len(self.browser.find_elements_by_xpath('//button[@class="btn btn-primary btn-mini"]')) > 0):
                        break;

                if(len(self.browser.find_elements_by_xpath('//button[@class="btn btn-primary btn-mini"]')) > 0):
                    if(botCfg['auto_cart']):
                        self.browser.find_element_by_xpath("//button[@class='btn btn-primary btn-mini']").click();
                        print("Added " + desired_cards[count] + " To Cart!");
                        sleep(0.95);
                        self.browser.find_element_by_xpath("//button[@class='btn btn-undefined btn-primary']").click();

                        if(len(self.browser.find_elements_by_xpath('//button[@class="close"]')) > 0):
                            self.browser.find_elements_by_xpath('//button[@class="close"]').close();

                        break;
                    else:
                        print("Please continue if desired");
                else:
                    print("Out of Stock, checking next....\n");
                    sleep(random.uniform(5, 10));
                count += 1;



bot = NewEggBot();
bot.startNewEgg(um, pw);
