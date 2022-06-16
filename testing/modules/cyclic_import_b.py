import cyclic_import_a

def do_in_b():
    print("Ahoj ze souboru B!")

def do_something_in_b():
    cyclic_import_a.do_a()