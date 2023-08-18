from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import input, recommendationForm, findLibrary
from django.contrib import messages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd
import json


 
def index(request):
    context ={}
 
    # create object of form
    form = input(request.POST or None)
    form2 = recommendationForm(request.POST or None)
    form3 =  findLibrary(request.POST or None)
    # check if form data is valid
    context['form']= form
    

    if form.is_valid():
        # save the form data to model
        form.save()
        USERNAME = form.cleaned_data['username']
        PASSWORD = form.cleaned_data['password']
        booklist = form.cleaned_data['booklist']
        BOOKLIST = booklist.split(",")
        
        wantToRead(USERNAME,PASSWORD,BOOKLIST)
        messages.success(request, "Your books had been added, go to your goodreads profile to check it our!")

        #return redirect('/success/')
        return render(request, "index.html", context)
    
    if form2.is_valid():
        form2.save()
        USERNAME = form2.cleaned_data['username']
        PASSWORD = form2.cleaned_data['password']
        
        df = getRecommendations(USERNAME,PASSWORD)
        #recs = df.to_html()
        json_records = df.reset_index().to_json(orient ='records')
        data = []
        data = json.loads(json_records)
        context = {'d': data}
  
        return render(request, 'table.html', context)
    
    if form3.is_valid():
        form3.save()
        address = form3.cleaned_data['location']
        ADDRESS = address.split(" ")
        url = "https://www.google.com/maps/embed/v1/search?key=AIzaSyA7W2zL5BxDEfqr6mJgOV_cYWEw4H94T7c&q=library+near"
        for item in ADDRESS:
            url+="+"
            url+=item
        print(url)
        context={'map':url}
        return render(request, "index.html", context)
 
    return render(request, "index.html", context)

def success(request):
    return render(request, "success.html")

def table(request):
    return render(request, "table.html")


def wantToRead(username, password, booklist):

    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    op.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=op)
    #driver = webdriver.Chrome()
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
        driver.find_element(By.XPATH, '//form[@class="searchBox__form"]/button').click()
        driver.find_elements(By.XPATH,'//button[@class="wtrToRead"]')[0].click()
    sleep(5)
    driver.quit()

def getRecommendations(username, password):
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    op.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=op)
    #driver = webdriver.Chrome()
    driver.get("https://www.goodreads.com")
    driver.implicitly_wait(10)
    signin = '//*[@id="signIn"]/div/div/a'
    driver.find_element(By.XPATH, signin).click()
    email_signin = '//*[@id="choices"]/div/a[5]/button'
    driver.find_element(By.XPATH, email_signin).click()
    MY_EMAIL = username
    MY_PASSWORD = password
    email_path = '//*[@id="ap_email"]'
    password_path = '//*[@id="ap_password"]'
    email_input = driver.find_element(By.XPATH, email_path)
    password_input = driver.find_element(By.XPATH, password_path)
    email_input.send_keys(MY_EMAIL)
    password_input.send_keys(MY_PASSWORD)
    driver.find_element(By.XPATH, '//*[@id="signInSubmit"]').click()
    driver.find_element(By.XPATH, '//*[@class="primaryNavMenu primaryNavMenu--siteHeaderBrowseMenu ignore-react-onclickoutside"]').click()
    driver.find_elements(By.XPATH, '//*[contains(text(), "Recommendations")]')[0].click()
    driver.find_elements(By.XPATH,'//*[@class="actionLinkLite"]')[0].click()
    books = driver.find_elements(By.XPATH, '//*[@class="readable"]')
    authors = driver.find_elements(By.XPATH, '//*[@class="authorName"]')
    book_recs = []
    author_recs = []
    for i in range(len(books)):
        book_recs.append(books[i].text)
        author_recs.append(authors[i].text)
    df = pd.DataFrame(list(zip(book_recs, author_recs)), columns = ['Book', 'Author'])
    return df


