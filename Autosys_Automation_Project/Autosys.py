test_string = "P74.test1.4232 \nP74.test1.4232 \nP74.test1.4232 \nP74.test1.last\n"
test_string1 = "P74.test1.1234" \
               "p74.test1.4323" \
               "p74.test1.4323" \
               "p74.test1.4323"



func = lambda s: s[:1].lower() + s[1:] if s else ''


def test(x):
    jobs = x.split()
    count = 0
    valueauto = ''

    while(count < len(x.split())):
        valueauto = valueauto + (func(jobs[count]) + ",")
        count = count + 1

    valueauto = valueauto[:-1]
    print(valueauto)


test(test_string1)
