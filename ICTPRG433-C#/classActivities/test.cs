namespace TAFE_C__classActivities
{
    [ExerciseAttribute(Title="test", Description = "Run the current experiment")]
    internal class Test : IExercise
    {
        public void Run()
        { // Put things here for testing!



            ////Try/Catch
            //Console.Write("Provide a number: ");
            //string input = Console.ReadLine();
            //try
            //{
            //    int num = Convert.ToInt32(input);
            //}
            //catch
            //{
            //    Console.WriteLine("Houston, we have a problem.");
            //}

            //// foreach
            //int[] numbers = new int[3] { 0, 1, 2 };// Array, different from a list, can't be resized (will be covered next week).
            //foreach (int index in numbers)
            //{
            //    Console.WriteLine(index);
            //}

            //// While Loop
            //int i = 0;
            //while(i < 3)
            //{
            //    Console.WriteLine(i);
            //    ++i;
            //}

            //// float vs decimal
            //decimal accurate = 1.234567891234567M;
            //float notAccurate = 1.234567891234567f;
            //Console.WriteLine(accurate);
            //Console.WriteLine(notAccurate);

            //// increment prefix and suffix
            //int x = 0;
            //Console.WriteLine(++x); // returns 1
            //Console.WriteLine(x++); // returns 1 - sends 'x' to Console.WriteLine, THEN increments
            //Console.WriteLine(x); // will return 2
            //                      // Same thing with decrement.
            //x = 0;
            //Console.WriteLine(x++ + x++); // returns 1
            //Console.WriteLine(x); // will return 2
            //                      // Same thing with decrement.

            //// comparisons
            //Console.WriteLine("aaa".CompareTo("bbb"));
            //string string1 = "dog cat";
            //Console.WriteLine(string1 == "dog"); /// will return False

            //// varaible assignment
            //int number1 = 42;
            //double number2 = 13.37;
            //string message = $"The answer is {number1}, this is {number2}!";

            //// printing
            //Console.WriteLine(message);
        }

    }
}
