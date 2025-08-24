using TAFE_C__classActivities;

namespace Week_2
{
    class Exercise3MonthSeason : IExercise
    {
        public void Run()
        {
            Console.WriteLine("Please enter your the month you were born in: ");
            var month = Console.ReadLine()?.Trim().ToLower();
            string season = month switch
            {
                ("12" or "dec" or "december" or "1" or "jan" or "january" or "2" or "feb" or "february") => "Summer",
                ("3" or "mar" or "march" or "4" or "apr" or "april" or "5" or "may") => "Autumn",
                ("6" or "jun" or "june" or "7" or "jul" or "july" or "8" or "aug" or "august") => "Winter",
                ("9" or "sep" or "september" or "10" or "oct" or "october" or "11" or "nov" or "november") => "Spring",
                (_) => "Unknown"
            };
            if (season == "Unknown")
                Console.WriteLine($"{month} is not a valid month");
            else
                Console.WriteLine($"You were born in {season}");
        }
    }
}
