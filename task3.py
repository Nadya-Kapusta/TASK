import json

def Busca_id (ID_Tests, Values): 
        for thing in Values['values']:
            if thing['id'] == ID_Tests:
                return thing['value']
                
def Condition(smth,data,val_data):
    smth_values=smth.get('values',None)
    if smth_values != None:
        for value in smth_values:
            value['value'] = Busca_id(value['id'], val_data)
            Condition(value,data,val_data)
            with open('report.json', 'w') as json_file:
                json.dump(data, json_file, indent=2)

with open('values.json') as json_file:
    val_data = json.load(json_file)    

with open('tests.json') as json_file:
    data = json.load(json_file)
    tests=data['tests']
    for smth in tests:
        smth['value'] = Busca_id(smth['id'], val_data)
        Condition(smth,data,val_data)                      
    print('Информация записана в файл "report.json"')    