db={'username':'sravani','password':'sravs@321'}
username=input('enter username')
password=input('enter password')
if db['username']==username and db['password']== password:
    print('valid')
else:
    print('invalid')


