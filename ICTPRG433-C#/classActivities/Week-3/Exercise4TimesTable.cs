using TAFE_C__classActivities;

namespace Week_3
{
    [Exercise(Title = "3.1", Description = "Print a times table")]
    class Exercise4TimesTable : IExercise
    {
        public void Run()
        {
            int multiplicand;

            Console.Write("Please enter a number between 1 and 12 to view its times table: ");
            string userInput = Console.ReadLine()!.Trim();

            void Validate(string userInput)
            {
                bool isNumber = int.TryParse(userInput, out multiplicand);
                while (isNumber == false || 1 > multiplicand || multiplicand > 12)
                {
                    if (isNumber == false)
                    {
                        Console.Write("Input must be a number, please enter a number between 1 and 12: ");
                        userInput = Console.ReadLine()!.Trim();
                        isNumber = int.TryParse(userInput, out multiplicand);
                    }
                    else if (1 >= multiplicand || multiplicand >= 12)
                    {
                        Console.Write("Number must be between 1 and 12, please enter another: ");
                        userInput = Console.ReadLine()!.Trim();
                        isNumber = int.TryParse(userInput, out multiplicand);
                    }
                };
                return;
            }

            Validate(userInput);
            Console.WriteLine($"The {multiplicand} times table is:");
            for (int i=1; i <= 12; ++i)
            {
                Console.WriteLine($"{multiplicand} x {i} = {multiplicand * i}");
            }
        }    
    }
}
