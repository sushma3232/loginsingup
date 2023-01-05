import json
def register():
    enter=input("enter login/signup:")
    if enter=="signup":
        user_name=input("enter the username:")
        password=input("enter the password:")
        p=len(password)
        numbers="0123456789"
        lower_case="abcdefghijklmnopqrstuvwxyz"
        upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        Speacial_char="@#$&"
        i=0
        while i<len(password):
            if password[i] in numbers:
                n=n+1
            if password[i] in lower_case:
                l=l+1
            if password[i] in upper_case:
                u=u+1
            if password[i] in special_char:
                s=s+1
            i=i+1
        if p>=6:
            if n>=1 and l>=1 and s>=1 and u>=1:
                print("strong password")
                conform_password=input("enter conform_password")
                if conform_password==password:
                    print("both passwords are same")
                    des=input("enter the description:")
                    birth=int(input("enter the birth date"))
                    hobbies=input("enter the hobies")
                    gender=input('enter the gender')
                    d1["description"]=des
                    d1["date of birth"]=birth
                    d1["hobbies"]=hobbies
                    d1["gender"]=gender
                    d["username"]=user_name
                    d["password"]=p
                    d["profile"]=d1
                    dic["user"]=[d]
                                
                    print(dic)
                    file= open("signup.json","w")
                    json.dump(dic,file,indent=4)
                    file.close()
                    print("congrats",user_name,"signup successful")
        
                    
                else:
                    print("both passwords are not same")
            else:
                print("password should contain num,lower_case,upper_casespecial character")
        else:
            print("password should contain atleast 6 char")
#                 
#     elif enter=="login":
#         login_user_name=input("enter the user_name:")
#         password=input("enter the password:")
#         a=open("signup1.json","r")
#         f=json.load(a)
         
#         if f["user"][0]["user_name"]==login_user_name:
#             if f["user"][0]["password"]==password:
#                 print("congrats.......successfully login")
#             else:
#                 print("password is wrong try again...")
#         else:
#             print("username is not matching.....")
                
    
register()
                
                
                    
    