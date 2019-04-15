Title: Python, For The ❤ of It
Author: Abdur-Rahmaan Janhangeer
Date: 2019-04-01 9:00
Category: blogging
Tags: python, love
Slug: python-for-the-love-of-it

![py love]({static}/img/py_love.png)

This (long) post describes my first meeting with python, my subsequent trip with it. It recounts my impressions as a complete beginner, my brush with the community and the things i built with it. My coding path in sum. Shared in exclusivity with the Codementor community. Specially dedicated to all those beginning to code. As the words below depict, it might be a long journey, but a journey at the very least, albeit, a thrilling one. Written by one with py at ❤.

### The Path Opens Up

To tell the truth, at school i did not know about Python, no, rather at first i did not care about Programming at all. But, being fascinated with computers, one day i wanted to code. I begun with HtML, that yes, something needing symbols as weird as < > must be real programming. Well it was like magic, some texts on that glaring white background (well notepad it was) and boom! you got UI elements, buttons, inputs and ... text itself. Hum i thought, the deeper the nesting, the better a devloper must you be. Le site du zero [1] was in it's last years then and i was busy extracting info from it.

My nest step was Khan Academy, the programming module (really it's ProcessingJS, the John Resig's port of processing) looked interesting. You could draw shapes by coding, whatever you wanted. You could even code animations. It was really cool and it got 3 modules, ending with Natural Simulations, that i can tell was no pasta. Later i discovered that it was adapted from Daniel Shiffman's Nature of Code which includes a section on Neural Networks. But hey i thought, with all those cool graphics it must be kids' stuffs. By then i thought loops was only associated with lines drawn. Well the community programs seemed so complex that i decided that loops, the this keyword and .prototype were definitively advanced concepts. Better back away unless you have to solve those end-of-lesson quizzes or fill in the code exercises.

Then as HSC [2] loomed ahead, coding went to the bottom of my todo drawer. Yes, it would never see the light again fully until months after.

### The Days When Python Was Total Garbage

After school i decided to learn C++, yes ... at last that was some real programming. Ooooh for the first time i was seeing a return statement. I was seeing vectors, indeed, with such words coming straight from a sci-fi movie, this time i've hit upon a real nugget. Oh my, i seemed to lose the hang of pointers as soon as i lifted my eyes off the tutorial screen. At the end of the course you have to build some guis using qt. Hum so much of -> got me seriously thinking about doing anything with that framework. Some guis later and ... goodbye CodeBlocks, goodbye C++, you are not my everyday buddy.

One day i wanted to code some games. I came across a seemigly easy tutorial of shooting arrows done with Pygame and ... Python. Since the game needed that thing called to run, i decided to explore Python first. All i got was a nice cli which allowed me to do some calculations and ... upto now i'm wondering what i downloaded that day. Well python was not that interesting i decided. It was abandoned straight away.

### Mastery Knocks (at my door) - part 1

Sololearn was one aspect, back then you had to download some 10 apps to code in 10 languages. Well i decided to try them all. There i was, learning ruby, then php then swift hey ... i must finish them all. As you might've guess, it did not have any good debugging tutos, just syntax, libs and exercises. But i was begining to see some patterns, the secret behind, kick syntax, learn concepts and ... off you go. The mask had fallen.

Freecodecamp was nice, very nice for web. For the first time in my life JQuery was really easy, bootstrap was no longer was some wizard's wand, mobile responsiveness was child's play and ... the way of teaching was just awesome. No comments.

### Mastery Knocks (at my door) - part 2

Two of my friends older than me were at University. One asked me some C++ info as he knew that i completed some C++ course. Well thoses memories were buried under layers of dust, time buried them deep under. But i decided to help him but in a unique way. Each day i prepared some notes, from the begining to advanced concepts, from variables to templates. I added some 🚇🍇🍓🍥🎯 emojis to make them less boring. But that meant i had to know C++ first. I found myself untangling deference operators from pointers, appreciating dynamic arrays, discovering C code execution, diving into OOP. Well after that, there was no turning back. Coding was something In. What's more, i just came from some seas, i discovered, few ships dared set sail.

### What Threw Me In Python's Arms (headlong)

But Java was far more interesting. Java was crazy until i understood that everything was an object. The language at that instant became pure bliss. I was able to comprehend why some constructs were like that. I found my house said i. OOP just landed in it's natural habitat.

Then fate decided to nudge the pen of destiny. I was writing an IRC [3] bot when i could not find the proper Java code to do it. When i did find it, i could not make sense out of it. What was that thing with three dots we were passing as parameters
(some methods). It was out of my control. Ironically google owners wrote their crawler in Java 1.0 before switching to Python.

I decided to go with py and i still vividly remember that i was googling

```
python print
```

I was a complete beginner. I now officially entered the Dojo.

Well i must say that i was really impressed with Python as the bot connected immediately in few lines of code, many edits later, the bot can be found over there. My next mission was finding a nice way to run the files.

### Indents and The IDE Quest

One thing which constantly annoyed me was the tabs v/s white space issue. I loved tabs ... but they always came into the way when i was editing others' codes. The interpreter was always complaining. Finally, it went away with finding a good IDE. A good IDE just adds 4 spaces when you press tab. In the begining i was running files on the command line but it was getting boring. A single edit and ... you have to retype again. Well, i could've made a shortcut to run at the click of a button but it did not occur at that time. I tried one editor called Geany. It was nice, it could run code but i felt it was more of an editor than an IDE, maybe, the looks of it made me go for another one, or maybe, i could not run the code for i only saw the compile button, maybe i was just a beginner ...

I finally settled with Wing IDE and used it for a looong time. I had no issues with it. Just a tidbit starting time but it was customisable and offered profiling options. The switch came with the monstrously equipped Anaconda. That one came with Spyder the IDE and Jupyter. It was super loaded with nice packages. It was simply awesome (but spyder can be heavy). It saved the pain to intall numpy and pandas at the very least!

Then, one day someone named James Rodri from Kynesim LTD (Cambridge) told me he was using Sublime Text as his everyday py tool. I said what? that editor? It was unbelievable. That's precisely the difference between an IDE and an editor. How can he do pro dev with that prehistoric tool, it was just crazy! I asked him few questions like did he not miss some variable inspector or things like that. He seemed to be really ok with his editor. Finally, while researching i discovered that you can make sublime text execute your code with ctrl+b and ... you get to choose what py vers you want. You just have to specify the executable path (the pyhon.exe) beforehand. That blew away my IDE-was-better notion. It was light, had syntax highlighting and ... had all what i needed.

### Doing Things In Style (in enters PEP8)

While getting help for debugging my code, reviewers were having a hardTime reading mycode as i was not following PEP8, neither in VariableNaming, nor in alignment nor in anything. I decided to apply PEP8, well, it makes codes more readable and ensures a minimal consistency among devs. Even when using an IDE, if a linter is not available, you'll miss some points ... which others discover when they open their's equiped with linters. PEP8 i believe is the first step towards professionalism!

### The Community, An Incredible Argument

The python mailing lists were incredible. It's not only about QnAs or RTFM, but, it's about the touch of liveliness. Sure, you'll get your answer but, with a touch of uniqueness. You can help others ... and you clear away doubts instantly. I learnt really much just reading that list. Sometimes, it's just about coding in general, or about dev experience of an embedded programmer or some stuffs like that. The topics are quite loose with the mods stepping in when needed (and banning occasionally). XD when master and slaves were removed from the docs, an issue popped up about beautiful and ugly and prejudice. Some funny issues like the +1 issue or witness the discussion over a PEP (with venerable Guido leaving, leaving it to a steering committee). I recommend following all the official lists (bug tracker can be a real bug as it is annoying but does not have an unsubscribe link).

### The Open Python Model: A Lesson in Corporate Management

Python's devlopment is influenced by it's members. It's not a hard rule under a dictatorship. Anybody can write a PEP and submit for approval. If no technical barriers, it'll be more likely adopted and implemented. It's just incredible, you get to follow the formation of killer features! Py features don't appear overnight, they grow!

### Data Science and Machine Learning: What Makes The Python Coder Stands Out

Data and ML is in the syllabus. It's an initiation ritual. No need to be a researcher, it's already in the path. Compare the data-dedicated R and Python. Compare the codes. R is leaner, but Py is just some 5 lines behind; not bad for a general purpose language. Let us take the example of you doing backend dev with py. You've collected data. Now, AI is just few imports away. Simple. Just imagine that treasure.

### Startups and Economic Incentives

By picking py, you are picking an oil rig for your startup, just ... naturally. Add IoT to it, and ... well that's just a crazy package. The line is really blurred between a webdev and a penetration tester. One language that really fits in a number of fields. A dream team aligned on the same language? Totally possible. And, that saves money while increasing broadness of vision! Let python be the river that flows through your gardens or the electricity that power up your appliances. But don't be like Digg, learn py well!

### Clutter-free: Designed for humans

Well, no main function to say hello. This is what impressed beginner coders (my students) who just arrived from Java. You want a script, a deadly simple one, no need to remember import this.resource.that or #define that or whatever. It's just quick, it just does your job. Come on, in this century of ours where car drive themselves, why so much clutter? We need to upgrade our language specification standards! (that for another post)

### An Avalanche of Packages

I once read a home astrophysics book with codes written in Basic. I wondered how we can apply what's in the book as Basic is nowhere to be seen. Dr. Ernest T. Wright (NASA) told me no worry, py has awesome packages for that (though he himself disliked py). Indeed, pip seems just like part of python, not a remote collection

### Conclusion

Since meeting py, i'm still with it. I choose langs according to needs of projects, but the language of choice remains python. It's up to become the most popular language. Just a tidbit more!
