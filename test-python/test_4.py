"""
  4) ordenar los terceros que se tienen en el archivo data.py por identificationNumber
"""
from data import get_thirds

def order_thirds():
    all_thirds = get_thirds()

    ordered_thirds = sorted(all_thirds, key=lambda x: x["identificationNumber"])

    print(ordered_thirds)