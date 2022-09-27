from brasilapy import BrasilAPI

c = BrasilAPI()

cep = c.get_cep(cep="58073030")

banks = c.get_banks()

for bank in banks:
    bank.code
