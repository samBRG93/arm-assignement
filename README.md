# Performance Analysis of Machine Learning (ML) Loads

## Duration: 1 Day

---

## Exercise

A team developing ML devices has requested an analysis of the performance data produced by their testing infrastructure.

You have been provided with two data files:  
- `TestInfo.csv`  
- `TestResults.pickle`

Your task is to analyze the performance data and provide:

1. An **executive summary** of your findings  
2. Clear **visualizations** of the findings with annotations  
3. **Suggestions and follow-up actions** based on your findings to discuss with the development team

---

## Deliverables

- **Executive summary:**  
 A clear, one-page overview understandable by stakeholders unfamiliar with the data or technical details.

- **Visualizations:**  
 Graphs or charts that illustrate your analysis, annotated for clarity.

- **Follow-up actions:**  
 Recommended next steps or investigations based on your findings.

---

## Guidance and Hints

- The two files are related by the field `TestId`.  
- `TestResults.pickle` was created using **pandas** and **Python 3.7**.  
- This is **not a quantitative/statistical analysis** task — focus on understanding and communicating the data.  
- Include **reasons or justifications** in your summary explaining why certain behaviours may have occurred.  
- `TestId` is solely for mapping tests to results.  
- `Build` refers to different software versions.  
- `Device` refers to different hardware versions.

---

Good luck with your analysis!

## Deliverables  
Please take a look at this iPython file!  
[Performance analysis of Machine Learning (ML) loads.ipynb](DataAnalysis%2FPerformance%20analysis%20of%20Machine%20Learning%20%28ML%29%20loads.ipynb)

---

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

**Expected Output:**  
- A Python script that:  
  - Calls the API every 5 seconds  
  - Prints the USD → EUR value to the console  
  - Runs for a total of 1 minute

---

### Step 2: Averaging and Logging

2.1 Compute the **average exchange rate** over the 60 seconds  
2.2 Write the average to a **log file** (e.g., `usd_eur_avg.log`)  
2.3 Refactor and **optimize your code** (use tools like `black`, `flake8`, or other linters)

**Expected Output:**  
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

**Expected Output:**  
- A working `Dockerfile`  
- Docker image that:  
  - Installs all dependencies  
  - Runs the exchange script  
  - Produces the average log file

---

## Deliverables

- `Dockerfile`  
- Docker image (includes Python script and logs)

**DockerHub Repository:**  
🔗 [https://hub.docker.com/repository/docker/sambrn/tech_assignement_2/general](https://hub.docker.com/repository/docker/sambrn/tech_assignement_2/general)

---

## Output

- The Docker container runs the Python application and produces a log file with the **average USD→EUR exchange rate**.  
- You can access this log inside the container or by mounting a volume to your local system.

**Yes, it is possible to view the saved average exchange rate log inside the container.**
