using System;
using System.Drawing;
using Week_1;
using Week_2;
using Week_3;

namespace TAFE_C__classActivities
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Which week (or test)? ");
            var input = Console.ReadLine();            
            switch (input)
            {
                case "test":
                    Test.Run(); 
                    break;

                case "1":
                    var bio = new Exercise1Bio();
                    bio.Print();
                    break;

                case "2":
                    Console.WriteLine("activity to run (1-2)? ");
                    var w2 = Console.ReadLine();
                    if (w2 == "1")
                    {                        
                        var compare = new Exercise2Comparisons();
                        compare.Compare();
                        break;
                    }
                    else if (w2 == "2")
                    {
                        var birthSeason = new Exercise3MonthSeason();
                        birthSeason.Season();
                        break;
                    }
                    else
                    {
                        Console.WriteLine("That activity doesn't exist");
                        break;
                    }
                case "3":
                    Console.WriteLine("activity to run (1-2)? ");
                    var w3 = Console.ReadLine();
                    if (w3 == "1")
                    {
                        var times = new Exercise4TimesTable();
                        times.TimesTable();
                        break;
                    }
                    else if (w3 == "2")
                    {   
                        // This was an exercise in debugging
                        myFunction();

                        void myFunction()
                        {
                            int myInt = 5;
                            Console.WriteLine(myInt);
                        }
                        break;
                    }
                    else
                    {
                        Console.WriteLine("That activity doesn't exist");
                        break;
                    }
            }
        }
    }
}
