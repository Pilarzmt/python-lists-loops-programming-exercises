
names = ['Liam','Emma','Noah','Olivia','William','Ava','James','Isabella','Logan','Sophia',
'Benjamin','Mia','Mason','Charlotte','Elijah','Amelia','Oliver','Evelyn','Jacob','Abigail',
'Lucas','Harper','Michael','Emily','Alexander','Elizabeth','Ethan','Avery','Daniel','Sofia',
'Matthew','Ella','Aiden','Madison','Henry','Scarlett','Joseph','Victoria','Jackson','Aria',
'Samuel','Grace','Sebastian','Chloe','David','Camila','Carter','Penelope','Wyatt','Riley']


#Your code go here:
def filter_names_with_string(names, search_string):
    filtered_names = [name for name in names if search_string.lower() in name.lower()]
    return filtered_names
given_string = 'am'
result = filter_names_with_string(names, given_string)
print(result)