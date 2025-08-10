using Week_1;
using Week_2;

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
                    var activity = Console.ReadLine();
                    if (activity == "1")
                    {                        
                        var compare = new Exercise2Comparisons();
                        compare.Compare();
                        break;
                    }
                    else if (activity == "2")
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
            }
        }
    }
}
