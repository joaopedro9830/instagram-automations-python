from re import search
from tasks import like

def chooseTask(login, password):

    # Initialize variables
    searchObject = ''
    citys = []

    print('What do you want?')
    print('')
    print('1 - Like by hashtag')
    print('')
    print('2 - Like by location')
    print('')
    
    numberOption = int(input('Enter the option number you want: '))
    
    print('')
    
    if numberOption == 1:
        searchObject = input('Enter the hashtag you want: #')
    elif numberOption == 2:
        searchObject = input('Enter the first location you want: ')
        citys.append(searchObject)
        
        print('')
        
        searchObject = input('Enter the second location you want: ')
        citys.append(searchObject)
        
        print('')
          
        searchObject = input('Enter the third location you want: ')
        citys.append(searchObject)
        
        print('')
        
        searchObject = input('Enter the fourth location you want: ')
        citys.append(searchObject)
        
        print('')
        
        searchObject = input('Enter the fifth location you want: ')
        citys.append(searchObject)  
        
    print('')
    
    message = input('Inform the message you want to send to your followers: ')
    
    print('')
    
    like.likeTask(login, password, numberOption, citys, message)


print('')
print('Running automation program in version: 1.1.2')
print('')
login = input('Inform your login: ')
print('')
password = input('Inform your password: ')
print('')

chooseTask(login, password)