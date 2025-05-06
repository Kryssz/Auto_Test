namespace Grades.NUnitTest
{
    public class GradeCalculatorTests
    {
        private StudentGrades.GradeCalculator _gradeCalculator { get; set; } = null!;

        [SetUp]
        public void Setup()
        {
            _gradeCalculator = new StudentGrades.GradeCalculator();
        }

        // Happy Path
        [TestCase(90)]
        [TestCase(95)]
        [TestCase(97)]
        [TestCase(99)]
        public void GetGradeByPercentage_Equal_Test(int percentage)
        {
            // Assign
            //var percentage = 90;

            // Act
            var grade = _gradeCalculator.GetGradeByPercentage(percentage);

            // Assert
            Assert.That(grade, Is.EqualTo("A"));
            Assert.AreEqual("A", grade);
            Assert.IsTrue(grade == "A");
            Assert.IsFalse(grade == "B");
        }

        [TestCase(1)]
        [TestCase(60)]
        [TestCase(70)]
        [TestCase(79)]
        public void GetGradeByPercentage_NotEqual_Test(int percentage)
        {
            // Assign
            //var percentage = 90;

            // Act
            var grade = _gradeCalculator.GetGradeByPercentage(percentage);

            // Assert
            Assert.That(grade, Is.Not.EqualTo("A"));
            Assert.AreNotEqual("A", grade);
            Assert.IsTrue(grade != "A");
            Assert.IsFalse(grade == "B");
        }

        [Test]
        public void GetGradeByPercentage_Negative_Percentage_Test()
        {
            // Assign
            var percentage = -1;

            // Act
            var grade = _gradeCalculator.GetGradeByPercentage(percentage);

            // Assert
            Assert.That(grade, Is.EqualTo("Invalid"));
            Assert.AreEqual("Invalid", grade);
            Assert.IsTrue(grade != "A");
            Assert.IsFalse(grade == "B");
        }

        [Test]
        public void GetGradeByPercentage_Over_100_Percentage_Test()
        {
            // Assign
            var percentage = 101;
            // Act
            var grade = _gradeCalculator.GetGradeByPercentage(percentage);
            // Assert
            Assert.That(grade, Is.EqualTo("Invalid"));
        }
    }
}