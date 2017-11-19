#######################################
#[Special alarm minutes in Falcon.811]#
######################################
#|   I share the idea of a simple script passable, you can appreciate and enlarge the best idea of the script    |
#|   The idea of the script from:falcon.811    |
#|    The idea is simply a specific alert Annotation on the theory |
#|     Marty Lopdale. Lopdale studied psychology at Pearce College in Washington State for 40 years.   |
#|     It is a theory of intelligent reasoning |
######################################
#|
import webbrowser #A library call enables you to handle web pages
import time #Call library enables you to handle time
print('''
######################################
#[Special alarm minutes in Falcon.811]#
######################################
|   ╔═══╗──╔╗──────────╔═══╗╔╗─╔╗    |
|   ║╔══╝──║║──────────║╔═╗╠╝║╔╝║    |
|   ║╚══╦══╣║╔══╦══╦═╗─║╚═╝╠╗║╚╗║    |
|   ║╔══╣╔╗║║║╔═╣╔╗║╔╗╗║╔═╗║║║─║║    |
|   ║║──║╔╗║╚╣╚═╣╚╝║║║╠╣╚═╝╠╝╚╦╝╚╗   |
|   ╚╝──╚╝╚╩═╩══╩══╩╝╚╩╩═══╩══╩══╝   |
######################################
''')
while True:
	#Here we ask
 user= str (input("#Do you want to reset the time [yes]or[no]==>:"))
 if user == 'yes':
    #If he says yes we calculate the time
    falcon_time=time.sleep(1800)
    print(falcon_time)
    #When the time is up we bring in the requested page
    test = "file:///E:/test/test1.html"
    webbrowser.open_new_tab(test )
    print(user)
 elif user == 'no':
    print ("#[thank you see you leater.]")
    print(user)
    break
