import ftplib
import sys
 
def FTP_JSON_pusher():
    error = 0
    cridentials = []
    try:
        with open('cridentials.txt') as f:
            cridentials = f.readlines()    
            ftpcridserver = cridentials[0].replace("\n","")
            ftpcridusername = cridentials[1].replace('\n','')
            ftpcridpassword = cridentials[2].replace('\n','')

        print(ftpcridserver)

        ftp = ftplib.FTP(ftpcridserver)
        ftp.login(ftpcridusername, ftpcridpassword)

        # öppna filen för att läsa
        with open('albums.json', 'rb') as file:
            ftp.storbinary('STOR albums.json', file)
            print("Filen skall vara uppdaterad")

        ftp.quit()
    except:
        error = -1
    return error
