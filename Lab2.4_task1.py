class Vehicle:
    """
    Базовый класс для транспортных средств.

    Атрибуты:
    - brand (str): Производитель транспортного средства.
    - model (str): Модель транспортного средства.
    - year (int): Год выпуска.
    - mileage (float): Пробег (в километрах).
    """

    def __init__(self, brand: str, model: str, year: int, mileage: float) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self._mileage = mileage  # Инкапсуляция, чтобы избежать неконтролируемого изменения пробега

    def __str__(self) -> str:
        return f"{self.brand} {self.model} ({self.year}) - {self._mileage} km"

    def __repr__(self) -> str:
        return f"Vehicle('{self.brand}', '{self.model}', {self.year}, {self._mileage})"

    def drive(self, distance: float) -> None:
        """
        Метод для увеличения пробега.

        :param distance: Расстояние, на которое увеличивается пробег (в километрах).
        """
        if distance > 0:
            self._mileage += distance
        else:
            print("Ошибка: Расстояние должно быть положительным числом")



class Car(Vehicle):
    """
    Дочерний класс для легковых автомобилей.

    Добавляет атрибут fuel_type (тип топлива).
    """

    def __init__(self, brand: str, model: str, year: int, mileage: float, fuel_type: str) -> None:
        super().__init__(brand, model, year, mileage)
        self.fuel_type = fuel_type

    def __str__(self) -> str:
        return f"{self.brand} {self.model} ({self.year}), {self.fuel_type} - {self._mileage} km"

    def drive(self, distance: float) -> None:
        """
        Переопределенный метод движения.

        Включает дополнительную проверку, что у автомобиля есть топливо.
        """
        if self.fuel_type.lower() in ["gasoline", "diesel"]:
            print(f"{self.brand} {self.model} проехал {distance} км на {self.fuel_type}.")
            super().drive(distance)
        else:
            print(f"Неизвестный тип топлива: {self.fuel_type}. Движение невозможно.")


# Пример использования:
car = Car("Toyota", "Corolla", 2020, 30000, "gasoline")
print(car)  # Toyota Corolla (2020), gasoline - 30000 km

car.drive(150)
print(car)  # Toyota Corolla (2020), gasoline - 30150 km
