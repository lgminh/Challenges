package circular_ring_buffer;

/**
 * Created by daniel on 12/3/17.
 */
public class RingBuffer {
	private int writePos;
	private int readPos;
	private int item[];
	private boolean flipped;
	private int capability;

	public RingBuffer(int N){
		this.item = new int[N];
		this.writePos = 0;
		this.readPos = 0;
		this.flipped = false;
		this.capability = N;
	}

	public void addItem(int newItem) {
		if (flipped) {
			int availableSlot = readPos - writePos;
			if (availableSlot > 0 ) {
				this.item[writePos++] = newItem;
			}
		} else {
			int availableSlot = capability - writePos + readPos;
			if (availableSlot > 0 ) {
				if (writePos < capability) {
					item[writePos++] = newItem;
				} else {
					writePos = 0;
					this.flipped = true;
					if (writePos < readPos){
						this.item[writePos++] = newItem;
					}
				}
			}
		}
	}

	public int getItem() {
		if (flipped) {
			if (readPos < capability) {
				int value = item[readPos];
				item[readPos++] = -1;
				return value;
			} else {
				flipped = false;
				readPos = 0;
				if (readPos < writePos) {
					int value = item[readPos];
					item[readPos++] = -1;
					return value;
				} else {
					return -1;
				}
			}
		} else {
			if (readPos < writePos) {
				int value = item[readPos];
				item[readPos++] = -1;
				return value;
			} else {
				return -1;
			}
		}
	}

	public void showItems() {
		System.out.println("================");
		for (int i = 0; i < item.length ; i ++) {
			System.out.println("Item " + i + ": " +  item[i]);
		}
	}
}
