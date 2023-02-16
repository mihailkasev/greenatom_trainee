def compare_versions(a_version:str, b_version: str) -> int:
    """ Сравнивает версии и возвращает соответствующее значение. """
    a = a_version.split('.') # разбиваем на части точки для сравнения
    b = b_version.split('.')
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1

def main():
    """Выводит результат сравнения версий. """
    # Получает данные от пользователя и разбивает значение на две части: до и после точки
    a_version = input()
    b_version = input()
    result = compare_versions(a_version, b_version)
    print(result)


if __name__ == "__main__":
    main()
