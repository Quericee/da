import math
import pandas as pd

data = pd.read_csv("works.csv").dropna()

count_people = 0
for (jobTitle, qualification) in zip(data['jobTitle'], data['qualification']):
    if jobTitle != qualification:
        count_people += 1
print(f"У {count_people} человек профессия и должность не совпадают")

menegers = data[data['jobTitle'].str.lower().str.contains("менеджер")]['qualification'].value_counts().head()
print("Топ 5 образований менеджеров: ")
print(menegers)


injineers = data[data['qualification'].str.lower().str.contains("инженер")]['jobTitle'].value_counts().head()
print("Топ 5 специальностей инженеров: ")
print(injineers)

# У 1052 человек профессия и должность не совпадают

# Топ 5 образований менеджеров:
# Бакалавр      9
# менеджер      5
# Специалист    5
# Менеджер      5
# Экономист     4

# Топ 5 специальностей инженеров:
# заместитель директора                    2
# Инженер лесопользования                  2
# главный инженер                          2
# Директор                                 2
# заместитель директора по производству    1
