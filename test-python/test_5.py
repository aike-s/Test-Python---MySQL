"""
  5) ordenar los terceros que se tienen en el archivo data.py por nombre y 
  agregar dentro de cada tercero una propiedad que muestre la compañia a la que pertenece
"""

from data import get_thirds, get_companies

def order_thirds():

    all_thirds = get_thirds()
    ordered_thirds = []

    for third in all_thirds:
        if third.get("tradename") == "":
            firstname = third.get("firstname")
            lastname = third.get("lastname")
            maidenname = third.get("maidenname")
            tradename = {"tradename":firstname + " " + lastname + " " + maidenname}
        else:
            tradename = {"tradename":third.get("tradename")}
        third.update(tradename)
        ordered_thirds.append(third)
        
    ordered_thirds = sorted(all_thirds, key=lambda x: x["tradename"])
    
    return ordered_thirds

def add_property():

    all_thirds = order_thirds()
    all_companies = get_companies()
    new_thirds = []

    for third in all_thirds:
        third["companyName"] = (company["name"] for company in all_companies
                                if company["id"] == third["companyid"])
        new_thirds.append(third)

    print(new_thirds)