# -*- coding: utf8  -*-

import os
import sys
import zipfile
import datetime
import subprocess


now	 = datetime.datetime.now() #data atual

dt = now.strftime('%Y-%m-%d')

def main():

	zipper("C:\DigiSat\GG4\DADOS", "C:\Dropbox\/backupGerencial\/backup_gerencial."+dt+".zip")
	
	
def zipper(dir, zip_file):
    
    zip = zipfile.ZipFile(zip_file, 'w', compression=zipfile.ZIP_DEFLATED)
    root_len = len(os.path.abspath(dir))
    
    print root_len

    print "Aguarde Enquanto o Backup do Gerencial é realizado"
    print "Iniciando Backup do Banco de Dados Gerencial.."

    print "Backup dos aquivos"

    for root, dirs, files in os.walk(dir):
        archive_root = os.path.abspath(root)[root_len:]
        for f in files:
            fullpath = os.path.join(root, f)
            archive_name = os.path.join(archive_root, f)

            #print f
            print 'fullpath'+fullpath
            #print 'archive_name'+archive_name
            #print zipfile.ZIP_DEFLATED

            zip.write(fullpath, archive_name, zipfile.ZIP_DEFLATED)
    zip.close()
    
    print "Backup Finalizado"

    return zip_file

if __name__ == '__main__':

    main()
