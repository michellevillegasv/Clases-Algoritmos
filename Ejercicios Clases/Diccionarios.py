currency_dictionary = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
currency_input = input("Please enter a currency, eg: Euro, Dollar or Yen: ")
print(currency_dictionary.get(currency_input, "Currency not found"))