from storage import Storage
import storage_pb2

def main():
	s = Storage(100)

	for i in range(1000):
		POW = "o12odn21onkl1n2000000"
		entry = storage_pb2.Entry(
			pow = POW,
			block = 10,
			key = 1,
			value = 2
		)
		s.add(entry)

if __name__ == "__main__":
	main()

