import os
from decouple import config


print(config('SEGREDO'))
print(config('SEM_SEGREDO', default="sem"))
print(config('TESTE_DEFAULT', default="default"))
