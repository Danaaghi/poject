def ThankYouForUsing ():
      print('Thank you for using our program ')
def wellcome():
    print('     * * * * * * wellcome to intersts program* * * * * * * * ')

    x = input('what you intrest about ' +str(intrect)+" :")

    if x == '1' :
      print(*CategoriesBook,sep="\n")
      
      input5 = input('Choice categories that you , Interested about : ' )
      if (input5 =='1'):
        print(*BookCriminal ,sep='\n')
        ThankYouForUsing()
        WantToAdd()
      elif(input5 =='2'):
       print(*BookEducation ,sep='\n')
       ThankYouForUsing()
       WantToAdd()
       wellcome()
      elif (input5 =='3'):
       print(*BookLiterary,sep='\n')
       ThankYouForUsing()
       WantToAdd()
       wellcome()
      elif(input5=='4'):
       print(*BookDrama,sep="\n")
       ThankYouForUsing()
       WantToAdd()
       wellcome()

               


    elif x== '2':
       print(*Music,sep='\n')
       input6 = input('Choice categories that you , Interested about : ')
       if input6 =='1':
        print(*classicalMusic,sep='\n')
        WantToAdd()
        
       elif input6 =='2':
        print(*RockMusic,sep='\n')
        WantToAdd()
       elif input6 =='3':
          print(*CalmMusic,sep='\n')
          WantToAdd()




    elif x== '3':
       print(*movies,sep="\n")
       input7 = input('Choice categories that you , Interested about : ')
       if input7 =='1':
          print(*moviesAction,sep="\n")
          WantToAdd()
       elif input7 =='2':
         print(*moviesDrama ,sep ="\n")
         WantToAdd()
       elif input7 =='3':
          print(*moviesScience , sep="\n")
    else:
       print("")    
    WantToAdd()  
    
     

def Thank():
   print("thank you for adding new sug")



def WantToAdd():
    input1 = input("-You want to add A sug? ")
    if input1 =='yes':
        print(intrect)
        input2 = input("-where you want to add ")

        if input2=='1':
            print(*CategoriesBook ,sep='\n')
            input3 = input("what the category you want to add : ")

            if input3 == '1':
             item = input(str("enter the name of the criminal book : "))
             BookCriminal.append(item)
             print(*BookCriminal,sep="\n")
             Thank()
             wellcome()  

            elif input3 =='2':
             item = input(str("enter the name of the literary book : "))
             BookLiterary.append(item)
             print(*BookLiterary,sep='\n')
             Thank()
             wellcome() 
            elif input3 =='3':
             item = input(str("enter the name of the eduaction book : "))
             BookEducation.append(item)
             print(*BookEducation,sep='\n')
             Thank()
             wellcome() 

            elif input3 =='4':
             item = input(str("enter the name of the drama book : "))
             BookDrama.append(item)
             print(*BookDrama,sep='\n')
             Thank()
             wellcome() 

        elif input2 =='2':
            print(*Music,sep='\n')
            input4 = input("what the category you want to add : ")
            if input4 =='1':
              item = ("enter the classic music you want to add : ")
              classicalMusic.append(item)
               
              print(*classicalMusic,sep="\n")
              Thank()
              
              wellcome()
            elif input4 =='2':
              item = ("enter the rock music you want to add : ")
              RockMusic.append(item)
              print(*RockMusic,sep="\n")
              Thank()
              
              wellcome()
            elif input4 =='3':
              item = ("enter the calm music you want to add : ")
              CalmMusic.append(item)
              print(*CalmMusic,sep="\n")
              Thank()
               
              wellcome()
        elif input2 =='3':
          print(*movies,sep="\n")
          input8 =input("what the category you want to add : ") 
          if input8 =='1':
            item =input("enter the action movie you want to add : ")
            moviesAction.append(item)
            print(*moviesAction,sep='\n')
          
          if input8 =='2':
             item =input("enter the drama movie you want to add : ")
             BookDrama.append(item)
             print(*BookDrama,sep="\n")
          
          if input8 =='2':
            item =input("enter the Science fiction movie you want to add : ")
            moviesScience.append(item)
            print(*moviesScience,sep="\n")
    else:
      ThankYouForUsing()
      wellcome()

     
######################################################        
            
CategoriesBook = ["1. Criminal",
                  "2. Literary books",
                  "3. Education",
               "4. Drama"]

BookCriminal =["- Murder on the Orient Express",
         "- And Then There Were None", 
         "- The Murder of Roger Ackroyd", 
         "- Death on the Nile" ,"The ABC Murders",  
         ]
BookEducation =['- The Smartest Kids in the World',
            '- Make it Stick',
           '- How Children Succeed:' ]
BookDrama=['- Shutter me ',
           '- No longer human',
           '- The kite runner']
BookLiterary = ['The Great Gatsby',
                'The Handmaids Tale',
                'The Secret History'] 
##########################################################

intrect = ('1.books','2.music','3.movies')
########################################################
Music =["1. classical music",
        "2. Rock Music",
        "3. calm Music"]
classicalMusic =["ayayay",
                 "Feeling good",
                 "sway"]
RockMusic =["you only live once",
            "rockstar",
            "rolling in the deep"]
CalmMusic =['perfect',' ']
########################################################

movies =['1. action','2. Drama','3. Science fiction']
moviesAction =['- The dark knight',
               '- Ford v Ferrari',
               '- logan']
moviesDrama =['- Oppenheimer',
              '- Knives Out',
              'top gun']
moviesScience =['- Interstellar',
                '- avatar',
                '- gurdians galaxy']

wellcome()

            