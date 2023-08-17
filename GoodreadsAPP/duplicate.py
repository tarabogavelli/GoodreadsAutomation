"""def index(request):
    context ={}
 
    # create object of form
    if request.method == "POST":
        form = input(request.POST or None)
     
        # check if form data is valid
        if form.is_valid():
            USERNAME = form.cleaned_data['username']
            PASSWORD = form.cleaned_data['password']
            booklist = form.cleaned_data['booklist']
            BOOKLIST = booklist.split(",")
            form.save()
            doAutomation(USERNAME,PASSWORD,BOOKLIST)
            return redirect('/success/')
    return render(request, "index.html", context=context)

def success(request):
    return render(request, "success.html")"""

"""def doAutomation(username, password, booklist):
    # Initialize the webdriver
    driver = webdriver.Chrome()
    # Navigate to the webpage
    driver.get("https://www.goodreads.com")
    driver.implicitly_wait(10)

    # GET EMAIL SIGN IN PAGE
    signin = '//*[@id="signIn"]/div/div/a'
    driver.find_element(By.XPATH, signin).click()
    email_signin = '//*[@id="choices"]/div/a[5]/button'
    driver.find_element(By.XPATH, email_signin).click()

    MY_EMAIL = username
    MY_PASSWORD = password
    BOOK_LIST = booklist

    # SIGN IN WITH EMAIL AND PASSWORD
    email_path = '//*[@id="ap_email"]'
    password_path = '//*[@id="ap_password"]'

    email_input = driver.find_element(By.XPATH, email_path)
    password_input = driver.find_element(By.XPATH, password_path)
    email_input.send_keys(MY_EMAIL)
    password_input.send_keys(MY_PASSWORD)
    driver.find_element(By.XPATH, '//*[@id="signInSubmit"]').click()
    for item in BOOK_LIST:
        search_box = driver.find_element(By.XPATH, '//*[@class="searchBox__input searchBox__input--navbar"]')
        search_box.send_keys(item)
        #driver.find_element(By.XPATH, '//*[@id="bodycontainer"]/div/div[2]/div/header/div[1]/div/div[2]/form/button').click()
        driver.find_element(By.XPATH, '//form[@class="searchBox__form"]/button').click()
        driver.find_elements(By.XPATH,'//button[@class="wtrToRead"]')[0].click()

    sleep(5)
    driver.quit()"""