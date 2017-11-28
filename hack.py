from os import system, name

def main():
    i=1
    while True:
        with open('plik.txt', 'a') as file:
            file.write('X{}'.format(i))
        system('git add .')
        system('git commit -m "commit #{}"'.format(i))
        if i%100:
            system('git push')

        i += 1
    
main()