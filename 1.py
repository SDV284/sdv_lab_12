import json
cars = [{
    "Model": "Honda",
    "Age": 5,
    "Price": 29000
},{
    "Model": "Hyundai",
    "Age": 7,
    "Price": 38000
},{
    "Model": "Toyota",
    "Age": 3,
    "Price": 36000
},{
    "Model": "BMW",
    "Age": 2,
    "Price": 26000
},{
    "Model": "Mercedes",
    "Age": 6,
    "Price": 45000
},{
    "Model": "Volkswagen",
    "Age": 10,
    "Price": 43000
},{
    "Model": "Chevrolet",
    "Age": 12,
    "Price": 56000
},{
    "Model": "Renault",
    "Age": 4,
    "Price": 39000
},{
    "Model": "Ford",
    "Age": 8,
    "Price": 42000
},{
    "Model": "Opel",
    "Age": 7,
    "Price": 31000
}]

jsonData = json.dumps(cars)
with open("cars.json", "wt") as file:
    file.write(jsonData)

file.close()

while True:    
    print("Select an option:\n 1 - Add data\n 2 - View data\n 3 - Find average price of 6+ years old cars\n 4 - Exit") 
    x = input("Choose an option:\n") 
    x = int(x)
    if x == 1:
        with open("cars.json", "at") as file:
            cars = json.loads(jsonData)
            def add_car(data):
                print("Add: ")
                Model = input("Model:")
                Age = input("Age:")
                Price = input("Price:")
                dictData.append({"Model": Model, "Age": Age, "Price": Price})
                return data
            cars = add_car(cars)
            jsonData = json.dumps(cars)
            file.write(cars)
            file.close
    if x == 2:
        with open("cars.json", "rt") as file:
            cars = json.loads(jsonData)
            print(*cars, sep='\n')
    if x == 3:
        with open("cars.json", "rt") as file:
            cars = json.load(file)
            total_price = 0
            count = 0
            for car in cars:
                if car["Age"] > 6:
                    total_price += car["Price"]
                    count += 1
            if count > 0:
                average_price = total_price / count
                print(f"Середня вартість автомобілів старше 6 років: {average_price:.2f}")
            else:
                print("Немає автомобілів старше 6 років.")
    if x == 4:
        quit(0)