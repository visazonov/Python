# переменные окружения вариант 1
import os
# Pass = os.getenv('PASS')
# print(Pass)


# переменные окружения вариант 2
# pip install python-dotenv

import os
from dotenv import load_dotenv
load_dotenv()

Pass = os.getenv('PASS')
print(Pass)