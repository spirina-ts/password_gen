#coding:utf-8
import random

print("Здравствуй, мой юный друг.")
print("Кажется у тебя возникли проблемы с генерацией пароля для своих соц.сетей или других сервисов.") 
print("Я могу тебе с этим помочь, но для начала тебе нужно выбрать несколько категорий, что бы предложенный пароль подходил тебе и тебе было легче его запомнить.")
print("выбери категорию, которая подходит именно тебе.")
print("введи 1 если хочешь выбрать математику")
print("введи 2 если хочешь выбрать информатику")
print("введи 3 если хочешь выбрать физику")
print("введи 4 если хочешь выбрать химию")
print("введи 5 если хочешь выбрать биологию")
print("введи 6 если хочешь выбрать литературу")
math = 0
computer_science = 1
physics = 2
chemistry = 3
biology = 4
literature = 5
#создание первоначальных категорий из которых будет выдергиваться слово в соответствии с тем какую именно категорию выбрал пользователь
words = {
math : 
	["numbers", "squareroot", "arithmetic", "algebra", "geometry", "circumference", "length", "width", "height", "fraction", "decimal", "circle", "square", "triangle", "rectangle", "pentagon", "hexagon", "pyramid", "percent", "volume"],
computer_science: 
	["file", "error", "monitor", "Interface", "hyperlink", "traffic", "server", "software", "install", "instruction", "freeware", "algorithm", "uninstall", "symbol", "formatting", "pixel", "device"],
physics:
	["force", "traction", "friction", "quantity", "displacement", "distance", "scalar", "acceleration", "gravity", "magnitude", "thrust", "slope", "tension", "surface", "motion", "equilibrium", "collision", "momentum"],
chemistry:
	["alchemy", "atom", "matter", "interaction", "hydrogen", "oxygen", "covalent", "oxide", "proton", "synthesis", "alloy", "carbon", "photon", "electron", "energy"],
biology:
	["abdomen", "amphibian", "cell", "chloroplast", "chlorophyll", "chromatin", "embry", "herbivore", "heredity", "invertebrate", "nucleus", "omnivorous", "offspring", "predator", "respiration", "vertebrate"],
literature:
	["thriller", "paragraph", "pocketbook", "memoir", "poem", "poetry", "nonfiction", "preface", "novella", "fantasy", "pamphlet", "rhyme", "saga", "satire", "volume", "writer", "sonnet"]
	}
kategoria = random.choice(words[int(input())-1]) #выбор рандомного слова из нужной категории

print("для усложнения пароля введите пожалуйста любое слово на английском которое вам близко или которое вам будет легко запомнить. например - cucumber")
print("ПОМНИТЕ!!! что личную информацию добавлять в пароль нельзя. Не используйте пожалуйста фамилию или имя своей собачки, иначе злоумышленнику будет проще взломать ваш пароль")
word = str(input()) #пользовательское любое слово благодаря которому будет сгенерирован пароль
your_password = str(kategoria) + str(word) #склеивание пароля из двух слов. из категории и из word
print("на данный момент твой пароль выглядит так -")
print(your_password) #вывод пароля пользователю,что бы он мог увидеть его перед изменениями

print("выберите категорию сложности пароля")
print("введи слитно комбинацию тех чисел, каким хочешь видеть свой пароль:")
print("1 - в пароле будут числа")
print("2 - в пароле будут знаки препинания")
print("3 - в пароле будут заглавные буквы")
print("4 - в пароле будут символы похожие на буквы")
print("5 - простой пароль без дополнительных усложнений")

print("пример введенного значения 12 - это значит что твой пароль будет усложнен числами и знаками препинания")
#набор данных для усложнения пароля
#number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
znaki_prep = ["!", "*", "+", "=", "$"]
Zag_bykva = [chr(x) for x in range(ord('A'), ord('Z')+1)]
str_bykva = [chr(x) for x in range(ord('a'), ord('z')+1)]
Zag_bykva1 = list(range(65, 91))
str_bykva1 = list(range(97, 123))
izvrashenie = ["@", "|3", "(", "|)", "&", "|=", "9", "|=|", "|", "]", "|<", "1", "|\/|", "|\|", "*", "|0", "0|", "l`", "$", "'|'", "|_|", "\/", "\/\/", "}{", "`/", "%"]
sloghnost = input()

#создание функций под каждое усложнение
def chisla(password):#числа1
    print("введи любое число")
    chislo = int(input())
    razdelenie = random.randint(0, len(password))
    password = str(your_password[:razdelenie]) + str(chislo) + (password[razdelenie:])
    return password
def znPrep(password):#знаки препинания2
    razdelenie = random.randint(0, len(password))
    password = str(your_password[:razdelenie]) + str(random.choice(znaki_prep)) + str(password[razdelenie:])
    return password
def ZagBykva(password):#заглавная буква3
    chislo_for_ord = random.randint(0, len(password)) #индекс буквы
    bykva_for_ord = your_password[chislo_for_ord] #рандомная буква
    chislo_for_ord22 = ord(bykva_for_ord) #ord строчной буквы
    chislo_for_ord22 = chislo_for_ord22 - 32#ord заглавной буквы
    bykva_for_ord = chr(chislo_for_ord22) # заглавная буква
    password = str(your_password[:chislo_for_ord]) + str(bykva_for_ord) + str(your_password[chislo_for_ord +1:])
    return password
def Izvrashenie(password):#извращение4 
    razdelenie = random.randint(0, len(password))
    chislo_for_ord = random.randint(0, len(password))
    while not(ord(your_password[chislo_for_ord])>=ord('a') and ord(your_password[chislo_for_ord])<=ord('z')):
        chislo_for_ord = random.randint(0, len(password))
    bykva_for_ord = your_password[chislo_for_ord] #рандомная буква
    
    chislo_for_ord22 = ord(bykva_for_ord) #ord строчной буквы
    chislo_for_ord22 = chislo_for_ord22 - 32 -65 #индекс символа
    bykva_for_ord = izvrashenie[chislo_for_ord22] # испорченная буква
    password = str(your_password[:chislo_for_ord]) + str(bykva_for_ord) + str(your_password[chislo_for_ord +1:])
    return password

functions = {'1': chisla, '2': znPrep, '3': ZagBykva, '4': Izvrashenie}
#взависимости от вводимого значения изменить пароль так, как захотел того пользователь.
for i in sloghnost:
    your_password = functions[i](your_password)
#funcsia = chisla(your_password)
#funcsia = znPrep(your_password)
#funcsia = ZagBykva(your_password)
#funcsia = Izvrashenie(your_password)
print(your_password)
