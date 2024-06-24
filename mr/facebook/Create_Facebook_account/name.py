# انشاء اسماء وهمية
from faker import Faker
import arabic_reshaper
from bidi.algorithm import get_display
import os


def generate_names(num_names, lang_choice):
    base_dir = os.path.join(
        os.path.expanduser("~"),
        "Desktop",
        "mr",
        "facebook",
        "Create_Facebook_account",
        "text",
    )
    if lang_choice == 1:
        arabic_male_names_file = os.path.join(base_dir, "arabic_male_names.txt")
        arabic_female_names_file = os.path.join(base_dir, "arabic_female_names.txt")
        arabic_surnames_file = os.path.join(base_dir, "lar.txt")
        faker_arabic = Faker("ar")
        faker_english = None
    elif lang_choice == 2:
        english_male_names_file = os.path.join(base_dir, "english_male_names.txt")
        english_female_names_file = os.path.join(base_dir, "english_female_names.txt")
        english_surnames_file = os.path.join(base_dir, "len.txt")
        faker_arabic = None
        faker_english = Faker("en_US")
    else:
        print("Invalid language choice.")
        return

    for _ in range(num_names):
        if lang_choice == 1:
            # Generate Arabic male name
            arabic_male_name = arabic_reshaper.reshape(faker_arabic.first_name_male())
            with open(arabic_male_names_file, "a", encoding="utf-8") as file:
                file.write(get_display(arabic_male_name) + "\n")  # تعديل هنا

            # Generate Arabic female name
            arabic_female_name = arabic_reshaper.reshape(
                faker_arabic.first_name_female()
            )
            with open(arabic_female_names_file, "a", encoding="utf-8") as file:
                file.write(get_display(arabic_female_name) + "\n")  # تعديل هنا

            # Generate Arabic surname
            arabic_surname = arabic_reshaper.reshape(faker_arabic.last_name())
            with open(arabic_surnames_file, "a", encoding="utf-8") as file:
                file.write(get_display(arabic_surname) + "\n")  # تعديل هنا
        elif lang_choice == 2:
            # Generate English male name
            english_male_name = faker_english.first_name_male()
            with open(english_male_names_file, "a", encoding="utf-8") as file:
                file.write(english_male_name + "\n")

            # Generate English female name
            english_female_name = faker_english.first_name_female()
            with open(english_female_names_file, "a", encoding="utf-8") as file:
                file.write(english_female_name + "\n")

            # Generate English surname
            english_surname = faker_english.last_name()
            with open(english_surnames_file, "a", encoding="utf-8") as file:
                file.write(english_surname + "\n")


num_names = int(input("Enter the number of names to generate: "))
lang_choice = int(input("Enter '1' for Arabic or '2' for English: "))
generate_names(num_names, lang_choice)
