using System.Collections.Generic;
using System.Reflection;
using Week_1;
using Week_2;
using Week_3;
using Week_4;
using Week_5;

namespace TAFE_C__classActivities
{
    interface IExercise
    {
        void Run();
    }
    public class ExerciseAttribute : Attribute
    {
        public string Title { get; set; }
        public string Description { get; set; }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Type[] classes=typeof(IExercise).Assembly.GetTypes();
            classes = Array.FindAll(classes, _class => _class.IsClass && _class.IsAssignableTo(typeof(IExercise)));

            var thingsToRun = new Dictionary<string, (IExercise Exercise, string DisplayName)>();
            Array.ForEach(classes, _class => {
                ExerciseAttribute attrib = _class.GetCustomAttribute<ExerciseAttribute>();
                string title = _class.Name;
                string description = _class.Name;
                if (attrib != null)
                {
                    title = attrib.Title;
                    description = attrib.Description;
                }
                IExercise toRun = (IExercise)Activator.CreateInstance(_class);
                thingsToRun.Add(title, (toRun, description));
            });
            //{
                //{ "test", (new Test(), "Run the current experiment") },
                //{ "1", (new Exercise1Bio(), "Personal bio exercise") },
                //{ "2.1", (new Exercise2Comparisons(), "Comparison of personal bios")},
                //{ "2.2", (new Exercise3MonthSeason(), "Show season from birth month") },
                //{ "3.1", (new Exercise4TimesTable(), "Print a times table") },
                //{ "3.2", (new Exercise5Debugging(), "Debugging exercise") },
                //{ "4.1", (new Exercise6DeclareFunction(), "Declaring and using functions") },
                //{ "4.2", (new Exercise7Prarmeters(), "Simple addition or multiplication calculator") },
                //{ "4.3", (new Exercise8ASimpleName(), "Return of the welcome message!") },
                //{ "4.4", (new Exercise8BComplexComparison(), "Comparison of personal info but with input") },
                //{ "4.5", (new Exercise9StringCheckForInt(), "Check if there is an int in a string") },
                //{ "4.6", (new Exercise10ParametersReturn(), "The Calculator but better!") },
                //{ "5.1", (new Exercise11PrintArray(), "Function to print arrays") },
                //{ "5.2", (new Exercise12Print2Arrays(), "Print 2 arrays for student grades") },
                //{ "5.3", (new Exercise13AverageInputs(), "Find the average of 5 user inputs") }
            //};


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
