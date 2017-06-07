#input
list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

#program
list_check = []
i = 0
if len(list_one) == len (list_two):
    while i < len(list_one):
        if list_one[i] == list_two[i]:
            list_check.append(list_one[i])
            i = i + 1
        else:
            break
    if len(list_one) == len(list_check) == len(list_two):
        print "The lists are the same"
    else:
        print "The lists are not the same"
