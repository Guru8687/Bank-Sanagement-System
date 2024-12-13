sum=0
print('''Language choice number : 
         1 : English 
         2 : Marathi 
         3 : Hindi ''')
Language = int(input("For choosing language Entar language choice number : "))
if (Language  == 1):
    print('''
1 : create Account 
2 : Debit money 
3 : Credit amount
4 : Delete account 
    ''') 
    print("In Given tasks ..... Which task you want to perform ")
    print("If you are new member then first createaccount ")

    tasknum = int(input("Entar your choice : "))

    if (tasknum == 1 ):
        
        name = str(input("Enter your name : "))
        accno = int(input("Create account number : "))
        depositmoney =int(input("Enter ammount :"))
        account_type =input("Account type : 1 : Saving Account  2 : Current Account  :  ")


        print(f'''
Account holder name : {name}
account no :{accno}
acc type : {account_type}
account balence :{depositmoney} ''')
        sum=sum+depositmoney
    def state1():
        for i in range(1,100):
    
            operation = int(input('''
1 : Debit money 
2 : Credit amount
3 : Delete account 
Entar opration number :'''))
                
                
            if (operation==1):
               amount = int(input("Enter amount :"))
               sum= sum - amount
               print("Account balence is :",sum)
               
            elif(operation == 2):
                amnt = int(input("Enter amount :"))
                sum = sum+amnt
                print("Available balence is : ",sum)
            elif (operation == 3):
                accno = ("Entar account number :")
                if tasknum ==1:
                    print("Your account is deleted.")
                else:
                    print("Account does not exist.")
            else:
                print("Invalid opration number .")
    conti = str(input("Do you want to continue the proccess (Y/N):")).lower
    if conti=='y':
        state1()
        print("-----------Thank you for continue the proccess ------------")
    else: 
        print("--------------Thank you for visiting------------------")
                
elif (Language == 2 ):
        i=0
        while(i==1):
            print('''
1 : खाते तयार करा 
२ : डेबिट मनी 
3 : क्रेडिट रक्कम
४ : अकाऊंट डिलीट करा
                ''')
            
            print("दिलेल्या कामांमध्ये ..... तुम्हाला कोणते काम करायचे आहे. ")
            print("जर तुम्ही नवीन सदस्य असाल तर आधी खाते तयार करा. ")
        
            tasknum = int(input("आपली निवड प्रविष्ट करा : "))
        
            if (tasknum == 1 ):
                name = chr(input("आपले नाव प्रविष्ट करा : "))
                accno = int(input("खाते क्रमांक तयार करा : "))
                acctype = chr(input("खात्याचा प्रकार : १ : सेव्हिंग खाते २ : चालू खाते  :  "))
                depositmoney =int(input("रक्कम प्रविष्ट करा :"))
        
                print(f'''
                    खातेदाराचे नाव : {name}
                    खाते क्रमांक  : {accno}
                    खाते प्रकार : {acctype}
                    अकाऊंट बॅलन्स : {depositmoney}
                      ''')
                opration = int(input('''
                    १ : डेबिट मनी 
                    2 : क्रेडिट रक्कम
                    ३ : अकाऊंट डिलीट करा 
                    ऑपरेशन नंबर प्रविष्ट करा :'''))
        
                if (opration == 1):
                    amount = str(input("रक्कम प्रविष्ट करा :"))
                    sum= sum - amount
                    print("उपलब्ध शिल्लक :",sum)
                elif (opration == 2):
                    amnt = str(input("रक्कम प्रविष्ट करा :"))
                    sum = sum+amnt
                    print("उपलब्ध शिल्लक :",sum)
                elif(opration == 3):
                    accno = ("खाते क्रमांक प्रविष्ट करा :")
                    if tasknum ==1:
                        print("तुमचे अकाऊंट डिलीट झाले आहे.")
                    else:
                        print("खाते अस्तित्वात नाही.")
                else:
                    print("अवैध ओप्रेशन नंबर .")
                a=input(print('''Do you want to continue the proccess for new member(Yes/No) :
                 1: Yes
                 2: No'''))
                if (a==1):
                    i==1
                else:
                    i==2
                    break
                    
elif (Language == 3):
        i=0
        while(i==1):
            print('''
1: खाता बनाएँ 
2 : डेबिट मनी 
3 : क्रेडिट राशि
4: खाता हटाएं 
                    ''')
            
            print("दिए गए कार्यों में ..... आप कौन सा कार्य करना चाहते हैं ")
            print("अगर आप नए मेंबर हैं तो पहले अकाउंट बनाएं ")
        
            tasknum = int(input("अपनी पसंद को एंटर करें : "))
         
            if (tasknum == 1 ):
               name = str(input("अपना नाम दर्ज करें : "))
               accno = int(input("खाता संख्या बनाएं : "))
               acctype = str(input("खाते का प्रकार : 1 : बचत खाता 2 : चालू खाता  :  "))
               depositmoney =int(input("राशि दर्ज करें :"))
        
               print(f'''
खाताधारक का नाम : {name}
खाता संख्या : {accno}
खाता प्रकार : {acctype}
खाते की शेष राशि : {depositmoney}
                    ''')
            opration = int(input('''
1 : डेबिट मनी 
2 : क्रेडिट राशि
3 : खाता हटाएं 
ऑपरेशन नंबर दर्ज करें :'''))
            if (opration == 1):
                    amount = int(input("राशि दर्ज करें :  "))
                    sum= sum - amount
                    print("उपलब्ध शेष राशि : ",sum)
            elif (opration == 2):
                    amnt =int(input("राशि दर्ज करें :"))
                    sum = sum+amnt
                    print(" उपलब्ध शेष राशि :",sum)
            elif (opration == 3):
                    accno = ("खाता संख्या दर्ज करें :")
                    if tasknum ==1:
                        print("आपका खाता हटा दिया गया है.")
                    else:
                        print("खाता मौजूद नहीं है.")
            else:
                    print("अमान्य ऑपरेशन नंबर .")
                
            a=input(print('''Do you want to continue the proccess for new member(Yes/No) :
                     1: Yes
                     2: No'''))
            if (a==2):
                break
        else :
            print("अमान्य इनपुट ..... कृपया पुनः प्रयास करें.")
             
            