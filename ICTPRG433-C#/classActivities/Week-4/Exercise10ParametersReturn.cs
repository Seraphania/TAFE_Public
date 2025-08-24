using TAFE_C__classActivities;

namespace Week_4
{
    internal class Exercise10ParametersReturn : IExercise
    {
        public void Run()
        {
            string Multiply(decimal num1, decimal num2)
            {
                decimal multiple = num1 * num2;
                return $"{num1} x {num2} = {multiple}";
            }

            string Add(decimal num1, decimal num2)
            {
                decimal sum = num1 * num2;
                return $"{num1} + {num2} = {sum}";
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
                Console.WriteLine(Add(n1, n2));
            }
            else if (operation == "*")
            {
                Console.WriteLine(Multiply(n1, n2));
            }
            else
            {
                Console.WriteLine("Nevermind!");
            }
        }
    }
}
