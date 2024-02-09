"""Function Decorators"""
def positives_only(func):
    def wrapper(values):
        values = [i for i in values if i >= 0]
        return func(values)
    return wrapper

@positives_only
def average(numbers):
    return sum(numbers)/len(numbers)


def main():
    print("Hello")
    print("Hello")
    print("Hello")

if __name__ == "__main__":
    main()