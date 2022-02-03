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

def increase_basic(data):
    for i in data.keys():
        data[i]["salary"]["basic"]=data[i]["salary"]["basic"]+((data[i]["salary"]["basic"])/10)

def filter_record(data):
    filterdata = {}
    for key,value in data.items():
        if (data[key]["personal"]["city"]) == "Ahmedabad":
            filterdata[key]=value
    return filterdata

print("Basic Before Incease :\n")
for i in data:
    print(data[i]["salary"]["basic"])

increase_basic(data)

print("\nBasic After Incease By 10%:\n")
for i in data:
    print(data[i]["salary"]["basic"])

print("\nfilter data : \n")

filter_data = filter_record(data)
print(filter_data)