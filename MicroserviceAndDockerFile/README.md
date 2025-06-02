# Exchange Rate Challenge

## Time Estimated: 1 Day

---

## Description

This task simulates the conversion rate of currencies (USD to EUR) and involves:

- Web scraping/API interaction
- Real-time data sampling
- Averaging and logging
- Code optimization
- Dockerization

You may:

- Use any **programming language** (Python preferred)
- Use your own **development tools and libraries**
- Rely on any external packages that help make the code **cleaner or more efficient**

---

## Task Breakdown

### Step 1: Live Rate Sampling

1.1 Search for a **USD to EUR exchange rate API**  
Suggested: [`https://www.freeforexapi.com/api/live?pairs=USDEUR`](https://www.freeforexapi.com/api/live?pairs=USDEUR)

1.2 Sample the exchange rate **every 5 seconds for 1 minute** and print the result

**Expected Output**:  
- A Python script that:  
  - Calls the API every 5 seconds  
  - Prints the USD → EUR value to the console  
  - Runs for a total of 1 minute

---

### 🔹 Step 2: Averaging and Logging

2.1 Compute the **average exchange rate** over the 60 seconds  
2.2 Write the average to a **log file** (e.g., `usd_eur_avg.log`)  
2.3 Refactor and **optimize your code** (use tools like `black`, `flake8`, or other linters)

**Expected Output**:  
- A clean, refactored Python script with:  
  - Data fetching  
  - Averaging logic  
  - Logging  
  - Proper formatting and code linting

---

### Step 3: Dockerization

3.1 Write a `Dockerfile` to run the script inside a **containerized Ubuntu environment**  
3.2 Run the container and confirm that the log file is generated  
3.3 Fine-tune the `Dockerfile` for **best practices and efficiency**

**Expected Output**:  
- A working `Dockerfile`  
- Docker image that:  
  - Installs all dependencies  
  - Runs the exchange script  
  - Produces the average log file

---

## Deliverables

- `Dockerfile`  
- Docker image (includes Python script and logs)

**DockerHub Repository**:  
🔗 [https://hub.docker.com/repository/docker/sambrn/tech_assignement_2/general](https://hub.docker.com/repository/docker/sambrn/tech_assignement_2/general)

---

## Output

- The Docker container runs the Python application and produces a log file with the **average USD→EUR exchange rate**.  
- You can access this log inside the container or by mounting a volume to your local system.

✅ **Yes, it is possible to view the saved average exchange rate log inside the container.**
