package MainApp;

import bank_account.Bank;
import bank_account.Employee;
import circular_ring_buffer.Reader;
import circular_ring_buffer.RingBuffer;
import circular_ring_buffer.RingBufferThreadSafe;
import circular_ring_buffer.Writer;

import java.util.Random;

/**
 * Created by daniel on 12/5/17.
 */
public class Main {
	public  static  void  main(String args[]) {
		RingBufferThreadSafe ringBufferThreadSafe = new RingBufferThreadSafe(10);

		Random random = new Random(1234);
		for(int i = 0; i < 7; i++) {
			int randomValue = random.nextInt();
			Writer writer = new Writer(ringBufferThreadSafe);
			writer.writeItem(randomValue);
		}

		for (int i = 0; i < 50; i ++) {
			int randomValue = random.nextInt();
			if (randomValue % 2 == 0) {
				Reader reader = new Reader(ringBufferThreadSafe);
				reader.getItem();
				ringBufferThreadSafe.showItems();
			} else if (randomValue % 3 == 0) {
				Writer writer = new Writer(ringBufferThreadSafe);
				writer.writeItem(randomValue);
				ringBufferThreadSafe.showItems();
			}
		}
	}
}
