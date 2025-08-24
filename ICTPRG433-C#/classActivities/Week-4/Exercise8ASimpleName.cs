using TAFE_C__classActivities;

namespace Week_4
{
    internal class Exercise8ASimpleName : IExercise
    {
        public void Run()
        {
            void WelcomeMessage(string name)
            {
                Console.WriteLine(new string('*', name.Length + 32));
                Console.WriteLine($" Hi {name}! Welcome to My Application! ");
                Console.WriteLine(new string('*', name.Length + 32));
            }
            Console.WriteLine("Please enter your name: ");
            string name = Console.ReadLine()!;
            WelcomeMessage((string.IsNullOrEmpty(name) ? "Mysterious Stranger" : name));
        }
    }
}
