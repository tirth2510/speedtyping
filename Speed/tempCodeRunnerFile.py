#words=["lary is kind of kind maybe", "tom is coming here.", "kids are not playing."]
        words = ["An ever-growing number of complex and rigid rules plus hard-to-cope-with regulations are"]
        word = random.randint(0, (len(words)-1))
        
        x2 = Label(window, text=words[word], bg="black", fg="white", height=7, width=47, font="times 15", wraplength=500)
        x2.place(x=15, y=10)
        
        x3 = Button (window, text="Submit!", font="times 20", bg="#fc2828", command=check_result)
        x3.place(x=220, y=350)
        
        ally=Text(window)
        ally.place(x=100, y=180, height=150, width=350)
        
        b2 = Button(window, text="Done", font="times 13", bg='#ffc003', width=12, command=finish)
        b2.place(x=155, y=420)
        
        b3 = Button (window, text="Another One?", font="times 13", bg='#ffc003', width=12, command=game)
        b3.place(x=265, y=420)

        start=timer()

        window.