# Tiny Mad Library
# Ask user for words, and make a story out of them!

SENTENCE_START : str = "Code in Place is fun. I learnt to program and used\
 python to make my"

class MadLib:
    def generate_sentence(self):
        print(SENTENCE_START + " " + self.adjective + " " + self.noun + " " + self.verb + "!")

    def __init__(self,adjective : str,noun: str,verb: str):
        self.noun = noun
        self.adjective = adjective
        self.verb = verb

def main():
    # Prompt the user for the words
    adjective : str = input("Please type an adjective and press enter. ")
    noun : str = input("Please type a noun and press enter. ")
    verb : str = input("Please type a verb and press enter. ")

    # Create a madlib instance
    mad_lib : MadLib = MadLib(adjective=adjective,noun=noun,verb=verb)

    # Display the sentence!
    mad_lib.generate_sentence()

if __name__ == '__main__':
    main()