package circular_ring_buffer;

public class Writer extends Thread {
	private final RingBufferThreadSafe ringBuffer;
	private int item;

	public Writer(RingBufferThreadSafe ringBuffer,int Item) {
		this.ringBuffer = ringBuffer;
		this.item = Item;
		start();
	}

	public void run() {
		this.ringBuffer.addItem(this.item);
	}



}
