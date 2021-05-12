#Shubham Arya 1001650536

fileContent = open("textfile.txt", "r")

allContent = list()

for line in fileContent:
    newLine = list(line.replace(" ","").rstrip("\n"))
    allContent.append(newLine)

baseball_game_on_TV = 0

baseball_X_watches = 0
notbaseball_X_watches = 0

out_of_cat_food = 0

watches_outOfFood_feedsCat = 0
watches_outOfFood = 0

watches_notoutOfFood_feedsCat = 0
watches_notoutOfFood = 0

notwatches_outOfFood_feedsCat = 0
notwatches_outOfFood = 0

notwatches_notoutOfFood_feedsCat = 0
notwatches_notoutOfFood = 0

for content in allContent:
    # P(baseball_game_on_TV)
    if content[0] == '1':
        baseball_game_on_TV += 1
        
    # P(baseball_game_on_TV / George_watches_T)
    if content[0] == '1' and content[1] == '1':
        baseball_X_watches += 1
    if content[0] == '0' and content[1] == '1':
        notbaseball_X_watches += 1
        
    # P(out_of_cat_food)
    if content[2] == '1':
        out_of_cat_food += 1
        
    # P(George_feeds_cat | George_watches_TV , out_of_cat_food)
    if content[1] == '1' and content[2] == '1' and content[3] == '1':
        watches_outOfFood_feedsCat += 1
    
    if content[1] == '1' and content[2] == '1':
        watches_outOfFood += 1
        
    if content[1] == '1' and content[2] == '0' and content[3] == '1':
        watches_notoutOfFood_feedsCat += 1
    
    if content[1] == '1' and content[2] == '0':
        watches_notoutOfFood += 1
        
    if content[1] == '0' and content[2] == '1' and content[3] == '1':
        notwatches_outOfFood_feedsCat += 1
    
    if content[1] == '0' and content[2] == '1':
        notwatches_outOfFood += 1
        
    if content[1] == '0' and content[2] == '0' and content[3] == '1':
        notwatches_notoutOfFood_feedsCat += 1
    
    if content[1] == '0' and content[2] == '0':
        notwatches_notoutOfFood += 1
    
print("P(baseball_game_on_TV) = ", baseball_game_on_TV/365)

print("--------------------------------------------------")
print("P(baseball_game_on_TV = T / George_watches_TV = T) ",baseball_X_watches/ baseball_game_on_TV)
print("P(baseball_game_on_TV = T / George_watches_TV = F) ",notbaseball_X_watches / (365 - baseball_game_on_TV))

print("--------------------------------------------------")        
print("P(out_of_cat_food) ", out_of_cat_food/365)

print("--------------------------------------------------")
print("P(George_feeds_cat = T | George_watches_TV = T , out_of_cat_food = T)  ", watches_outOfFood_feedsCat/watches_outOfFood)
print("P(George_feeds_cat = T | George_watches_TV = T , out_of_cat_food = F)  ", watches_notoutOfFood_feedsCat/watches_notoutOfFood)
print("P(George_feeds_cat = T | George_watches_TV = F , out_of_cat_food = T)  ", notwatches_outOfFood_feedsCat/notwatches_outOfFood)
print("P(George_feeds_cat = T | George_watches_TV = F , out_of_cat_food = F)  ", notwatches_notoutOfFood_feedsCat/notwatches_notoutOfFood)











