#Мазалевская Вариант 4
print(f"start code...") 
import json 
import os 

DATA_FILE = "CarInfo.json" 

operations_count = 0 


# Загрузка данных из файла
cars=[]
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'r', encoding='utf-8') as file:
        cars = json.load(file)


while True:
    print("\n" + "=" * 40)
    print("МЕНЮ УПРАВЛЕНИЯ БАЗОЙ ДАННЫХ АВТОМОБИЛЕЙ")
    print("=" * 40)
    print("1. Вывести все записи")
    print("2. Вывести запись по полю (id)")
    print("3. Добавить запись")
    print("4. Удалить запись по полю (id)")
    print("5. Выйти из программы")
    print("-" * 40)
    
    try:
        choice = input("Выберите пункт меню (1-5): ").strip()
        
        if choice == "1":
            print("\n" + "=" * 60)
            print("ВСЕ ЗАПИСИ ОБ АВТОМОБИЛЯХ")
            print("=" * 60)
            
            if not cars:
                print("База данных пуста.")
            else:
                for i, car in enumerate(cars, 1):
                    fuel_type = "бензин" if car["is_petrol"] else "не бензин"
                    print(f"Запись #{i}")
                    print(f"  ID: {car['id']}")
                    print(f"  Модель: {car['name']}")
                    print(f"  Производитель: {car['manufacturer']}")
                    print(f"  Тип топлива: {fuel_type}")
                    print(f"  Объем бака: {car['tank_volume']} л")
                    print("-" * 30)
            
            operations_count += 1
        
        elif choice == "2":
            try:
                search_id = int(input("Введите ID автомобиля для поиска: "))
                found = False
                
                for i, car in enumerate(cars):
                    if car["id"] == search_id:
                        print("\n" + "=" * 50)
                        print("НАЙДЕННАЯ ЗАПИСЬ")
                        print("=" * 50)
                        print(f"Позиция в базе данных: {i + 1}")
                        fuel_type = "бензин" if car["is_petrol"] else "не бензин"
                        print(f"ID: {car['id']}")
                        print(f"Модель: {car['name']}")
                        print(f"Производитель: {car['manufacturer']}")
                        print(f"Тип топлива: {fuel_type}")
                        print(f"Объем бака: {car['tank_volume']} л")
                        found = True
                        break
                
                if not found:
                    print(f"\nЗапись с ID {search_id} не найдена!")
                else:
                    operations_count += 1
                    
            except ValueError:
                print("Ошибка: ID должен быть числом!")
        
        elif choice == "3":
            print("\n" + "=" * 40)
            print("ДОБАВЛЕНИЕ НОВОЙ ЗАПИСИ")
            print("=" * 40)
            
            try:
                new_id = int(input("Введите ID новой записи: "))
                id_exists = False
                for car in cars:
                    if car["id"] == new_id:
                        id_exists = True
                        break
                
                if id_exists:
                    print(f"Ошибка: Запись с ID {new_id} уже существует!")
                else:
                    name = input("Введите название модели: ").strip()
                    manufacturer = input("Введите производителя: ").strip()
                    
                    fuel_input = input("Заправляется бензином? (да/нет): ").strip().lower()
                    is_petrol = fuel_input in ["да", "yes", "y", "д"]
                    
                    tank_volume = int(input("Введите объем бака (в литрах): "))
                    
                    new_car = {
                        "id": new_id,
                        "name": name,
                        "manufacturer": manufacturer,
                        "is_petrol": is_petrol,
                        "tank_volume": tank_volume
                    }
                    
                    cars.append(new_car)
                  
                    with open(DATA_FILE, 'w', encoding='utf-8') as file:
                        json.dump(cars, file, indent=2, ensure_ascii=False)
                    
                    print(f"Запись с ID {new_id} успешно добавлена!")
                    operations_count += 1
                    
            except ValueError as e:
                print(f"Ошибка ввода данных: {e}")
        
        elif choice == "4":
           
            try:
                delete_id = int(input("Введите ID записи для удаления: "))
                found_index = -1 
               
                for i, car in enumerate(cars):
                    if car["id"] == delete_id:
                        found_index = i
                        break
                
                if found_index == -1:
                    print(f"\nЗапись с ID {delete_id} не найдена!")
                else: 
                    car_to_delete = cars[found_index]
                    print("\n" + "=" * 40)
                    print("УДАЛЕНИЕ ЗАПИСИ")
                    print("=" * 40)
                    fuel_type = "бензин" if car_to_delete["is_petrol"] else "не бензин"
                    print(f"ID: {car_to_delete['id']}")
                    print(f"Модель: {car_to_delete['name']}")
                    print(f"Производитель: {car_to_delete['manufacturer']}")
                    print(f"Тип топлива: {fuel_type}")
                    print(f"Объем бака: {car_to_delete['tank_volume']} л")
                    
                    confirm = input("\nВы уверены, что хотите удалить эту запись? (да/нет): ").strip().lower()
                    
                    if confirm in ["да", "yes", "y", "д"]:
                       
                        del cars[found_index]
                        
                        with open(DATA_FILE, 'w', encoding='utf-8') as file:
                            json.dump(cars, file, indent=2, ensure_ascii=False)
                        
                        print(f"Запись с ID {delete_id} успешно удалена!")
                        operations_count += 1
                    else:
                        print("Удаление отменено.")           
            except ValueError:
                print("Ошибка: ID должен быть числом!")
        elif choice == "5":
            print("\n" + "=" * 40)
            print("ЗАВЕРШЕНИЕ РАБОТЫ ПРОГРАММЫ")
            print("=" * 40)
            print(f"Количество выполненных операций: {operations_count}")
            print("До свидания!")
            break
        
        else:
            print("Неверный выбор. Пожалуйста, выберите пункт от 1 до 5.")
    except KeyboardInterrupt:
        print("\n\nПрограмма прервана пользователем.")
        break
    except Exception as e:
        print(f"Произошла ошибка: {e}")
print(f"end code...")