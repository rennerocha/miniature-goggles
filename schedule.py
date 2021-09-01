import os
from decouple import config


print(config('SEGREDO'))
print(config('SEM_SEGREDO'))
