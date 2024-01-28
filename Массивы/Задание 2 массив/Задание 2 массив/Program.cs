using System;

class Program
{
    static void Main()
    {
        string[] array = { "apple", "banana", "orange", "pear" };

        Console.Write("Введите новую строку: ");
        string userInput = Console.ReadLine();

        bool isStringFound = false;
        foreach (var str in array)
        {
            if (str == userInput)
            {
                isStringFound = true;
                break;
            }
        }

        if (isStringFound)
        {
            Console.WriteLine("Строка найдена!");
        }
        else
        {
            Console.WriteLine("Строка не найдена!");
        }
    }
}