import schedule
from plyer import notification
from pyautogui import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import webbrowser

def login(link):
    path = "F:\\driver\\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get(link)
    cookies = driver.find_element_by_id("acceptAllBtn")
    cookies.click()
    search = driver.find_element_by_id("Usrname")
    search.send_keys("*********")
    search = driver.find_element_by_id("Passwd")
    search.send_keys("*********")
    search.send_keys(Keys.RETURN)
    try:
        btn = driver.find_element_by_xpath("//span[@class='_conferBtn float-left']")
        btn.click()
 
        redirected_link()

    except:
        notifyme("ALERT! Error occured with join now button")
    # driver.quit()

def notifyme(reminder):
    notification.notify(
        title="ALERT!",
        message= reminder,
        app_icon="F:\\ALL\\timer.ico",
        timeout=180
    )
    # webbrowser.open("https://g09.tcsion.com/LX/home/show_my_communities?c_id=Sreenidhi-Institute-of-Science-Technology-14490&from=dashboard&current_community_id=Sreenidhi-Institute-of-Science-Technology-14490")


def redirected_link():
    time.sleep(5)
    click(834, 510)
    time.sleep(2)
    write("19311A12K8")
    click(839, 543)
    write(".")
    click(907, 576)
    write("19311a12k8@sreenidhi.edu.in")
    click(859, 739)
    time.sleep(3)
    click(796, 944)
    time.sleep(1)
    click(493, 981)
    time.sleep(1)
    click(287, 975)
    time.sleep(1)
    click(369, 801)
    time.sleep(5)
    click(952, 978)
    time.sleep(5)
    time.sleep(2100)


def M2():
    notifyme("Hey Mr.vishal,join M-II class soon")
    webbrowser.open("https://g09.tcsion.com/LX/home/home_page?c_id=btech-ii-it-d-mathematics-iim-ii-7hc16-588-14490")
    login("https://g09.tcsion.com/LX/home/home_page?c_id=btech-ii-it-d-mathematics-iim-ii-7hc16-588-14490")


def DC():
    notifyme("Hey Mr.vishal,join DC class soon")
    webbrowser.open("https://g09.tcsion.com/LX/home/home_page?c_id=btech-ii-it-d-data-communicationsdc-7cc57-640-14490")
    login("https://g09.tcsion.com/LX/home/home_page?c_id=btech-ii-it-d-data-communicationsdc-7cc57-640-14490")


def DBMS():
    notifyme("Hey Mr.vishal,join DBMS class soon")
    # webbrowser.open(
    #     "https://g09.tcsion.com/LX/home/home_page?c_id=btech-ii-it-d-database-management-systemsdbms-7ec0-339-14490")
    login("https://g09.tcsion.com/LX/home/home_page?c_id=btech-ii-it-d-database-management-systemsdbms-7ec0-339-14490")


def SEANDOOAD():
    notifyme("Hey Mr.vishal,join SE & OOAD class soon")
    # webbrowser.open(
    #     "https://g09.tcsion.com/LX/home/home_page?c_id=btech-ii-it-d-software-engineering-and-ooadseooad-908-14490")
    login("https://g09.tcsion.com/LX/home/home_page?c_id=btech-ii-it-d-software-engineering-and-ooadseooad-908-14490")


def DE():
    notifyme("Hey Mr.vishal,join DE class soon")
    webbrowser.open("https://g09.tcsion.com/LX/home/home_page?c_id=btech-ii-it-d-digital-electronicsde-7cc55-443-14490")
    login("https://g09.tcsion.com/LX/home/home_page?c_id=btech-ii-it-d-digital-electronicsde-7cc55-443-14490")


def CO():
    notifyme("Hey Mr.vishal,join CO class soon")
    webbrowser.open(
        "https://g09.tcsion.com/LX/home/home_page?c_id=btech-ii-it-d-computer-organizationco-7d408-689-14490")
    login("https://g09.tcsion.com/LX/home/home_page?c_id=btech-ii-it-d-computer-organizationco-7d408-689-14490")


def ESE():
    notifyme("Hey Mr.vishal,join ESE class soon")
    webbrowser.open("https://g09.tcsion.com/LX/home/home_page?c_id=btech-ii-it-d-environmental-science-and-ecologyese-794-14490")
    login("https://g09.tcsion.com/LX/home/home_page?c_id=btech-ii-it-d-environmental-science-and-ecologyese-794-14490")


def TS():
    notifyme("ABSENT")
#     webbrowser.open("https://g09.tcsion.com/LX/home/home_page?c_id=btechiiit-d-discrete-mathematics-339-14490")
#     login("https://g09.tcsion.com/LX/home/home_page?c_id=btechiiit-d-discrete-mathematics-339-14490")


# monday
schedule.every().monday.at("09:36").do(CO)
schedule.every().monday.at("10:26").do(M2)
schedule.every().monday.at("11:26").do(DBMS)
schedule.every().monday.at("12:26").do(SEANDOOAD)
schedule.every().monday.at("14:06").do(DBMS)
schedule.every().monday.at("14:56").do(DBMS)  # LAB SECOND REMINDER
# schedule.every().monday.at("15:46").do(DBMS)


# tuesday
schedule.every().tuesday.at("09:36").do(DC)
schedule.every().tuesday.at("10:26").do(SEANDOOAD)
schedule.every().tuesday.at("11:26").do(DE)
schedule.every().tuesday.at("12:26").do(ESE)
schedule.every().tuesday.at("14:06").do(M2)
schedule.every().tuesday.at("14:56").do(CO)
schedule.every().tuesday.at("15:46").do(DBMS)

# wednesday
schedule.every().wednesday.at("09:36").do(ESE)
schedule.every().wednesday.at("10:26").do(CO)
schedule.every().wednesday.at("11:26").do(M2)
schedule.every().wednesday.at("12:26").do(DBMS)
schedule.every().wednesday.at("14:06").do(SEANDOOAD)
schedule.every().wednesday.at("14:56").do(DE)
schedule.every().wednesday.at("15:46").do(DC)

# thursday
schedule.every().thursday.at("09:36").do(DE)
schedule.every().thursday.at("10:26").do(DC)
schedule.every().thursday.at("11:26").do(SEANDOOAD)
schedule.every().thursday.at("12:26").do(DBMS)
schedule.every().thursday.at("14:06").do(SEANDOOAD)
schedule.every().thursday.at("14:56").do(SEANDOOAD)  # lAB SECOND REMINDER
# schedule.every().thursday.at("15:46").do(SEANDOOAD)


# friday
schedule.every().friday.at("09:36").do(M2)
schedule.every().friday.at("10:26").do(CO)
schedule.every().friday.at("11:26").do(DBMS)
schedule.every().friday.at("12:26").do(DE)
schedule.every().friday.at("14:06").do(SEANDOOAD)
schedule.every().friday.at("14:56").do(DC)
schedule.every().friday.at("15:46").do(ESE)

# saturday
schedule.every().saturday.at("09:36").do(DC)
schedule.every().saturday.at("11:00").do(ESE)
schedule.every().saturday.at("11:26").do(CO)
schedule.every().saturday.at("12:26").do(M2)
schedule.every().saturday.at("14:06").do(DE)
schedule.every().saturday.at("14:56").do(TS)
schedule.every().saturday.at("15:46").do(TS)  #TECH SEM SECOND REMAINDER


def fun():
    notifyme("CODE RUNNING IN BACKGROUND")
    while True:
        schedule.run_pending()
        time.sleep(10)

fun()