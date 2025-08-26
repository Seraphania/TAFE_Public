using TAFE_C__classActivities;

namespace Week_5
{
    [Exercise(Title = "5.1", Description = "Function to print arrays")]
    internal class Exercise11PrintArray : IExercise
    {
        public void Run()
        {
            int[] intArray = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
            
            void PrintArray(int[] thing)
            {
                for (int i=0; i<thing.Length; i++)
                    {
                        Console.Write(thing[i]);
                    }
            }
            PrintArray(intArray);
        }
    }
}
