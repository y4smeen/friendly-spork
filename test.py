d = {
    "one": 1,
    "two": 2,
    "three": 3
}

def primaryEmotion( data ):
    l = d
    return max(l, key=lambda i: l[i])

emotion1 = primaryEmotion(d)
d.pop(emotion1,None)
emotion2 = primaryEmotion(d)

print str(emotion1) + "+" + str(emotion2)
