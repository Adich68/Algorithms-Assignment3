import time
import subprocess
import matplotlib.pyplot as plt

sizes = [25, 50, 100, 200, 300, 400, 500, 600, 700, 800]
times = []

for i, size in enumerate(sizes):
    filename = f"data/test{i+1}.in"
    start = time.time()
    subprocess.run(['python', 'src/hvlcs.py', filename], capture_output=True)
    end = time.time()
    elapsed = end - start
    times.append(elapsed)
    print(f"test{i+1}.in (size={size}): {elapsed:.4f} seconds")

plt.plot(sizes, times, marker='o')
plt.title('HVLCS Runtime vs Input Size')
plt.xlabel('String Length')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.savefig('data/runtime_graph.png')
print("Graph saved to data/runtime_graph.png")