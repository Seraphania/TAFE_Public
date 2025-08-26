using System;
using System.Drawing;
using TAFE_C__classActivities;

namespace Week_3
{
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
