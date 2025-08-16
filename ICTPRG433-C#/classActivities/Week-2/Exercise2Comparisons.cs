namespace Week_2
{
    class Exercise2Comparisons
    {
        struct Students 
        {
            public string firstName;
            public string lastName;
            public int age;
            public bool international;
            public int petCount;
            public string petType;
        };
        public void Compare()
        {
            Students Student1;
            Students Student2;

            Student1.firstName = "Seraphania";
            Student1.lastName = "Lastname";
            Student1.age = 40;
            Student1.international = false;
            Student1.petCount = 2;
            Student1.petType = "Cats";

            Student2.firstName = "J";
            Student2.lastName = "Man";
            Student2.age = 19;
            Student2.international = false;
            Student2.petCount = 1;
            Student2.petType = "Dog";

            // Who is older
            // age difference
            var ageDiffernce = Student1.age - Student2.age;
            if (Student1.age > Student2.age) {
                Console.WriteLine($"{Student1.firstName} is older than {Student2.firstName}.");
                Console.WriteLine($"The age difference is {ageDiffernce} years.");
            }
            else if (Student1.age < Student2.age) {
                Console.WriteLine($"{Student2.firstName} is older than {Student1.firstName}.");
                Console.WriteLine($"The age difference is {Math.Abs(ageDiffernce)} years.");
            }

            else {
                Console.WriteLine($"{Student1.firstName} and {Student2.firstName} are the same age.");
            }

            // who hass longer name
            var s1NameLength = $"{Student1.firstName}+{Student1.lastName}".Length;
            var s2NameLength = $"{Student2.firstName}+{Student2.lastName}".Length;
            if (s1NameLength > s2NameLength)
            {
                Console.WriteLine($"{Student1.firstName} has a longer name than {Student2.firstName}");
            }
            else if (s1NameLength < s2NameLength)
            {
                Console.WriteLine($"{Student2.firstName} has a longer name than {Student1.firstName}");
            }
            else
            {
                    Console.WriteLine($"{Student2.firstName}'s name and {Student1.firstName}'s name are the same length");
            }
        }
    }
}
