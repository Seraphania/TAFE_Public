using System;
using System.Drawing;
using System.Reflection;
using TAFE_C__classActivities;

namespace Week_3
{
    [Exercise(Title="3.2", Description = "Debugging exercise")]
    class Exercise5Debugging : IExercise
    {
        public void Run()
        {
            // Debug the code:
            //myFunction();

            //void myFunction()
            //{
            //    //int myInt = 5
            //    console.WriteLing(myInt);
            //}

            myFunction();
            void myFunction()
            {
                int myInt = 5;
                Console.WriteLine(myInt);
            }
        }
    }
}
