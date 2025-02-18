# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 16:55:29 2023

@author: Arribaat
"""
import os
import getpass
import json

#var penyimpanan data user sementara
stripvar = "---------------------"

def greeting():
    os.system('cls')
    print(stripvar*4)
    print("Selamat datang di Wallabi ".center(90))
    print("Konsultan keuangan digital".center(90))
    print(stripvar*4)
    print("")

def init():
    print("1. Login")
    print("2. Sign Up")
    choice = int(input("Pilih menu: "))
    if choice == 1:
        greeting()
        login()
        
    elif choice == 2:
        greeting()
        sign_up()
        
    else:
        print("Invalid choice.\nSilahkan masukkan 1 atau 2")
        
def sign_up():
    client = {"password":""}
    username = input("Masukkan username: ")
    password = getpass.getpass("Masukkan password: ")
    konfirmasi = getpass.getpass("Konfirmasi password: ")
    if konfirmasi == password:
        greeting()
        print("Sandi cocok")
        client["password"] = password
        
        with open(username + ".json",'x') as file:
            json.dump(client,file)
        
        init()
            
    else:
        greeting()
        print("Sandi tidak cocok")
        init()

def login():
    
    username = input("Masukkan username: ")
    
    try :
        with open(username + ".json") as datauser:
            data_user = json.load(datauser)
        file_exist = True
    except:
        file_exist =  False
    
    if file_exist == True :
        password = getpass.getpass("Masukkan password: ")
        if password == data_user["password"] :
            print("Login Berhasil!")
            
        else :
            greeting()
            print("Login Gagal, mohon ingat password anda")
            print("")
            init()
            
    elif file_exist == False:
        greeting()
        print("Username Tidak Ditemukan")
        print("")
        init()

greeting()        
init()

#write data di akhir program ketika program berhenti
#selama program masih berjalan, maka data akan disimpan variabel di dalam terminal
