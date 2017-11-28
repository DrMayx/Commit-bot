from os import system, name

for i in range(100):
    with open('plik.txt', 'a') as file:
        file.write('X{}'.format(i))
    system('git add plik.txt')
    system('git commit -m "commie commit {}"'.format(i))
    system('git push')
    system('drmayx')
    system('kotpies123')