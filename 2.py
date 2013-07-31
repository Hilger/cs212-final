"""
UNIT 2: Logic Puzzle

You will write code to solve the following logic puzzle:

1. The person who arrived on Wednesday bought the laptop.
2. The programmer is not Wilkes.
3. Of the programmer and the person who bought the droid,
   one is Wilkes and the other is Hamming.
4. The writer is not Minsky.
5. Neither Knuth nor the person who bought the tablet is the manager.
6. Knuth arrived the day after Simon.
7. The person who arrived on Thursday is not the designer.
8. The person who arrived on Friday didn't buy the tablet.
9. The designer didn't buy the droid.
10. Knuth arrived the day after the manager.
11. Of the person who bought the laptop and Wilkes,
    one arrived on Monday and the other is the writer.
12. Either the person who bought the iphone or the person who bought the tablet
    arrived on Tuesday.

You will write the function logic_puzzle(), which should return a list of the
names of the people in the order in which they arrive. For example, if they
happen to arrive in alphabetical order, Hamming on Monday, Knuth on Tuesday, etc.,
then you would return:

['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']

(You can assume that the days mentioned are all in the same week.)
"""

from itertools import permutations

def day_after(a,b):
    return a == b + 1

def logic_puzzle():
    "Return a list of the names of the people, in the order they arrive."
    ## your code here; you are free to define additional functions if needed
    days = Monday, Tuesday, Wednesday, Thursday, Friday = [1, 2, 3, 4, 5]
    orderings = list(permutations(days))

    result = list(next((Hamming, Knuth, Minsky, Simon, Wilkes)
                for (Hamming, Knuth, Minsky, Simon, Wilkes) in orderings
                if day_after(Knuth, Simon) #6
                for (programmer, writer, designer, manager, nojob) in orderings
                if designer != Thursday #7
                if Wilkes != programmer #2
                if Minsky != writer #4
                if Knuth != manager #5
                if day_after(Knuth, manager) #10
                for (laptop, tablet, droid, iphone, nopurchase) in orderings
                if laptop == Wednesday #1
                if ((Wilkes == droid and Hamming == programmer) or \
                   (Wilkes == programmer and Hamming == droid)) #3
                if tablet != manager #5
                if tablet != Friday #8
                if designer != droid #9
                if ((Wilkes == writer and laptop == Monday) or \
                   (Wilkes == Monday and laptop == writer)) #11
                if tablet == Tuesday or iphone == Tuesday #12
                ))

    people = ["Hamming", "Knuth", "Minsky", "Simon", "Wilkes"]
    return map(lambda x: x[0], sorted(zip(people, result), key=lambda x: x[1]))