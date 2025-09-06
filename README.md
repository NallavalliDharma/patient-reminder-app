# Patient Reminder Web Application

## 📌 Overview  
The **Patient Reminder Web Application** is a cloud-based solution built on AWS to send automated **Email** and **SMS** reminders to patients. It uses **serverless architecture** with AWS services like **S3, API Gateway, Lambda, Step Functions, SES, and SNS** to ensure scalability, reliability, and low cost.

---

## 🚀 Project Workflow  

### 1. Frontend (Static Website Hosting)  
![Step1](images/Screenshot%2025-09-06%204114.png)
- Uploaded `index.html` file to **Amazon S3 bucket**.  
![Step2](images/Screenshot%2025-09-06%204154.png)
- Enabled **bucket versioning** for better management.  
![Step3](images/Screenshot%2025-09-06%204325.png)
- Enabled **static website hosting** and hosted the frontend.  
![Step4](images/Screenshot%2025-09-06%204608.png)
- Configured **Object Ownership** → *ACLs enabled* & *Bucket owner preferred*.  
![Step5](images/Screenshot%2025-09-06%204445.png)
- Disabled **Block Public Access** to allow access to the hosted site.  
![Step6](images/Screenshot%2025-09-06%204722.png)
- Copied the **S3 website URL** to access the patient reminder frontend. 

---


### 2. API Layer (Amazon API Gateway)  
![Step1](images/Screenshot%2025-09-06%205001.png)
- Created a **REST API** in API Gateway.  
![Step2](images/Screenshot%2025-09-06%205255.png)
- Configured **resources, methods, and stages**, then deployed the API.  
![Step3](images/Screenshot%2025-09-06%205758.png)
- Obtained the **Invoke URL** from API Gateway.  
![Step4](images/Screenshot%2025-09-06%20160352.png)
- Integrated the **API Gateway URL** with `index.html`.   

---


### 3. Backend (AWS Lambda Functions)  
![Step1](images/Screenshot%2025-09-06%20160624.png)
Created **three Lambda functions**:  
1. `PatientReminderProcessorLambda` – Handles incoming requests.  
2. `SendEmailLambda` – Sends email notifications using **Amazon SES**.  
3. `SendSmsLambda` – Sends SMS notifications using **Amazon SNS**.  

- Uploaded **Python code** for each Lambda.  
- Functions process input from **API Gateway** and trigger the workflow.  

---

### 4. Workflow Orchestration (AWS Step Functions)  
![Step1](images/Screenshot%202025-09-06%20161117.png)
![Step2](images/Screenshot%202025-09-06%20161437.png)  
- Designed a **Step Function** to manage the reminder flow.  
- Logic flow:  
  - If input = **Email**, trigger `SendEmailLambda`.  
  - If input = **SMS**, trigger `SendSmsLambda`.  
  - If input = **Both**, trigger both Lambda functions in sequence.   

---

---

## 📊 Output / Demo

### Patient Reminder Website (Hosted on S3)
![Patient Reminder Website](images/Screenshot%202025-09-06%20162602.png)

### Email Reminder Example
![Email Reminder](images/Screenshot%202025-09-06%20163050.png)


---

## 🛠️ Tech Stack  
- **Frontend**: HTML (S3 hosting)  
- **Backend**: Python (AWS Lambda)  
- **AWS Services**: S3, API Gateway, Lambda, Step Functions, SES, SNS  

---

