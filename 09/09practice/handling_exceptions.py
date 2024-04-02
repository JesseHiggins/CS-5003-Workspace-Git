import random
random.seed(0)

def generate_random_error():
    value = random.randint(0, 3)
    if value == 0:
        raise ZeroDivisionError(value)
    elif value == 1:
        raise TypeError(value)
    elif value == 2:
        raise ValueError(value)
    else:
        raise NameError(value)
    
def main():
    for i in range(20):
        
        try:

            generate_random_error()

        except TypeError:
            print("Type error raised   -- 1")
        except ValueError:
            print("Value error raised  -- 2")
        except ZeroDivisionError:
            print("Zero division error -- 0")
        except NameError:
            print("Name error raised   -- 3")

if __name__ == "__main__":
    main()