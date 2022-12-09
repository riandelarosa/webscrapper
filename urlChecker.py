import requests

def get_url_status(urls):  # checks status for each url in list urls
    for url in urls:
        try:
            r = requests.get(url)
            if (r.status_code == 404):
                print(url + "\tStatus: " + str(r.status_code))
        except Exception as e:
            print(url + "\tNA FAILED TO CONNECT\t" + str(e))
    return None

def main():
    names = ["Adam Mokoka","Aleksandar Radojevic","Alex Abrines","Alex Len","Alexey Shved","Alexis Ajinca","Alperen Sengun","Alpha Kaba","Alvin Jones","Andrea Bargnani","Andreas Glyniadakis","Andrei Kirilenko","Andris Biedrins","Ante Zizic","Anthony Randolph","Antoine Rigaudeau","Antonis Fotsis","Anzejs Pasecniks","Arnoldas Kulboka","Arvydas Macijauskas","Arvydas Sabonis","Axel Toupane","Ben Gordon","Beno Udrih","Bogdan Bogdanovic","Bojan Bogdanovic","Boris Diaw","Bostjan Nachbar","Brian Oliver","Bruno Sundov","Byron Mullens","Cal Bowdler","Cedi Osman","Cezary Trybanski","Chris Kaman","Chris Welp","Calint Capela","Cory Carr","DJ. Mbenga","Dairis Bertans","Dalibor Bagaric","Damien Inglis","Damir Markota","Damjan Rudez","Dan Gadzuric","Daniel Theis","Danilo Gallinari","Dario Saric","Darius Songaila","Darius Washington","Darko Milicic","Davis Bertans","Deividas Sirvydis","Deni Avdija","Dennis Schroder","Detlef Schrempf","Dino Radja","Dirk Nowitzki","Domantas Sabonis","Donatas Motiejunas","Dragan Bender","Drazen Petrovic","Duje Dukan","Dzanan Musa","Efthimios Rentzias","Elias Harris","Elie Okobo","Enes Kanter Freedom","Erik Murphy","Ersan Ilyasova","Evan Fournier","Fernando Martin","Filip Petrusev","Francisco Elson","Frank Ntilikina","Franze Wagner","Furkan Aldemir","Furkan Korkmaz","Gabriel Lundberg","Gal Mekel","Geert Hammink","George Zidek","Georgios Kalaitzakis","Georgios Papagiannis","Gheorghe Muresan","Giannis Antetokounmpo","Gigi Datome","Goga Bitadze","Goran Dragic","Gordan Giricek","Guerschon Yabusele","Gundars Vetra","Hanno Mottola","Hedo Turkoglu","Howard Carter","Ian Mahinmi","Ibrahim Kutluay","Ignas Brazdeikis","Igor Rakocevic","Isaiah Hartenstein","Issac Bonga","Ivica Zubac","J.R. Bremer","Jacob Pullen","Jacob Wiley","Jake Tsakalidis","Jakob Poeltl","James Donaldson","Jan Vesely","Jaylen Hoard","Jeff Nordgaard","Jeffery Taylor","Jeremy Sochan","Jerome Moiso","Jiri Welsch","Joakim Noah","Joel Ayayi","Joel Bolomboy","Joel Freeland","Joffrey Lauvergne","Johan Petro","John Amaechi","Johnny Rogers","Jonah Bolden","Jonas Jerebko","Jonas Valanciunas","Jorge Garbajosa","Jose Calderon","Juan Carlos Navarro","Juancho Hernangomez","Justin Hamilton","Jusuf Nurkic","Kelly McCarty","Kevin Seraphin","Killian Hayes","Killian Tillie","Kornel David","Kosta Koufos","Kosta Perovic","Kostas Antetokounmpo","Kostas Papanikolaou","Kristaps Porzingis","Kyrylo Fesenko","Lauri Markkanen","Linas Kleiza","Lorenzo Brown","Luka Doncic","Luka Garza","Luka Mitrovic","Luka Samanic","Luke Zeller","Luol Deng","Maalik Wayns","Maciej Lampe","Marc Gasol","Marcin Gortat","Marco Belinelli","Mario Hezonja","Mario Kasun","Marko Milic","Marko Simonovic","Martin Muursepp","Marty Conlon","Martynas Andriuskevicius","Maxi Kleber","Mehmet Okur","Melvin Sanders","Mickael Gelabale","Mickael Pietrus","Mike Tobey","Mile Ilic","Milos Vujanic","Milovan Rakovic","Mindaugas Kuzminskas","Mirsad Turkcan","Mirza Teletovic","Mladen Sekularac","Moritz Wagner","Moussa Diabate","Nando DeColo","Ndudi Ebi","Neemias Queta","Nemanja Bjelica","Nemanja Dangubic","Nenad Krstic","Nick Calathes","Nico Mannion","Nicolas Batum","Nicolo Melli","Nikola Jokic","Nikola Jovic","Nikola Milutinov","Nikola Mirotic","Nikola Pekovic","Nikola Vucevic","Nikoloz Tskitishvili","OG Anunoby","Ognjen Jaramaz","Oleksiy Pecherov","Oliver Lafayette","Olivier Sarr","Omar Cook","Omer Asik","Omer Yurtseven","Omri Casspi","Ousmane Dieng","Paolo Banchero","Pape Sy","Pat Burke","Pau Gasol","Paul Zipser","Pavel Podkolzin","Pero Antic","Petr Cornelie","Petur Guomundsson","Pooh Jeter","Pops Mensah-Bonsu","Predrag Danilovic","Predrag Drobnjak","Predrag Savovic","Primoz Brezec","Rade Zagorac","Rasho Nesterovic","Ratko Varda","Raul Lopez","Richard Petruska","Ricky Rubio","Rik Smits","Robert Archibald","Rodions Kurucs","Rodrigue Beaubois","Roko Ukic","Ronny Turiaf","Rudy Fernandez","Rudy Gobert","Ryan Arcidiacono","Ryan Stack","Sandro Mamukelashvili","Santi Aldama","Sarunas Jasikevicius","Sarunas Marciulionis","Sasha Kaun","Sasha Vujacic","Sekou Doumbouya","Semih Erden","Serge Ibaka","Sergei Bazarevich","Sergei Monia","Sergey Karasev","Sergio Rodriguez","Shammond Williams","Shane Larkin","Shawn Bradley","Shayne Whittington","Simone Fontecchio","Slava Medvedenko","Slavko Vranes","Stefano Rusconi","Steve Bucknall","Stojko Vrankovic","Svi Mykhailiuk","Swen Nater","T.J. Leaf","Tadija Dragicevic","Tariq Abdul-Wahad","Taurean Green","Thabo Sefolosha","Thanasis Antetokounmpo","Theo Maledon","Tibor Pleis","Tim Ohibrecht","Timofey Mozgov","Timothe Luwawu-Cabarrot","Tomas Satoransky","Toni Kukoc","Tony Parker","Torgeir Bryn","Tornike Shengelia","Travis Diener","Travis Hansen","Tyler Dorsey","Uros Slokar","Usman Garuba","Uwe Blab","Vanja Marinkovic","Vasilije Micic","Vassilis Spanoulis","Viacheslav Kravtsov","Victor Claver","Viktor Khryapa","Vincent Poirier","Vincenzo Esposito","Vit Krejci","Vitaly Potapenko","Vlade Divac","Vladimir Radmanovic","Vladimir Stepania","Vlatko Cancar","William Howard","Willy Hernangomez","Yakhouba Diawara","Yaroslav Korolev","Yves Pons","Zan Tabak","Zarko Cabarkapa","Zaza Pachulia","Zeljko Rebraca","Zoran Dragic","Zoran Planinic","Zydrunas Ilgauskas"]
    player_codes = []
    url = "https://www.basketball-reference.com/players/{code}.html"
    urls = []
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
        urls.append(url.replace("{code}", code))
        print(count, "-", player + ":", url.replace("{code}", code))
        count += 1
    #get_url_status(urls)
    #print(player_codes)

if __name__ == "__main__":
    main()
