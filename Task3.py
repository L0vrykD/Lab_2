class ElectronicComponent:
    """
    Клас, що представляє окремий електронний компонент.
    Містить інформацію про назву, значення та одиницю виміру компонента.
    """
    def __init__(self, name, value, unit):
        self.name = name
        self.value = value
        self.unit = unit

    def get_name(self):
        """Повертає назву компонента."""
        return self.name

    def get_value(self):
        """Повертає значення компонента."""
        return self.value

    def get_unit(self):
        """Повертає одиницю виміру компонента."""
        return self.unit

    def __str__(self):
        """Повертає рядок, що представляє інформацію про компонент."""
        return f"Компонент: {self.value} {self.unit}"


class ElectronicInventory:
    """
    Клас, що представляє інвентар електронних компонентів.
    Відповідає за додавання, видалення, пошук та підрахунок компонентів.
    """
    def __init__(self):
        self.components = []  # Список для зберігання електронних компонентів

    def add_component(self, name, value, unit):
        """
        Додає новий електронний компонент до інвентаря.
        Якщо компонент з таким ім'ям вже існує, виводить повідомлення.
        """
        component = self.find_component(name)
        if component:
            print(f"Компонент '{name}' вже існує в інвентарі.")
        else:
            new_component = ElectronicComponent(name, value, unit)
            self.components.append(new_component)
            print(f"Компонент '{name}' додано до інвентаря.")

    def get_all_components(self):
        """Повертає список усіх електронних компонентів в інвентарі."""
        return self.components

    def find_component(self, name):
        """
        Шукає електронний компонент в інвентарі за його назвою.
        Повертає знайдений компонент або None, якщо не знайдено.
        """
        for component in self.components:
            if component.get_name() == name:
                return component
        return None

    def remove_component(self, name):
        """
        Видаляє електронний компонент з інвентаря за його назвою.
        Якщо компонент не знайдено, виводить повідомлення.
        """
        component = self.find_component(name)
        if component:
            self.components.remove(component)
            print(f"Компонент '{name}' видалено з інвентаря.")
        else:
            print(f"Компонент '{name}' не знайдено в інвентарі.")

    def get_component_count(self):
        """Повертає кількість електронних компонентів в інвентарі."""
        return len(self.components)

    def __str__(self):
        """Повертає рядок, що представляє інформацію про всі компоненти в інвентарі."""
        component_info = "\n".join(str(component) for component in self.components)
        return f"Інвентар:\n{component_info}"

# Приклад використання
inventory = ElectronicInventory()
inventory.add_component("Резистор", 10, "Ом")
inventory.add_component("Конденсатор", 100, "мкФ")
print(inventory)

found_component = inventory.find_component("Резистор")
if found_component:
    print(f"Знайдено компонент: {found_component}")

inventory.remove_component("Резистор")
print(f"Кількість компонентів в інвентарі: {inventory.get_component_count()}")
