import json
import os
import random

def create_car_data(filename="cars.json"):
    """Створює JSON файл з даними про автомобілі, якщо його немає."""
    if not os.path.exists(filename):
        car_data = {
            "cars": [
                {"model": f"Model {i+1}", "price": random.randint(1000, 50000), "age": random.randint(1, 25)}
                for i in range(10)
            ]
        }
        with open(filename, "w") as f:
            json.dump(car_data, f, indent=4)
        print(f"Створено файл {filename} з прикладними даними.")

def display_json(filename="cars.json"):
    """Виводить вміст JSON файлу на екран у зручному форматі."""
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            if data and "cars" in data and data["cars"]: #перевіряємо, чи є дані
                print("Список автомобілів:")
                for i, car in enumerate(data["cars"]):
                    print(f"{i+1}. Модель: {car['model']}, Ціна: {car['price']}, Вік: {car['age']}")
            else:
                print("Список автомобілів порожній.")

    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
    except json.JSONDecodeError:
        print(f"Помилка розбору JSON у файлі {filename}.")
    except KeyError:
        print("Неправильна структура JSON файлу.")


def add_car(filename="cars.json"):
    """Додає новий запис до JSON файлу."""
    try:
        with open(filename, "r+") as f:
            data = json.load(f)
            model = input("Введіть модель автомобіля: ")
            price = int(input("Введіть ціну автомобіля: "))
            age = int(input("Введіть вік автомобіля: "))
            new_car = {"model": model, "price": price, "age": age}
            data["cars"].append(new_car)
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            print("Автомобіль успішно додано.")
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
    except json.JSONDecodeError:
        print(f"Помилка розбору JSON у файлі {filename}.")
    except (ValueError, KeyError):
        print("Некоректний ввід даних.")


def delete_car(filename="cars.json"):
    """Видаляє запис з JSON файлу за номером."""
    try:
        with open(filename, "r+") as f:
            data = json.load(f)
            print("Список автомобілів:")
            for i, car in enumerate(data["cars"]):
                print(f"{i+1}. {car['model']}")

            index_to_delete = int(input("Введіть номер автомобіля для видалення: ")) - 1
            if 0 <= index_to_delete < len(data["cars"]):
                del data["cars"][index_to_delete]
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()
                print("Автомобіль успішно видалено.")
            else:
                print("Некоректний номер.")
    except (FileNotFoundError, json.JSONDecodeError, ValueError, IndexError, KeyError):
        print("Помилка при видаленні автомобіля.")


def search_cars(filename="cars.json"):
    """Шукає автомобілі за заданим полем."""
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            search_field = input("Введіть поле для пошуку (model, price, age): ").lower()
            search_value = input("Введіть значення для пошуку: ")

            results = []
            for car in data["cars"]:
                if search_field in car and str(car[search_field]).lower().startswith(search_value.lower()):
                    results.append(car)

            if results:
                print("Результати пошуку:")
                print(json.dumps(results, indent=4))
            else:
                print("Автомобілі не знайдено.")

    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        print("Помилка під час пошуку.")


def calculate_average_price(filename="cars.json", output_filename="result.json"):
    """Розраховує середню вартість автомобілів старших за 6 років."""
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            old_cars = [car for car in data["cars"] if car["age"] > 6]
            if old_cars:
                average_price = sum(car["price"] for car in old_cars) / len(old_cars)
                result = {"average_price_of_old_cars": average_price}
                with open(output_filename, "w") as outfile:
                    json.dump(result, outfile, indent=4)
                print(f"Середня ціна автомобілів старших за 6 років: {average_price}")
                print(f"Результат записано до файлу {output_filename}")
            else:
                print("Не знайдено автомобілів старших за 6 років.")
    except (FileNotFoundError, json.JSONDecodeError, ZeroDivisionError, KeyError):
        print("Помилка під час розрахунку середньої ціни.")

def main():
    create_car_data() #створюємо файл з даними якщо його немає
    while True:
        print("\nМеню:")
        print("1. Вивести дані з JSON файлу")
        print("2. Додати новий запис")
        print("3. Видалити запис")
        print("4. Пошук автомобілів")
        print("5. Розрахувати середню ціну автомобілів старших за 6 років")
        print("6. Вихід")

        choice = input("Введіть ваш вибір: ")

        if choice == "1":
            display_json()
        elif choice == "2":
            add_car()
        elif choice == "3":
            delete_car()
        elif choice == "4":
            search_cars()
        elif choice == "5":
            calculate_average_price()
        elif choice == "6":
            break
        else:
            print("Некоректний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()