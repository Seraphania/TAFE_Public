using System.Collections.Generic;
using Week_1;
using Week_2;
using Week_3;
using Week_4;

namespace TAFE_C__classActivities
{
    interface IExercise
    {
        void Run();
    }

    class Program
    {
        static void Main(string[] args)
        {
            var thingsToRun = new Dictionary<string, (IExercise Exercise, string DisplayName)>
            {
                { "test", (new Test(), "Run the current experiment") },
                { "1", (new Exercise1Bio(), "Personal bio exercise") },
                { "2.1", (new Exercise2Comparisons(), "Comparison of personal bios")},
                { "2.2", (new Exercise3MonthSeason(), "Show season from birth month") },
                { "3.1", (new Exercise4TimesTable(), "Print a times table") },
                { "3.2", (new Exercise5Debugging(), "Debugging exercise") },
                { "4.1", (new Exercise6DeclareFunction(), "Declaring and using functions") },
                { "4.2", (new Exercise7Prarmeters(), "Simple addition or multiplication calculator") },
                { "4.3", (new Exercise8ASimpleName(), "Return of the welcome message!") },
                { "4.4", (new Exercise8BComplexComparison(), "Comparison of personal info but with input") },
                { "4.5", (new Exercise9StringCheckForInt(), "Check if there is an int in a string") },
                { "4.6", (new Exercise10ParametersReturn(), "The Calculator but better!") }
            };

            ShowMenu();
            string userInput = ValidateInput(NormaliseInput(Console.ReadLine()!));
            Console.Clear();
            while (userInput != "exit")
            {
                thingsToRun[userInput].Exercise.Run();
                Console.Write("\n\nPress any key to return to the menu... ");
                Console.ReadKey(true);
                Console.Clear();
                ShowMenu();
                userInput = ValidateInput(NormaliseInput(Console.ReadLine()!));
            }

            string NormaliseInput(string s) => s.Trim().ToLower();

            void ShowMenu()
            {
                Console.WriteLine($"AVAILABLE EXERCISES:\n\nOption\t: Description" );
                foreach (var item in thingsToRun)
                {
                    Console.WriteLine($"{item.Key}\t: {item.Value.DisplayName}");
                }
                Console.Write("Please select an option or 'exit':> ");    
            }

            string ValidateInput(string input)
            {
                while (input != "exit" && !thingsToRun.ContainsKey(input))
                {
                    Console.Clear();
                    Console.WriteLine($"'{input}' is not a valid option, please select another...\n");
                    ShowMenu();
                    input = NormaliseInput(Console.ReadLine()!);
                    Console.Clear();
                }
                return input;
            }
        }
    }
}
