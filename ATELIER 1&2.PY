      #ATELIER 1 :
#EX 1
#declaration de la fonction factorielle
def factorielle(x) :
    if x==0:
        return 1
    else:
        return x*factorielle(x - 1)
#demande de l utilusateur pour saisir la valeur de n
n=int(input("entrer la valeur de n:"))
#initialisation du variable sum par 0
sum=0
#utilusation de boucle for afin de parcourir tout les elements
for i in range(1,n+1):
    sum = sum + factorielle(i)/i
#affichage de la somme final
    print(sum)

#EX 2
#declaration de la fonction qui converti un nbr decimal en binaire
def decimal_to_binary(n):
    binary = ""
#la condition d arret
    while(n != 0 ) :
        binary += str(n % 2)
        n = n // 2
#pour inverser le code binaire
    return binary[::-1]
n = int(input("entrer un nbr"))
#affichage de resultat
print(decimal_to_binary(n))

#EX 3
#declaration d une fct qui fait la somme en utilusant la recursivité
def somme(n):
   if n == 0:
      return 0
   else:
      return n + somme(n - 1)
#demande de la saisie d une valeur
n=int(input("entrer la valeur de n:"))
#affichage de la somme
print(somme(n))

#EX 4
#declaration de la fct
def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
#demande de l'utilisateur pour taper le nbr de termes voulu
n = int(input("Entrez le nombre de termes:"))
print("Suite de Fibonacci en utilisant la recursion :")
for i in range(n):
#affichage de resultat
    print(fibonacci(i))

#EX 5
#declaration d une fct qui compte les chiffres
def compte(N):
#declaration d un variable a stoké et l'initialiser par 0
    nbr = 0
    while N != 0:
        N=int(N/10)
        nbr += 1
    return nbr
#demande de l utilisateur a taper le nbr voulu
N = int(input("saisir un nbr : "))
#affichage de resultat
print("le nbr total de chiffre dans le nombre ",N,"est",compte(N))

#EX 6
#declaration de la premiere fct triante
def tri_bull(tab):
    n = len(tab)
    for i in range(n):
        for j in range(0,n-i-1):
            if tab[j] > tab[j+1]:
                tab[j],tab[j+1] = tab[j+1],tab[j]
    return tab
#declaration de la deusieme fct triante
def tri_selection(tab):
    for i in range (len(tab)):
        min = i
        for j in range (i+1 , len(tab)):
            if tab[min] > tab[j]:
                min = j
        tmp = tab[i]
        tab[i] = tab[min]
        tab[min] = tmp
    return tab
#declaration de la troisieme fct triante
def tri_insertion(tab):
    for i in range(1,len(tab)):
        k = tab[i]
        j = i - 1
        while j>=0 and k<tab[j]:
            tab[j+1] = tab[j]
            j=-1
            tab[j+1] = k
    return tab
#declaration du tableau a trier
tab = [60,22,35,9,100,230,514,24,66,10,15,67,669]
#affichage de resultat selon les algorithmes
  #premiere resultat:
print("EN UTILUSANT TRI A BULL VOICI LE RESULTAT : ",tri_bull(tab))
  #seconde resultat:
print("EN UTILUSANT TRI PAR SELECTION VOICI LE RESULTAT: ",tri_selection(tab))
  #tertiaire resultat
print("EN UTILUSANT TRI PAR INSERTION VOICI LE RESULTAT: ",tri_insertion(tab))
#et finalement on obtient le meme resultat

#EX 7
#declaration de la chaine a inverser
str="yousra"
string_reversed=[]
i = len(str)
while i > 0:
    string_reversed += str[i-1]
    i = i -1
#affichage du chaine inversée
print("the reversed string is",string_reversed)


#EX 8
#declaration de la fonction
def find(str , char):
    return str.count(char)
#demande de l utilusateur d'entrer le nom
str0 = input("enter the string :")
#demande de l'utilusateur d'entrer la lettre voulu compté
char0 =input("enter the  char:")
#afficher le resultat
print("char",char0,"repetrer",find(str0,char0),"fois")

       #Atelier 2 :
#EX 1
#declaration de la fct
def get_odds(list1, list2):
#declaration des 2 listes
    a, b = [], []
    for i in range(0, len(list1)):
#verification de la parité des élements de la premiére liste
        if i % 2 != 0: a.append(list1[i])
    for j in range(0, len(list2)):
#verification de la parité des élements de la second liste
        if j % 2 == 0: b.append(list1[j])
    return a + b
#affichage de resultat
print(get_odds([1, 2, 3, 4, 5], [1, 2,  3]))

#EX 2
#declaration de la fct
def divide_conquere(data):
    i = 0
    export = []
    for i in range(0, 9, 3):
        export.append(data[i:i + 3])
    return export

print(divide_conquere([0, 8, 5, 6, 6, 4, 7, 3, 9]))

#EX 3
#declaration de la fct occurence
def occurence(list):
    a = {}
    for j in list:
        if str(j) in a:
            a[str(j)] = a.get(str(j)) + 1
        else:
            a[str(j)] = 1
    return a
#affichage des occurences
print(occurence([6, 6, 3, 4, 5, 2, 2, 4]))

#EX 4
def difference(set1, set2):
    a = set((""))
    for i in set1:
        for j in set2:
            if i == j: a.add(i)
    b = set1.copy()
    for i in set1:
        if i in a: b.remove(i)

    print("this is the difference => ", a, "this is the remainder of set1", b)

print(difference({23, 42, 65, 57, 78, 83, 29}, {57, 83, 29, 67, 73, 43, 48}))


#EX 5
#declaration du fct
def get(list1,dict1):
#affectation des elements clés au dictionnair
    keys = list(dict1.keys())
    result = []
#utiluser la boucle for pour verifier l existances des élements assemblés
    for i in keys:
        for j in list1:
            if dict1[str(i)] == j :
                result.append(j)
    return result
#declaration de la liste et du dictionnaire en appelant la fct get
print(get([47,64,69,37,76,83,95,97],
{'Yassine':47, 'Imane':69, 'Mohammed':76, 'Abir':97}))