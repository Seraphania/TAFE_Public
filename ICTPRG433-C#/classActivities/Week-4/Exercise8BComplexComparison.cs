using TAFE_C__classActivities;

namespace Week_4
{
    record Student(
                    string firstName,
                    string lastName,
                    int age,
                    bool international,
                    int petCount,
                    string petType
                    );

    [Exercise(Description = "Comparison of personal info but with input",Title = "4.4")]
    class Exercise8BComplexComparison : IExercise
    {
        public void Run() 
        {
            Student s1 = GetInfo("1");
            Student s2 = GetInfo("2");

            AgeCompare();
            NameCompare();

            Student GetInfo(string i)
            {
                string Clean(string s) => s.Trim().ToLower();
                string Input(string prompt)
                {
                    Console.Write(prompt);
                    return Clean(Console.ReadLine()!);
                }

                Console.WriteLine($"Welcome Student {i}, please enter some information\n");
                string firstName = Input("Please enter your first name: ");
                string lastName = Input("Please enter your last name: ");
                int age = Convert.ToInt32(Input("How old are you?: "));
                bool international = (Input("Are you an international student? (yes/no): ") == "yes" ? international = true : international = false);
                int petCount = Convert.ToInt32(Input("What Number of pets do you have: "));
                string petType = Input("What type of pets do you have?: ");
                Console.WriteLine("Press any key to continue... ");
                Console.ReadKey(true);
                Console.Clear();
                return new Student(firstName, lastName, age, international, petCount, petType);
            }


            void AgeCompare()
            {
                var ageDiffernce = s1.age - s2.age;
                if (s1.age > s2.age)
                {
                    Console.WriteLine($"{s1.firstName} is older than {s2.firstName}.");
                    Console.WriteLine($"The age difference is {ageDiffernce} years.");
                }
                else if (s1.age < s2.age)
                {
                    Console.WriteLine($"{s2.firstName} is older than {s1.firstName}.");
                    Console.WriteLine($"The age difference is {Math.Abs(ageDiffernce)} years.");
                }

                else
                {
                    Console.WriteLine($"{s1.firstName} and {s2.firstName} are the same age.");
                }
            }

            void NameCompare()
            {
                int NameLength(string s1, string s2) => (s1 + s2).Length;
                if (NameLength(s1.firstName, s1.lastName) > NameLength(s2.firstName, s2.lastName))
                {
                    Console.WriteLine($"{s1.firstName} has a longer name than {s2.firstName}");
                }
                else if (NameLength(s1.firstName, s1.lastName) < NameLength(s2.firstName, s2.lastName))
                {
                    Console.WriteLine($"{s2.firstName} has a longer name than {s1.firstName}");
                }
                else
                {
                    Console.WriteLine($"{s1.firstName}'s name and {s2.firstName}'s name are the same length");
                }
            }
        }
    }
}


