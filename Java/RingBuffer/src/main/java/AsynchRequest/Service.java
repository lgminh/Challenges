package AsynchRequest;

public class Service implements Runnable {

	private boolean[] array;
	private int start;
	private int end;
	private int result;

	public Service(boolean[] array, int start, int end) {
		this.array = array;
		this.start = start;
		this.end = end;
	}

	public int getResult() {
		return result;
	}

	public void run() {
		for(int i = start; i <= end; i++) {
			if(array[i])
				result++;
		}
	}
}

