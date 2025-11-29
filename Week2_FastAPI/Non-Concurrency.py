import time
def fetch_data():
    print('HI')
    time.sleep(3)
    print("Bye")


def main():
    time_start = time.perf_counter() # Lấy thời gian bắt đầu

    for _ in range(2):
        fetch_data()
    time_end = time.perf_counter() # Lấy thời gian kết thúc

    print(f"Tổng thời gian thực hiện: {time_end-time_start:.2f} s")

if __name__ == "__main__":
    main()