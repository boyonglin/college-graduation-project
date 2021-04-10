import pickle

with open('usrs_info.pickle', 'rb') as usr_file:
    usrs_info = pickle.load(usr_file)
    
print(usrs_info)
