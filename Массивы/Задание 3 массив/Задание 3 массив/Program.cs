using System;

class Program
{
    static void Main()
    {
        int[] numbers = { 5, 10, 15, 20, 25 };

        int sum = 0;
        foreach (var num in numbers)
        {
            sum += num;
        }

        double average = (double)sum / numbers.Length;

        Console.WriteLine("Сумма элементов массива: " + sum);
        Console.WriteLine("Среднее арифметическое значение элементов массива: " + average);
    }
}