import os
import pyuac

def main():
    quser = list(i.encode('cp1251').decode('cp866') for i in os.popen('quser'))[1:]

    if len(quser) > 1:
        print('Ошибка: больше одной сессии\n\n')
        input('Нажмите Enter для продолжения...')
        quit()

    session = quser[0].split()[2]

    os.system(f'tscon {session} /password:password /dest:console')


if not pyuac.isUserAdmin():
    pyuac.runAsAdmin()

else:
    main()


