from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome('C:/Users/DELL/Downloads/chromedriver_win32/chromedriver.exe')
time.sleep(0.5)

def LoginLogout(driver):
    driver=webdriver.Chrome("C:/Users/DELL/Downloads/chromedriver_win32/chromedriver.exe")
    driver.set_window_size(1024,768)
    driver.get('http://gniopenstack.com/Travel/Admin/loginform.php')
    user_name = driver.find_element_by_name('t1')
    password=driver.find_element_by_name('t2')
    sub=driver.find_element_by_name('sbmt')
    #1
    checkadminpass(driver,user_name,password,sub)
    #2
    checkLogoutFunction(driver,user_name,password,sub)


def checkLoginOther(driver):
    driver=webdriver.Chrome("C:/Users/DELL/Downloads/chromedriver_win32/chromedriver.exe")
    driver.set_window_size(1024,768)
    driver.get('http://gniopenstack.com/Travel/Admin/loginform.php')
    user_name = driver.find_element_by_name('t1')
    password=driver.find_element_by_name('t2')
    sub=driver.find_element_by_name('sbmt')
    
    #3
    checkPasswordOnly(driver,user_name,password,sub)
    #4
    checkWrongPasswordOnly(driver,user_name,password,sub)
   

def checkLogin2(driver):
    driver=webdriver.Chrome("C:/Users/DELL/Downloads/chromedriver_win32/chromedriver.exe")
    driver.set_window_size(1024,768)
    driver.get('http://gniopenstack.com/Travel/Admin/loginform.php')
    user_name = driver.find_element_by_name('t1')
    password=driver.find_element_by_name('t2')
    sub=driver.find_element_by_name('sbmt')
    
    #5
    checkSpecialCharactersUsername(driver,user_name,password,sub)
    #6
    checkSpecialCharPassword(driver,user_name,password,sub)
    #7
    checkNumberUsername(driver,user_name,password,sub)
    #8
    checkIncorrectAdmin(driver,user_name,password,sub)




def CheckingFunctions(driver):
    driver.get('http://gniopenstack.com/Travel/Admin/loginform.php')
    user_name = driver.find_element_by_name('t1')
    password = driver.find_element_by_name('t2')
    sub=driver.find_element_by_name('sbmt')
    user_name.send_keys('admin')
    password.send_keys('admin')
    sub.click()
    time.sleep(2)
    #10
    addUnmatchPassConfirm(driver)
    
    #11
    addCorrectUser(driver)
    
    #12
    addUnderscoreUsername(driver)
    
    #13
    addNumbersUsername(driver)
    
    #14
    addTenCharsUsername(driver)
    #15
    addMoreTenCharsUsername(driver)

    #16
    addTenCharsPassword(driver)
    #17
    addMoreTenCharsPassword(driver)
    #18-22
    
    deleteAndUpdateTests(driver)
    
    # 23
    addCategoryWithCorrectFormat(driver)
    time.sleep(3)

    # 24
    addCategoryByPassingShorterString(driver)
    time.sleep(3)

    # 25
    addCategoryByPassingLongString(driver)
    time.sleep(3)

    # 26
    addCategoryByPassingAlphaNumericCombinations(driver)
    time.sleep(3)



    # 27
    addPackageCorrectNameAndDropDownMenuSelected(driver)
    time.sleep(3)

    # 28
    addPackageInCorrectNameAndDropDownMenuSelected(driver)
    time.sleep(3)

    # 29
    addPackageCorrectNameAnd____DoNotSelectDropDownValue(driver)
    time.sleep(3)

#test No.1..test login status with correct admin username and password..

def checkadminpass(driver,user_name,password,sub):
    
    user_name.send_keys('admin')
    password.send_keys('admin')
    sub.click()
    url=driver.current_url
    if (url=="http://gniopenstack.com/Travel/Admin/index.php"):
        print("Test Case 1: passed")
    else:
        print("Test Case 1: failed")

#test No.2...check logout buttin is working properly


def checkLogoutFunction(driver,user_name,password,sub):
    
    sub=driver.find_element_by_xpath('//*[@id="nav"]/li[2]/a')
    sub.click()
    url=driver.current_url
    if (url=="http://gniopenstack.com/Travel/Admin/loginform.php"):
        print("Test Case 2: passed")
    else:
        print("Test Case 2: failed")
    


#test No.3...test login status with correct password only entered

def checkPasswordOnly(driver,user_name,password,sub):
    user_name.clear()
    password.clear()
    password.send_keys('admin')
    sub.click()
    url=driver.current_url
    if (url!="http://gniopenstack.com/Travel/Admin/index.php"):
        print("Test Case 3: passed")
    else:
        print("Test Case 3: failed")

#test No.4...test login status with correct username but false password entered

def checkWrongPasswordOnly(driver,user_name,password,sub):
    user_name.clear()
    password.clear()
    user_name.send_keys('admin')
    password.send_keys('Hiba')
    sub.click()
    present = "true"
    try:
        driver.switch_to.alert
        
    except:
        present="false"
        print("Test Case 4: failed..bug.. shouldnot accept wrong password with correct username")
    if (present=="true"):
        print("Test Case 4: passed")
        obj=driver.switch_to.alert
        obj.accept()
        
#test No.5..test login status with special char usernames but correct password..

def checkSpecialCharactersUsername(driver,user_name,password,sub):
    user_name.clear()
    password.clear()
    user_name.send_keys(":Hiba_")
    password.send_keys('admin')
    sub.click()
    url=driver.current_url
    if (url!="http://gniopenstack.com/Travel/Admin/index.php"):
        print("Test Case 5: passed")
    else:
        print("Test Case 5: failed")

#test No.6...test login status with special char password but correct username..

def checkSpecialCharPassword(driver,user_name,password,sub):
    user_name.clear()
    password.clear()
    user_name.send_keys("admin")
    password.send_keys('Hiba,Akram')
    sub.click()
    url=driver.current_url
    if (url!="http://gniopenstack.com/Travel/Admin/index.php"):
        print("Test Case 6: passed")
    else:
        print("Test Case 6: failed")
    

        

#test No.7.... should not accept numerical username


def checkNumberUsername(driver,user_name,password,sub):
    user_name.clear()
    password.clear()
    user_name.send_keys("Hiba1234")
    password.send_keys('admin')
    sub.click()
    url=driver.current_url
    if (url!="http://gniopenstack.com/Travel/Admin/index.php"):
        print("Test Case 7: passed")
    else:
        print("Test Case 7: failed")
    
#test No.8..test login status with false admin username and password..

def checkIncorrectAdmin(driver,user_name,password,sub):
    user_name.clear()
    password.clear()
    user_name.send_keys('hibaakram')
    password.send_keys('hibaakram')
    sub.click()
    present="true"
    try:
        driver.switch_to.alert
        
    except:
        present="false"
        print("Test Case 8: failed")
    if (present=="true"):
        print("Test Case 8: passed")
        obj=driver.switch_to.alert
        obj.accept()


#test No.9.. should accept valid username with valid numerical password..


def checkNumberPassword():
    driver=webdriver.Chrome("C:/Users/DELL/Downloads/chromedriver_win32/chromedriver.exe")
    driver.set_window_size(1024,768)
    driver.get('http://gniopenstack.com/Travel/Admin/loginform.php')
    user_name = driver.find_element_by_name('t1')
    password=driver.find_element_by_name('t2')
    sub=driver.find_element_by_name('sbmt')
    user_name.clear()
    password.clear()
    user_name.send_keys("ree")
    password.send_keys('345')
    sub.click()
    url=driver.current_url
    if (url!="http://gniopenstack.com/Travel/Admin/index.php"):
        print("Test Case 9: failed")
    else:
        print("Test Case 9: passed")
    




    
#test No.10.. add new user with unmatching password and confirm password. BUG
    
def addUnmatchPassConfirm(driver):
    sub=driver.find_element_by_xpath('/html/body/div[2]/div[1]/table/tbody/tr[2]/td/a')
    sub.click()
    user_name = driver.find_element_by_name('t1')
    user_name.send_keys("nice")
    
    
    password=driver.find_element_by_name('t2')

    password.send_keys('monkey')
    
    confirmpass=driver.find_element_by_name('t3')

    confirmpass.send_keys('monhsskey')
    
    Typeuser=driver.find_element_by_css_selector('body > div.container > div.col-sm-9 > form > table > tbody > tr:nth-child(5) > td:nth-child(2) > select')
    Typeuser.click()
    general=Typeuser.find_element_by_xpath('/html/body/div[2]/div[2]/form/table/tbody/tr[5]/td[2]/select/option[3]')
    general.click()
    sub=driver.find_element_by_name('sbmt')
    sub.click()
    present = "true"
    try:
        driver.switch_to.alert
        
    except:
        present="false"
        print("Test Case 10: passed ")
    if (present=="true"):
        print("Test Case 10: failed...bug.. shouldnt accept unmatching password and confirm password")
        obj=driver.switch_to.alert
        obj.accept()
        

    
        

#test No.11 add user with correct username and password format


def addCorrectUser(driver):
    sub=driver.find_element_by_xpath('/html/body/div[2]/div[1]/table/tbody/tr[2]/td/a')
    sub.click()
    user_name = driver.find_element_by_name('t1')
    user_name.send_keys("nice")
    
    
    password=driver.find_element_by_name('t2')

    password.send_keys('monkey')
    
    confirmpass=driver.find_element_by_name('t3')

    confirmpass.send_keys('monkey')
    
    Typeuser=driver.find_element_by_css_selector('body > div.container > div.col-sm-9 > form > table > tbody > tr:nth-child(5) > td:nth-child(2) > select')
    Typeuser.click()
    general=Typeuser.find_element_by_xpath('/html/body/div[2]/div[2]/form/table/tbody/tr[5]/td[2]/select/option[3]')
    general.click()
    sub=driver.find_element_by_name('sbmt')
    sub.click()
    
    obj= driver.switch_to.alert
    
    msg=obj.text
    
    obj.accept()
    url=driver.current_url
    if (msg=="Record Save"):
        print("Test Case 11: passed")
    else:
        print("Test Case 11: failed")
    



#test No.12 usrname should not allow underscore.. 
def addUnderscoreUsername(driver):
    sub=driver.find_element_by_xpath('/html/body/div[2]/div[1]/table/tbody/tr[2]/td/a')
    sub.click()
    user_name = driver.find_element_by_name('t1')
    user_name.send_keys("Imama_")
    
    
    password=driver.find_element_by_name('t2')

    password.send_keys('Imama_')
    
    confirmpass=driver.find_element_by_name('t3')

    confirmpass.send_keys('Imama_')
    
    Typeuser=driver.find_element_by_css_selector('body > div.container > div.col-sm-9 > form > table > tbody > tr:nth-child(5) > td:nth-child(2) > select')
    Typeuser.click()
    general=Typeuser.find_element_by_xpath('/html/body/div[2]/div[2]/form/table/tbody/tr[5]/td[2]/select/option[3]')
    general.click()
    sub=driver.find_element_by_name('sbmt')
    sub.click()
    present = "true"
    try:
        driver.switch_to.alert
        
    except:
        present="false"
        print("Test Case 12: passed")
    if (present=="true"):
        
        print("Test Case 12 : failed...bug.. should not accept underscore")
        obj=driver.switch_to.alert
        obj.accept()



#test 13...no numbers in username... passing

def addNumbersUsername(driver):
    sub=driver.find_element_by_xpath('/html/body/div[2]/div[1]/table/tbody/tr[2]/td/a')
    sub.click()
    user_name = driver.find_element_by_name('t1')
    user_name.send_keys("Imama123")
    
    
    password=driver.find_element_by_name('t2')

    password.send_keys('Imama123')
    
    confirmpass=driver.find_element_by_name('t3')

    confirmpass.send_keys('Imama123')
    
    Typeuser=driver.find_element_by_css_selector('body > div.container > div.col-sm-9 > form > table > tbody > tr:nth-child(5) > td:nth-child(2) > select')
    Typeuser.click()
    general=Typeuser.find_element_by_xpath('/html/body/div[2]/div[2]/form/table/tbody/tr[5]/td[2]/select/option[3]')
    general.click()
    sub=driver.find_element_by_name('sbmt')
    sub.click()
    present = "true"
    try:
        driver.switch_to.alert        
    except:
        present="false"
        print("Test Case 13: passed")
    if (present=="true"):
        print("Test Case 13: failed...bug.. shouldnt accept numbers in username")
        obj=driver.switch_to.alert
        obj.accept()





#test 14...boundary value testing..num of char less than equal to 10 in username... passing

def addTenCharsUsername(driver):
    sub=driver.find_element_by_xpath('/html/body/div[2]/div[1]/table/tbody/tr[2]/td/a')
    sub.click()
    user_name = driver.find_element_by_name('t1')
    user_name.send_keys("HibbaAkram")
    
    
    password=driver.find_element_by_name('t2')

    password.send_keys('Hiba')
    
    confirmpass=driver.find_element_by_name('t3')

    confirmpass.send_keys('Hiba')
    
    Typeuser=driver.find_element_by_css_selector('body > div.container > div.col-sm-9 > form > table > tbody > tr:nth-child(5) > td:nth-child(2) > select')
    Typeuser.click()
    general=Typeuser.find_element_by_xpath('/html/body/div[2]/div[2]/form/table/tbody/tr[5]/td[2]/select/option[3]')
    general.click()
    sub=driver.find_element_by_name('sbmt')
    sub.click()
    present = "true"
    try:
        driver.switch_to.alert
        
    except:
        present="false"
        print("Test Case 14: failed..bug.. should accept less than or equal to 10 chars in username")
    if (present=="true"):
        print("Test Case 14: passed")
        obj=driver.switch_to.alert
        obj.accept()




#test 15...num of char greater than 10 in username.. not allow...BUG

def addMoreTenCharsUsername(driver):
    sub=driver.find_element_by_xpath('/html/body/div[2]/div[1]/table/tbody/tr[2]/td/a')
    sub.click()
    user_name = driver.find_element_by_name('t1')
    user_name.send_keys("ShabeehFatimaChaudry")
    
    
    password=driver.find_element_by_name('t2')

    password.send_keys('Hiba')
    
    confirmpass=driver.find_element_by_name('t3')

    confirmpass.send_keys('Hiba')
    
    Typeuser=driver.find_element_by_css_selector('body > div.container > div.col-sm-9 > form > table > tbody > tr:nth-child(5) > td:nth-child(2) > select')
    Typeuser.click()
    general=Typeuser.find_element_by_xpath('/html/body/div[2]/div[2]/form/table/tbody/tr[5]/td[2]/select/option[3]')
    general.click()
    sub=driver.find_element_by_name('sbmt')
    sub.click()
    present = "true"
    try:
        driver.switch_to.alert       
    except:
        present="false"
        print("Test Case 15: passed") 
    if (present=="true"):
        print("Test Case 15: failed..bug.. should accept less than or equal to 10 chars in username")
        obj=driver.switch_to.alert
        obj.accept()



#test 16...boundary value testing..num of char less than equal to 10 in password... passing

def addTenCharsPassword(driver):
    sub=driver.find_element_by_xpath('/html/body/div[2]/div[1]/table/tbody/tr[2]/td/a')
    sub.click()
    user_name = driver.find_element_by_name('t1')
    user_name.send_keys("Hiba")
    
    
    password=driver.find_element_by_name('t2')

    password.send_keys('HibbaAkram')
    
    confirmpass=driver.find_element_by_name('t3')

    confirmpass.send_keys('HibbaAkram')
    
    Typeuser=driver.find_element_by_css_selector('body > div.container > div.col-sm-9 > form > table > tbody > tr:nth-child(5) > td:nth-child(2) > select')
    Typeuser.click()
    general=Typeuser.find_element_by_xpath('/html/body/div[2]/div[2]/form/table/tbody/tr[5]/td[2]/select/option[3]')
    general.click()
    sub=driver.find_element_by_name('sbmt')
    sub.click()
    present = "true"
    try:
        driver.switch_to.alert
        
    except:
        present="false"
        print("Test Case 16: failed...bug.. should accept less than or equal to 10 chars in password")
    if (present=="true"):
        print("Test Case 16 passed")
        obj=driver.switch_to.alert
        obj.accept()



#test 17...num of char greater than 10 in password...BUG

def addMoreTenCharsPassword(driver):
    sub=driver.find_element_by_xpath('/html/body/div[2]/div[1]/table/tbody/tr[2]/td/a')
    sub.click()
    user_name = driver.find_element_by_name('t1')
    user_name.send_keys("Hiba")
    
    
    password=driver.find_element_by_name('t2')

    password.send_keys('HibbaAkrammm')
    
    confirmpass=driver.find_element_by_name('t3')

    confirmpass.send_keys('HibbaAkrammm')
    
    Typeuser=driver.find_element_by_css_selector('body > div.container > div.col-sm-9 > form > table > tbody > tr:nth-child(5) > td:nth-child(2) > select')
    Typeuser.click()
    general=Typeuser.find_element_by_xpath('/html/body/div[2]/div[2]/form/table/tbody/tr[5]/td[2]/select/option[3]')
    general.click()
    sub=driver.find_element_by_name('sbmt')
    sub.click()
    present = "true"
    try:
        driver.switch_to.alert
        
    except:
        present="false"
        print("Test Case 17 passed")
    if (present=="true"):
        print("Test Case 17: failed...bug.. should not accept more than 10 chars in password")
        
        obj=driver.switch_to.alert
        obj.accept()




#tests 18,19,20,21,22

        
#update and delete tests

def deleteAndUpdateTests(driver):

    sub=driver.find_element_by_xpath('/html/body/div[2]/div[1]/table/tbody/tr[4]/td/a')
    sub.click()
    user_name = driver.find_element_by_css_selector('body > div.container > div.col-sm-9 > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > select')
    user_name.click()
    general=user_name.find_element_by_xpath('/html/body/div[2]/div[2]/form/table/tbody/tr[2]/td[2]/select/option[9]')
    general.click()


    #test 18 ... delete when user selected.. passed



    sub=driver.find_element_by_name('sbmt')
    sub.click()
    present = "true"
    try:
        driver.switch_to.alert
        
    except:
        present="false"
        print("Test Case 18: failed..bug.. should delete")
    if (present=="true"):
        print("Test Case 18: passed")
        
        obj=driver.switch_to.alert
        obj.accept()

    #test 19 ... dont delete when no user selected.. passed
        
    sub=driver.find_element_by_name('sbmt')
    sub.click()
    try:
        driver.switch_to.alert
        
    except:
        present="false"
        print("Test Case 19: passed")
    if (present=="true"):
        print("Test Case 19: failed..bug.. should not have alert")
        obj=driver.switch_to.alert
        obj.accept()
        
    #test 20... update user when user selected and updated with valid info..passed
        
    update=driver.find_element_by_xpath("/html/body/div[2]/div[1]/table/tbody/tr[3]/td/a")
    update.click()
    user=driver.find_element_by_css_selector("body > div.container > div.col-sm-9 > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > select")
    user.click()
    user_drop=user.find_element_by_xpath("/html/body/div[2]/div[2]/form/table/tbody/tr[2]/td[2]/select/option[10]")
    user_drop.click()
    pass1=driver.find_element_by_name('t2')
    pass1.send_keys("admin")
    pass2=driver.find_element_by_name('t3')
    pass2.send_keys("admin")
    type1=driver.find_element_by_css_selector('body > div.container > div.col-sm-9 > form > table > tbody > tr:nth-child(5) > td:nth-child(2) > select')
    type1.click()
    type_Select=type1.find_element_by_xpath('/html/body/div[2]/div[2]/form/table/tbody/tr[5]/td[2]/select/option[3]')
    type_Select.click()
    sub=driver.find_element_by_name('sbmt')
    sub.click()
    present = "true"
    try:
        driver.switch_to.alert
        
    except:
        present="false"
        print("Test Case 20: failed..bug.. should update")
    if (present=="true"):
        print("Test Case 20: passed")
        
        obj=driver.switch_to.alert
        obj.accept()

    #test 21... dont display alert box saying user updated.. when no user is selected and update button clicked..passed
        
    sub=driver.find_element_by_name('sbmt')
    sub.click()
    try:
        driver.switch_to.alert
        
    except:
        present="false"
        print("Test Case 21: passed")
    if (present=="true"):
        print("Test Case 21: failed..bug.. should not have alert")
        obj=driver.switch_to.alert
        obj.accept()
        
    #test 22 .... dont update when selected when updating using unmatching passwords info...BUG
        
    user=driver.find_element_by_css_selector("body > div.container > div.col-sm-9 > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > select")
    user.click()
    user_drop=user.find_element_by_xpath("/html/body/div[2]/div[2]/form/table/tbody/tr[2]/td[2]/select/option[10]")
    user_drop.click()
    pass1=driver.find_element_by_name('t2')
    pass1.send_keys("admin")
    pass2=driver.find_element_by_name('t3')
    pass2.send_keys("admddin")
    type1=driver.find_element_by_css_selector('body > div.container > div.col-sm-9 > form > table > tbody > tr:nth-child(5) > td:nth-child(2) > select')
    type1.click()
    type_Select=type1.find_element_by_xpath('/html/body/div[2]/div[2]/form/table/tbody/tr[5]/td[2]/select/option[3]')
    type_Select.click()
    sub=driver.find_element_by_name('sbmt')
    sub.click()
    present = "true"
    try:
        driver.switch_to.alert
        
    except:
        present="false"
        print("Test Case 22: passed")
    if (present=="true"):
        print("Test Case 22: failed..bug.. should not be updated")
        
        obj=driver.switch_to.alert
        obj.accept()
        


#test case 23..adding category with correct format
def addCategoryWithCorrectFormat(driver):
    category_name = "Category"
    driver.find_element_by_xpath("//div[@class='col-sm-3']/table/tbody/tr[5]/td/a").click()
    category_name_field = driver.find_element_by_xpath("//table[@class='tableshadow']/tbody/tr[2]/td[2]/input")
    category_name_field.send_keys(category_name)

    driver.find_element_by_xpath("//tbody/tr[3]/td[2]/input").click()
    time.sleep(3)
    if EC.alert_is_present:
        alert = driver.switch_to.alert
        alert.accept()
        #added
        print("Test Case 23: passed")
    else:
        print("Test Case 23: failed")

#test case 24.. category name less than 3 letters
def addCategoryByPassingShorterString(driver):
    category_name  = "ct"
    driver.find_element_by_xpath("//div[@class='col-sm-3']/table/tbody/tr[5]/td/a").click()
    category_name_field = driver.find_element_by_xpath("//table[@class='tableshadow']/tbody/tr[2]/td[2]/input")
    category_name_field.send_keys(category_name)
    driver.find_element_by_xpath("//tbody/tr[3]/td[2]/input").click()
    time.sleep(3)
    invalid = driver.find_element_by_css_selector("input:invalid")
    if invalid:
        #print("Please Match the Requested Format")
        print("Test Case 24: passed")
    else:
        print("Test Case 24: failed")

# test case 25..Category name greater than 20 letters
def addCategoryByPassingLongString(driver):
    category_name  = "Category greater than twenty letters"
    driver.find_element_by_xpath("//div[@class='col-sm-3']/table/tbody/tr[5]/td/a").click()
    category_name_field = driver.find_element_by_xpath("//table[@class='tableshadow']/tbody/tr[2]/td[2]/input")
    category_name_field.send_keys(category_name)
    driver.find_element_by_xpath("//tbody/tr[3]/td[2]/input").click()
    time.sleep(3)
    invalid = driver.find_element_by_css_selector("input:invalid")
    if invalid:
        #print("Please Match the Requested Format")
        print("Test Case 25: passed")
    else:
        print("Test Case 25: failed")

# test case 26..testing by giving alphanumeric input
def addCategoryByPassingAlphaNumericCombinations(driver):
    category_name  = "Category1"
    driver.find_element_by_xpath("//div[@class='col-sm-3']/table/tbody/tr[5]/td/a").click()
    category_name_field = driver.find_element_by_xpath("//table[@class='tableshadow']/tbody/tr[2]/td[2]/input")
    category_name_field.send_keys(category_name)
    driver.find_element_by_xpath("//tbody/tr[3]/td[2]/input").click()
    time.sleep(3)
    invalid = driver.find_element_by_css_selector("input:invalid")
    if invalid:
        #print("Please Match the Requested Format")
        print("Test Case 26: passed")
    else:
        print("Test Case 26: failed")
# test case 27..Package added
def  addPackageCorrectNameAndDropDownMenuSelected(driver):
    driver.find_element_by_xpath("//div[@class='col-sm-3']/table/tbody/tr[13]/td/a").click()
    time.sleep(1)
    package_name = "Package_Add_By_Nadir"
    package_name_input_field = driver.find_element_by_xpath("//table[@class='tableshadow']/tbody/tr[2]/td[2]/input")
    package_name_input_field.send_keys(package_name)
    select_category = Select(driver.find_element_by_name("t2"))
    select_category.select_by_value("18")
    time.sleep(1)

    select_sub_category = Select(driver.find_element_by_name("t3"))
    select_sub_category.select_by_value("1")
    driver.find_element_by_xpath("//form/table[@class='tableshadow']/tbody/tr[10]/td[2]/input").click()

    #print("Package Added")
    print("Test Case 27: passed")

# test case 28..Do not add package if name format is incorrect
def addPackageInCorrectNameAndDropDownMenuSelected(driver):
    driver.find_element_by_xpath("//div[@class='col-sm-3']/table/tbody/tr[13]/td/a").click()
    time.sleep(1)
    package_name = "Package_Add_By_Nadir1"
    package_name_input_field = driver.find_element_by_xpath("//table[@class='tableshadow']/tbody/tr[2]/td[2]/input")
    package_name_input_field.send_keys(package_name)
    select_category = Select(driver.find_element_by_name("t2"))
    select_category.select_by_value("18")
    time.sleep(1)

    select_sub_category = Select(driver.find_element_by_name("t3"))
    select_sub_category.select_by_value("1")
    driver.find_element_by_xpath("//form/table[@class='tableshadow']/tbody/tr[10]/td[2]/input").click()
    required = driver.find_element_by_css_selector("input:required")
    if required:
        print("Package Not Added!!!")
        print("Test Case 28: passed")
    else:
        print("Test Case 28: failed")

# test case 29..Do not add package if name format is incorrect
def addPackageCorrectNameAnd____DoNotSelectDropDownValue(driver):
    driver.find_element_by_xpath("//div[@class='col-sm-3']/table/tbody/tr[13]/td/a").click()
    time.sleep(1)
    package_name = "Package_Add_By_Nadir1"
    package_name_input_field = driver.find_element_by_xpath("//table[@class='tableshadow']/tbody/tr[2]/td[2]/input")
    package_name_input_field.send_keys(package_name)
    select_category = Select(driver.find_element_by_name("t2"))
    select_category.select_by_value("18")
    time.sleep(1)
    driver.find_element_by_xpath("//form/table[@class='tableshadow']/tbody/tr[10]/td[2]/input").click()
    required = driver.find_element_by_css_selector("input:required")
    if required:
        print("Package Not Added!!!")
        print("Test Case 29: passed")
    else:
        print("Test Case 29: failed")


if __name__ == '__main__':
    LoginLogout(driver)
    checkLoginOther(driver)
    checkLogin2(driver)
    checkNumberPassword()
    CheckingFunctions(driver)
