
def volume_sphere(radius):

    volume = (4 / 3) * 3.14159 * radius ** 3

    return volume


def main():

    result = volume_sphere(10)

    print(result)


if __name__ == "__main__":
    main()
