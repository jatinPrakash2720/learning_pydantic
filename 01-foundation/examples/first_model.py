from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data = {'id':101, 'name':"ChaiCode",'is_active':True}
# pydantic will try by itself to convert the data type to the declared data type as in above example we can, pydantic converted the 'True' to True which is in boolean, so it did not give any error, 
# TEST CASES !!!!!!
# input_data = {'id':101, 'name':"ChaiCode",'is_active':'sahi'}
# pydantic will try by itself to convert the data type to the declared data type as in above example we can, pydantic can not convert the 'sahi' to True which will be in boolean,so it give error,

# input_data = {'id':101, 'name':"ChaiCode",'is_active':'1'}
#it also worked !!

# input_data = {'id':101, 'name':"ChaiCode",'is_active':1}
#it also worked!!

# input_data = {'id':101, 'name':"ChaiCode",'is_active':10}
#it did not worked!!


user = User(**input_data)

print(user)
