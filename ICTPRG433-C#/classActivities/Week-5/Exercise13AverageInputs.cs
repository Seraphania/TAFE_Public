using TAFE_C__classActivities;

namespace Week_5
{
    internal class Exercise13AverageInputs : IExercise
    {
        public void Run()
        {
            int[] inputs = new int[5];
            int[] GetInputs()
            {
                for (int i = 0; i < 5; i++)
                {
                    Console.Write($"Please enter input {i+1}: ");
                    int n = Convert.ToInt32(Console.ReadLine());
                    inputs[i] = n;
                }
                return inputs;
            }

            int AverageArray(int[] inputs)
            {
                int sum = 0;
                for (int i=0; i<inputs.Length; i++)
                    {
                    sum = sum + inputs[i];
                    }
                return sum / inputs.Length;
            }
            GetInputs();
            Console.WriteLine($"The average is: {AverageArray(inputs)}");
        }
    }
}
