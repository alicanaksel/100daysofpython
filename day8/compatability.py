def calculate_love_score(name1, name2):
    true="true"
    love="love"
    true_count=0
    love_count=0
    for i in name1:
        if i in true:
            true_count +=1
        if i in love:
            love_count += 1
    for i in name2:
        if i in true:
            true_count +=1
        if i in love:
            love_count += 1
        
    love_score=f"{true_count}{love_count}"
    print(love_score)


calculate_love_score("Kanye","Kim")