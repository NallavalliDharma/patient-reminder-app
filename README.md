# Patient Reminder Web Application

![Project Architecture](assets/project-diagram.png)

## 📌 Overview  
The **Patient Reminder Web Application** is a cloud-based solution built on AWS to send automated **Email** and **SMS** reminders to patients. It uses **serverless architecture** with AWS services like **S3, API Gateway, Lambda, Step Functions, SES, and SNS** to ensure scalability, reliability, and low cost.

---

## 🚀 Project Workflow  

### 1. Frontend (Static Website Hosting)  
![Step1](images/Screenshot 2025-09-06 154114.png)
- Uploaded `index.html` file to **Amazon S3 bucket**.  
![Step2](images/Screenshot 2025-09-06 154154.png)
- Enabled **bucket versioning** for better management.  
![Step3](images/Screenshot 2025-09-06 154325.png)
- Enabled **static website hosting** and hosted the frontend.  
![Step4](images/Screenshot 2025-09-06 154608.png)
- Configured **Object Ownership** → *ACLs enabled* & *Bucket owner preferred*.  
![Step5](images/Screenshot 2025-09-06 154445.png)
- Disabled **Block Public Access** to allow access to the hosted site.  
![Step6](images/Screenshot 2025-09-06 154722.png)
- Copied the **S3 website URL** to access the patient reminder frontend. 

---


### 2. API Layer (Amazon API Gateway)  
![Step1](images/Screenshot 2025-09-06 155001.png)
- Created a **REST API** in API Gateway.  
![Step2](images/Screenshot 2025-09-06 155255.png)
- Configured **resources, methods, and stages**, then deployed the API.  
![Step3](images/Screenshot 2025-09-06 155758.png)
- Obtained the **Invoke URL** from API Gateway.  
![Step4](images/Screenshot 2025-09-06 160352.png)
- Integrated the **API Gateway URL** with `index.html`.

---


### 3. Backend (AWS Lambda Functions)  
![Step1](images/Screenshot 2025-09-06 160624.png)
Created **three Lambda functions**:  
1. `PatientReminderProcessorLambda` – Handles incoming requests.  
2. `SendEmailLambda` – Sends email notifications using **Amazon SES**.  
3. `SendSmsLambda` – Sends SMS notifications using **Amazon SNS**.  

- Uploaded **Python code** for each Lambda.  
- Functions process input from **API Gateway** and trigger the workflow.  

---

### 4. Workflow Orchestration (AWS Step Functions)  
![Step1](images/Screenshot 2025-09-06 161117.png)
![Step2](images/Screenshot 2025-09-06 161437.png)
- Designed a **Step Function** to manage the reminder flow.  
- Logic flow:  
  - If input = **Email**, trigger `SendEmailLambda`.  
  - If input = **SMS**, trigger `SendSmsLambda`.  
  - If input = **Both**, trigger both Lambda functions in sequence.   

---

---

## 📊 Output / Demo

### Patient Reminder Website (Hosted on S3)
![Patient Reminder Website](images/Screenshot 2025-09-06 162602.png)

### Email Reminder Example
![Email Reminder](images/Screenshot 2025-09-06 163050.png)
