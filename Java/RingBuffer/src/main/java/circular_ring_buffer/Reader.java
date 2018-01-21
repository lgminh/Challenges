package circular_ring_buffer;

public class Reader extends Thread {
	private final RingBufferThreadSafe ringBuffer;
	private int Item;
	public Reader(RingBufferThreadSafe ringBuffer) {
		this.ringBuffer = ringBuffer;
		start();
	}

	public void run() {
		this.Item = ringBuffer.getItem();
	}

	public int getItem(){
		return  this.Item;
	}

}
