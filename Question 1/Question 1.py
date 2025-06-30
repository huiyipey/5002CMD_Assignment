import random
from datetime import datetime
from collections import defaultdict

# create hash function (generate hash code from IC no dash)
# accept IC as parameter
# use appropriate folding technique
def folding_hash(ic, table_size):
    if len(ic) != 12:
        raise ValueError("IC number must be 12 digits long.")

    total = 0
    # Split into 4 digit per parts
    for i in range(0, len(ic), 4):
        part = ic[i:i+4]
        total += int(part)
    return total % table_size

# insert 1000 IC into 2 hash tables (function upper)
# first table size = 1009
# second table size = 2003
# use separate chaining (collision)
# repeat 10 rounds each table

def generate_ic():
    # Generate random birth year & month (from 1900 to current)
    current_year = datetime.now().year
    birth_year = random.randint(1900, current_year)
    birth_month = random.randint(1, 12)

    # Handle days per month (leap years)
    if birth_month == 2:
        if(birth_year % 400 == 0) or (birth_year % 100 != 0 and birth_year % 4 == 0):
            max_day = 29
        else:
            max_day = 28
    elif birth_month in [4, 6, 9, 11]:
        max_day = 30
    else:
        max_day = 31

    birth_day = random.randint(1, max_day)

    # Format birthdate display
    yymmdd = f"{birth_year % 100:02d}{birth_month:02d}{birth_day:02d}"

    # Generate state code (1-16, 21-68, 71-72, 74-79, 82-93, 98-99)
    state_list = (list(range(1, 17)) + list(range(21, 69)) + list(range(71, 73))
                   + list(range(74, 80)) + list(range(82, 94)) + list(range(98, 100)))
    state_code = f"{random.choice(state_list):02d}"

    # Generate last 4 digits
    generic_num = ''.join(str(random.randint(0, 9)) for _ in range(4))

    ## CAN REMOVE STR()!!!!!!!!!!
    return f"{yymmdd}{state_code}{generic_num}"
    # return ''.join(str(random.randint(0, 9)) for _ in range(12))
    # return random.randint(000000000000, 999999999999)

def insert_to_table(table_size, rounds):
    # total_collisions_per_round=[]
    total_collisions = 0
    collision_rate = 0
    # print(f"Hash Table Size: {table_size}")

    for r in range(rounds):
        hash_table = defaultdict(list)
        collisions = 0

        for _ in range(1000):
            ic = generate_ic()
            # print(f"IC number: {ic}")
            index = folding_hash(ic, table_size)
            # print(f"Hash index: {index}")

            # Collision occurred
            if hash_table[index]:
                collisions += 1
            hash_table[index].append(ic)

        for i in range(table_size):
            if hash_table[i]:
                print(f"table[{i}]", end="")
                for item in hash_table[i]:
                    print(f" --> {item}", end="")
                print()
            else:
                print(f"table[{i}]")

        total_collisions += collisions
        collision_rate = (total_collisions / (1000 * 10)) * 100
        print(f"Round {r+1}: {collisions} collisions")
        # total_collisions_per_round.append(collisions)
    print(f"Average collisions: {total_collisions / rounds:.2f}")
    return collision_rate
    # avg_collisions = sum(total_collisions_per_round) / rounds
    # return total_collisions_per_round, avg_collisions

def main():
    print("Hash Table with size 1009:")
    col_1009 = insert_to_table(1009, 10)
    # col_1009, avg_1009 = insert_to_table(1009)
    # print("Collisions per round:", col_1009)
    # print("Average collisions:", avg_1009)

    print("\nHash Table with size 2003:")
    col_2003 = insert_to_table(2003, 10)
    # col_2003, avg_2003 = insert_to_table(2003)
    # print("Collisions per round:", col_2003)
    # print("Average collisions:", avg_2003)

    print("\nCollision Rate for Smaller Hash Table: {:.2f} %".format(col_1009))
    print("Collision Rate for Bigger Hash Table: {:.2f} %".format(col_2003))

if __name__ == "__main__":
    main()

# calculate total collision for each 10 rounds (round 1: , round 2: , ...)
# calculate average collisions for each table (table 1: , table 2: )
# show output

