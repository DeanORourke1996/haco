from ftplib import FTP


ftp = FTP('ba1.geog.umd.edu', 'user', 'burnt_area')
ftp.login()
ftp.cwd('gfed4')
ftp.retrlines('LIST')

with open('README', 'wb') as fp:
    ftp.retrbinary('RETR README', fp.write)

ftp.quit()
