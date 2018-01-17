package circular_ring_buffer;

public class Writer extends Thread {
	private static RingBufferThreadSafe ringBuffer;
	private int item;

	public Writer(RingBufferThreadSafe ringBuffer) {
		this.ringBuffer = ringBuffer;
	}

	public void writeItem(int item) {
		start();
	}

	public void run() {
		this.ringBuffer.addItem(this.item);
	}



}
