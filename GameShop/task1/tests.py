from django.test import TestCase

# Create your tests here.
#
# import os
# import hashlib
#
# # Пример генерации
# salt = os.urandom(32)
# key = hashlib.pbkdf2_hmac('sha256', 'mypassword'.encode('utf-8'), salt, 100000)
#
# print(f'salt {salt}, key {key}')
#
# # Хранение как
# storage = salt + key
# print(type(storage))
#
# # Получение значений обратно
# salt_from_storage = storage[:32]  # 32 является длиной соли
# key_from_storage = storage[32:]
#
# print(f'salt {salt}, key {key}')

from models import Buyer, Game, News


def test_news():
    print(News.objects.all().order_by('-date'))

if __name__ == '__main__':
    test_news()