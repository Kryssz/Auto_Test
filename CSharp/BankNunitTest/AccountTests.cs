namespace BankNunitTestProject1
{
    public class AccountTests
    {
        private Bank.BankAccount account;


        [SetUp]
        public void Setup()
        {
            // Arrange
            account = new Bank.BankAccount(5000);
        }

        [TearDown] public void Teardown() { }

        // Happy path tests

        [Test]
        public void Adding_Founds_Balance_Update()
        {         
            // Act
            account.Add(500);

            // Assert
            Assert.That(account.Balance, Is.EqualTo(5500));
        }

        [Test]
        public void Withdrawing_Founds_Balance_Update()
        {
            // Act
            account.Withdraw(500);

            // Assert
            Assert.That(account.Balance, Is.EqualTo(4500));
        }

        [Test]
        public void Transfering_Founds_Update_Accounts()
        {
            // Arrange
            var account2 = new Bank.BankAccount(0);

            // Act
            account.TransferFundsTo(account2, 2500);

            // Assert
            Assert.That(account.Balance, Is.EqualTo(2500));
            Assert.That(account2.Balance, Is.EqualTo(2500));
        }

        // Unhappy path tests

        [Test]
        public void Adding_Negative_Founds_Throws()
        {
            // Act + Assert
            Assert.Throws<ArgumentOutOfRangeException>(() => account.Add(-500));
        }

        [Test]
        public void Withdrawing_More_Than_Balance_Throws()
        {
            // Act + Assert
            Assert.Throws<ArgumentOutOfRangeException>(() => account.Withdraw(10000));
        }

        [Test]
        public void Withdrawing_Negative_Founds_Throws()
        {
            // Act + Assert
            Assert.Throws<ArgumentOutOfRangeException>(() => account.Withdraw(-500));
        }

        [Test]
        public void Transfer_To_Non_Existing_Account_Throws()
        {
            // Act + Assert
            Assert.Throws<ArgumentNullException>(() => account.TransferFundsTo(null, 2000));
        }
    }
}