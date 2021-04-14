#Project by networkGeek
from selenium import webdriver
import time
import sys
import os


asker = input('''\n\n\n\n\n\n
██████╗ ██╗   ██╗  ███╗  ██╗███████╗████████╗ ██╗       ██╗ █████╗ ██████╗ ██╗  ██╗ ██████╗ ███████╗███████╗██╗  ██╗
██╔══██╗╚██╗ ██╔╝  ████╗ ██║██╔════╝╚══██╔══╝ ██║  ██╗  ██║██╔══██╗██╔══██╗██║ ██╔╝██╔════╝ ██╔════╝██╔════╝██║ ██╔╝
██████╦╝ ╚████╔╝   ██╔██╗██║█████╗     ██║    ╚██╗████╗██╔╝██║  ██║██████╔╝█████═╝ ██║  ██╗ █████╗  █████╗  █████═╝ 
██╔══██╗  ╚██╔╝    ██║╚████║██╔══╝     ██║     ████╔═████║ ██║  ██║██╔══██╗██╔═██╗ ██║  ╚██╗██╔══╝  ██╔══╝  ██╔═██╗ 
██████╦╝   ██║     ██║ ╚███║███████╗   ██║     ╚██╔╝ ╚██╔╝ ╚█████╔╝██║  ██║██║ ╚██╗╚██████╔╝███████╗███████╗██║ ╚██╗
╚═════╝    ╚═╝     ╚═╝  ╚══╝╚══════╝   ╚═╝      ╚═╝   ╚═╝   ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
\n\n\nGithub Repository: https://github.com/naturalpianist\n\n\n\n\n\n:''')


########################################First Option############################################################################
if asker == "1":
    link = "http://quotes.toscrape.com"
    driver = webdriver.Chrome('') #The path of your Chromedriver
    driver.get(link)
    driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[1]/span[2]/a').click()
    albert = driver.find_element_by_xpath('/html/body/div/div[2]/div')
    sys.stdout = open("information.txt", "w")
    print("\n" + albert.text + "\n")
    sys.stdout.close()
    driver.close()
    driver.quit()

#######################################Second Option#############################################################################
elif asker == "2":
    link = "http://quotes.toscrape.com"
    driver = webdriver.Chrome('') #The path of your Chromedriver
    driver.get(link)
    driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/span[2]/a').click()
    albert = driver.find_element_by_xpath('/html/body/div/div[2]/div')
    sys.stdout = open("information.txt", "w")
    print("\n" + albert.text + "\n")
    sys.stdout.close()
    driver.close()
    driver.quit()

##########################################Third Option##########################################################################
elif asker == "3":
    link = "https://www.goalcast.com/2017/12/07/27-bill-gates-quotes/"
    driver = webdriver.Chrome('')
    driver.get(link)
    bill = driver.find_element_by_xpath('//*[@id="post-6018"]/div[2]/div/div[1]/div/div[3]/blockquote[4]/p')
    sys.stdout = open("information.txt", "w")
    print("\n" + bill.text + "\n")
    print('''
    Don’t compare yourself with anyone in this world…if you do so, you are insulting yourself.
    I choose a lazy person to do a hard job. Because a lazy person will find an easy way to do it.\n
    Success is a lousy teacher. It seduces smart people into thinking they can’t lose.\n
    If you are born poor it’s not your mistake, but if you die poor it’s your mistake.\n
    Life is not fair get, used to it!\n
    We make the future sustainable when we invest in the poor, not when we insist on their suffering.\n
    It’s fine to celebrate success but it is more important to heed the lessons of failure.\n
    We all need people who will give us feedback. That’s how we improve.\n
    Treatment without prevention is simply unsustainable.\n
    Discrimination has a lot of layers that make it tough for minorities to get a leg up.\n
    As we look ahead into the next century, leaders will be those who empower others.\n
    We’ve got to put a lot of money into changing behavior.\n
    The most amazing philanthropists are people who are actually making a significant sacrifice.\n
    The general idea of the rich helping the poor, I think, is important.\n
    I believe that if you show people the problems and you show them the solutions they will be moved to act.\n
    If all my bridge coach ever told me was that I was ‘satisfactory,’ I would have no hope of ever getting better.\n
    How would I know who was the best? How would I know what I was doing differently?\n
    Legacy is a stupid thing! I don’t want a legacy.\n
    Lectures should go from being like the family singing around the piano to high-quality concerts.\n
    Personally, I’d like to see more of our leaders take a technocratic approach to solving our biggest problems.\n
    Like my friend Warren Buffett, I feel particularly lucky to do something every day that I love to do. He calls it ‘tap-dancing to work.’\n
    We have to find a way to make the aspects of capitalism that serve wealthier people serve poorer people as well.\n
    Expectations are a form of first-class truth: If people believe it, it’s true.\n
    The belief that the world is getting worse, that we can’t solve extreme poverty and disease, isn’t just mistaken. It is harmful.\n
    When a country has the skill and self-confidence to take action against its biggest problems, it makes outsiders eager to be a part of it.\n
    Money has no utility to me beyond a certain point.\n
    I really had a lot of dreams when I was a kid, and I think a great deal of that grew out of the fact that I had a chance to read a lot.\n
    If you think your teacher is tough, wait ’til you get a boss. He doesn’t have tenure.\n
    Be nice to nerds. Chances are you’ll end up working for one.\n''')
    sys.stdout.close()
    driver.close()
    driver.quit()


######################################Fourth Option##############################################################################
elif asker == "4":
    sys.stdout = open("information.txt", "w")
    print('''    
    "When something is important enough, you do it even if the odds are not in your favor."\n
    "If you get up in the morning and think the future is going to be better, it is a bright day. Otherwise, it's not."\n
    "There have to be reasons that you get up in the morning and you want to live. Why do you want to live? What's the point? What inspires you? What do you love about the future? If the future does not include being out there among the stars and being a multi-planet species, I find that incredibly depressing."\n
    "When Henry Ford made cheap, reliable cars, people said, 'Nah, what's wrong with a horse?' That was a huge bet he made, and it worked."\n
    "Persistence is very important. You should not give up unless you are forced to give up."\n
    "It's OK to have your eggs in one basket as long as you control what happens to that basket."\n
    "If you go back a few hundred years, what we take for granted today would seem like magic-being able to talk to people over long distances, to transmit images, flying, accessing vast amounts of data like an oracle. These are all things that would have been considered magic a few hundred years ago."\n
    "We're going to make it happen. As God is my bloody witness, I'm hell-bent on making it work."\n
    "The first step is to establish that something is possible; then probability will occur."\n
    "I think it is possible for ordinary people to choose to be extraordinary."\n
    "I could either watch it happen or be a part of it.\n
    "“A company is a group organized to create a product or service, and it is only as good as its people and how excited they are about creating. I do want to recognize a ton of super-talented people. I just happen to be the face of the companies"\n
    ''')
    sys.stdout.close()
    driver.close()
    driver.quit()

####################################################################################################################
