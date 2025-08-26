﻿using TAFE_C__classActivities;

namespace Week_4
{
    [Exercise(Title = "4.2", Description = "Simple addition or multiplication calculator")]
    internal class Exercise7Prarmeters : IExercise
    {
        public void Run()
        {
            void Multiply(decimal num1, decimal num2)
            {
                decimal multiple = num1 * num2;
                Console.WriteLine($"{num1} x {num2} = {multiple}");
            }

            void Add(decimal num1, decimal num2)
            {
                decimal sum = num1 * num2;
                Console.WriteLine($"{num1} + {num2} = {sum}");
            }

            decimal Numberfy(string s) => decimal.Parse(s);

            Console.WriteLine("Please enter a number: ");
            decimal n1 = Numberfy(Console.ReadLine()!);

            Console.WriteLine("Please enter another number: ");
            decimal n2 = Numberfy(Console.ReadLine()!);

            Console.WriteLine($"You chose {n1} and {n2}\n" +
                $"Would you like to add the numbers or multply them?" +
                $" enter '+' or '*'> ");
            var operation = Console.ReadLine();
            if (operation == "+")
            {
                Add(n1, n2);
            }
            else if (operation == "*")
            {
                Multiply(n1, n2);
            }
            else
            {
                Console.WriteLine("Nevermind!");
            }
        }
    }
}
