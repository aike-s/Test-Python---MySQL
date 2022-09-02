"""
  3) ordenar los terceros que se tienen en el archivo data.py 
  por nombre, para obtener el nombre correcto se debe tener en 
  cuenta la siguiente validación:
  
  si el tercero tiene un (tradename != '') entonces se muestra este valor, 
  en caso contrario se debe obtener concatenando los siguientes 
  campos: (firstname, lastname, maidenname) en el orden dado
"""
from data import get_thirds

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

    print(ordered_thirds)
