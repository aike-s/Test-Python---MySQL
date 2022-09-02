"""
  2) teniendo en cuenta el punto 1, cree una función que permita
  consultar las sucursales por su id, debe hacerse el mismo procedimiento
  que se realizó en el punto 1, pero, utilizando la función creada
"""
from data import get_branches, get_companies

def consult_branch(branch_ids):
    all_branches = get_branches()
    company_branch = []

    for branche in all_branches:
        if branche.get("id") in branch_ids:
            company_branch.append({"name":branche.get("name"),
                                    "id":branche.get("id")})

    # Returns a list of dicts with the info of the branch 
    # that belongs to the company
    return company_branch

def company_branches():
    all_companies = get_companies()
    companies_branch_info = []

    for company in all_companies:
        branches = {"branches":consult_branch(company.get("branches"))}
        # Now key branch will be a list with the info of the current branch
        company.update(branches)
        companies_branch_info.append(company)

    print(companies_branch_info)