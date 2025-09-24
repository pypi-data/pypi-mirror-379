# -*- coding: utf-8 -*-
"""
#=========================================================
목적 : selenium Firefox 브라우저 동작 정의
* headless
* 쿠키
* 프록시
* 익스텐션 설치

1 - To find the current Profile Folder, type about:support on the url field and press enter.
2 - To see all user profiles type about:profiles on the url field and press enter.

* 커스텀 profile 생성
about:profiles -> create new profile 이용하여 프로파일을 생성 후 할당한다.

* 문제점
- 구글로그인에 문제가 있음. "This browser or app may not be secure" 
navigatar.webdriver = False 설정이 필요하나, 현재는 방법을 못찾음.
Firefox 다운그레이드가 필요할 듯
#=========================================================
"""
import os, sys
from datetime import datetime
from time import sleep, time
from random import uniform, randint

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from webdriver_manager.firefox import GeckoDriverManager

import shutil
import pickle

import logging
from . import basicBrowser

import subprocess

## 로거 설정
log = logging.getLogger('TEST')
log.debug("Logging Started... {}".format(__name__))


TYPING_SPEED = 0.1 # 0.1 의 경우 적합

class BaseFirefox(basicBrowser.BasicBrowser):

    def __init__(self, config):

        self.driver     = None
        self.headless   = config['headless']
        self.user_agent = None
        self.profile    = config['profile']
        self.extension  = config['extension']
        try:
            self.firefox_arm64 = config['firefox_arm64']
        except KeyError:
            self.firefox_arm64 = None
        if 'proxy' in config:
            self.proxy = config['proxy']
        else:
            self.proxy = ''

        self.setUpOptions()

        #self.setUpProfile()
        #self.setUpCapabilities()
        # self.setUpProxy() # comment this line for ignore proxy

        # On Linux?
        # https://github.com/mozilla/geckodriver/issues/1756
        # binary = FirefoxBinary('/usr/lib/firefox-esr/firefox-esr')
        #self.driver = webdriver.Firefox(options=self.options, capabilities=self.capabilities, firefox_profile=self.profile, executable_path='./geckodriver.exe', firefox_binary=binary)
        #self.driver = webdriver.Firefox(options=self.options, capabilities=self.capabilities, firefox_profile=self.profile, executable_path='../geckodriver.exe')
        #self.driver = webdriver.Firefox(options=self.options, capabilities=self.capabilities, executable_path='geckodriver.exe', service_log_path=os.devnull)
        
    

    def get_driver(self):
        """웹드라이버 설정"""

        # 가상 디스플레이 사용 코드 추가
        #self.display = Display(visible=0, size=(1920, 1080))
        #self.display.start()
        # log_output=subprocess.STDOUT, log_output='browser.log'
        # log_output=subprocess.STDOUT, service_args=['--log', 'error']

        if os.name == 'nt':
          service = Service(executable_path=(GeckoDriverManager().install()))
          #options = webdriver.FirefoxOptions(options=self.options)
          self.driver = webdriver.Firefox(service=service, options=self.options)
          #self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        else:
          # Window Driver Location: C:\Users\[Username]\.wdm\drivers\geckodriver
          # Linux Location: ~/.wdm/drivers/geckodriver
          if self.firefox_arm64:
            service = Service(self.firefox_arm64)
            self.driver = webdriver.Firefox(service=service, options=self.options)
          else:             
            service = Service(GeckoDriverManager().install())
            self.driver = webdriver.Firefox(service=service, options=self.options)

        # selenium 4용
        if self.extension:
            #self.driver.install_addon(r'/home/ubuntu/extension/browser@tunnelbear.com.xpi')
            self.driver.install_addon(self.extension)

        return self.driver
  

    # Setup options for webdriver
    def setUpOptions(self):
        
        self.options = FirefoxOptions()

        self.options.add_argument("--no-sandbox"); # Bypass OS security model
        self.options.add_argument("--disable-gpu"); # applicable to windows os only
        self.options.add_argument('--disable-blink-features=AutomationControlled') # 구글 로그인 에러 해결
        #self.options.add_argument("--disable-web-security")
        #self.options.add_argument("--allow-running-insecure-content")
        #self.options.add_argument("--ignore-certificate-errors")
                
        if self.headless:
            self.options.add_argument("--headless")

        if self.user_agent:
            self.options.add_argument('user-agent={0}'.format(self.user_agent))

        if self.profile:
            #self.options.add_argument("-profile")
            #self.options.add_argument(self.profile)
            # selenium 4
            #self.options.profile = self.profile
            #self.options.set_profile(self.profile)
            #self.options.set_preference('profile', self.profile)
            #firefox_options = Options()
            self.options.add_argument(f"-profile={self.profile}")
        
        if self.proxy:            
            self.options.add_argument('--proxy-server={}'.format(self.proxy))

            # self.options.set_preference('network.proxy.type', 1)
            # self.options.set_preference('network.proxy.socks', proxy[0])
            # self.options.set_preference('network.proxy.socks_port', proxy[1])
            # self.options.set_preference('network.proxy.socks_remote_dns', True)

        if self.extension:
            # selenium 3에서만 동작  
            #self.options.add_extension(r'/home/ubuntu/extension/browser@tunnelbear.com.xpi')
            #self.driver.install_addon(self.extension)
            log.debug(f"loaded extension...")
        


    # Setup profile with buster captcha solver
    # profile을 설정하는 경우, new tab이 new window로 열림. 해결책은 아직 못 찾음.
    def setUpProfile(self):
        self.profile = webdriver.FirefoxProfile()
        #self.profile._install_extension("buster_captcha_solver_for_humans-0.7.2-an+fx.xpi", unpack=False)
        self.profile.set_preference("security.fileuri.strict_origin_policy", False)
        self.profile.set_preference("dom.webdriver.enabled", False) # navigator.webdriver = undefined 변경
        self.profile.set_preference('useAutomationExtension', False)
        #user-agent 변경
        self.profile.set_preference("general.useragent.override", 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0')
        self.profile.set_preference("intl.accept_languages", "en-US,en;q=0.8;q=0.3")
        self.profile.update_preferences()


    # Enable Marionette, An automation driver for Mozilla's Gecko engine
    def setUpCapabilities(self):
        self.capabilities = webdriver.DesiredCapabilities.FIREFOX
        self.capabilities['marionette'] = True

    # Setup proxy
    def setUpProxy(self):
        self.log(PROXY)
        self.capabilities['proxy'] = {
            "proxyType": "MANUAL",
            "httpProxy": PROXY,
            "ftpProxy": PROXY,
            "sslProxy": PROXY
        }

    # Simple logging method
    def log(s,t=None):
        now = datetime.now()
        if t == None :
            t = "Main"
        print ("%s :: %s -> %s " % (str(now), t, s))

    # Use time.sleep for waiting and uniform for randomizing
    def wait_between(self, a, b):
        rand=uniform(a, b)
        sleep(rand)


    def dump_cookie(self, filename):

        pickle.dump(self.driver.get_cookies(), open("cookies.pkl", "wb"))


    def load_cookie(self, filename):

        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)


    def run(self, url):

        service = Service(executable_path="./geckodriver.exe")

        self.driver = webdriver.Firefox(service=service, options=self.options)
        #self.driver = webdriver.Firefox(service=service, firefox_profile=self.profile)

        driver = self.driver
        driver.set_window_position(0, 0)
        driver.set_window_size(1180, 800)

        print('{} \n'.format(dir(driver)))
        print(driver.capabilities)

        browserDir = driver.capabilities['moz:profile']
        cookieFile = os.path.join(browserDir, 'cookies.sqlite')
        shutil.copy2(cookieFile, 'newname.ext')

        driver.get(url)

        self.dump_cookie('cookie.txt')

        # get window position
        print(driver.get_window_rect())


if __name__ == "__main__":

    driver = baseFirefox(headless=False, profile=r'G:\PyExample\ebay_rank\profile\nlu6zntz.zzzzz')

    url = 'https://www.google.com/'
    driver.run(url)