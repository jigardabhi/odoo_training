data = {
101 : {'personal':{'name':'ABC', 'city':'Ahmedabad'},
         'salary':{'basic':5000, 'allowance':500, 'deductions': 50}},
102 : {'personal':{'name':'ABC', 'city':'Delhi'},
         'salary':{'basic':7000, 'allowance':700, 'deductions': 70}},
103 : {'personal':{'name':'DEF', 'city':'Ahmedabad'},
         'salary':{'basic':4000, 'allowance':400, 'deductions': 40}},
104 : {'personal':{'name':'GHI', 'city':'Ahmedabad'},
         'salary':{'basic':2000, 'allowance':200, 'deductions': 20}},
105 : {'personal':{'name':'DEF', 'city':'Delhi'},
         'salary':{'basic':1000, 'allowance':100, 'deductions': 10}
}}

def tax_in_salary():

    for k,v in data.items():
        v['salary']["tax"]= v['salary']["allowance"] * 10 / 100

a=tax_in_salary()
print(data)