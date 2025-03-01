# Основная программа (A) - определяет, какую задачу решать
import task_solver

def main():
    while True:
        print("Выберите номер задачи (1-3) или 0 для выхода:")
        choice = input("Введите номер задачи: ")
        
        if choice == "0":
            print("Выход из программы.")
            break
        
        if choice in ["1", "2", "3"]:
            task_solver.solve_task(int(choice))
        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()