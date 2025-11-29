import asyncio
import time
# Định nghĩa nhiệm vụ thứ i
async def fetch_data():
    print(f"Hi")
    await asyncio.sleep(3)
    print(f"Bye")

async def main():
    Time_start = time.perf_counter() # Thời gian bắt đầu thực thi

    tasks = [fetch_data() for _ in range(2)]
    # Thực hiện nhiệm theo kiểu concurrency
    await asyncio.gather(*tasks)
    Time_end = time.perf_counter() # Thời gian kết thúc

    print(f"Total time: {Time_end - Time_start} s")

asyncio.run(main())