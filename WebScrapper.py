#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import pandas as pd
# checks status for each url in list urls
def get_url_status(urls):
    for url in urls:
        try:
            r = requests.get(url)
            if (r.status_code == 404):
                print(url + "\tStatus: " + str(r.status_code))
        except Exception as e:
            print(url + "\tNA FAILED TO CONNECT\t" + str(e))
    return None

def get_data(url):
    print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # get timed period of player
    years = soup.find(id="all_per_game-playoffs_per_game")
    years = years.find('table', id="per_game")
    years = years.find_all('tbody')
    years = str(years).split('id="per_game.')
    years.pop(0)
    for i in range(len(years)):
        temp1 = years[i].split('"><th class=')
        years[i] = int(temp1[0])
    years = list(set(years))
    years.sort()
    # get minutes data
    minutes = soup.find(id="all_per_game-playoffs_per_game").find('table', id="per_game").find_all('tr')
    rows_data = [[td.getText() for td in minutes[i].findAll('td')] for i in range(len(minutes))]
    minutes_data = []
    flag = 0
    for i in rows_data:
        if flag == 0:
            if len(i) > 0:
                if 'TOT' in i:
                    flag = 2
                    for j in i:
                        if i.index(j) == 6:
                            minutes_data.append(float(j))
                else:
                    for j in i:
                        if i.index(j) == 6:
                            minutes_data.append(float(j))
        else:
            flag -= 1
        if len(minutes_data) == len(years):
            break
    minutes_data.append(round((sum(minutes_data)/len(years)),1))
    minutes_data.insert(0, minutes_data.pop())
    # get salaries data
    salaries = soup.find(id="all_all_salaries")
    salaries_data = str(salaries)
    salaries_data = salaries_data.split('a href="/leagues/NBA_')
    salaries_data.pop(0)
    salaries_dict = {}
    for i in salaries_data:
        temp2 = i.split('.html">NBA</a></td>')
        temp3 = temp2[1].split('csk="')
        temp3 = temp3[1].split('" >$')
        if int(temp2[0]) in salaries_dict:
            salaries_dict[int(temp2[0])] += int(temp3[0])
        else:
            salaries_dict[int(temp2[0])] = int(temp3[0])
    # format data
    #print("Years -", len(years), years)
    years.append('Total')
    years.insert(0, years.pop())
    minutes_dict = {}
    for i in range(len(years)):
        minutes_dict[years[i]] = minutes_data[i]
    #print("Mins -", len(minutes_dict), minutes_dict)
    temp4 = sum(salaries_dict.values())
    temp4 = {'Total': temp4}
    temp4.update(salaries_dict)
    salaries_dict = temp4
    #print("Salary -", len(salaries_dict), salaries_dict)
    player_dict = {}
    if len(minutes_dict) > len(salaries_dict):
        for i in minutes_dict.keys():
            if salaries_dict.get(i) is None:
                player_dict[i] = str(minutes_dict[i]) + '$' + str(0)
            else:
                player_dict[i] = str(minutes_dict[i]) + '$' + str(salaries_dict[i])
    elif len(salaries_dict) > len(minutes_dict):
        for i in salaries_dict.keys():
            if minutes_dict.get(i) is None:
                player_dict[i] = str(0.0) + '$' + str(salaries_dict[i])
            else:
                player_dict[i] = str(minutes_dict[i]) + '$' + str(salaries_dict[i])
    else:
        for i in years:
            if i != 2023:
                player_dict[i] = str(minutes_dict[i]) + '$' + str(salaries_dict[i])
    return player_dict

def main():
    csv = []
    br_dict = {}

    names = ["Aleksandar Radojevic", "Alex Abrines", "Alex Len", "Alexey Shved", "Alexis Ajinca","Alperen Sengun", "Alvin Jones", "Andrea Bargnani", "Andreas Glyniadakis","Andrei Kirilenko", "Andris Biedrins", "Ante Zizic", "Anthony Randolph", "Antoine Rigaudeau", "Antonis Fotsis", "Anzejs Pasecniks", "Arvydas Macijauskas","Arvydas Sabonis", "Ben Gordon", "Beno Udrih", "Bogdan Bogdanovic", "Boris Diaw", "Bostjan Nachbar", "Brian Oliver", "Bruno Sundov", "Byron Mullens", "Cal Bowdler", "Cezary Trybanski", "Chris Kaman", "Chris Welp", "Calint Capela", "Cory Carr", "DJ. Mbenga", "Dairis Bertans", "Dalibor Bagaric", "Damien Inglis", "Damir Markota", "Damjan Rudez", "Dan Gadzuric", "Daniel Theis", "Danilo Gallinari", "Dario Saric", "Darius Songaila", "Darius Washington", "Darko Milicic", "Davis Bertans", "Deividas Sirvydis", "Deni Avdija", "Dennis Schroder", "Detlef Schrempf", "Dino Radja", "Dirk Nowitzki", "Domantas Sabonis", "Donatas Motiejunas", "Dragan Bender", "Drazen Petrovic""Duje Dukan", "Dzanan Musa", "Efthimios Rentzias", "Elias Harris", "Elie Okobo", "Enes Kanter Freedom", "Erik Murphy", "Ersan Ilyasova", "Evan Fournier", "Fernando Martin", "Francisco Elson",  "Franze Wagner", "Furkan Aldemir", "Furkan Korkmaz","Gal Mekel", "Geert Hammink", "George Zidek", "Georgios Kalaitzakis", "Georgios Papagiannis", "Gheorghe Muresan", "Giannis Antetokounmpo", "Goga Bitadze", "Goran Dragic", "Gordan Giricek", "Guerschon Yabusele", "Gundars Vetra", "Hanno Mottola", "Hedo Turkoglu", "Howard Carter", "Ibrahim Kutluay", "Igor Rakocevic", "Isaiah Hartenstein", "Issac Bonga", "Ivica Zubac", "Jake Tsakalidis", "Jakob Poeltl", "James Donaldson", "Jan Vesely", "Jeff Nordgaard", "Jeffery Taylor", "Jeremy Sochan", "Jerome Moiso", "Jiri Welsch", "Joakim Noah", "Joel Freeland", "Joffrey Lauvergne", "Johan Petro", "John Amaechi", "Johnny Rogers", "Jonah Bolden", "Jonas Jerebko", "Jonas Valanciunas", "Jorge Garbajosa", "Jose Calderon",  "Juancho Hernangomez", "Justin Hamilton", "Jusuf Nurkic", "Kelly McCarty", "Kevin Seraphin","Killian Hayes",  "Kornel David", "Kosta Koufos", "Kosta Perovic", "Kostas Papanikolaou", "Kristaps Porzingis", "Kyrylo Fesenko", "Lauri Markkanen", "Linas Kleiza",  "Luka Doncic", "Luka Garza", "Luke Zeller", "Luol Deng", "Maalik Wayns", "Maciej Lampe", "Marc Gasol", "Marcin Gortat", "Marco Belinelli", "Mario Hezonja", "Mario Kasun", "Marko Milic", "Marko Simonovic", "Martin Muursepp", "Marty Conlon", "Martynas Andriuskevicius", "Mehmet Okur","Melvin Sanders", "Mickael Gelabale", "Mickael Pietrus", "Mike Tobey", "Mile Ilic",  "Mindaugas Kuzminskas", "Mirsad Turkcan", "Mirza Teletovic",  "Moritz Wagner", "Moussa Diabate", "Nando DeColo", "Ndudi Ebi", "Nemanja Bjelica", "Nenad Krstic", "Nick Calathes",  "Nicolas Batum", "Nicolo Melli", "Nikola Jokic", "Nikola Jovic", "Nikola Mirotic", "Nikola Pekovic", "Nikola Vucevic", "Nikoloz Tskitishvili", "OG Anunoby", "Oleksiy Pecherov", "Oliver Lafayette", "Olivier Sarr", "Omar Cook", "Omer Asik", "Omer Yurtseven", "Omri Casspi", "Ousmane Dieng", "Paolo Banchero", "Pape Sy", "Pat Burke", "Pau Gasol", "Paul Zipser", "Pavel Podkolzin", "Pero Antic", "Pops Mensah-Bonsu", "Predrag Drobnjak", "Predrag Savovic", "Primoz Brezec", "Rasho Nesterovic", "Ratko Varda", "Raul Lopez", "Richard Petruska", "Ricky Rubio", "Rik Smits", "Robert Archibald", "Rodions Kurucs","Rodrigue Beaubois", "Roko Ukic", "Ronny Turiaf", "Rudy Fernandez", "Rudy Gobert",  "Ryan Stack", "Santi Aldama", "Sarunas Jasikevicius", "Sarunas Marciulionis", "Sasha Kaun", "Sasha Vujacic", "Semih Erden", "Serge Ibaka", "Sergei Bazarevich", "Sergei Monia", "Sergey Karasev", "Sergio Rodriguez", "Shammond Williams", "Shane Larkin", "Shawn Bradley", "Shayne Whittington", "Simone Fontecchio",  "Slavko Vranes", "Stefano Rusconi", "Steve Bucknall", "Stojko Vrankovic", "Svi Mykhailiuk", "Swen Nater", "Tariq Abdul-Wahad", "Taurean Green", "Thabo Sefolosha", "Thanasis Antetokounmpo", "Theo Maledon", "Tibor Pleis", "Timofey Mozgov", "Timothe Luwawu-Cabarrot", "Tomas Satoransky", "Toni Kukoc", "Tony Parker", "Torgeir Bryn", "Travis Diener", "Travis Hansen", "Tyler Dorsey", "Uros Slokar", "Usman Garuba", "Uwe Blab","Vassilis Spanoulis", "Viacheslav Kravtsov", "Victor Claver", "Viktor Khryapa", "Vincent Poirier", "Vincenzo Esposito", "Vit Krejci", "Vitaly Potapenko", "Vladimir Radmanovic", "Vladimir Stepania", "Vlatko Cancar",  "Willy Hernangomez", "Yakhouba Diawara", "Yaroslav Korolev", "Zan Tabak", "Zarko Cabarkapa", "Zaza Pachulia", "Zeljko Rebraca", "Zoran Dragic", "Zoran Planinic", "Zydrunas Ilgauskas",]
    player_codes = []
    url = "https://www.basketball-reference.com/players/{code}.html"
    count = 1
    for player in names:
        a = str(player)
        f = "01"
        b = a.find(" ")
        c = len(a)
        if c - b > 5:
            d = a[b + 1:b + 6]
        else:
            d = a[b + 1:c]
        e = a[0:2]
        code = (d[0].strip() + '/' + d.strip() + e.strip() + f.strip()).lower()
        player_codes.append(code)
        br_dict[player] = url.replace("{code}", code)
        #print(count, "-", player + ":", url.replace("{code}", code))
        count += 1
    # get_url_status(br_dict.values())
    for i in br_dict.keys(): # main for loop
        temp5 = {}
        br_dict[i] = get_data(br_dict[i])
        temp6 = br_dict[i].pop('Total')
        for j in range(1980, 2023):
            if j not in br_dict[i].keys():
                temp5[j] = 0
            else:
                if j not in temp5.keys():
                    temp5.update(br_dict[i])
        temp7 = {'Name': i, 'Total': temp6}
        temp7.update(temp5)
        csv.append(temp7)
    # should print 310
    print(len(csv))
    # create the dataframe
    european = pd.DataFrame.from_dict(csv)
    # export dataframe to a CSV
    european.to_csv("european.csv", index=False, header=True)

if __name__ == "__main__":
    main()
