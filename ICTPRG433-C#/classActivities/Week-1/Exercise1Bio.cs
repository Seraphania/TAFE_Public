using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace Week_1
{
    class Exercise1Bio
        {
            string firstName = "Seraphania";
            string lastName = "Lastname";
            int age = 40;
            bool international = false;
            int petCount = 2;
            string petType = "Cats";

            public void Print()
            {   
                Exercise1Bio bio = new Exercise1Bio();
                Console.WriteLine("First Name: " + firstName);
                Console.WriteLine("Last Name: " + lastName);
                Console.WriteLine("Age: " + age);
                Console.WriteLine("International Student? " + international);
                Console.WriteLine("I have " + petCount + " " + petType);


            }    
        }
}
