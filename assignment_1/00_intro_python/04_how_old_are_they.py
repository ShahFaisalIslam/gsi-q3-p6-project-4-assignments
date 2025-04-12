# How old are they?
# Solve an age-related riddle

def main():
    # Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:
    # Anton is 21 years old
    anton : int = 21
    # Beth is 6 years younger than Anton
    beth : int = anton - 6
    # Chen is 20 years older than Beth
    chen : int = beth + 20
    # Drew is as old as Chen's age plus Anton's age
    drew : int = chen + anton
    # Ethan is the same age as Chen
    ethan : int = chen

    # Print their ages
    print(f"""\
Anton is {anton}
Beth is {beth}
Chen is {chen}
Drew is {drew}
Ethan is {ethan}
""")

if __name__ == '__main__':
    main()