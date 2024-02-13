print("BASIC QUIZ GAME-->") # game name
print('choose any one option \n')
start = input('type yes to start: ')# input to start game

def sta(start):# user defined function
    if start == 'yes':
        points = 0  # Initialize points variable
        print('Q1. What is the capital of India ? a) Delhi b) Mumbai c) Uttar Pradesh ')# Q1
        ans = input("answer(only type option alphabet): ")
        if ans == 'a':
            print("yes write answer + 1 point \n")
            points += 1  # Increment points for correct answer
        else:
            print('wrong answer right answer was a) Delhi, no point \n ')

        print('Q2. What is the longest river of India ? a) Brahmaputra b) Ganga c) Narmada ')#Q2
        ans2 = input('answer(only type option alphabet): ')
        if ans2 == 'b':
            print('yes write answer + 1 point \n')
            points += 1  # Increment points for correct answer
        else:
            print('wrong answer right answer was b) Ganga, no point \n')

        print('Q3."Red Fort" is situated in which state of India ? a)Rajasthan b)Uttar Pradesh c) Delhi ')#Q3
        ans3 = input('answer(only type option alphabet): ')
        if ans3 == 'c':
            print('yes write answer + 1 point \n')
            points += 1  # Increment points for correct answer
        else:
            print('wrong answer right answer was c) Delhi, no point \n')
            
        print('Q4.Who is known as the Father of the Nation in India ? a) Jawaharlal Nehru b) Sardar Patel c) Mahatma Gandhi ? ')#Q4
        ans4 = input('answer(only type option alphabet): ')
        if ans4 == 'c':
            print('yes write answer + 1 point \n')
            points += 1  # Increment points for correct answer
        else:
            print('wrong answer right answer was c)Mahatma Gandhi , no point \n')

        print('Q5.Which festival is known as the Festival of Lights in India ? a) Diwali b) Holi c) Eid ')#Q5
        ans5 = input('answer(only type option alphabet): ')
        if ans5 == 'a':
            print('yes write answer + 1 point \n')
            points += 1  # Increment points for correct answer
        else:
            print('wrong answer right answer was a) Diwali, no point \n')

        print('Q6.In which direction is the Himalayan mountain range located in India ? a) North b) South c) East')#Q6
        ans6 = input('answer(only type option alphabet): ')
        if ans6 == 'a':
            print('yes write answer + 1 point \n')
            points += 1  # Increment points for correct answer
        else:
            print('wrong answer right answer was a) North, no point \n')


        print('You scored',points,f'{"point" if points==1 else "points"} out of 6 points.')  # Display total points
    else:
        print('type yes to start the game')

sta(start)
