#!/usr/bin/env python3
import csv

def main():
    with open('salaries.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        count = 0
        countries = {}
        for row in reader:
            if count > 0:
                temp = str(row[0]).split(",")
                for i in range(len(temp)):
                    if temp[i] == '':
                        temp[i] = '0.0$0'
                #print(count, temp)
                key = str(temp[0])
                if (key not in countries.keys()):
                    countries[key] = []
                    countries[key].append(temp)
                else:
                    countries[key].append(temp)
            count+=1
        list = []
        for k in countries:
            list.append(k)
            for j in range(43):
                list.append('0.0$0')
            for l in countries[k]:
            #     print(len(l), l) # what we are going through
                for m in range(1, len(l)):
                    #print(list[m], l[m])
                    if list[m] == '0.0$0' and l[m] != '0.0$0':
                        list[m] = l[m]
                    elif list[m] != '0.0$0' and l[m] != '0.0$0':
                        tempFirst = list[m].split('$')
                        tempSecond = l[m].split('$')
                        tempFloat = round(((float(tempFirst[0])+float(tempSecond[0]))/2),1)
                        tempInt = int(tempFirst[1])+int(tempSecond[1])
                        tempFinal = str(tempFloat)+'$'+str(tempInt)
                        list[m] = tempFinal
            countries[k] = list
            list = []
        # for removing dollar sign
        for k in countries:
            fList = countries[k]
            for l in range(1, len(fList)):
                if fList[l] == '0.0$0':
                   fList[l] = 0
                else:
                    ftemp = fList[l].split('$')
                    fList[l] = int(ftemp[1])
            countries[k] = fList
        #countinuing total/average
        for k in countries:
            fList = countries[k]
            for l in range(2, len(fList)):
                fList[l] =  fList[l-1]+ fList[l]
            countries[k] =fList
        # print dictionary
        for i in countries:
            print(countries[i])

if __name__ == "__main__":
    main()
