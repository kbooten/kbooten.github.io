## Leaping Loom
## Kyle Booten
## Python, 2024

from random import choice, randrange
import time
print("Weave a poem this way:\nLine 1: A line of poetry.")
actions = ["rhyming with"]*90+["syntactically echoing",
"using a phrase from","riffing on"]*26+["contradicting"]*10
actions += ["%s the %s word of" % (ac,word) for ac in 
["using","using a more precise word for",
"internally rhyming with"]*6+["punning on"] for word in 
["(ignoring stop words) first","(ignoring stop words) last",
"most salient","rarest"]]
c = 2
while True:
    print("Line %d: This one %s Line %d." 
        % (c,choice(actions),randrange(1,c)))
    c+=1
    time.sleep(3)

# Weave a poem this way:
# Line 1: A line of poetry.
# Line 2: This one using a more precise word for the (ignoring stop words) first word of Line 1.
# Line 3: This one using the (ignoring stop words) first word of Line 2.
# Line 4: This one using a more precise word for the (ignoring stop words) first word of Line 3.
# Line 5: This one internally rhyming with the rarest word of Line 2.
# Line 6: This one using a more precise word for the most salient word of Line 5.
# Line 7: This one using a phrase from Line 1.
# Line 8: This one punning on the most salient word of Line 4.
# Line 9: This one using a phrase from Line 1.
# Line 10: This one syntactically echoing Line 4.
# Line 11: This one using the (ignoring stop words) first word of Line 9.
# Line 12: This one using a phrase from Line 11.
# Line 13: This one using the (ignoring stop words) first word of Line 1.
# Line 14: This one rhyming with Line 4.
# Line 15: This one rhyming with Line 9.
# Line 16: This one syntactically echoing Line 10.
# Line 17: This one rhyming with Line 6.
# Line 18: This one riffing on Line 2.
# Line 19: This one internally rhyming with the most salient word of Line 10.
# Line 20: This one rhyming with Line 9.
# Line 21: This one rhyming with Line 12.
# Line 22: This one riffing on Line 8.
# Line 23: This one using the (ignoring stop words) last word of Line 1.
# Line 24: This one using a phrase from Line 21.
# Line 25: This one syntactically echoing Line 24.
# Line 26: This one syntactically echoing Line 8.
# Line 27: This one using a more precise word for the (ignoring stop words) last word of Line 20.