#!C:\Users\91780\AppData\Local\Programs\Python\Python37-32\Python.exe
import webbrowser
import project
import cgi,cgitb
form=cgi.FieldStorage()
print('content-type:text/html\r\n\n')
print('<html>')
print('<head>')
print('</head>')
print('<body style="margin:0;">')
print('<form method="post">')
print('<div style="background-image:url(image1.jpg);width:100%;height:15%;font-size:50;font-color:white"><center>NATIONAL INSTITUTE OF TECHNOLOGY HAMIRPUR</center></div>')
print('<div style="background-image:url(image12.jpg);width:100%;height:85%;font-size:30;">')
print('<div style="width:85%;height:100%;font-size:30;float:right;">')
print('<div style="width:80%;height:100%;font-size:30;float:left;">')
print('<p align="center" style="font-size:30;color:white;margin-left:-4em;">')
print("<b>Branch</b>  : <input type='text' name='Branch'>")
print('<br>')
print("<b>Year  </b> : <input type='text' name='Year'>")
print('<br>')
print('<center><input type="submit" name="submit" value="SUBMIT" style="font-size:0.5em;color:blue;display:block;"></center>')
print('</div>')
print('</div>')
print('</div>')
import copy
if form.getvalue("submit"):
    Branch=form.getvalue("Branch")
    Year=form.getvalue("Year")
    if Branch=='CSE' and Year=='1':
        print('hello')
        a=copy.deepcopy(tt_cs1)
        b=copy.deepcopy(tea_cs1)
        c=copy.deepcopy(room_cs1)
        print('<table border="3">')

        for i in range(0,10):
            print('<tr>')
            for j in range(0,10):
                print('<th>',a[i][j],' <br/> ',b[i][j] ,'<br/> ',c[i][j] ,'</th>')
            print('</tr><tr>')
        print('</table>')
    if Branch=='CSE' and Year=='2':
        a=tt_cs2
        b=tea_cs2
        c=room_cs2
    if Branch=='CSE' and Year=='3':
        a=tt_cs3
        b=tea_cs3
        c=room_cs3
    if Branch=='CSE' and Year=='4':
        a=tt_cs4
        b=tea_cs4
        c=room_cs4
print('</form></body>')
print('</html>')

'''print('content-type:text/html\r\n\n')
print('<html>')
print('<head>')
print('<title>table </title>')
print('</head>')
print('<body>')
print('helllo')
print('<table border="3">')

for i in range(0,10):
    print('<tr>')
    for j in range(0,10):
        print('<th>',a[i][j],' <br/> ',b[i][j] ,'<br/> ',c[i][j] ,'</th>')
    print('</tr><tr>')
print('</table>')
print('</body>')
print('</html>')
'''
