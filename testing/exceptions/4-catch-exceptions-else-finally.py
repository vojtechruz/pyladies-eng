
def test():
    try:
        print("This will do")
        raise ValueError
    except ValueError:
        print("This will be printed if there's a ValueError.")
    except NameError:
        print("This will be printed if there's a NameError.")
    except Exception:
        print("This will be printed if there's some other exception.")
        # (apart from SystemExit a KeyboardInterrupt, we don't want to catch those)
    except TypeError:
        print("This will never be printed")
        # ("except Exception" above already caught the TypeError)
    else:
        print("This will be printed if there's no error in try block")
    finally:
        print("This will always be printed; even if there's e.g. a 'return' in the 'try' block.")


if __name__ == '__main__':
    print(test())