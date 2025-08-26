using TAFE_C__classActivities;

namespace Week_4
{
    [Exercise(Title = "4.1", Description = "Declaring and using functions")]
    internal class Exercise6DeclareFunction : IExercise
    {
        public void Run()
        {
            void WelcomeMessage()
            {
                Console.WriteLine("****************************");
                Console.WriteLine(" Welcome to My Application! ");
                Console.WriteLine("****************************");
            }
            WelcomeMessage();
        }
    }
}
