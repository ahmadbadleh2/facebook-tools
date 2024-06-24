# توليد كلمات مرور عشوائية
import os
import secrets
import string


def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(alphabet) for i in range(length))
    return password


# طلب من المستخدم تحديد عدد كلمات المرور
num_passwords = int(input("Enter the number of passwords to generate: "))
# طلب من المستخدم تحديد طول كلمة المرور
password_length = int(input("Enter password length: "))

# تحديد مسار ملف النصي باستخدام دليل المستخدم الرئيسي
file_name = os.path.join(
    os.path.expanduser("~"),
    "Desktop",
    "mr",
    "facebook",
    "Create_Facebook_account",
    "text",
    "pass.txt",
)

# فتح الملف للكتابة
with open(file_name, "w") as file:
    # توليد كلمات المرور بالطول الذي حدده المستخدم وكتابتها في الملف النصي
    for i in range(num_passwords):
        password = generate_password(password_length)
        file.write(password + "\n")

print("Passwords have been saved to", file_name)
