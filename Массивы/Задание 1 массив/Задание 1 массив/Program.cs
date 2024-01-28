using System;

class Program
{
    static void Main()
    {
        int[] array = { 2, 5, 8, 11, 6, 3, 9, 4, 7 };

        Console.WriteLine("Нечетные числа:");
        foreach (var num in array)
        {
            if (num % 2 != 0)
            {
                Console.WriteLine(num);
            }
        }
    }
}