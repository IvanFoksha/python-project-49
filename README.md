# Brain Games

Brain Games — это набор консольных игр для тренировки логического мышления. Проект включает следующие игры:

- **brain-even**: проверка, является ли число чётным.
- **brain-calc**: решение арифметических выражений.
- **brain-gcd**: нахождение наибольшего общего делителя.
- **brain-progression**: поиск пропущенного числа в арифметической прогрессии.
- **brain-prime**: проверка, является ли число простым.

---

### Hexlet tests and linter status:

[![Actions Status](https://github.com/IvanFoksha/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/IvanFoksha/python-project-49/actions)

### Code Climate - Maintainability

<a href="https://codeclimate.com/github/IvanFoksha/python-project-49/maintainability"><img src="https://api.codeclimate.com/v1/badges/d6d20eb15880e1dba659/maintainability" /></a>

---

## Требования

- Python >=3.12
- Установленный пакетный менеджер `uv`.
- GNU Make (для использования команд из `Makefile`).

---

## Установка и запуск

1. Склонируйте репозиторий:

   ```bash
   git clone https://github.com/IvanFoksha/python-project-49.git
   cd python-project-49
   ```

2. Установите зависимости с помощью `Makefile`:

   ```bash
   make install
   ```

3. Запустите игру через `Makefile`:
   `bash
    make brain-games
    `
   Или напрямую с использованием `uv`:
   `bash
    uv run brain-games
    `

4. Для установки пакета глобально выполните:
   `bash
    make package-install
    `
   После этого команды будут доступны без `uv run`:
   `bash
    brain-calc
    `

---

### Asciinema - use brain-even

[![asciicast](https://asciinema.org/a/9izBYnz0uB5aOPZ1lcIr8r4vt.svg)](https://asciinema.org/a/9izBYnz0uB5aOPZ1lcIr8r4vt)

Запись демонстрирует игровой процесс в игре "Четное число" с успешным и неудачным завершением.

### Asciinema - use brain-calc

[![asciicast](https://asciinema.org/a/n78vCv2ftX95A6ep232XzdzHt.svg)](https://asciinema.org/a/n78vCv2ftX95A6ep232XzdzHt)

Запись демонстрирует игровой процесс в игре "Калькулятор" с успешным и неудачным завершением.

### Asciinema - use brain-gcd

[![asciicast](https://asciinema.org/a/xhqycnwwoD40JIvWWdcm95eMJ.svg)](https://asciinema.org/a/xhqycnwwoD40JIvWWdcm95eMJ)

Запись демонстрирует игровой процесс в игре "НОД (Наибольший Общий Делитель)" с успешным и неудачным завершением.

### Asciinema - use brain-progression

[![asciicast](https://asciinema.org/a/1yHZQ1Kb9AzKIhStuuxOymgIa.svg)](https://asciinema.org/a/1yHZQ1Kb9AzKIhStuuxOymgIa)

Запись демонстрирует игровой процесс в игре "Арефметическая прогрессия " с успешным и неудачным завершением.

### Asciinema - use brain-prime

[![asciicast](https://asciinema.org/a/lTqPlY5bxWBHhjs8QqqlwVQXK.svg)](https://asciinema.org/a/lTqPlY5bxWBHhjs8QqqlwVQXK)

Запись демонстрирует игровой процесс в игре "Простое число" с успешным и неудачным завершением.
