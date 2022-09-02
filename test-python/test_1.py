""" 
  1) consulte la información del archivo data.py
  cree un objeto que contenga las empresas y dentro 
  las sucursales que corresponden para cada empresa
"""
from data import get_companies, get_branches

def company_branches():
    all_companies = get_companies()
    all_branches = get_branches()
    companies_info = []

    for company in all_companies:
        co_info = {"name":company.get("name"),
                    "company_id":company.get("id")}
        for branch in all_branches:
            if branch.get("id") in company.get("branches"):
                co_info["branch"] = branch.get("name")
                co_info["branch_id"] = branch.get("id")
        companies_info.append(co_info)

    print(companies_info)