package bank_account;

import java.util.Random;

/**
 * Created by daniel on 12/5/17.
 */
public class Employee extends Thread {
	private Bank bank;
	public String name;

	public Employee(String name, Bank bank) {
		super(name);
		this.bank = bank;
		this.name = name;
		start();
		while (this.isAlive());
	}

	public void run() {
		for(int i = 0;i < 100; i ++) {
			int acountnr = 1;
			float amount = 1;
			bank.booking(name, acountnr,amount);
		}
	}
}
