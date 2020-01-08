Category = input('Category: ')
product_url = 'https://www.supremenewyork.com/shop/all/%s'%(Category)
product_title = input('Name of product (must be official name): ')
name = input('Full Name: ')
email = input('E-mail: ')
phone_number = input('Phone number: ')
adress = input('Adress: ')
city = input('City: ')
zip_code = input("Zip code: ")
ccinfo = input('CC number: ')
ccmonth = input('CC month: ')
ccyear = input('CC year(1 is 2019, 2 is 2020 etc): ')
cvv = input('CVV: ')



keys = {
    "product_title": product_title,
    "product_url": product_url,
    "name": name,
    "email": email,
    "phone_number": phone_number,
    "adress": adress,
    "city": city,
    "zip": zip_code,
    "ccinfo": ccinfo,
    "ccmonth": ccmonth,
    "ccyear": ccyear,
    "CVV": cvv
}
