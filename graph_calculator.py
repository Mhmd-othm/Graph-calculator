import numpy as np
import matplotlib.pyplot as plt
import math
import string


def menu() -> int:
    """
    input: The func dose not take any input
    output: The func return an int number between 0 and 10
    """
    print("Välkommen till den grafiska algebrakalkylatorn\n"+"-"*46)
    print("""1. Mata in vektor a
2. Mata in vektor b
3. Beräkna a + b
4. Beräkna a - b
5. Multiplicera a med skalär (konstant)
6. Beräkna skalärprodukt mellan a och b
7. Beräkna vektorprodukt mellan a och b
8. Mata in plan p
9. Visa planet p
10. Projicera vektorn a på planet p
0. Avsluta programmet""")
    choice = input("Ditt val: ")
    while not choice.isnumeric() or int(choice) > 10:
        choice = input("Ditt val: ")
    return int(choice)


def input_vector() -> None:
    """
    input: the func take vector name
    output: the func return ndarray type list which contain 3 elenment
    """
    vector = input("Mata in vektorvärden (x,y,z) på formen x y z:").split()
    while len(vector) != 3 or\
            not vector[0].replace("-", "").replace(".", "").replace("/", "").isnumeric() or\
            not vector[1].replace("-", "").replace(".", "").replace("/", "").isnumeric() or\
            not vector[2].replace("-", "").replace(".", "").replace("/", "").isnumeric():
        vector = input("Mata in vektorvärden (x,y,z) på formen x y z: ").split()

    for i, num in enumerate(vector):
        if "/" in vector[i]:
            vector_splited = vector[i].split("/")
            vector[i] = float(vector_splited[0]) / float(vector_splited[1])
        else:
            vector[i] = float(num)

    vector = np.array(vector)
    return vector


def input_plane():
    print("Ekvationen för ett plan är a*x + b*y + c*z + d = 0 ")
    all_num = input("Mata in önskade parametrar på formen a b c d: ").split()
    while len(all_num) != 4 or\
            not all_num[0].replace("-", "").replace(".", "").replace("/", "").isnumeric() or\
            not all_num[1].replace("-", "").replace(".", "").replace("/", "").isnumeric() or\
            not all_num[2].replace("-", "").replace(".", "").replace("/", "").isnumeric() or\
            not all_num[3].replace("-", "").replace(".", "").replace("/", "").isnumeric() or\
            (float(all_num[0]) == 0.0 and float(all_num[1]) == 0.0 and float(all_num[2]) == 0.0):

        print("Det finns inget sådant plan! Försök igen! ")
        all_num = input("Mata in önskade parametrar på formen a b c d: ").split()

    for i, num in enumerate(all_num):
        if "/" in all_num[i]:
            vector_splited = all_num[i].split("/")
            all_num[i] = float(vector_splited[0]) / float(vector_splited[1])
        else:
            all_num[i] = float(num)

    a, b, c, d = all_num
    plane = np.array([a, b, c, d])

    return plane


def vector_calculation(a: np.ndarray, b: np.ndarray, operation: string) -> np.ndarray:
    if operation == "+":
        result = a + b
        a_version = tuple(a.tolist())
        b_version = tuple(b.tolist())
        result_version = tuple(result.tolist())
        print(f"Resultatet är: {a_version} + {b_version} = {result_version}")
    elif operation == "-":
        result = a - b
        a_version = tuple(a.tolist())
        b_version = tuple(b.tolist())
        result_version = tuple(result.tolist())
        print(f"Resultatet är: {a_version} - {b_version} = {result_version}")

    return result


def save_vector_image(vector_a, vector_b, result: np.ndarray, operation: string) -> None:

    ORIGiN = np.zeros_like(vector_a)
    myfig = plt.figure()
    axes = myfig.add_subplot(projection="3d")
    axes.set_xlabel("X")
    axes.set_ylabel("Y")
    axes.set_zlabel("Z")

    all_vector = np.array([vector_a, vector_b, result])
    max_value = np.max(np.abs(all_vector))
    limit = max_value * 1.6
    if sum(vector_a) + sum(vector_b) + sum(result) == 0:
        axes.set_xlim(-5, 5)
        axes.set_ylim(-5, 5)
        axes.set_zlim(-5, 5)
    else:
        axes.set_xlim(-limit, limit)
        axes.set_ylim(-limit, limit)
        axes.set_zlim(-limit, limit)
    if operation == "+":
        plt.quiver(*ORIGiN, *vector_a, color="red", label="vektor a")
        plt.quiver(*vector_a, *vector_b, color="green", label="vektor b")
        plt.quiver(*ORIGiN, *result, color="blue", label="vektor a + b")
    elif operation == "-":
        plt.quiver(*ORIGiN, *vector_a, color="red", label="vektor a")
        plt.quiver(*result, *vector_b, color="green", label="vektor b")
        plt.quiver(*ORIGiN, *result, color="blue", label="vektor a - b")
    elif operation == "scalar":
        plt.quiver(*ORIGiN, *vector_b, color="red", label="vektor")
        plt.quiver(*ORIGiN, *vector_a, color="green", label="skälar  vektor", linestyle=':')
    elif operation == "vector_product":
        plt.quiver(*ORIGiN, *vector_a, color="red", label="vektor a")
        plt.quiver(*ORIGiN, *vector_b, color="green", label="vektor b")
        plt.quiver(*ORIGiN, *result, color="blue", label="produkt vektor")
    plt.legend()
    plt.show()

    svar = input("Vill du spara bilden på fil (J/N)?").lower()
    if svar == "j":
        filename = input("Filnamn: ")
        while not filename.endswith(".png") and\
                not filename.endswith(".pdf") and\
                not filename.endswith(".svg"):
            filename = input("Filnamn(Filnamn måste sluta med .png, .pdf eller svg): ")
    if svar == "j":
        myfig.savefig(filename)

    plt.close(myfig)


def vector_size(vector: list) -> int:
    return math.sqrt(vector[0]*vector[0] + vector[1]*vector[1] + vector[2]*vector[2])


def scalar_vector(vector_a: np.ndarray, vector_b: np.ndarray) -> np.ndarray:
    scalar_check = False
    zero_vector = np.array([0, 0, 0])
    which_vector = input("Vilken vektor vill du multiplicera med skälar(a eller b):").lower()
    while which_vector != "a" and which_vector != "b":
        which_vector = input("\nVilken vektor vill du multiplicera med skälar(a eller b):").lower()

    if which_vector == "a" and isinstance(vector_a, np.ndarray):
        scalar = input("Vilken skälar vill du multiplicera vector med: ")

        while not scalar.replace("-", "").replace(".", "").replace("/", "").isnumeric():
            print("Ogiltig siffra")
            scalar = input("Vilken skälar vill du multiplicera vector med: ")
        if "/" in scalar:
            scalar_splited = scalar.split("/")
            scalar = float(scalar_splited[0]) / float(scalar_splited[1])
        scalar = float(scalar)

        result_scalar = vector_a*scalar
        print("Resultat: ", tuple(result_scalar.tolist()), "\n")
        scalar_check = True
        return result_scalar, "a"

    elif which_vector == "b" and isinstance(vector_b, np.ndarray):
        scalar = input("Vilken skälar vill du multiplicera vector med: ")
        while not scalar.replace("-", "").replace(".", "").replace("/", "").isnumeric():
            print("Ogiltig siffra")
            scalar = input("Vilken skälar vill du multiplicera vector med: ")
        if "/" in scalar:
            scalar_splited = scalar.split("/")
            scalar = float(scalar_splited[0]) / float(scalar_splited[1])
        scalar = float(scalar)
        result_scalar = vector_b*scalar

        print("Resultat: ", tuple(result_scalar.tolist()), "\n")
        scalar_check = True
        return result_scalar, "b"
    else:
        if scalar_check is False and which_vector == "a":
            print("Vektor a finns inte! ")
        elif scalar_check is False and which_vector == "b":
            print("Vektor b finns inte! ")
        return zero_vector, ""


def plane_vector_image(plane_abcd):
    a, b, c, d = plane_abcd
    x, y = np.meshgrid(range(11), range(11))

    if c != 0:
        z = -(a * x + b * y + d) / c
    elif b != 0:
        y = -(a * x + d) / b
        # ---------
        x, z = np.meshgrid(range(11), range(11))
        # ---------
    elif a != 0:
        x = -(d) / a
        y, z = np.meshgrid(range(11), range(11))

    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")

    ax.plot_surface(x, y, z, color="cyan", alpha=0.7)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

    svar = input("Vill du spara bilden på fil (J/N)?").lower()
    if svar == "j":
        filename = input("Filnamn: ")
        while not filename.endswith(".png") and\
                not filename.endswith(".pdf") and\
                not filename.endswith(".svg"):
            filename = input("Filnamn(Filnamn måste sluta med .png, .pdf eller svg): ")
    if svar == "j":
        fig.savefig(filename)

    plt.close()


def projection_vector_on_plane(plane_abcd, vector):
    # rita planet
    a, b, c, d = plane_abcd
    all_vector = np.array([vector])
    max_value = np.max(np.abs(all_vector))
    limit = max_value * 1.6
    limit_int = int(limit) + 1

    # x_range = np.array(range(-limit_int, limit_int))
    # y_range = np.array(range(-limit_int, limit_int))

    x, y = np.meshgrid(range(-limit_int, limit_int), range(-limit_int, limit_int))
    if c != 0:
        z = -(a * x + b * y + d) / c
        start = np.array([0, 0, -d/c])
    elif b != 0:
        y = -(a * x + d) / b
        # ---------
        x, z = np.meshgrid(range(-limit_int, limit_int), range(-limit_int, limit_int))
        # ---------
        start = np.array([0, -d/b, 0])
    elif a != 0:
        x = -(d) / a
        y, z = np.meshgrid(range(-limit_int, limit_int), range(-limit_int, limit_int))
        start = np.array([-d/a, 0, 0])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(x, y, z, color="cyan", alpha=0.7)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    # räkna vecktor

    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)
    ax.set_zlim(-limit, limit)

    n = np.array([a, b, c])
    proj = vector - ((np.dot(vector, n)) / (vector_size(n))**2) * n

    ax.quiver(*start, *vector, color="red", label="Vektor")
    ax.legend()
    if np.array_equal(proj, np.array([0, 0, 0])):
        print("Projectionen är nollvektor! ")
        ax.quiver(*start, *proj, color="blue", label="Nollvektor")
    else:
        ax.quiver(*start, *proj, color="blue", label="projectionen")

    print(f"Resultat: {tuple(proj.tolist())}")

    plt.show()
    svar = input("Vill du spara bilden på fil (J/N)?").lower()
    if svar == "j":
        filename = input("Filnamn: ")
        while not filename.endswith(".png") and\
                not filename.endswith(".pdf") and\
                not filename.endswith(".svg"):
            filename = input("Filnamn(Filnamn måste sluta med .png, .pdf eller svg): ")

    if svar == "j":
        fig.savefig(filename)

    plt.close(fig)
    plt.close()


def main():

    main_choice = menu()
    vector_a = 0
    vector_b = 0
    plane_abcd = None

    while main_choice != 0:
        if main_choice == 1:
            print("Tar in värden för vektor a!")
            vector_a = input_vector()
            print("\n")
        elif main_choice == 2:
            print("Tar in värden för vektor b!")
            vector_b = input_vector()
            print("\n")
        elif main_choice == 3:
            if type(vector_a) == int or type(vector_b) == int:
                print("Vektor a eller b saknas!")
            else:

                return_result = vector_calculation(vector_a, vector_b, "+")

                print("Vill du spara resultatet i a eller b?")
                print("(Svara a eller b för att spara, andra val betyder nej.)")
                save_answer = input("Ditt val: ")

                if save_answer == "a":
                    save_vector_image(vector_a, vector_b, return_result, "+")
                    vector_a = return_result[:]
                elif save_answer == "b":
                    save_vector_image(vector_a, vector_b, return_result, "+")
                    vector_b = return_result[:]
                else:
                    save_vector_image(vector_a, vector_b, return_result, "+")

                print("\n")
        elif main_choice == 4:
            if type(vector_a) == int or type(vector_b) == int:
                print("Vektor a eller b saknas!")
            else:
                return_result = vector_calculation(vector_a, vector_b, "-")

                print("Vill du spara resultatet i a eller b?")
                print("(Svara a eller b för att spara, andra val betyder nej.)")
                save_answer = input("Ditt val: ")
                if save_answer == "a":
                    save_vector_image(vector_a, vector_b, return_result, "-")
                    vector_a = return_result[:]
                elif save_answer == "b":
                    save_vector_image(vector_a, vector_b, return_result, "-")
                    vector_b = return_result[:]
                else:
                    save_vector_image(vector_a, vector_b, return_result, "-")

            print("\n")
        elif main_choice == 5:

            scaled_vector, which = scalar_vector(vector_a, vector_b)
            zero_vector = np.array([0, 0, 0])

            if which == "a":
                save_vector_image(scaled_vector, vector_a, zero_vector, "scalar")
            elif which == "b":
                save_vector_image(scaled_vector, vector_b, zero_vector, "scalar")
            print("\n")
        elif main_choice == 6:
            if isinstance(vector_a, np.ndarray) and isinstance(vector_b, np.ndarray):
                scalar_product = np.dot(vector_a, vector_b)
                print("Resultat:", scalar_product)
            else:
                print("Vektor a eller b saknas! ")
            print("\n")
        elif main_choice == 7:
            if isinstance(vector_a, np.ndarray) and isinstance(vector_b, np.ndarray):
                scalar_product = np.cross(vector_a, vector_b)
                print("Vektor produkt blir:", tuple(scalar_product.tolist()))
                save_vector_image(vector_a, vector_b, scalar_product, "vector_product")
            else:
                print("Vektor a eller b saknas! ")
            print("\n")
        elif main_choice == 8:
            plane_abcd = input_plane()
            print("\n")
        elif main_choice == 9:
            if plane_abcd is None:
                print("Du har matat in någon plan! ")
            else:
                plane_vector_image(plane_abcd)
            print("\n")
        elif main_choice == 10:
            if plane_abcd is None:
                print("Du har inte matat in någon plan! ")
            else:
                which_vector = input("Vill projicera vector a eller b på planet:").lower()
                while which_vector != "a" and which_vector != "b":
                    which_vector = input("\nMultiplicera med skälar vektor (a eller b): ").lower()
                if which_vector == "a" and isinstance(vector_a, np.ndarray):
                    projection_vector_on_plane(plane_abcd, vector_a)
                elif which_vector == "b" and isinstance(vector_b, np.ndarray):
                    projection_vector_on_plane(plane_abcd, vector_b)
                else:
                    print("Vektor a eller b saknas! ")
            print("\n")
        main_choice = menu()
    print("Porgrammet avslutas ...")


if __name__ == "__main__":

    main()
