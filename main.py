from datetime import datetime

from car.car_factory import CarFactory

def main():

    current_date = datetime.now()

    # Ejemplo de creación de un coche Calliope
    calliope_car = CarFactory.create_calliope(current_date, datetime(2023,8,20), 50000, 45000)
    print("Calliope Car:")
    print("Needs Service:", calliope_car.needs_service())

    # Ejemplo de creación de un coche Glissade
    glissade_car = CarFactory.create_glissade(current_date, datetime(2023,10,11), 40000, 38000)
    print("\nGlissade Car:")
    print("Needs Service:", glissade_car.needs_service())

    # Ejemplo de creación de un coche Palindrome
    palindrome_car = CarFactory.create_palindrome(current_date, "2023-12-25", True)
    print("\nPalindrome Car:")
    print("Needs Service:", palindrome_car.needs_service())

    # Ejemplo de creación de un coche Rorschach
    rorschach_car = CarFactory.create_rorschach(current_date, "2023-11-15", 30000, 28010)
    print("\nRorschach Car:")
    print("Needs Service:", rorschach_car.needs_service())

    # Ejemplo de creación de un coche Thovex
    thovex_car = CarFactory.create_thovex(current_date, "2023-09-30", 45000, 42000)
    print("\nThovex Car:")
    print("Needs Service:", thovex_car.needs_service())

if __name__ == "__main__":
    main()