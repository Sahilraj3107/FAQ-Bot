# FAQ Chatbot

A simple AI-powered FAQ chatbot I built to learn Kubernetes and CI/CD practices. It uses LangChain with the Groq API to answer frequently asked questions.

## What This Project Does

This chatbot can have conversations with users and answer their questions. It remembers the conversation history so it can understand context. The whole thing runs in Docker containers and can be deployed to Kubernetes clusters.

I built this mainly to practice Kubernetes deployment and set up automated pipelines with GitHub Actions.

## Technologies Used

- Python for the main application
- LangChain to work with the AI model
- Groq API with the llama-3.1-8b-instant model
- Flask for the web API
- Docker for containerization
- Kubernetes for deployment
- GitHub Actions for automation

## Project Structure

FAQ-Bot/
├── .github/
│ └── workflows/
│ └── cicd.yml
├── main.py
├── requirements.txt
├── Dockerfile
├── deployment.yml
├── service.yml
├── .env
├── .dockerignore
└── .gitignore


## What You Need

Before running this project, make sure you have:

- Python 3.10 or newer installed
- Docker Desktop running on your computer
- A Kubernetes cluster like Minikube for local testing
- A Groq API key from console.groq.com
- A Docker Hub account to store images

## Running It Locally

### Step 1: Clone the Repository

git clone https://github.com/yourusername/FAQ-Bot.git
cd FAQ-Bot


### Step 2: Create Virtual Environment

python -m venv venv
source venv/bin/activate


On Windows use:
venv\Scripts\activate


### Step 3: Install Dependencies

pip install -r requirements.txt


### Step 4: Set Up Environment Variables

Create a file called .env in the project folder and add:

GROQ_API_KEY=your_groq_api_key_here


### Step 5: Run the Application

python main.py


The chatbot will start running at http://localhost:8080

## How to Use It

### API Endpoint

The chatbot has one endpoint where you send questions.

**POST** /chat

Request format:
{
"input": "What is Kubernetes?"
}


Response format:
{
"response": "Kubernetes is a container orchestration platform...",
"history": "..."
}


### Example with curl

curl -X POST http://localhost:8080/chat -H "Content-Type: application/json" -d '{"input": "What is Docker?"}'


## Docker Setup

### Step 1: Build Docker Image

docker build -t yourusername/faq-chatbot:latest .


### Step 2: Run Container Locally

docker run -p 8080:8080 -e GROQ_API_KEY=your_api_key yourusername/faq-chatbot:latest


### Step 3: Push to Docker Hub

docker push yourusername/faq-chatbot:latest


## Deploying to Kubernetes

### Step 1: Start Minikube

minikube start


### Step 2: Create Kubernetes Secret

kubectl create secret generic groq-api-secret --from-literal=GROQ_API_KEY=your_api_key


### Step 3: Deploy the Application

kubectl apply -f deployment.yml
kubectl apply -f service.yml


### Step 4: Check Deployment Status

kubectl get pods
kubectl get services


### Step 5: Access the Service

minikube service faq-chatbot-service


## Automated Deployment Pipeline

The project includes a GitHub Actions workflow that automatically builds, pushes, and deploys your code when you push to the main branch.

### Step 1: Add GitHub Secrets

Go to your GitHub repository, click Settings, then Secrets and variables, then Actions, then New repository secret.

Add these three secrets:

**DOCKER_USERNAME**
- Name: DOCKER_USERNAME
- Value: your Docker Hub username

**DOCKER_PASSWORD**
- Name: DOCKER_PASSWORD
- Value: your Docker Hub password

**KUBE_CONFIG_DATA**
- Name: KUBE_CONFIG_DATA
- Value: your base64 encoded kubeconfig

### Step 2: Generate Kubeconfig Base64

On Linux or Mac:
cat ~/.kube/config | base64


On Windows PowerShell:

Copy the output and paste it as the value for KUBE_CONFIG_DATA secret.

### Step 3: Push Your Code

git add .
git commit -m "Update application"
git push origin main


The GitHub Actions workflow will automatically:
1. Checkout your code
2. Login to Docker Hub
3. Build the Docker image
4. Push the image to Docker Hub
5. Deploy to your Kubernetes cluster

### Step 4: Check Workflow Status

Go to your GitHub repository and click the Actions tab to see the workflow running.

## Things to Know

### Important Limitations

GitHub Actions cannot deploy to a local Minikube cluster because it runs on GitHub's servers and cannot reach your local machine. The deployment step will fail with local Minikube.

If you want the full pipeline to work including deployment, you need to use a cloud Kubernetes provider like:
- AWS EKS
- Google GKE
- DigitalOcean Kubernetes
- Azure AKS

The conversation memory currently stores everything in memory, so it resets when the container restarts.

## What I Learned

I built this project to practice:

- Deploying applications to Kubernetes
- Creating Docker containers
- Setting up CI/CD pipelines with GitHub Actions
- Working with LangChain and LLM APIs
- Building RESTful APIs with Flask

## Future Ideas

Some things I might add later:

- Save conversation history to a database
- Add user authentication
- Improve the prompts for better responses
- Add monitoring with Prometheus and Grafana
- Create Helm charts for easier deployment
- Add rate limiting to prevent abuse
- Write tests for the code

## Common Problems

### Docker build fails
Check that all packages are listed in requirements.txt

### Kubernetes deployment fails
Make sure your Docker image is public on Docker Hub

### API returns errors
Verify your Groq API key is set correctly in Kubernetes secrets

### GitHub Actions deployment fails
With local Minikube this is expected because GitHub cannot reach your local machine. Deploy manually instead using kubectl apply commands.

### Workflow shows red cross
Click on the failed workflow, then click on the job name, then click on the failed step to see detailed error logs.

## Troubleshooting Steps

If something goes wrong:

1. Check the GitHub Actions logs for detailed error messages
2. Verify all secrets are set correctly in GitHub
3. Make sure Docker Desktop is running
4. Confirm your Docker Hub username is correct in the workflow
5. Test Docker build locally before pushing to GitHub
6. Check Kubernetes pod logs with kubectl logs pod-name
