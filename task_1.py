import queue
import random
import time
import threading

request_queue = queue.Queue()

def generate_request():
    request_id = random.randint(1000, 9999)
    request_data = f"Request-{request_id}"
    print(f"New request generated: {request_data}")
    request_queue.put(request_data)

def process_request():
    if not request_queue.empty():
        request_data = request_queue.get()
        print(f"Processing {request_data}")
        time.sleep(1)                  
        print(f"{request_data} processed")
    else:
        print("No requests to process, queue is empty.")

def main():
    while True:
        generate_request()                    # Генеруємо нові заявки
        process_request()                     # Обробляємо наявні заявки
        time.sleep(2)                         # Затримка між циклами

if __name__ == "__main__":
    # Програма працює, доки користувач не натисне Ctrl+C для завершення
    try:
        main()
    except KeyboardInterrupt:
        print("Program terminated by user.")
