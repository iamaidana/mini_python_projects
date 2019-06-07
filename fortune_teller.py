import random
print("Hello Truth Seeker! Greetings to you and all that is around you. "
      "I am a fortune-teller, and this is what I say about you: ")

def getAnswer(answerNumber):
    if answerNumber == 1:
        return '\nYou will get money from an unexpected place.'
    elif answerNumber == 2:
        return '\nA thrilling time is in your near future.'
    elif answerNumber == 3:
        return '\nSomeone will call you today.'
    elif answerNumber == 4:
        return '\nBe careful what you say behind a friend\'s back.'
    elif answerNumber == 5:
        return '\nInjuries from harsh words should soon be repaired.'
    elif answerNumber == 6:
        return '\nAn item lost will soon be found, in a very unusual place.'
    elif answerNumber == 7:
        return '\nYou are very smart.'
    elif answerNumber == 8:
        return '\nIf you look for happiness in the darkness, do not be surprised that you cannot see it.'
    elif answerNumber == 9:
        return '\nWhen things look darkest have faith. They will soon brighten again.'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)