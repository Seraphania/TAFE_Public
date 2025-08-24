using TAFE_C__classActivities;

namespace Week_1
{
    class Exercise1Bio : IExercise
    {
        public void Run()
        {
            string firstName = "Seraphania";
            string lastName = "Lastname";
            int age = 40;
            bool international = false;
            int petCount = 2;
            string petType = "Cats";

            void Print()
            {
                Exercise1Bio bio = new Exercise1Bio();
                Console.WriteLine("First Name: " + firstName);
                Console.WriteLine("Last Name: " + lastName);
                Console.WriteLine("Age: " + age);
                Console.WriteLine("International Student? " + international);
                Console.WriteLine("I have " + petCount + " " + petType);
            }
            Print();
        }
    }
}
