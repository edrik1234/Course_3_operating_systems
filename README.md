🌐 JSON Downloader Project

A Python project that downloads multiple JSON files from internet links concurrently using multithreading and multiprocessing, while avoiding race conditions. 🐍💻

🚀 Features

Download JSON files from multiple URLs via API 🌐

Count the total number of characters across all downloaded files 📊

Multithreading with dedicated counters to avoid race conditions 🧵

Multiprocessing with a Queue to safely aggregate results ⚙️

Includes small delays to simulate realistic workloads ⏱️

🛠️ Technologies

Python 3 🐍

threading

multiprocessing

requests

json

⚡ Results

Prints number of characters downloaded per URL ✅

Prints total characters across all files 📊

Compares execution time between threads and processes ⏱️
