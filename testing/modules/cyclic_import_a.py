import cyclic_import_b

def do_a():
    print("Hi from A!")

def do_something_a():
    cyclic_import_b.do_something_in_b()