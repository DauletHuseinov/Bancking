from random import randint
from datetime import date

from credit.models import Client, Account

human_1 = Client.objects.create(name='Nursultan N.D', birth_year='1994-12-4', work_place='Codify', )
human_2 = Client.objects.create(name='Daulet K.SH', birth_year='2006-02-27', work_place='Google', )

account_1 = Account.objects.create(number=randint(100000000000000, 9999999999999999), account_type=2, client=human_1)
account_2 = Account.objects.create(number=randint(100000000000000, 9999999999999999), account_type=3, client=human_1)
account_3 = Account.objects.create(number=randint(100000000000000, 9999999999999999), account_type=4, client=human_2)
account_4 = Account.objects.create(number=randint(100000000000000, 9999999999999999), account_type=5, client=human_2)


account_1.credits.create(sum=20000, )
account_2.credits.create(sum=20000, )
account_3.credits.create(sum=20000, )
account_4.credits.create(sum=20000, )
