def true_false_to_NUM(bool_word):
    if bool_word == False:
        num_bool = 0
    else:
        num_bool = 1
    print (num_bool)

true_false_to_NUM(True and True)
true_false_to_NUM(False and True)
true_false_to_NUM(1 == 1 and 2 == 1)
true_false_to_NUM("test" == "test")
true_false_to_NUM(1 == 1 or 2 != 1)
true_false_to_NUM(True and 1 == 1)
true_false_to_NUM(False and 0 != 0)
true_false_to_NUM(True or 1 == 1)
true_false_to_NUM("test" == "testing")
true_false_to_NUM(1 != 0 and 2 == 1)
true_false_to_NUM("test" != "testing")
true_false_to_NUM("test" == 1)
true_false_to_NUM(not (True and False))
true_false_to_NUM(not (1 == 1 and 0 != 1))
true_false_to_NUM(not (10 == 1 or 1000 == 1000))
true_false_to_NUM(not (1 != 10 or 3 == 4))
true_false_to_NUM(not ("testing" == "testing" and "Zed" == "Cool Guy"))
true_false_to_NUM(1 == 1 and (not ("testing" == 1 or 1 == 0)))
true_false_to_NUM("chunky" == "bacon" and (not (3 == 4 or 3 == 3)))
true_false_to_NUM(3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")))
