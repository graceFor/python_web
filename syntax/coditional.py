user_id = input('id?')
user_pwd = input('password?')
 
'''
if user_pwd == '111111':
    print('Hello master')
else:
    print('Who are you?')
'''
'''
user_id == 'egoing'인 경우 :
    user_pwd == '111111'인 경우 :
        인쇄 ( 'Hello master')
    그밖에:
        print ( '누구 니?')
그밖에:
    print ( '누구 니?')
'''

if user_id  ==  'egoing'  and  user_pwd  ==  '111111' :
    print( 'Hello master' )
elif  user_id  ==  'leezche'  and  user_pwd  ==  '222' :
    print( 'Hello master' )
else :
    print( '당신은 누구십니까?' )