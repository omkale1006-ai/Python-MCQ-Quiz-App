# Quiz app 
quations = [
    "1.  Bharat ka samvidhan kis din lagu hua tha?"
    "2. CPU ka full form kya hai?"
    "3. Python ko kisne banaya tha?"
    "4. HTML ka full form kya hai?"
    "5. Mahabharat ke mukhya kavi kaun the?"
    
]

options = [
    ["a)15 August 1947","b) 26 January 1950", "c) 2 October 1948","d) 26 November 1949"],
    ["a) Central Performance Unit", "b) Central Processing Unit", "c) Computer Processing Unit", "d) Control Power Unit"],
    ["a) Dennis Ritchie", "b) James Gosling", "c) Guido van Rossum", "d) Mark Zuckerberg"],
    ["a) Hyper Trainer Marking Language", "b) Hyper Text Markup Language", "c) Hyper Text Making Line", "d) High Text Markup Language"],
    ["a) Valmiki", "b) Ved Vyas", "c) Tulsidas", "d) Kalidas"]

]

answer = ["b", "b", "c", "b", "b"]

score = 0

for i in range(len(quations)):
    print("\n"+ quations[i])
    for opt in options[i]:
        print(opt)
        user_ans=input("Enter your answer:(as a/b/c/d)").lower()
        if user_ans == answer[i]:
            print(f"{user_ans}Your answer is correct")
            score +=1
        else:
            print(f"your given answer is incorrect: correct answer is {answer[i]}")

print("\n aapka final score:",score,"/" ,len(quations))
if score == len(quations):
  print("bahut badiya! aapne sabhi sahi kiye!")
elif score >=2:
  print("achha kiya! thoda aur mehant karo.")
else:
  print("aapko thoda aur padhe ki zarurat hai.")
    