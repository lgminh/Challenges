package bank_account;

/**
 * Created by daniel on 12/5/17.
 */
public class BankAccount {
	private float balance;
	private String name;
	BankAccount(float balance, String name) {
		balance = 0;
		this.name = name;
	}
	public void setBalance(float amount) {
		if (amount >= 0) {
			balance = amount;
		}
		System.out.println("Account " + name + ": " + amount);
	}

	public float getBalance(){
		return balance;
	}

}
