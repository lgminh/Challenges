package bank_account;

import org.apache.commons.lang3.RandomStringUtils;

/**
 * Created by daniel on 12/5/17.
 */
public class Bank {
	private BankAccount[] accounts;
	String bankName;

	public Bank(String bankName, int n) {
		this.bankName = bankName;
		accounts = new BankAccount[n];
		for (int i = 0; i < n; i++) {
			String name = RandomStringUtils.randomAlphabetic(10);
			accounts[i] = new BankAccount(0, name);
		}
	}

	public void booking(String employee, int accountnr, float amount) {
		//synchronized (accounts[accountnr]) {
		float oldBalance = accounts[accountnr].getBalance();
		float newBalance = oldBalance + amount;
		accounts[accountnr].setBalance(newBalance);
		//}
	}

}
