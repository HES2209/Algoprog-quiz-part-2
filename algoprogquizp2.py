class Binusmaya :
    def __init__ (self) : 
        self.lecturers = [
            {
                'name' : 'Ir. Mr. PhD. Jude',
                'subject' : 'Algorithm and Programming',
                'id' : '108957300'
                },
            {
                'name' : 'Dr. MH. Orlando',
                'subject' : 'HCI LAB',
                'id' : '278930944'
                },
            {
                'name' : 'MSi. Mr. Adijaya',
                'subject' : 'Program Design Method',
                'id' : '899093033'
                },
        ]
        self.classes = ['L1AC', 'L3BD', 'L2DM']
        self.schedules = []

    def add_proflie_lecturer (self) : 
        name = input("Enter your name : ")
        subject = input("Enter the subject that you teach : ")
        mid = input("Enter you ID here : ")
        datalecturer = {'name' : name, 'subject' : subject, 'id' : mid}
        self.lecturers.append(datalecturer)
        print(f"Hello Mr/Miss, your data have been added.")
    
    def rmv_profile_lecturer (self) : 
        print(self.lecturers)
        removename = input(f"Enter the lecturer name you want to remove : ")
        removesubject = input(f"Enter the subject that the lecturer teach : ")
        removelid = input(f"Enter the id of the lecturer that you wanted to remove : ")
        removelecturer = {'name' : removename, 'subject' : removesubject, 'id' : removelid}
        self.lecturers.remove(removelecturer)
        print(f"The lecturer profile has been removed.")

    def profile_lecturer(self) : 
        print(self.lecturers)

    def add_my_classes(self) : 
        newclass = input("Enter your new classes : ")
        self.classes.append(newclass)
        print("Your class haave been added.")

    def rmv_my_classes(self) : 
        removeclass = input(f"{self.classes}, What class do you want to remove : ")
        if removeclass in self.classes : 
            self.classes.remove(removeclass)
            print(f"You now only have {self.classes} class.")
        else:
            print(f"Class{removeclass} did not exists...")

    def add_my_schedule(self) : 
        assignments = input("Enter your to do lists : ")
        self.schedules.append(assignments)
        print(f"Your tasks is : {self.schedules}")
    
    def rmv_my_schedule(self) : 
        removeass = input(f"{self.schedules}, What assignment do yo want to remove? : ")
        if removeass in self.schedules : 
            self.schedules.remove(removeass)
            print(f"You now only have {self.schedules} tasks.")
        else:
            print(f"Task {removeass} did not found.")

def start(): 
    bimay = Binusmaya()
    while True: 
        print(f"[1] Check your lecturers.")
        print(f"[2] Add a new leturer profile.")
        print(f"[3] Remove a lecturer profile.")
        print(f"[4] Add your classes.")
        print(f"[5] Remove you classes.")
        print(f"[6] Add a tasks or assignment to your schedule.")
        print(f"[7] Remove a tasks or assignment from your schedule.")
        print(f"[8] Donee!!!")

        choice = input("What do you want to do : ")
        
        if choice == "1" :
            bimay.profile_lecturer()
        elif choice == "2" : 
            bimay.add_proflie_lecturer()
        elif choice == "3" : 
            bimay.rmv_profile_lecturer()
        elif choice == "4" : 
            bimay.add_my_classes()
        elif choice == "5" : 
            bimay.rmv_my_classes()
        elif choice == "6" : 
            bimay.add_my_schedule()
        elif choice == "7" :
            bimay.rmv_my_schedule()
        elif choice == "8" : 
            print("Thank youu, Goodbye...")
            exit()
        else : 
            print("There is no such option...")

if __name__ == '__main__' : 
    start()


