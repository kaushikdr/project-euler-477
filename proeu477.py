def generate_seq(num):
    seq_list = []
    #pdb.set_trace()
    seq_list.append(0)
    for i in xrange(0,num-1):
        seq_list.append(((seq_list[i]**2)+45) % 1000000007)
    return seq_list

#t = input()
#pdb.set_trace()

#lis = generate_seq(t)
#for i in lis:
#   print i

def calculate(seq_list):
    first = True
    total = 0
    while (len(seq_list)>3):
        if (((seq_list[len(seq_list)-2]>seq_list[0]) and (seq_list[len(seq_list)-2]>seq_list[len(seq_list)-1])) and ((seq_list[1]>seq_list[0]) and (seq_list[1]>seq_list[len(seq_list)-1])) ):
            if (seq_list[1]>seq_list[len(seq_list)-2]):
                if first:
                    total += seq_list.pop()
                    first = False
                else:
                    seq_list.pop()
                    first = True
            else:
                if first:
                    total += seq_list.pop(0)
                    first = False
                else:
                    seq_list.pop(0)
                    first = True
        else:
            if (seq_list[0]>seq_list[len(seq_list)-1]):
                if first:
                    total += seq_list.pop(0)
                    first = False
                else:
                    seq_list.pop(0)
                    first = True
            else:
                if first:
                    total += seq_list.pop()
                    first = False
                else:
                    seq_list.pop()
                    first = True
    while (len(seq_list)>1):
        if (seq_list[0]>seq_list[len(seq_list)-1]):
            if first:
                total += seq_list.pop(0)
                first = False
            else:
                seq_list.pop(0)
                first = True
        else:
            if first:
                total += seq_list.pop()
                first = False
            else:
                seq_list.pop()
                first = True
    if first:
        total += seq_list.pop()

    return total

print "Enter N for F(N)"
num = input()
sequence_list = generate_seq(num)
fn = calculate(sequence_list)
print fn
