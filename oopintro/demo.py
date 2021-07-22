import datetime as dt
ct = dt.datetime.now()
f1 = ct.strftime("%d-%m-%Y,%A")
print(f1)
x = ''
if ct.strftime('%d') == '01':
    x = 'st'
elif ct.strftime('%d') == '02':
    x = 'nd'
elif ct.strftime('%d') == '03':
    x = 'rd'
elif ct.strftime('%d') == '31':
    x = 'st'
else:
    x = 'th'

print(ct.strftime('On %A,'))
print(ct.strftime('%d'+x+'%b%Y'))
print(ct.strftime('at %I:%M %p'))