#import module
import os
from termcolor import colored

#variables
main = True
menu = True
about = False
start = False
anim_1 = False
anim_2 = False
anim_3 = False
anim_4 = False
anim_5 = False

#main app
while main:
    while menu:
        print('\n')
        print(colored('py beefetch + + +', 'white', 'on_yellow'))
        print(colored(r'''
              \     /
               o w o    
            \ (     ) /
 ____________(%%%%%%%)____________
(     /   /  )       (  \   \     )
(___/___/__/           \__\___\___)
   (     /  /(       )\  \     )
    (__/___/ (       ) \___\__)
             /(%%%%%)\   
               (%%%)
                 v
        ''', 'yellow'))
        print('\n')
        print(colored('1. about this application', 'yellow'))
        print(colored('2. start', 'yellow'))
        print(colored('3. quit', 'yellow'))
        choice = input(colored('> ', 'white', 'on_yellow'))
        if choice == '1':
            menu = False
            about = True
        if choice == '2':
            menu = False
            start = True
        if choice == '3':
            quit()
        elif choice:
            pass
    while about:
        print('\n')
        print(colored('about this application + + +', 'white', 'on_yellow'))
        print('choose the bee that you want to see!! let me explain.')
        print('when you type [1] and \'enter\' on the main menu, you will be prompted into a settings screen which')
        print('will ask you for basic customizations for the ascii bee that will be animated.')
        print('after configuring the bee, the screen will flicker and a lot of bees will appear!!')
        print('if you want it to stop, just close the terminal.')
        print('\n')
        print(colored('type [9] and then \'enter\' to go back to the menu'))
        choice_about = input(colored('> ', 'white', 'on_yellow'))
        if choice_about == '9':
            menu = True
            about = False
        elif choice_about:
            pass
    while start:
        print('\n')
        print(colored('choose your bee color before starting + + +', 'white', 'on_yellow'))
        print(colored(r'''
              \     /
               o w o    
            \ (     ) /
 ____________(%%%%%%%)____________
(     /   /  )       (  \   \     )
(___/___/__/           \__\___\___)
   (     /  /(       )\  \     )
    (__/___/ (       ) \___\__)
             /(%%%%%)\   
               (%%%)
                 v   type [1] and \'enter\'
        ''', 'yellow'))
        print(colored(r'''
              \     /
               o w o    
            \ (     ) /
 ____________(%%%%%%%)____________
(     /   /  )       (  \   \     )
(___/___/__/           \__\___\___)
   (     /  /(       )\  \     )
    (__/___/ (       ) \___\__)
             /(%%%%%)\   
               (%%%)
                 v  type [2] and \'enter\'
        ''', 'green'))
        print(colored(r'''
              \     /
               o w o    
            \ (     ) /
 ____________(%%%%%%%)____________
(     /   /  )       (  \   \     )
(___/___/__/           \__\___\___)
   (     /  /(       )\  \     )
    (__/___/ (       ) \___\__)
             /(%%%%%)\   
               (%%%)
                 v  type [3] and \'enter\'
        ''', 'red'))
        print(colored(r'''
              \     /
               o w o    
            \ (     ) /
 ____________(%%%%%%%)____________
(     /   /  )       (  \   \     )
(___/___/__/           \__\___\___)
   (     /  /(       )\  \     )
    (__/___/ (       ) \___\__)
             /(%%%%%)\   
               (%%%)
                 v  type [4] and \'enter\'
        ''', 'blue'))
        print(colored(r'''
              \     /
               o w o    
            \ (     ) /
 ____________(%%%%%%%)____________
(     /   /  )       (  \   \     )
(___/___/__/           \__\___\___)
   (     /  /(       )\  \     )
    (__/___/ (       ) \___\__)
             /(%%%%%)\   
               (%%%)
                 v  type [5] and \'enter\'
        ''', 'light_magenta'))
        print('\n')
        select = input(colored('> ', 'white', 'on_yellow'))
        if select == '1':
            start = False
            anim_1 = True
        if select == '2':
            start = False
            anim_2 = True
        if select == '3':
            start = False
            anim_3 = True
        if select == '4':
            start = False
            anim_4 = True
        if select == '5':
            start = False
            anim_5 = True
        elif select:
            pass
    while anim_1:
        print('\n')
        print(colored(r'''
              \     /
               o w o    
            \ (     ) /
 ____________(%%%%%%%)____________
(     /   /  )       (  \   \     )
(___/___/__/           \__\___\___)
   (     /  /(       )\  \     )
    (__/___/ (       ) \___\__)
             /(%%%%%)\   
               (%%%)
                 v
        ''', 'yellow'))
        print(colored(r'''
              \     /
               > w <    
            \ (     ) /
  ___________(%%%%%%%)___________
 (    /   /  )       (  \   \    )
 (__/___/__/           \__\___\__)
    (       /(       )\  \    )
     (_/___/ (       ) \___\_)
             /(%%%%%)\   
               (%%%)
                 v
        ''', 'yellow'))
    while anim_2:
        print('\n')
        print(colored(r'''
              \     /
               o w o    
            \ (     ) /
 ____________(%%%%%%%)____________
(     /   /  )       (  \   \     )
(___/___/__/           \__\___\___)
   (     /  /(       )\  \     )
    (__/___/ (       ) \___\__)
             /(%%%%%)\   
               (%%%)
                 v
        ''', 'green'))
        print(colored(r'''
              \     /
               > w <    
            \ (     ) /
  ___________(%%%%%%%)___________
 (    /   /  )       (  \   \    )
 (__/___/__/           \__\___\__)
    (       /(       )\  \    )
     (_/___/ (       ) \___\_)
             /(%%%%%)\   
               (%%%)
                 v
        ''', 'green'))
    while anim_3:
        print('\n')
        print(colored(r'''
              \     /
               o w o    
            \ (     ) /
 ____________(%%%%%%%)____________
(     /   /  )       (  \   \     )
(___/___/__/           \__\___\___)
   (     /  /(       )\  \     )
    (__/___/ (       ) \___\__)
             /(%%%%%)\   
               (%%%)
                 v
        ''', 'red'))
        print(colored(r'''
              \     /
               > w <    
            \ (     ) /
  ___________(%%%%%%%)___________
 (    /   /  )       (  \   \    )
 (__/___/__/           \__\___\__)
    (       /(       )\  \    )
     (_/___/ (       ) \___\_)
             /(%%%%%)\   
               (%%%)
                 v
        ''', 'red'))
    while anim_4:
        print('\n')
        print(colored(r'''
              \     /
               o w o    
            \ (     ) /
 ____________(%%%%%%%)____________
(     /   /  )       (  \   \     )
(___/___/__/           \__\___\___)
   (     /  /(       )\  \     )
    (__/___/ (       ) \___\__)
             /(%%%%%)\   
               (%%%)
                 v
        ''', 'blue'))
        print(colored(r'''
              \     /
               > w <    
            \ (     ) /
  ___________(%%%%%%%)___________
 (    /   /  )       (  \   \    )
 (__/___/__/           \__\___\__)
    (       /(       )\  \    )
     (_/___/ (       ) \___\_)
             /(%%%%%)\   
               (%%%)
                 v
        ''', 'blue'))
    while anim_5:
        print('\n')
        print(colored(r'''
              \     /
               o w o    
            \ (     ) /
 ____________(%%%%%%%)____________
(     /   /  )       (  \   \     )
(___/___/__/           \__\___\___)
   (     /  /(       )\  \     )
    (__/___/ (       ) \___\__)
             /(%%%%%)\   
               (%%%)
                 v
        ''', 'light_magenta'))
        print(colored(r'''
              \     /
               > w <    
            \ (     ) /
  ___________(%%%%%%%)___________
 (    /   /  )       (  \   \    )
 (__/___/__/           \__\___\__)
    (       /(       )\  \    )
     (_/___/ (       ) \___\_)
             /(%%%%%)\   
               (%%%)
                 v
        ''', 'light_magenta'))