f=open("covid_19_india.csv","r")
covid_list={}
for lines in f:
    no,Date,Time,State,ConfirmedIndianNational,ConfirmedForeignNational,Cured,Deaths,Confirmed=lines.rstrip("\n").split(",")
    if no not in covid_list:
         covid_list[no]={"Sno":no,"Date":Date,"Time":Time,"State":State,"ConfirmedIndianNational":ConfirmedIndianNational,"ConfirmedForeignNational":ConfirmedForeignNational,"Cured":Cured,"Deaths":Deaths,"Confirmed":Confirmed}
def print_covid(**kwargs):
    no=kwargs["no"]
    if no in covid_list:
        print(covid_list[no]["State"])
        if "prop" in kwargs:
            prop=kwargs["prop"]
            print(covid_list[no][prop])
        else:
            pass
    else:
        print("no case")
print_covid(no="3",prop="Confirmed")














