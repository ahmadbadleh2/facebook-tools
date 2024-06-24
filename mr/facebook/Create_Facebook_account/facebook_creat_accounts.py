# استيراد المكتبات والوحدات الضرورية
from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import os
import random
import pytz
import time
from threading import Thread
from fake_useragent import UserAgent
from faker import Faker
from random2 import randint
import hashlib

ua = UserAgent()
executable_path = "C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe"


# انشاء حسابات
def execute_registration(first_name_file, last_name_file, gender_choice, proxy,
                         agent, screen, timezone,
                         canvas):

    fake = Faker()

    with open(first_name_file, "r", encoding="utf-8") as file:
        first_names = file.readlines()

    # تحميل ملف الأسماء الأخيرة
    with open(last_name_file, "r", encoding="utf-8") as file:
        last_names = file.readlines()
    canvas_signature = hashlib.md5(fake.text(max_nb_chars=100).encode()).hexdigest()

    print("Canvas signature:", canvas_signature)
    # إعداد WebDriver
    options = ChromeOptions()

    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(f"--disable-features=CanvasDefender")
    options.add_argument(f"--enable-features=CanvasDefender{canvas_signature}")



   # options.add_argument('--proxy-server=http://' + proxy)
    options.add_argument(f'user-agent={agent}')

    # توليد قيمة عشوائية لعرض وارتفاع النافذة
    width = random.randint(200, 1200)  # قيمة عشوائية بين 400 و 1200
    height = random.randint(200, 900)  # قيمة عشوائية بين 300 و 800
    options.add_argument(f"--window-size={width},{height},{screen}")
    # الحصول على قائمة بكل التايم زونات
    timezones = list(pytz.all_timezones)
    # اختيار تايم زون بشكل عشوائي
    random_timezone = random.choice(timezones)
    options.add_argument(f"--use-timezone={random_timezone},{timezone}")


   # print(f"Using proxy: {proxy}")
    print(f"User-Agent: {agent}")
    print(f"Random timezone: {random_timezone}")

    driver = Chrome(options=options)


    driver.get("https://mbasic.facebook.com/reg/")

    try:
        # التحقق من توفر زر قبول ملفات تعريف الارتباط
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(("name", "accept_only_essential")))
        button.click()
    except:
        pass

    # البحث عن حقل إدخال الاسم الأول وملئه بالاسم الأول عشوائي
    random_first_name = random.choice(first_names).strip()
    input_text = driver.find_element("name", "firstname")
    input_text.send_keys(random_first_name)
    # time.sleep(2)

    # البحث عن حقل إدخال الاسم الأخير وملئه بالاسم الأخير عشوائي
    random_last_name = random.choice(last_names).strip()
    input_text = driver.find_element("name", "lastname")
    input_text.send_keys(random_last_name)
    # time.sleep(2)

    # فتح صفحة البريد الإلكتروني المؤقت ونسخ البريد الإلكتروني المؤقت
    driver.execute_script(
        "window.open('https://10minutemail.net/m/?lang=ar', '_blank');")
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
    try:  # البحث عن عنصر الـ checkbox
        checkbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="challenge-stage"]/div/label/input"]')))
        checkbox.click()

    except:
        pass

    # button = driver.find_element("class", "fc-button-label")
    # button.click()
    try:
        # التحقق من توفر زر قبول ملفات تعريف الارتباط
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(("class", "fc-button-label")))
        button.click()
    except:
        pass

    element = driver.find_element("id", "span_mail")
    text_to_copy = element.text

    print("Email Address:", text_to_copy)

    time.sleep(3)
    # تحديد مسار الملف لحفظ البريد الإلكتروني
    file_path = os.path.join(
        os.path.expanduser("~"),
        "Desktop",
        "mr",
        "facebook",
        "Create_Facebook_account",
        "text",
        "mail.txt",
    )
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text_to_copy)

    driver.switch_to.window(driver.window_handles[0])

    # قراءة البريد الإلكتروني من الملف
    file_path = os.path.join(
        os.path.expanduser("~"),
        "Desktop",
        "mr",
        "facebook",
        "Create_Facebook_account",
        "text",
        "mail.txt",
    )
    with open(file_path, "r", encoding="utf-8") as file:
        text_from_file = file.read()

    # إدخال البريد الإلكتروني في النموذج
    input_element = driver.find_element("id", "contactpoint_step_input")
    input_element.send_keys(text_from_file)
    time.sleep(2)

    # إدخال قيمة الجنس المختارة في النموذج
    element = driver.find_element(
        By.XPATH,
        f'//input[@type="radio" and @name="sex" and @value="{gender_choice}"]')
    element.click()
    time.sleep(2)

    # اختيار تاريخ الميلاد
    select_element = driver.find_element(By.ID, "day")
    select = Select(select_element)
    options = select.options
    random_index = random.randint(1, len(options) - 1)
    select.select_by_index(random_index)
    time.sleep(2)

    select_element = driver.find_element(By.ID, "month")
    select = Select(select_element)
    options = select.options
    random_index = random.randint(1, len(options) - 1)
    select.select_by_index(random_index)
    time.sleep(2)

    select_element = driver.find_element(By.ID, "year")
    select = Select(select_element)
    options = select.options
    random_index = random.randint(26, len(options) - 1)
    select.select_by_index(random_index)
    time.sleep(2)

    # تحديد مسار ملف الكلمات المرور
    file_path = os.path.join(
        os.path.expanduser("~"),
        "Desktop",
        "mr",
        "facebook",
        "Create_Facebook_account",
        "text",
        "pass.txt",
    )

    # قراءة كلمات المرور من الملف
    with open(file_path, "r", encoding="utf-8") as file:
        passwords = file.readlines()

    # اختيار كلمة مرور عشوائية من القائمة
    random_password = random.choice(passwords)

    # إيجاد عنصر إدخال كلمة المرور وإدخال الكلمة المرور العشوائية
    element = driver.find_element(By.ID, "password_step_input")
    element.send_keys(random_password)

    time.sleep(1000)

    # النقر على زر التسجيل
    element = driver.find_element(By.ID, "signup_button")
    element.click()

    time.sleep(1000)

    # اختيار لغة الأسماء بين العربية والإنجليزية

proxies_file_path = os.path.join(os.path.expanduser("~"),"Desktop",
        "mr",
        "facebook",
        "Create_Facebook_account",
        "text", "proxies.txt")
with open(proxies_file_path, "r") as file:
    proxies = file.read().splitlines()

language_choice = input("Choose a language 1 for Arabic, 2 for English (1/2): ")
# اختيار الجنس
gender_choice = input("Choose gender 1 for female, 2 for male (1/2): ")
# طلب عدد المحاولات من المستخدم
num_threads = int(input("The number of accounts you want to create: "))

# تحديد ملفات الأسماء بناءً على اختيار المستخدم
if language_choice == "1" and gender_choice == "2":  # ذكر عربي
    first_name_file = os.path.join(
        os.path.expanduser("~"),
        "Desktop",
        "mr",
        "facebook",
        "Create_Facebook_account",
        "text",
        "arabic_male_names.txt",
    )
    last_name_file = os.path.join(
        os.path.expanduser("~"),
        "Desktop",
        "mr",
        "facebook",
        "Create_Facebook_account",
        "text",
        "lar.txt",
    )
elif language_choice == "1" and gender_choice == "1":  # أنثى عربية
    first_name_file = os.path.join(
        os.path.expanduser("~"),
        "Desktop",
        "mr",
        "facebook",
        "Create_Facebook_account",
        "text",
        "arabic_female_names.txt",
    )
    last_name_file = os.path.join(
        os.path.expanduser("~"),
        "Desktop",
        "mr",
        "facebook",
        "Create_Facebook_account",
        "text",
        "lar.txt",
    )
elif language_choice == "2" and gender_choice == "2":  # ذكر إنجليزي
    first_name_file = os.path.join(
        os.path.expanduser("~"),
        "Desktop",
        "mr",
        "facebook",
        "Create_Facebook_account",
        "text",
        "english_male_names.txt",
    )
    last_name_file = os.path.join(
        os.path.expanduser("~"),
        "Desktop",
        "mr",
        "facebook",
        "Create_Facebook_account",
        "text",
        "len.txt",
    )
elif language_choice == "2" and gender_choice == "1":  # أنثى إنجليزية
    first_name_file = os.path.join(
        os.path.expanduser("~"),
        "Desktop",
        "mr",
        "facebook",
        "Create_Facebook_account",
        "text",
        "english_female_names.txt",
    )
    last_name_file = os.path.join(
        os.path.expanduser("~"),
        "Desktop",
        "mr",
        "facebook",
        "Create_Facebook_account",
        "text",
        "len.txt",
    )
else:
    print("Invalid choice. Please choose '1' for Arabic or '2' for English.")
    exit()

    # إنشاء قائمة لتخزين الخيوط
threads = []
for i in range(num_threads):

    proxy = proxies[i % len(proxies)]
    agent = ua.random
    screen = random.randint
    timezone = random.randint
    canvas = random.randint
    thread = Thread(target=execute_registration,
                    args=(first_name_file, last_name_file, gender_choice,
                          proxy, agent, screen, timezone,
                          canvas))
    thread.start()
    threads.append(thread)

# الانضمام إلى جميع الخيوط
for thread in threads:
    thread.join()
