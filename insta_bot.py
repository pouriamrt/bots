from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import autoit
import time

class Bot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\pouria\Python_Crawler\chromedriver')
        
    def login(self):
        self.driver.get('http://instagram.com')
        time.sleep(1)
        try:
            coockie = self.driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN._4Yzd2 > div > div > button.aOOlW.bIiDR')
            coockie.click()
            time.sleep(10)
        except:
            pass
        
        user = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#loginForm > div > div:nth-child(1) > div > label > input')))
        user.click()
        user.send_keys('')
        
        passwd = self.driver.find_element_by_css_selector('#loginForm > div > div:nth-child(2) > div > label > input')
        passwd.click()
        passwd.send_keys('')
        
        login = self.driver.find_element_by_css_selector('#loginForm > div > div.qF0y9.Igw0E.IwRSH.eGOV_.acqo5._4EzTm.bkEs3.CovQj.jKUp7.DhRcB')
        login.click()
        time.sleep(1)
        try:
            not_save_info = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > div > div > div > button')))
            not_save_info.click()
            time.sleep(5)
            
            not_notif = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, '_a9_1')))
            not_notif.click()
            time.sleep(2)
        except:
            pass
        
    def like_by_tags(self, tags, num):
        for tag in tags:
            search = self.driver.find_element_by_class_name('_aaw8')
            search.click()
            search = self.driver.find_element_by_class_name('_aauy')
            search.clear()
            tag = '#' + tag
            search.send_keys(tag)
            time.sleep(4)
            search.send_keys(Keys.ENTER)
            time.sleep(2)
            search.send_keys(Keys.ENTER)
            time.sleep(20)
            
            post = self.driver.find_element_by_class_name('_aagu')
            post.click()
            time.sleep(10)
            
            for _ in range(num):
                like = self.driver.find_element_by_class_name('_abl_')
                like.click()
                time.sleep(2)
                
                next_post = self.driver.find_elements_by_class_name('_aaqh')[-1]
                next_post.click()
                time.sleep(10)
            
            close = self.driver.find_element_by_class_name('mudwbb97')
            close.click()
            time.sleep(1)
            
    def follow_target_followers(self, page_id, num):
        url = f'https://www.instagram.com/{page_id}/'
        
        self.driver.get(url)
        time.sleep(20)
        
        followers_num = self.driver.find_element_by_css_selector('div > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div._a3gq > section > main > div > header > section > ul > li:nth-child(2) > a > div')
        followers_num.click()
        time.sleep(15)
        
        followers = self.driver.find_element_by_css_selector('div > div > div:nth-child(1) > div > div:nth-child(4) > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div > div')
        items = []
        for _ in range(num // 6):
            self.driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", followers)
            time.sleep(3)
            followed_num = len(items)
            items = self.driver.find_elements_by_css_selector('div > div > div:nth-child(1) > div > div:nth-child(4) > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div > div > div > div > div > div._aano > ul > div > li')
            for f in items[followed_num:]:
                follow = f.find_elements_by_css_selector('div > div')[-1]
                follow.click()
                time.sleep(3)
                
    def upload_post(self, address, filename):
        self.driver.get('https://www.instagram.com')
        time.sleep(5)
        
        post = self.driver.find_element_by_css_selector('div > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div._a3gq._ab-1 > section > nav > div._acc1._acc3 > div > div > div._acuq._acur > div > div:nth-child(3) > div > button > div')
        post.click()
        time.sleep(2)

        upload = self.driver.find_element_by_css_selector('div > div > div:nth-child(1) > div > div:nth-child(4) > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div > div > div > div > div > div > div._ac2r > div._ac2t > div > div > div._ab8w._ab94._ab97._ab9f._ab9k._ab9p._abc2 > div > button')
        upload.click()
        time.sleep(1)
        
        autoit.win_wait('Open', 4)
        autoit.mouse_move(349, 50)
        autoit.mouse_click()
        time.sleep(1)
        autoit.win_wait_active('Open', 4)
        autoit.send(address)
        autoit.send('{Enter}')
        time.sleep(1)
        autoit.win_wait_active('Open', 4)
        autoit.control_send('Open', 'Edit1', filename)
        time.sleep(1)
        autoit.win_wait_active('Open', 4)
        autoit.control_click('Open', 'Button1')
        time.sleep(1)
        
        size = self.driver.find_element_by_css_selector('div > div > div:nth-child(1) > div > div:nth-child(4) > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div > div > div > div > div > div > div._ac2r > div._ac2t > div > div > div > div._ab8w._ab94._ab99._ab9f._ab9m._ab9p._abak._abb0._abbi._abb-._abcf._abcg._abch > div > div:nth-child(2) > div > button > div')
        size.click()
        time.sleep(1)
        org_size = self.driver.find_element_by_css_selector('div > div > div:nth-child(1) > div > div:nth-child(4) > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div > div > div > div > div > div > div._ac2r > div._ac2t > div > div > div > div._ab8w._ab94._ab99._ab9f._ab9m._ab9p._abak._abb0._abbi._abb-._abcf._abcg._abch > div > div._ab8w._ab94._ab99._ab9f._ab9m._ab9p._ab9y._aba8 > div > button:nth-child(1) > div')
        org_size.click()
        Next1 = self.driver.find_element_by_css_selector('div > div > div:nth-child(1) > div > div:nth-child(4) > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div > div > div > div > div > div > div._ab8w._ab94._ab99._ab9f._ab9m._ab9p > div > div > div._ac7b._ac7d > div')
        Next1.click()
        time.sleep(2)
        Next2 = self.driver.find_element_by_css_selector('div > div > div:nth-child(1) > div > div:nth-child(4) > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div > div > div > div > div > div > div._ab8w._ab94._ab99._ab9f._ab9m._ab9p > div > div > div._ac7b._ac7d > div')
        Next2.click()
        time.sleep(2)
        share = self.driver.find_element_by_css_selector('div > div > div:nth-child(1) > div > div:nth-child(4) > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div > div > div > div > div > div > div._ab8w._ab94._ab99._ab9f._ab9m._ab9p > div > div > div._ac7b._ac7d > div')
        share.click()
        time.sleep(25)
        
        close = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div > div > div:nth-child(1) > div > div:nth-child(4) > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div.o9tjht9c.jar9mtx6.mbzxb4f5.njoytozt > div > div > svg')))
        close.click()
        time.sleep(1)
        
if __name__ == '__main__':
    bot = Bot()
    bot.login()
    # bot.like_by_tags(['pythonprogramming', 'instagram'], 5)
    # bot.follow_target_followers('selenagomez', 15)
    bot.upload_post('D:/photo', 'windows.jpg')
    
