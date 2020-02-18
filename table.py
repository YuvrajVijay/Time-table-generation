#!C:\Users\91780\AppData\Local\Programs\Python\Python37-32\Python.exe
import webbrowser
from project import *
print('content-type:text/html\r\n\n')
print('<html>')
print('<head>')
print('<title>table </title>')
print('</head>')
print('<body>')


print('<table border="3">')
print('<br/><br/>')
print('<tr><td colspan="11">CSE 2nd Year</td></tr>')
print('<tr><th>Time</th><th>8:00-9:00</th><th>9:00-10:00</th><th>10:00-11:00</th><th>11:00-12:00</th><th>12:00-1:00</th><th>1:00-2:00</th><th>2:00-3:00</th><th>3:00-4:00</th><th>4:00-5:00</th><th>5:00-6:00</th></tr>')
for i in range(0,10):
    print('<tr>')
    if i%2==1:
        print('<th><br/>G2<br/></th>')
    if i%2==0:
        print('<th><br/>G1<br/></th>')
    for j in range(0,10):
        print('<th>',tt_cs2[i][j],' <br/> ',tea_cs2[i][j] ,'<br/> ',rooms_cs2[i][j] ,'</th>')
    print('</tr><tr>')
print('</table>')


print('<table border="3">')
print('<tr><td colspan="11">CSE 1st Year</td></tr>')
print('<tr><th>Time</th><th>8:00-9:00</th><th>9:00-10:00</th><th>10:00-11:00</th><th>11:00-12:00</th><th>12:00-1:00</th><th>1:00-2:00</th><th>2:00-3:00</th><th>3:00-4:00</th><th>4:00-5:00</th><th>5:00-6:00</th></tr>')
for i in range(0,10):
    print('<tr>')
    if i%2==1:
        print('<th><br/>G2<br/></th>')
    if i%2==0:
        print('<th><br/>G1<br/></th>')
    for j in range(0,10):
        print('<th>',tt_cs1[i][j],' <br/> ',tea_cs1[i][j] ,'<br/> ',rooms_cs1[i][j] ,'</th>')
    print('</tr><tr>')
print('</table>')


print('<table border="3">')
print('<br/><br/>')
print('<tr><td colspan="11">CSE 3rd Year</td></tr>')
print('<tr><th>Time</th><th>8:00-9:00</th><th>9:00-10:00</th><th>10:00-11:00</th><th>11:00-12:00</th><th>12:00-1:00</th><th>1:00-2:00</th><th>2:00-3:00</th><th>3:00-4:00</th><th>4:00-5:00</th><th>5:00-6:00</th></tr>')
for i in range(0,10):
    print('<tr>')
    if i%2==1:
        print('<th><br/>G2<br/></th>')
    if i%2==0:
        print('<th><br/>G1<br/></th>')
    for j in range(0,10):
        print('<th>',tt_cs3[i][j],' <br/> ',tea_cs3[i][j] ,'<br/> ',rooms_cs3[i][j] ,'</th>')
    print('</tr><tr>')
print('</table>')



print('<table border="3">')
print('<br/><br/>')
print('<tr><td colspan="11">CSE 4th Year</td></tr>')
print('<tr><th>Time</th><th>8:00-9:00</th><th>9:00-10:00</th><th>10:00-11:00</th><th>11:00-12:00</th><th>12:00-1:00</th><th>1:00-2:00</th><th>2:00-3:00</th><th>3:00-4:00</th><th>4:00-5:00</th><th>5:00-6:00</th></tr>')
for i in range(0,10):
    print('<tr>')
    if i%2==1:
        print('<th><br/>G2<br/></th>')
    if i%2==0:
        print('<th><br/>G1<br/></th>')
    for j in range(0,10):
        print('<th>',tt_cs4[i][j],' <br/> ',tea_cs4[i][j] ,'<br/> ',rooms_cs4[i][j] ,'</th>')
    print('</tr><tr>')
print('</table>')


print('<table border="3">')
print('<br/><br/>')
print('<tr><td colspan="11">EE 1st Year</td></tr>')
print('<tr><th>Time</th><th>8:00-9:00</th><th>9:00-10:00</th><th>10:00-11:00</th><th>11:00-12:00</th><th>12:00-1:00</th><th>1:00-2:00</th><th>2:00-3:00</th><th>3:00-4:00</th><th>4:00-5:00</th><th>5:00-6:00</th></tr>')
for i in range(0,10):
    print('<tr>')
    if i%2==1:
        print('<th><br/>G2<br/></th>')
    if i%2==0:
        print('<th><br/>G1<br/></th>')
    for j in range(0,10):
        print('<th>',tt_ee1[i][j],' <br/> ',tea_ee1[i][j] ,'<br/> ',rooms_ee1[i][j] ,'</th>')
    print('</tr><tr>')
print('</table>')



print('<table border="3">')
print('<br/><br/>')
print('<tr><td colspan="11">EE 2nd Year</td></tr>')
print('<tr><th>Time</th><th>8:00-9:00</th><th>9:00-10:00</th><th>10:00-11:00</th><th>11:00-12:00</th><th>12:00-1:00</th><th>1:00-2:00</th><th>2:00-3:00</th><th>3:00-4:00</th><th>4:00-5:00</th><th>5:00-6:00</th></tr>')
for i in range(0,10):
    print('<tr>')
    if i%2==1:
        print('<th><br/>G2<br/></th>')
    if i%2==0:
        print('<th><br/>G1<br/></th>')
    for j in range(0,10):
        print('<th>',tt_ee2[i][j],' <br/> ',tea_ee2[i][j] ,'<br/> ',rooms_ee2[i][j] ,'</th>')
    print('</tr><tr>')
print('</table>')


print('<table border="3">')
print('<br/><br/>')
print('<tr><td colspan="11">EE 3rd Year</td></tr>')
print('<tr><th>Time</th><th>8:00-9:00</th><th>9:00-10:00</th><th>10:00-11:00</th><th>11:00-12:00</th><th>12:00-1:00</th><th>1:00-2:00</th><th>2:00-3:00</th><th>3:00-4:00</th><th>4:00-5:00</th><th>5:00-6:00</th></tr>')
for i in range(0,10):
    print('<tr>')
    if i%2==1:
        print('<th><br/>G2<br/></th>')
    if i%2==0:
        print('<th><br/>G1<br/></th>')
    for j in range(0,10):
        print('<th>',tt_ee3[i][j],' <br/> ',tea_ee3[i][j] ,'<br/> ',rooms_ee3[i][j] ,'</th>')
    print('</tr><tr>')
print('</table>')


print('<table border="3">')
print('<br/><br/>')
print('<tr><td colspan="11">EE 4th Year</td></tr>')
print('<tr><th>Time</th><th>8:00-9:00</th><th>9:00-10:00</th><th>10:00-11:00</th><th>11:00-12:00</th><th>12:00-1:00</th><th>1:00-2:00</th><th>2:00-3:00</th><th>3:00-4:00</th><th>4:00-5:00</th><th>5:00-6:00</th></tr>')
for i in range(0,10):
    print('<tr>')
    if i%2==1:
        print('<th><br/>G2<br/></th>')
    if i%2==0:
        print('<th><br/>G1<br/></th>')
    for j in range(0,10):
        print('<th>',tt_ee4[i][j],' <br/> ',tea_ee4[i][j] ,'<br/> ',rooms_ee4[i][j] ,'</th>')
    print('</tr><tr>')
print('</table>')


print('<table border="3">')
print('<br/><br/>')
print('<tr><td colspan="11">Chemical 1st Year</td></tr>')
print('<tr><th>Time</th><th>8:00-9:00</th><th>9:00-10:00</th><th>10:00-11:00</th><th>11:00-12:00</th><th>12:00-1:00</th><th>1:00-2:00</th><th>2:00-3:00</th><th>3:00-4:00</th><th>4:00-5:00</th><th>5:00-6:00</th></tr>')
for i in range(0,10):
    print('<tr>')
    if i%2==1:
        print('<th><br/>G2<br/></th>')
    if i%2==0:
        print('<th><br/>G1<br/></th>')
    for j in range(0,10):
        print('<th>',tt_ch1[i][j],' <br/> ',tea_ch1[i][j] ,'<br/> ',rooms_ch1[i][j] ,'</th>')
    print('</tr><tr>')
print('</table>')


print('<table border="3">')
print('<br/><br/>')
print('<tr><td colspan="11">Chemical 2nd Year</td></tr>')
print('<tr><th>Time</th><th>8:00-9:00</th><th>9:00-10:00</th><th>10:00-11:00</th><th>11:00-12:00</th><th>12:00-1:00</th><th>1:00-2:00</th><th>2:00-3:00</th><th>3:00-4:00</th><th>4:00-5:00</th><th>5:00-6:00</th></tr>')
for i in range(0,10):
    print('<tr>')
    if i%2==1:
        print('<th><br/>G2<br/></th>')
    if i%2==0:
        print('<th><br/>G1<br/></th>')
    for j in range(0,10):
        print('<th>',tt_ch2[i][j],' <br/> ',tea_ch2[i][j] ,'<br/> ',rooms_ch2[i][j] ,'</th>')
    print('</tr><tr>')
print('</table>')



print('<table border="3">')
print('<br/><br/>')
print('<tr><td colspan="11">Chemical 3rd Year</td></tr>')
print('<tr><th>Time</th><th>8:00-9:00</th><th>9:00-10:00</th><th>10:00-11:00</th><th>11:00-12:00</th><th>12:00-1:00</th><th>1:00-2:00</th><th>2:00-3:00</th><th>3:00-4:00</th><th>4:00-5:00</th><th>5:00-6:00</th></tr>')
for i in range(0,10):
    print('<tr>')
    if i%2==1:
        print('<th><br/>G2<br/></th>')
    if i%2==0:
        print('<th><br/>G1<br/></th>')
    for j in range(0,10):
        print('<th>',tt_ch3[i][j],' <br/> ',tea_ch3[i][j] ,'<br/> ',rooms_ch3[i][j] ,'</th>')
    print('</tr><tr>')
print('</table>')



"""
print('<table border="3">')
print('<br/><br/>')
for i in range(0,10):
    print('<tr>')
    if i%2==1:
        print('<th><br/>G2<br/></th>')
    if i%2==0:
        print('<th><br/>G1<br/></th>')
    for j in range(0,10):
        print('<th>',tt_ch4[i][j],' <br/> ',tea_ch4[i][j] ,'<br/> ',rooms_ch4[i][j] ,'</th>')
    print('</tr><tr>')
print('</table>')

"""

print('<table border="3">')
print('<br/><br/>')
print('<tr><td colspan="11">Material science 1st Year</td></tr>')
print('<tr><th>Time</th><th>8:00-9:00</th><th>9:00-10:00</th><th>10:00-11:00</th><th>11:00-12:00</th><th>12:00-1:00</th><th>1:00-2:00</th><th>2:00-3:00</th><th>3:00-4:00</th><th>4:00-5:00</th><th>5:00-6:00</th></tr>')
for i in range(0,10):
    print('<tr>')
    if i%2==1:
        print('<th><br/>G2<br/></th>')
    if i%2==0:
        print('<th><br/>G1<br/></th>')
    for j in range(0,10):
        print('<th>',tt_ms1[i][j],' <br/> ',tea_ms1[i][j] ,'<br/> ',rooms_ms1[i][j] ,'</th>')
    print('</tr><tr>')
print('</table>')



print('<table border="3">')
print('<br/><br/>')
print('<tr><td colspan="11">Material science 2nd Year</td></tr>')
print('<tr><th>Time</th><th>8:00-9:00</th><th>9:00-10:00</th><th>10:00-11:00</th><th>11:00-12:00</th><th>12:00-1:00</th><th>1:00-2:00</th><th>2:00-3:00</th><th>3:00-4:00</th><th>4:00-5:00</th><th>5:00-6:00</th></tr>')
for i in range(0,10):
    print('<tr>')
    if i%2==1:
        print('<th><br/>G2<br/></th>')
    if i%2==0:
        print('<th><br/>G1<br/></th>')
    for j in range(0,10):
        print('<th>',tt_ms2[i][j],' <br/> ',tea_ms2[i][j] ,'<br/> ',rooms_ms2[i][j] ,'</th>')
    print('</tr><tr>')
print('</table>')



print('<table border="3">')
print('<br/><br/>')
print('<tr><td colspan="11">Material science 3rd Year</td></tr>')
print('<tr><th>Time</th><th>8:00-9:00</th><th>9:00-10:00</th><th>10:00-11:00</th><th>11:00-12:00</th><th>12:00-1:00</th><th>1:00-2:00</th><th>2:00-3:00</th><th>3:00-4:00</th><th>4:00-5:00</th><th>5:00-6:00</th></tr>')
for i in range(0,10):
    print('<tr>')
    if i%2==1:
        print('<th><br/>G2<br/></th>')
    if i%2==0:
        print('<th><br/>G1<br/></th>')
    for j in range(0,10):
        print('<th>',tt_ms3[i][j],' <br/> ',tea_ms3[i][j] ,'<br/> ',rooms_ms3[i][j] ,'</th>')
    print('</tr><tr>')
print('</table>')

"""
 
print('<table border="3">')
print('<br/><br/>')
for i in range(0,10):
    print('<tr>')
    if i%2==1:
        print('<th><br/>G2<br/></th>')
    if i%2==0:
        print('<th><br/>G1<br/></th>')
    for j in range(0,10):
        print('<th>',tt_ms4[i][j],' <br/> ',tea_ms4[i][j] ,'<br/> ',rooms_ms4[i][j] ,'</th>')
    print('</tr><tr>')
print('</table>')
"""



print('<table border="3">')
print('<br/><br/>')
print('<tr><td colspan="11">Mechanical Engineer 1st Year</td></tr>')
print('<tr><th>Time</th><th>8:00-9:00</th><th>9:00-10:00</th><th>10:00-11:00</th><th>11:00-12:00</th><th>12:00-1:00</th><th>1:00-2:00</th><th>2:00-3:00</th><th>3:00-4:00</th><th>4:00-5:00</th><th>5:00-6:00</th></tr>')
for i in range(0,10):
    print('<tr>')
    if i%2==1:
        print('<th><br/>G2<br/></th>')
    if i%2==0:
        print('<th><br/>G1<br/></th>')
    for j in range(0,10):
        print('<th>',tt_me1[i][j],' <br/> ',tea_me1[i][j] ,'<br/> ',rooms_me1[i][j] ,'</th>')
    print('</tr><tr>')
print('</table>')




print('<table border="3">')
print('<br/><br/>')
print('<tr><td colspan="11">Mechanical Engineer 2nd Year</td></tr>')
print('<tr><th>Time</th><th>8:00-9:00</th><th>9:00-10:00</th><th>10:00-11:00</th><th>11:00-12:00</th><th>12:00-1:00</th><th>1:00-2:00</th><th>2:00-3:00</th><th>3:00-4:00</th><th>4:00-5:00</th><th>5:00-6:00</th></tr>')
for i in range(0,10):
    print('<tr>')
    if i%2==1:
        print('<th><br/>G2<br/></th>')
    if i%2==0:
        print('<th><br/>G1<br/></th>')
    for j in range(0,10):
        print('<th>',tt_me2[i][j],' <br/> ',tea_me2[i][j] ,'<br/> ',rooms_me2[i][j] ,'</th>')
    print('</tr><tr>')
print('</table>')





print('<table border="3">')
print('<br/><br/>')
print('<tr><td colspan="11">Mechanical Engineer 3rd Year</td></tr>')
print('<tr><th>Time</th><th>8:00-9:00</th><th>9:00-10:00</th><th>10:00-11:00</th><th>11:00-12:00</th><th>12:00-1:00</th><th>1:00-2:00</th><th>2:00-3:00</th><th>3:00-4:00</th><th>4:00-5:00</th><th>5:00-6:00</th></tr>')
for i in range(0,10):
    print('<tr>')
    if i%2==1:
        print('<th><br/>G2<br/></th>')
    if i%2==0:
        print('<th><br/>G1<br/></th>')
    for j in range(0,10):
        print('<th>',tt_me3[i][j],' <br/> ',tea_me3[i][j] ,'<br/> ',rooms_me3[i][j] ,'</th>')
    print('</tr><tr>')
print('</table>')




print('<table border="3">')
print('<br/><br/>')
print('<tr><td colspan="11">Mechanical Engineer 4th Year</td></tr>')
print('<tr><th>Time</th><th>8:00-9:00</th><th>9:00-10:00</th><th>10:00-11:00</th><th>11:00-12:00</th><th>12:00-1:00</th><th>1:00-2:00</th><th>2:00-3:00</th><th>3:00-4:00</th><th>4:00-5:00</th><th>5:00-6:00</th></tr>')
for i in range(0,10):
    print('<tr>')
    if i%2==1:
        print('<th><br/>G2<br/></th>')
    if i%2==0:
        print('<th><br/>G1<br/></th>')
    for j in range(0,10):
        print('<th>',tt_me4[i][j],' <br/> ',tea_me4[i][j] ,'<br/> ',rooms_me4[i][j] ,'</th>')
    print('</tr><tr>')
print('</table>')




print('<table border="3">')
print('<br/><br/>')
print('<tr><td colspan="11">ECE 1st Year</td></tr>')
print('<tr><th>Time</th><th>8:00-9:00</th><th>9:00-10:00</th><th>10:00-11:00</th><th>11:00-12:00</th><th>12:00-1:00</th><th>1:00-2:00</th><th>2:00-3:00</th><th>3:00-4:00</th><th>4:00-5:00</th><th>5:00-6:00</th></tr>')
for i in range(0,10):
    print('<tr>')
    if i%2==1:
        print('<th><br/>G2<br/></th>')
    if i%2==0:
        print('<th><br/>G1<br/></th>')
    for j in range(0,10):
        print('<th>',tt_ec1[i][j],' <br/> ',tea_ec1[i][j] ,'<br/> ',rooms_ec1[i][j] ,'</th>')
    print('</tr><tr>')
print('</table>')




print('<table border="3">')
print('<br/><br/>')
print('<tr><td colspan="11">ECE 2nd Year</td></tr>')
print('<tr><th>Time</th><th>8:00-9:00</th><th>9:00-10:00</th><th>10:00-11:00</th><th>11:00-12:00</th><th>12:00-1:00</th><th>1:00-2:00</th><th>2:00-3:00</th><th>3:00-4:00</th><th>4:00-5:00</th><th>5:00-6:00</th></tr>')
for i in range(0,10):
    print('<tr>')
    if i%2==1:
        print('<th><br/>G2<br/></th>')
    if i%2==0:
        print('<th><br/>G1<br/></th>')
    for j in range(0,10):
        print('<th>',tt_ec2[i][j],' <br/> ',tea_ec2[i][j] ,'<br/> ',rooms_ec2[i][j] ,'</th>')
    print('</tr><tr>')
print('</table>')




print('<table border="3">')
print('<br/><br/>')
print('<tr><td colspan="11">ECE 3rd Year</td></tr>')
print('<tr><th>Time</th><th>8:00-9:00</th><th>9:00-10:00</th><th>10:00-11:00</th><th>11:00-12:00</th><th>12:00-1:00</th><th>1:00-2:00</th><th>2:00-3:00</th><th>3:00-4:00</th><th>4:00-5:00</th><th>5:00-6:00</th></tr>')
for i in range(0,10):
    print('<tr>')
    if i%2==1:
        print('<th><br/>G2<br/></th>')
    if i%2==0:
        print('<th><br/>G1<br/></th>')
    for j in range(0,10):
        print('<th>',tt_ec3[i][j],' <br/> ',tea_ec3[i][j] ,'<br/> ',rooms_ec3[i][j] ,'</th>')
    print('</tr><tr>')
print('</table>')




print('<table border="3">')
print('<br/><br/>')
print('<tr><td colspan="11">ECE 4th Year</td></tr>')
print('<tr><th>Time</th><th>8:00-9:00</th><th>9:00-10:00</th><th>10:00-11:00</th><th>11:00-12:00</th><th>12:00-1:00</th><th>1:00-2:00</th><th>2:00-3:00</th><th>3:00-4:00</th><th>4:00-5:00</th><th>5:00-6:00</th></tr>')
for i in range(0,10):
    print('<tr>')
    if i%2==1:
        print('<th><br/>G2<br/></th>')
    if i%2==0:
        print('<th><br/>G1<br/></th>')
    for j in range(0,10):
        print('<th>',tt_ec4[i][j],' <br/> ',tea_ec4[i][j] ,'<br/> ',rooms_ec4[i][j] ,'</th>')
    print('</tr><tr>')
print('</table>')





print('<table border="3">')
print('<br/><br/>')
print('<tr><td colspan="11">Chemical 1st Year</td></tr>')
print('<tr><th>Time</th><th>8:00-9:00</th><th>9:00-10:00</th><th>10:00-11:00</th><th>11:00-12:00</th><th>12:00-1:00</th><th>1:00-2:00</th><th>2:00-3:00</th><th>3:00-4:00</th><th>4:00-5:00</th><th>5:00-6:00</th></tr>')
for i in range(0,10):
    print('<tr>')
    if i%2==1:
        print('<th><br/>G2<br/></th>')
    if i%2==0:
        print('<th><br/>G1<br/></th>')
    for j in range(0,10):
        print('<th>',tt_ce1[i][j],' <br/> ',tea_ce1[i][j] ,'<br/> ',rooms_ce1[i][j] ,'</th>')
    print('</tr><tr>')
print('</table>')





print('<table border="3">')
print('<br/><br/>')
print('<tr><td colspan="11">Chemical 2nd Year</td></tr>')
print('<tr><th>Time</th><th>8:00-9:00</th><th>9:00-10:00</th><th>10:00-11:00</th><th>11:00-12:00</th><th>12:00-1:00</th><th>1:00-2:00</th><th>2:00-3:00</th><th>3:00-4:00</th><th>4:00-5:00</th><th>5:00-6:00</th></tr>')
for i in range(0,10):
    print('<tr>')
    if i%2==1:
        print('<th><br/>G2<br/></th>')
    if i%2==0:
        print('<th><br/>G1<br/></th>')
    for j in range(0,10):
        print('<th>',tt_ce2[i][j],' <br/> ',tea_ce2[i][j] ,'<br/> ',rooms_ce2[i][j] ,'</th>')
    print('</tr><tr>')
print('</table>')




print('<table border="3">')
print('<br/><br/>')
print('<tr><td colspan="11">Chemical 3rd Year</td></tr>')
print('<tr><th>Time</th><th>8:00-9:00</th><th>9:00-10:00</th><th>10:00-11:00</th><th>11:00-12:00</th><th>12:00-1:00</th><th>1:00-2:00</th><th>2:00-3:00</th><th>3:00-4:00</th><th>4:00-5:00</th><th>5:00-6:00</th></tr>')
for i in range(0,10):
    print('<tr>')
    if i%2==1:
        print('<th><br/>G2<br/></th>')
    if i%2==0:
        print('<th><br/>G1<br/></th>')
    for j in range(0,10):
        print('<th>',tt_ce3[i][j],' <br/> ',tea_ce3[i][j] ,'<br/> ',rooms_ce3[i][j] ,'</th>')
    print('</tr><tr>')
print('</table>')



"""
print('<table border="3">')
print('<br/><br/>')
print('<tr><th>Time</th><th>8:00-9:00</th><th>9:00-10:00</th><th>10:00-11:00</th><th>11:00-12:00</th><th>12:00-1:00</th><th>1:00-2:00</th><th>2:00-3:00</th><th>3:00-4:00</th><th>4:00-5:00</th><th>5:00-6:00</th></tr>')
for i in range(0,10):
    print('<tr>')
    if i%2==1:
        print('<th><br/>G2<br/></th>')
    if i%2==0:
        print('<th><br/>G1<br/></th>')
    for j in range(0,10):
        print('<th>',tt_ce4[i][j],' <br/> ',tea_ce4[i][j] ,'<br/> ',rooms_ce4[i][j] ,'</th>')
    print('</tr><tr>')
print('</table>')

"""


print('</body>')
print('</html>')

