using TAFE_C__classActivities;

namespace Week_5
{
    [Exercise(Title = "5.2", Description = "Print 2 arrays for student grades")]
    internal class Exercise12Print2Arrays : IExercise
    {
        public void Run()
        {
            int[] grades = { 11, 25, 60, 89, 65, 95, 56, 78, 30, 50 };
            string[] students = { "Bob", "Mike", "Sera", "Mark", "Shirley", "Catherine", "Jennifer", "Ian", "Kate", "Kim" };

            void PrintArrays(string[] students, int[] grades)
            {
                for (int i=0; i<students.Length; i++)
                    {
                    Console.WriteLine($"{students[i]}'s grade is: {grades[i]}");
                    }
            }
            PrintArrays(students, grades);
        }
    }
}
