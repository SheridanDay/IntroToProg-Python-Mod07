**Creator:** *Sheridan Day*  
**Date:** *May 30, 2022*  
**Foundations of Programming**  
**Assignment 07**


# Document Your Knowledge 
 
## Introduction 
This new week came off what I though was an ok week six. When I saw we had to start with nothing and do our own research, I was both excited since I enjoy research, but also terrified because I don’t know if I know enough to know what I need or what will help. That came into play as my project came into focus. Luckily, despite my currently complicated relationship with my homework subject, *Star Wars*, the data became the least of my issues. 
 
## Topic 1 – Research, and the Search for Knowledge 
After reading the chapter of our book, I went straight to Google. I started with pages that gave general information on both pickling data and exception handling. They were useful for giving more information to supplement the video and book. However, later on, I had to do some more specific searches on different error types, why something didn’t work well with “try/except” issues, and more. Overall I had about a dozen pages open and saved several for future use in the app Pocket. I use this phone and web app to save websites for future use between devices. 


## Topic 2 – I Was Not in a Pickle…with Pickles. 
I will admit I’m not great a puns, but overall this is the one thing I didn’t have a hard problem with. After I decided the topic of my assignment would be *Star Wars*, I knew I wanted to model my pickled and shelved data after the literal pickle lists in book. Since the franchise can be broken into three set of three movies, it was easy to set them up and load them into a .dat file. I also downloaded Notepad++ and learned what an easy program it was to use (Figure 1). I’m happy I don’t have to mess with trying to format my code in PyCharm and inevitably mess up something that was working. 

```
print("I have pickled the Star Wars Trilogies!")
OT = ["ANH", "ESB", "ROTJ"]
PT = ["TPM", "AOTC", "ROTS"]
ST = ["TFA", "TLJ", "ROS"]
f = open("SWTrilogies.dat", "wb")
pickle.dump(OT, f)
pickle.dump(PT, f)
pickle.dump(ST, f)
f.close()
```
##### *Figure 1. A portion of my pickled data.*  

## Topic 3 – Putting Pieces Together, Somehow, Badly 
Ok, so I was able to pickle and unpickle my data. I felt pretty good. Now I knew what I wanted to do with the data, but wasn’t sure how to go about it. I knew I wanted a user to select a numbered answer from a list of *Star Wars* trilogies based on a question. It was hard to get my vision out of my head. I tried several ways, including dictionaries, lists, multiple “try/except” statements, and even a (poor) replication of the “Trivia Game” from the book. Nothing worked right or felt like how I wanted my stuff to look. 


## Topic 4 – Back to What I Know 
I spent a few hours messing with a variety of bad ideas that I didn’t like or didn’t work. I again was overcomplicating things, so I went back to an old assignment: if/else statements. It may result in my grade not being what I was hoping, but this worked and I did it all on my own. It displays the data I want, asks the question, and gives you an error if you select the wrong number or uses the “except” statement if you select no number at all (Figure 2). 

![Some of my code in Notepad++](https://github.com/SheridanDay/IntroToProg-Python-Mod07/blob/main/docs/images/NP_almost_there.PNG?raw=true "Some of my code in Notepad++")
##### *Figure 2. Some of my unpolished code in Notepad++ before it was polished up.*  

## Summary 
I really enjoyed doing some research and finding ways to complete a task on my own. The last couple of weeks were complicated, so the pre-written code was appreciated to cut back on time. I do feel like being able to write my own code, no matter how complicated, from start to finish made it more fulfilling. It’s hard to say which way is better. I’m just happy I found a solution that I’m happy with and that runs how I wanted it to look. 
