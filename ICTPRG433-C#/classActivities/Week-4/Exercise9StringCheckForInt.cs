using TAFE_C__classActivities;

namespace Week_4
{
    [Exercise(Title = "4.5", Description = "Check if there is an int in a string")]

    internal class Exercise9StringCheckForInt : IExercise
    {
        public void Run()
        {
            string CheckForInt(string s,int i)
                // A loop would allow for more options to check how many times the int is contained.
                // More complicated to write though.
            {
                bool intInString = s.Contains(i.ToString());
                if (intInString)
                {
                    return $"{i} is contained in {s}";
                }
                else
                {
                    return $"{i} is not contained in {s}";
                }
            }

            Console.Write("Please enter some characters: ");
            string str = Console.ReadLine()!;

            Console.Write("Please enter an integer: ");
            int num = int.Parse(Console.ReadLine()!);

            Console.WriteLine(CheckForInt(str, num));
        }
    }
}
