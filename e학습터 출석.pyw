from selenium import webdriver
import time
import schedule

bs = webdriver.Chrome("chromedriver.exe")


def a():
    bs.get("https://cls1.edunet.net/cyber/cm/mcom/pmco000b00.do")
    bs.find_element_by_xpath('//*[@id="main_cont"]/li[2]/div[1]/a').click()
    bs.find_element_by_id("login_id").send_keys("c0929163")
    bs.find_element_by_id("password").send_keys("chan69ik85!")
    bs.find_element_by_xpath("//*[@id=\"loginForm\"]/fieldset/ul[1]/li[2]/div/label").click()
    bs.find_element_by_class_name("doLogin").click()
    bs.find_element_by_class_name("btn_cancel").click()
    bs.find_element_by_class_name("layPop_closeBtn").click()
    time.sleep(0.5)
    bs.get("https://cls1.edunet.net/bbsBoard/board.do?bbs_innb=520859&bbsctt_innb=5549060&clas_innb=168139")
    bs.find_element_by_class_name("contents_inner").click()
    time.sleep(0.5)
    bs.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    elem = bs.find_element_by_name("answer_cn")
    elem.clear()
    elem.send_keys("출석 했습니다.")
    time.sleep(2)
    bs.find_element_by_xpath("//*[@id=\"BtnNewCmt\"]").click()

schedule.every().day.at("09:00").do(a)
while True:
    schedule.run_pending()
    time.sleep(1)




