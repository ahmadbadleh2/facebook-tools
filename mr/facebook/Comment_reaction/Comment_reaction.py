from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
import os
import time

choice = input(
    "\n1-like\n2-love\n3-Support\n4-Laugh\n5-wow\n6-sad\n7-angry\nChoose program to run: "
)

if choice == "1":

    def parse_cookies(cookies_str):
        cookies_dict = []
        cookies_pairs = cookies_str.split(";")
        for pair in cookies_pairs:
            if "=" in pair:
                key, value = pair.split("=", 1)
                cookies_dict.append({
                    "name": key.strip(),
                    "value": value.strip(),
                    "domain": ".facebook.com",
                })
        return cookies_dict

    def use_cookies(thread_id, cookies_str, post_url):
        driver = webdriver.Chrome()
        driver.get("https://mbasic.facebook.com")

        cookies = parse_cookies(cookies_str)
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("https://mbasic.facebook.com")
        driver.get(post_url)
        print(f"Thread {thread_id}: Logged in and accessed post URL")

        # إضافة محاولة للعثور على زر الإعجاب والنقر عليه

        try:
            # قراءة الـ ID من ملف النص
            file_path = os.path.join(os.path.expanduser("~"), "Desktop", "mr",
                                     "facebook", "Comment_reaction", "text",
                                     "comment_id.txt")
            with open(file_path, 'r') as file:
                comment_id = file.read().strip()
                #)
                div_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, comment_id)))
                interaction_element = div_element.find_element(
                    By.XPATH, "//a[contains(text(), 'تفاعل')]")
                interaction_element.click()

                like_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//span[contains(text(), 'أعجبني')]")))
                like_button.click()

            print("like button click")
        except Exception as e:
            print("An error occurred:", e)

        driver.quit()

    def distribute_cookies(num_threads, post_url):
        cookies_file_path = os.path.join(
            os.path.expanduser("~"),
            "Desktop",
            "mr",
            "facebook",
            "Comment_reaction",
            "text",
            "cookies.txt",
        )

        with open(cookies_file_path, "r") as file:
            all_cookies = file.readlines()

        threads = []

        for i in range(min(num_threads, len(all_cookies))):
            cookies = all_cookies[i].strip()
            thread = threading.Thread(target=use_cookies,
                                      args=(i, cookies, post_url))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    if __name__ == "__main__":
        try:
            num_threads = int(input("Number of interactions: "))
            post_link_path = os.path.join(
                os.path.expanduser("~"),
                "Desktop",
                "mr",
                "facebook",
                "Comment_reaction",
                "text",
                "comment_link.txt",
            )

            with open(post_link_path, "r") as file:
                post_url = file.read().strip()

            distribute_cookies(num_threads, post_url)
        except ValueError:
            print("Please enter a valid number.")

elif choice == "2":

    def parse_cookies(cookies_str):
        cookies_dict = []
        cookies_pairs = cookies_str.split(";")
        for pair in cookies_pairs:
            if "=" in pair:
                key, value = pair.split("=", 1)
                cookies_dict.append({
                    "name": key.strip(),
                    "value": value.strip(),
                    "domain": ".facebook.com",
                })
        return cookies_dict

    def use_cookies(thread_id, cookies_str, post_url):
        driver = webdriver.Chrome()
        driver.get("https://mbasic.facebook.com")

        cookies = parse_cookies(cookies_str)
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("https://mbasic.facebook.com")
        driver.get(post_url)
        print(f"Thread {thread_id}: Logged in and accessed post URL")

        try:
            # قراءة الـ ID من ملف النص
            file_path = os.path.join(os.path.expanduser("~"), "Desktop", "mr",
                                     "facebook", "Comment_reaction", "text",
                                     "comment_id.txt")
            with open(file_path, 'r') as file:
                comment_id = file.read().strip()
                #)
                div_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, comment_id)))
                interaction_element = div_element.find_element(
                    By.XPATH, "//a[contains(text(), 'تفاعل')]")
                interaction_element.click()

                love_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//span[contains(text(), 'أحببته')]")))
                love_button.click()
            print("love button click")
        except Exception as e:
            print("An error occurred:", e)
        driver.quit()

    def distribute_cookies(num_threads, post_url):
        cookies_file_path = os.path.join(
            os.path.expanduser("~"),
            "Desktop",
            "mr",
            "facebook",
            "Comment_reaction",
            "text",
            "cookies.txt",
        )

        with open(cookies_file_path, "r") as file:
            all_cookies = file.readlines()

        threads = []

        for i in range(min(num_threads, len(all_cookies))):
            cookies = all_cookies[i].strip()
            thread = threading.Thread(target=use_cookies,
                                      args=(i, cookies, post_url))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    if __name__ == "__main__":
        try:
            num_threads = int(input("Number of interactions:"))
            post_link_path = os.path.join(
                os.path.expanduser("~"),
                "Desktop",
                "mr",
                "facebook",
                "Comment_reaction",
                "text",
                "comment_link.txt",
            )

            with open(post_link_path, "r") as file:
                post_url = file.read().strip()

            distribute_cookies(num_threads, post_url)
        except ValueError:
            print("Please enter a valid number.")
elif choice == "3":

    def parse_cookies(cookies_str):
        cookies_dict = []
        cookies_pairs = cookies_str.split(";")
        for pair in cookies_pairs:
            if "=" in pair:
                key, value = pair.split("=", 1)
                cookies_dict.append({
                    "name": key.strip(),
                    "value": value.strip(),
                    "domain": ".facebook.com",
                })
        return cookies_dict

    def use_cookies(thread_id, cookies_str, post_url):
        driver = webdriver.Chrome()
        driver.get("https://mbasic.facebook.com")

        cookies = parse_cookies(cookies_str)
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("https://mbasic.facebook.com")
        driver.get(post_url)
        print(f"Thread {thread_id}: Logged in and accessed post URL")

        try:
            # قراءة الـ ID من ملف النص
            file_path = os.path.join(os.path.expanduser("~"), "Desktop", "mr",
                                     "facebook", "Comment_reaction", "text",
                                     "comment_id.txt")
            with open(file_path, 'r') as file:
                comment_id = file.read().strip()
                #)
                div_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, comment_id)))
                interaction_element = div_element.find_element(
                    By.XPATH, "//a[contains(text(), 'تفاعل')]")
                interaction_element.click()

                support_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//span[contains(text(), 'أدعمه')]")))
                support_button.click()
            print("support button click")
        except Exception as e:
            print("An error occurred:", e)
        driver.quit()

    def distribute_cookies(num_threads, post_url):
        cookies_file_path = os.path.join(
            os.path.expanduser("~"),
            "Desktop",
            "mr",
            "facebook",
            "Comment_reaction",
            "text",
            "cookies.txt",
        )

        with open(cookies_file_path, "r") as file:
            all_cookies = file.readlines()

        threads = []

        for i in range(min(num_threads, len(all_cookies))):
            cookies = all_cookies[i].strip()
            thread = threading.Thread(target=use_cookies,
                                      args=(i, cookies, post_url))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    if __name__ == "__main__":
        try:
            num_threads = int(input("Number of interactions:"))
            post_link_path = os.path.join(
                os.path.expanduser("~"),
                "Desktop",
                "mr",
                "facebook",
                "Comment_reaction",
                "text",
                "comment_link.txt",
            )

            with open(post_link_path, "r") as file:
                post_url = file.read().strip()

            distribute_cookies(num_threads, post_url)
        except ValueError:
            print("Please enter a valid number.")
elif choice == "4":

    def parse_cookies(cookies_str):
        cookies_dict = []
        cookies_pairs = cookies_str.split(";")
        for pair in cookies_pairs:
            if "=" in pair:
                key, value = pair.split("=", 1)
                cookies_dict.append(
                    {
                        "name": key.strip(),
                        "value": value.strip(),
                        "domain": ".facebook.com",
                    }
                )
        return cookies_dict

    def use_cookies(thread_id, cookies_str, post_url):
        driver = webdriver.Chrome()
        driver.get("https://mbasic.facebook.com")

        cookies = parse_cookies(cookies_str)
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("https://mbasic.facebook.com")
        driver.get(post_url)
        print(f"Thread {thread_id}: Logged in and accessed post URL")

        try:
            # قراءة الـ ID من ملف النص
            file_path = os.path.join(os.path.expanduser("~"), "Desktop", "mr",
                                     "facebook", "Comment_reaction", "text",
                                     "comment_id.txt")
            with open(file_path, 'r') as file:
                comment_id = file.read().strip()
                #)
                div_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, comment_id)))
                interaction_element = div_element.find_element(
                    By.XPATH, "//a[contains(text(), 'تفاعل')]")
                interaction_element.click()

                hahaha_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//span[contains(text(), 'هاهاها')]")))
                hahaha_button.click()
            print("hahaha button click")
        except Exception as e:
            print("An error occurred:", e)
        driver.quit()

    def distribute_cookies(num_threads, post_url):
        cookies_file_path = os.path.join(
            os.path.expanduser("~"),
            "Desktop",
            "mr",
            "facebook",
            "Comment_reaction",
            "text",
            "cookies.txt",
        )

        with open(cookies_file_path, "r") as file:
            all_cookies = file.readlines()

        threads = []

        for i in range(min(num_threads, len(all_cookies))):
            cookies = all_cookies[i].strip()
            thread = threading.Thread(target=use_cookies,
                                      args=(i, cookies, post_url))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    if __name__ == "__main__":
        try:
            num_threads = int(input("Number of interactions:"))
            post_link_path = os.path.join(
                os.path.expanduser("~"),
                "Desktop",
                "mr",
                "facebook",
                "Comment_reaction",
                "text",
                "comment_link.txt",
            )

            with open(post_link_path, "r") as file:
                post_url = file.read().strip()

            distribute_cookies(num_threads, post_url)
        except ValueError:
            print("Please enter a valid number.")
elif choice == "5":

    def parse_cookies(cookies_str):
        cookies_dict = []
        cookies_pairs = cookies_str.split(";")
        for pair in cookies_pairs:
            if "=" in pair:
                key, value = pair.split("=", 1)
                cookies_dict.append(
                    {
                        "name": key.strip(),
                        "value": value.strip(),
                        "domain": ".facebook.com",
                    }
                )
        return cookies_dict

    def use_cookies(thread_id, cookies_str, post_url):
        driver = webdriver.Chrome()
        driver.get("https://mbasic.facebook.com")

        cookies = parse_cookies(cookies_str)
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("https://mbasic.facebook.com")
        driver.get(post_url)
        print(f"Thread {thread_id}: Logged in and accessed post URL")

        try:
            # قراءة الـ ID من ملف النص
            file_path = os.path.join(os.path.expanduser("~"), "Desktop", "mr",
                                     "facebook", "Comment_reaction", "text",
                                     "comment_id.txt")
            with open(file_path, 'r') as file:
                comment_id = file.read().strip()
                #)
                div_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, comment_id)))
                interaction_element = div_element.find_element(
                    By.XPATH, "//a[contains(text(), 'تفاعل')]")
                interaction_element.click()

                Wow_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//span[contains(text(), 'واااو')]")))
                Wow_button.click()
            print("Wow button click")
        except Exception as e:
            print("An error occurred:", e)
        driver.quit()

    def distribute_cookies(num_threads, post_url):
        cookies_file_path = os.path.join(
            os.path.expanduser("~"),
            "Desktop",
            "mr",
            "facebook",
            "Comment_reaction",
            "text",
            "cookies.txt",
        )

        with open(cookies_file_path, "r") as file:
            all_cookies = file.readlines()

        threads = []

        for i in range(min(num_threads, len(all_cookies))):
            cookies = all_cookies[i].strip()
            thread = threading.Thread(target=use_cookies, args=(i, cookies, post_url))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    if __name__ == "__main__":
        try:
            num_threads = int(input("Number of interactions: "))
            post_link_path = os.path.join(
                os.path.expanduser("~"),
                "Desktop",
                "mr",
                "facebook",
                "Comment_reaction",
                "text",
                "comment_link.txt",
            )

            with open(post_link_path, "r") as file:
                post_url = file.read().strip()

            distribute_cookies(num_threads, post_url)
        except ValueError:
            print("Please enter a valid number.")

elif choice == "6":

    def parse_cookies(cookies_str):
        cookies_dict = []
        cookies_pairs = cookies_str.split(";")
        for pair in cookies_pairs:
            if "=" in pair:
                key, value = pair.split("=", 1)
                cookies_dict.append(
                    {
                        "name": key.strip(),
                        "value": value.strip(),
                        "domain": ".facebook.com",
                    }
                )
        return cookies_dict

    def use_cookies(thread_id, cookies_str, post_url):
        driver = webdriver.Chrome()
        driver.get("https://mbasic.facebook.com")

        cookies = parse_cookies(cookies_str)
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("https://mbasic.facebook.com")
        driver.get(post_url)
        print(f"Thread {thread_id}: Logged in and accessed post URL")

        try:
            # قراءة الـ ID من ملف النص
            file_path = os.path.join(os.path.expanduser("~"), "Desktop", "mr",
                                     "facebook", "Comment_reaction", "text",
                                     "comment_id.txt")
            with open(file_path, 'r') as file:
                comment_id = file.read().strip()
                #)
                div_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, comment_id)))
                interaction_element = div_element.find_element(
                    By.XPATH, "//a[contains(text(), 'تفاعل')]")
                interaction_element.click()

                sad_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//span[contains(text(), 'أحزنني')]")))
                sad_button.click()
            print("sad button click")
        except Exception as e:
            print("An error occurred:", e)
        driver.quit()

    def distribute_cookies(num_threads, post_url):
        cookies_file_path = os.path.join(
            os.path.expanduser("~"),
            "Desktop",
            "mr",
            "facebook",
            "Comment_reaction",
            "text",
            "cookies.txt",
        )

        with open(cookies_file_path, "r") as file:
            all_cookies = file.readlines()

        threads = []

        for i in range(min(num_threads, len(all_cookies))):
            cookies = all_cookies[i].strip()
            thread = threading.Thread(target=use_cookies, args=(i, cookies, post_url))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    if __name__ == "__main__":
        try:
            num_threads = int(input("Number of interactions: "))
            post_link_path = os.path.join(
                os.path.expanduser("~"),
                "Desktop",
                "mr",
                "facebook",
                "Comment_reaction",
                "text",
                "comment_link.txt",
            )

            with open(post_link_path, "r") as file:
                post_url = file.read().strip()

            distribute_cookies(num_threads, post_url)
        except ValueError:
            print("Please enter a valid number.")

elif choice == "7":

    def parse_cookies(cookies_str):
        cookies_dict = []
        cookies_pairs = cookies_str.split(";")
        for pair in cookies_pairs:
            if "=" in pair:
                key, value = pair.split("=", 1)
                cookies_dict.append(
                    {
                        "name": key.strip(),
                        "value": value.strip(),
                        "domain": ".facebook.com",
                    }
                )
        return cookies_dict

    def use_cookies(thread_id, cookies_str, post_url):
        driver = webdriver.Chrome()
        driver.get("https://mbasic.facebook.com")

        cookies = parse_cookies(cookies_str)
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("https://mbasic.facebook.com")
        driver.get(post_url)
        print(f"Thread {thread_id}: Logged in and accessed post URL")

        try:
            # قراءة الـ ID من ملف النص
            file_path = os.path.join(os.path.expanduser("~"), "Desktop", "mr",
                                     "facebook", "Comment_reaction", "text",
                                     "comment_id.txt")
            with open(file_path, 'r') as file:
                comment_id = file.read().strip()
                #)
                div_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, comment_id)))
                interaction_element = div_element.find_element(
                    By.XPATH, "//a[contains(text(), 'تفاعل')]")
                interaction_element.click()

                angry_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//span[contains(text(), 'أغضبني')]")))
                angry_button.click()
            print("angry button click")
        except Exception as e:
            print("An error occurred:", e)
        driver.quit()

    def distribute_cookies(num_threads, post_url):
        cookies_file_path = os.path.join(
            os.path.expanduser("~"),
            "Desktop",
            "mr",
            "facebook",
            "Comment_reaction",
            "text",
            "cookies.txt",
        )

        with open(cookies_file_path, "r") as file:
            all_cookies = file.readlines()

        threads = []

        for i in range(min(num_threads, len(all_cookies))):
            cookies = all_cookies[i].strip()
            thread = threading.Thread(target=use_cookies, args=(i, cookies, post_url))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    if __name__ == "__main__":
        try:
            num_threads = int(input("Number of interactions: "))
            post_link_path = os.path.join(
                os.path.expanduser("~"),
                "Desktop",
                "mr",
                "facebook",
                "Comment_reaction",
                "text",
                "comment_link.txt",
            )

            with open(post_link_path, "r") as file:
                post_url = file.read().strip()

            distribute_cookies(num_threads, post_url)
        except ValueError:
            print("Please enter a valid number.")

else:
    print("Incorrect selection")
